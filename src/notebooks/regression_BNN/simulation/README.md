Simulate FINN IP
----------------------------------------------------------------------------

Modified from: https://github.com/jterry-x/finn-examples/tree/main/build/fpga_flow

This simulation demonstrates how to bring a FINN compiled model into a traditional FPGA design environment for integration into a larger application. 


### Examine the Stitched IP

Navigate to the stitched IP project directory:

> cd ${REPO_PATH}/src/notebooks/regression_BNN/output_estimates_only/stitched_ip

And, open the project:

> vivado finn_vivado_stitch_proj.xpr

Explore the IPI board design and note the interfaces.  



## Simulating the Stitched IP with Verilog Test Bench

The included `testbench.sv` is a very simple test to illustrate how to feed data to the compiled model. 

The image data is 256*256*3 = 196608 bytes per frame, ? organized as 256x256x3 unsigned integer bytes ? (determine own).

Using the following image for coordinate reference where a byte is identified as <Brow_column> we see that B0_0 is the upper leftmost byte, and B255_255 is the lower right most byte:

--------------------------- TODO: FIX BELOW: ---------------------------
Thus, the input data for the first cycle is organized as such:
>  s_axis_0_tdata[391:0] = {B1_20,B1_19, ...  ,B1_0,B0_27, ...  ,B0_1,B0_0};

The test bench reads data from a simple text file (data.hex).  The included script `gen_tb_data.py` creates the test data as well as the ground truth expectations (Note: using ground truth is undesirable if the intent is to validate that the HW implementation matches the trained model).  The script takes the liberty of flipping the byte order such that veriliog's $readmemh brings B0_0 nicely into the LSB position.   To generate the test data:

```
cd ${REPO_PATH}/src/notebooks/regression_BNN/output_estimates_only/stitched_ip
mkdir -p finn_vivado_stitch_proj.sim/sim_1/behav/xsim
../../simulation/gen_tb_data.py > finn_vivado_stitch_proj.sim/sim_1/behav/xsim/data.hex
```
In Vivado, add the testbench as a simulation file. Paste this in to the Tcl Console:
> add_files -fileset sim_1 -norecurse ../../testbench.sv


Then, run the simulation (Flow Navigator -> Simulation -> Run Simulation).   Give the simulator a `run -all`  (click the "play" button in the simulator) to run the sim to it's $finish conclusion.  With 20 data points run, it should have 1 mismatch due using the ground-truth as the check source:

```
************************************************************ 
SIM COMPLETE
 Validated 20 data points 
 Total error count: ====>  1  <====
```

### Instantiation in Mission Design

There are any number of ways to bring the stitched IP into another design.  

You may want to package the stitched IP BD (or entire project) as its own IP.  A good reference for this is [UG1119](https://www.xilinx.com/support/documentation/sw_manuals/xilinx2020_1/ug1119-vivado-creating-packaging-ip-tutorial.pdf)  

Keep in mind that all of the User IP Repo's included in the Stitched IP project (from /tmp) need to also be brought in as IP Repo's to any project using the stitched IP.  It would be prudent to copy those IP repos to an appropriate archive location.


