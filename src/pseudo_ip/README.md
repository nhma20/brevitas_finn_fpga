Make pseudo IP for Vivado import
----------------------------------------------------------------------------

## Flow
0. Finish FINN build of accelerator.
1. Look through `<FINN_OUTPUT_DIR>/stitched_ip/make_project.tcl` to get sources for following steps.
2. Collect all generated source files from FINN build with `collect_srcs.py` (change paths to fit use-case).
3. Use `make_pseudo_ip.py` to create `finn_import.tcl` script for easy Vivado import of FINN IP (change paths to fit use-case).
	- To run, `source <path_to>/finn_import.tcl` in Tcl Console in Vivado. Should produce "finn_ip" block design element with 3 inputs and 1 output.
	
Source IPs for single person 256x256x3 bounding box network can also be downloaded here: https://nextcloud.sdu.dk/index.php/s/3xt6wTLyEqn7LJj


