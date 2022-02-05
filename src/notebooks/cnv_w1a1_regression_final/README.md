Binarized CNN for person detection (bounding box regression)
----------------------------------------------------------------------------

## Flow
1. Perform tasks as outlined in ../../dataset_creation/ README.
2. Launch Brevitas/FINN environment.
3. Open `cnv_w1a1_regression.ipynb` and update paths.
4. Train/load network parameters and perform FINN build.
5. Perform simulation in Vivado as outlined in /fpga_flow/ README

Outputs of generated IP should be multiplied by 2 to obtain the actual value.

