FPGA Accelerated AI
============================================================================

Neural network inference on FPGA with Brevitas and FINN
----------------------------------------------------------------------------


### Prerequisites
Ultra96V2 board, PC (with GPU recommended for training)

Tested with:
- `Ubuntu 20.04.3 LTS (host PC - R3950X+32GB+RTX2070Super)`
- `Vivado / Vitis / Vitis HLS 2020.2` (with Y2K22 bug patch)
- brevitas @ git+https://github.com/Xilinx/brevitas.git@32cc847fc7cd6ca4c0201fd6b7d185c1103ae088
- torch==1.10.1+cu113, torchaudio==0.10.1+cu113, torchvision==0.11.2+cu113
- onnx==1.10.2, onnxoptimizer==0.2.6
- FINN vitis_hls branch (https://github.com/Xilinx/finn/tree/feature/vitis_hls) SHA 955747f1784b1afecd1bd1cc2c33cb283f78afca




## Flow
1. Create environment that has Brevitas, Pytorch, ONNX etc.
2. Gather dataset
3. Define and train quantized network with Brevitas
4. Export to FINN
5. Build accelerator with FINN in docker
6. Construct IP wrapper to interface with accelerator
7. Deploy on FPGA


## MISC
- Interfacing with FINN generated accelerator IP: https://github.com/jterry-x/finn-examples/tree/main/build/fpga_flow#simulating-the-stitched-ip-with-verilog-test-bench
- Runtime loadable weights: https://github.com/Xilinx/finn/discussions/380
- Brevitas bnn training: https://github.com/Xilinx/brevitas/tree/master/src/brevitas_examples/bnn_pynq
- FINN bnn cnv: https://github.com/Xilinx/finn/blob/main/notebooks/end2end_example/bnn-pynq/cnv_end2end_example.ipynb3
- PE and SIMD: https://arxiv.org/pdf/1612.07119.pdf and https://github.com/Xilinx/finn/discussions/501
- imagenet models: https://github.com/Xilinx/brevitas/tree/master/src/brevitas_examples/imagenet_classification/models
- GPU in FINN docker: https://github.com/Xilinx/finn/discussions/507
- Feature dimension going into a maxpool layer (size=2, stride=2) must be divisible by 2:
  Input image size 32x32: 32 (padded conv2d) 32 (maxpool) 16 (padded conv2d) 16 (maxpool) 8 ... (Good)
  Input image size 30x30: 30 (padded conv2d) 30 (maxpool) 15 (padded conv2d) 15 (maxpool) 7? (Bad?)
- Minimize features in flattened layer between last CNV and first FC as this will likely consume most BRAMs.
- In folding_config.json, ram_style used to determine if BRAM (´block´), URAM (´uram´), or LUT (´distributed´) should be used to store values. Can set ´auto´ to determine automatically. 
