FPGA Accelerated AI
============================================================================

Neural network inference on FPGA with Brevitas and FINN
----------------------------------------------------------------------------


### Prerequisites
- Ultra96V2 board (other FPGAs supported with slight modifications)
- PC (with GPU recommended for training),
- Xilinx tools (Vivado, HLS, Vitis)
- Environment(s) with [Brevitas](https://github.com/Xilinx/brevitas) and [FINN](https://github.com/Xilinx/finn)



Tested with:
- `Ubuntu 20.04.3 LTS (host PC - R3950X+32GB+RTX2070Super)`
- `Vivado / Vitis / Vitis HLS 2020.2` (with Y2K22 bug patch)
- brevitas @ git+https://github.com/Xilinx/brevitas.git@32cc847fc7cd6ca4c0201fd6b7d185c1103ae088
- torch==1.10.1+cu113, torchaudio==0.10.1+cu113, torchvision==0.11.2+cu113
- onnx==1.10.2, onnxoptimizer==0.2.6
- FINN vitis_hls branch (https://github.com/Xilinx/finn/tree/feature/vitis_hls) SHA 955747f1784b1afecd1bd1cc2c33cb283f78afca




## Flow (without PYNQ)
0. Install Xilins tools  and create environment that has Brevitas, Pytorch, ONNX etc.
1. Gather dataset as outlined in /src/dataset_creation/ README.
2. Define and train quantized network with Brevitas as outlined in /src/notebooks/ README.
3. Export to FINN.
4. Explore folding settings with estimate reports and build accelerator with FINN in docker.
5. Create pseudo IP for easy Vivado import in any project as outlined in /src/pseudo_ip/ README.
6. (Optional) Simulate accelerator to verify behavior (example in /src/notebooks/regression_BNN/simulation/).
7. Construct IP wrapper to interface with accelerator.
8. Deploy on FPGA.


## MISC
- Useful FAQ on FINN: https://finn.readthedocs.io/en/latest/faq.html
- Interfacing with FINN generated accelerator IP: https://github.com/jterry-x/finn-examples/tree/main/build/fpga_flow#simulating-the-stitched-ip-with-verilog-test-bench
- Runtime loadable weights: https://github.com/Xilinx/finn/discussions/380
- Brevitas bnn training: https://github.com/Xilinx/brevitas/tree/master/src/brevitas_examples/bnn_pynq
- FINN bnn cnv: https://github.com/Xilinx/finn/blob/main/notebooks/end2end_example/bnn-pynq/cnv_end2end_example.ipynb
- PE and SIMD: https://arxiv.org/pdf/1612.07119.pdf and https://github.com/Xilinx/finn/discussions/501
- imagenet models: https://github.com/Xilinx/brevitas/tree/master/src/brevitas_examples/imagenet_classification/models
- GPU in FINN docker: https://github.com/Xilinx/finn/discussions/507
- Feature dimension going into a maxpool layer (size=2, stride=2) must be divisible by 2:

  Input image size 32x32: 32 (padded conv2d) 32 (maxpool) 16 (padded conv2d) 16 (maxpool) 8 ... (Good)
  
  Input image size 30x30: 30 (padded conv2d) 30 (maxpool) 15 (padded conv2d) 15 (maxpool) 7? (Bad?)
  
- Minimize features in flattened layer between last CNV and first FC as this will likely consume most BRAMs.
- In folding_config.json, ram_style used to determine if BRAM (`block`), URAM (`uram`), or LUT (`distributed`) should be used to store values. Can set `auto` to determine automatically. Only works if `mem_mode` is not `const` https://github.com/Xilinx/finn/blob/dev/src/finn/custom_op/fpgadataflow/streamingfclayer_batch.py#L95
- Fix /tmp/ IP dependency: https://github.com/Xilinx/finn/discussions/404
- List of all FINN generated verilog source files can be found in `<FINN_output_dir>/stitched_ip/all_verilog_srcs.txt`
- `memstream` or `*_wstrm` files not found: likely because wrong IP repository path. Point to /finn/finn-rtllib/memstream instead. 
- FINN build may produce error if building more than once in same directory.
- May be necessary to increase weight/activation bits for simulation/hardware to meet Brevitas performance
- [Place 30-487] The packing of instances into the device could not be obeyed. There are a total of 8820 CLBs in the device, of which 4904 CLBs are available, however, the unplaced instances require 5238 CLBs. Please analyze your design to determine if the number of LUTs, FFs, and/or control sets can be reduced.
Run: `report_qor_suggestions` in Tcl console possible suggestions. Try alternative directives or strategies during synthesis/implementation (can be found in project summary).
  - Area_ExploreWithRemap may work.
- Can use PE and SIMD of last layer to change shape of output, e.g. from 32 bits to 8 bits (read 4 times sequentially). PE and SIMD values above 1 in this layer may result in high ressource usage.
- Lower estimated throughput (FPS) results in longer build times (FIFO depths step specifically) https://github.com/Xilinx/finn/discussions/383

