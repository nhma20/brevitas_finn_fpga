Make pseudo IP for Vivado import
----------------------------------------------------------------------------

## Flow
0. Finish FINN build of accelerator (or download pre-built IPs and follow step 3).
1. Look through `<FINN_OUTPUT_DIR>/stitched_ip/make_project.tcl` to get sources for following steps.
2. Collect all generated source files from FINN build with `collect_srcs.sh <ip_destination_dir> <make_project.tcl> <memstream_dir> <tmp_finn_dev_dir>`.
	- e.g. `./collect_srcs.sh /home/user/src_ips_test/src_ips /home/user/finn_output/stitched_ip/ /home/user/FINN/finn-rtllib/memstream/ /tmp/finn_dev_user`
3. Use `make_pseudo_ip.sh` to create `finn_import.tcl <source_ips_origin_dir> <pseudo_ip_install_dir> <memstream_dir>` script for easy Vivado import of FINN IP.
	- e.g. `./make_pseudo_ip.sh /home/user/src_ips_test/src_ips /home/user/src_ips_test/pseudo_ip_install /home/user/FINN/finn-rtllib/memstream`
	- To use TCL script, `source <path_to>/finn_import.tcl` in Tcl Console in Vivado. Should produce "finn_ip" block design element with 3 inputs and 1 output.
	
Source IPs for single person 256x256x3 bounding box network can also be downloaded here: https://nextcloud.sdu.dk/index.php/s/6HGxxk8d72ysYDg/download/ip_pack.zip. Unzip and follow step 3 to create pseudo IP.


