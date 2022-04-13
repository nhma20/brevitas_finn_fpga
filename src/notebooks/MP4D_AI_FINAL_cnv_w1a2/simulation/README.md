## Input waveforms:

![accelerator_loading_waveform](https://user-images.githubusercontent.com/76950970/163166438-9ff4bb5f-e22b-43bd-8ae3-6303a406e07f.png)


## Output waveforms:

![accelerator_output_waveform](https://user-images.githubusercontent.com/76950970/163166428-61561c49-16b2-4d5c-899a-426d76ecf7d7.png)


## Simulation example:

![FINN_IP_sim](https://user-images.githubusercontent.com/76950970/163167999-103fa646-2658-408d-b683-af663db04f84.png)



Simulate FINN IP
----------------------------------------------------------------------------

Modified from: https://github.com/jterry-x/finn-examples/tree/main/build/fpga_flow

This simulation demonstrates how to bring a FINN compiled model into a traditional FPGA design environment for integration into a larger application. 


### Examine the Stitched IP

Navigate to the stitched IP project directory:

> cd ${REPO_PATH}/src/notebooks/regression_BNN/output_estimates_only/stitched_ip

And, open the project:

> vivado finn_vivado_stitch_proj.xpr

Explore the block diagram and note the interfaces.  



## Simulating the Stitched IP with Verilog Test Bench

The included `testbench.sv` is a very simple test to illustrate how to feed data to the compiled model. 

The image data is 256*256*3 = 196608 bytes per frame, organized as 256x256x3 unsigned integer bytes.

--------------------------- TODO: FIX BELOW: ---------------------------
Using the following image for coordinate reference where a byte is identified as <Brow_column> we see that B0_0 is the upper leftmost byte, and B255_255 is the lower right most byte:

Thus, the input data for the first cycle is organized as such:
>  s_axis_0_tdata[391:0] = {B1_20,B1_19, ...  ,B1_0,B0_27, ...  ,B0_1,B0_0};
---------------------------                  ---------------------------

The test bench reads data from a simple text file (data.hex), which holds the byte values of test images.  The included script `gen_tb_data.py` creates the test data as well as the ground truth expectations.  The script takes the liberty of flipping the byte order such that veriliog's $readmemh brings B0_0 nicely into the LSB position. To generate the test data:

```
cd ${REPO_PATH}/src/notebooks/regression_BNN/output_estimates_only/stitched_ip
mkdir -p finn_vivado_stitch_proj.sim/sim_1/behav/xsim
../../simulation/gen_tb_data.py > finn_vivado_stitch_proj.sim/sim_1/behav/xsim/data.hex
```
In Vivado, add the testbench as a simulation file. Paste this in to the Tcl Console:
> add_files -fileset sim_1 -norecurse ../../testbench.sv


Then, run the simulation (Flow Navigator -> Simulation -> Run Simulation).   Give the simulator a `run -all`  (click the "play" button in the simulator) to run the sim to it's $finish conclusion - may take hours.  Output of the simulation should look as follows:

```
.
.
.
Comparison 15:
Prediction:        170,        130,         42,         50
     Label: 178, 129,  36,  43
 
Comparison 16:
Prediction:        214,        178,         50,         94
     Label: 217, 167,  47, 104

************************************************************ 
  SIM COMPLETE
  Validated 16 data points 
```

### Instantiation in Mission Design

There are any number of ways to bring the stitched IP into another design.  

You may want to package the stitched IP BD (or entire project) as its own IP.  A good reference for this is [UG1119](https://www.xilinx.com/support/documentation/sw_manuals/xilinx2020_1/ug1119-vivado-creating-packaging-ip-tutorial.pdf)  

Keep in mind that all of the User IP Repo's included in the Stitched IP project (from /tmp) need to also be brought in as IP Repo's to any project using the stitched IP.  It would be prudent to copy those IP repos to an appropriate archive location.


