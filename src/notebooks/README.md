Network training with Brevitas and accelerator building with FINN
----------------------------------------------------------------------------

The subdirectories of this folder contain examples of how to set up, train, and build networks with Brevitas and FINN. A basic convolutional network for digit recognition can be found in [/basic_CNN/](/src/notebooks/basic_CNN/).

[/classes_BNN/](/src/notebooks/classes_BNN/) contains a binarized convolutional network for person detection and outputs 4x onehot encoded classes representing xmin, ymin, xmax, ymax.

[/regression_BNN/](/src/notebooks/regression_BNN/) contains a binarized convolutional network for person detection and outputs 4 vectors representing xmin, ymin, xmax, ymax. A simulation folder is included to demonstrate how data is loaded into and out of the accelerator.

[/cnv_w1a1_regression_final/](/src/notebooks/cnv_w1a1_regression_final/) contains a binarized regression bounding box network. Outputs are strongly affected (negatively) by binarization.

[/MP4D_AI_FINAL_cnv_w1a2/](/src/notebooks/MP4D_AI_FINAL_cnv_w1a2/) contains the heavily quantized brevitas/finn project used for the AI application in the paper "MPSoC4Drones: An Open Framework for ROS2, PX4, and FPGA Integration".  A simulation folder is included to demonstrate how data is loaded into and out of the accelerator.
