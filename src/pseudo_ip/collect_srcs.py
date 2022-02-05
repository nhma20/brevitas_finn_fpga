from distutils.dir_util import copy_tree
import copy


make_project_tcl_path = "/home/nm/FINN/hls_2020_2/finn/notebooks/end2end_example/cnv_w1a1_resize_regression_V5_surgery/stitched_ip_vivado_proj/vivado_stitch_proj_or5_fmik/collected_src_files/make_project.tcl"

finn_rtllib_path = "/home/nm/FINN/hls_2020_2/finn/finn-rtllib/memstream"

ip_copy_destination_path = "/home/nm/FINN/hls_2020_2/finn/notebooks/end2end_example/cnv_w1a1_resize_regression_V5_surgery/stitched_ip_vivado_proj/vivado_stitch_proj_or5_fmik/collected_src_files/src_ips"

# Read 2nd line of "make_project.tcl" which has all IP paths
with open(make_project_tcl_path) as fp:
    for i, line in enumerate(fp):
        if i == 1:
        	paths = line
        elif i > 1:
            break

paths = paths.replace("set_property ip_repo_paths [list /workspace/finn/finn-rtllib/memstream", finn_rtllib_path)
paths = paths.replace("] [current_project]", "")
paths_list = paths.split()
its = 0

# For each IP path, copy the IP to ip_copy_destination_path
for path in paths_list:

	if its == 0:
		its += 1
		continue
	
	# prune destination path path
	level_count = 0
	delete_up_to = 0
	delete_from = 999
	for i in range(len(path)):
		if path[i] == '/':
			level_count += 1
		
		if level_count == 2:
			delete_up_to = i
		
		if level_count == 3:
			delete_from = i
	
	to_directory = copy.deepcopy(path)
	to_directory = to_directory[0:delete_from+3]
	to_directory = to_directory[delete_up_to+1:-1]
	
	
	# set source path path
	from_directory = copy.deepcopy(path)
	from_directory = from_directory[0:delete_from+2]	
	

	# copy subdirectory
	to_directory = ip_copy_destination_path + to_directory
	print("Copied: ", from_directory)
	print("To: ", to_directory, "\n")

	copy_tree(from_directory, to_directory)
	

