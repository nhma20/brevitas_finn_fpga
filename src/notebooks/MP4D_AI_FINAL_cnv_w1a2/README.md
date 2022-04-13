W1A2 CNN for person detection (bounding box regression)
----------------------------------------------------------------------------

## Flow
1. Perform tasks as outlined in ../../dataset_creation/ README.
2. Launch Brevitas/FINN environment.
3. Open `cnv_w1a2_mp4d.ipynb` and update paths.
4. Train/load network parameters and perform FINN build.
5. Perform simulation in Vivado as outlined in /simulation/ README, which also holds expected sim results.
6. /expected_brevitas_results/ and /expected_hardware_results/ contain expected results from a set of test images found in /simulation/test_images/

Outputs of generated IP should be multiplied by 2 to obtain the actual value.

Example of how to wrap with writing/reading modules:
https://github.com/DIII-SDU-Group/finn-example-ip

Example of how to interface writing/reading modules from software:
https://github.com/DIII-SDU-Group/finn-example-ROS2-pkg
