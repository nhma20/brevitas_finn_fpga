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
