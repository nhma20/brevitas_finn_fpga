Network training with Brevitas and accelerator building with FINN
----------------------------------------------------------------------------

The subdirectories of this folder contain examples of how to set up, train, and build networks with Brevitas and FINN. A basic convolutional network for digit recognition can be found in /basic_CNN/.

/classes_BNN/ contains a binarized convolutional network for person detection and outputs 4x onehot encoded classes representing xmin, ymin, xmax, ymax.

/regression_BNN/ contains a binarized convolutional network for person detection and outputs 4 vectors representing xmin, ymin, xmax, ymax. A simulation folder is included to demonstrate how data is loaded into and out of the accelerator.

