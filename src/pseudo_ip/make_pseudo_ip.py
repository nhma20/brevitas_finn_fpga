from distutils.dir_util import copy_tree
import copy


make_project_tcl_path = "/home/nm/FINN/hls_2020_2/finn/notebooks/end2end_example/cnv_w1a1_resize_regression_V5_surgery/stitched_ip_vivado_proj/vivado_stitch_proj_or5_fmik/collected_src_files/make_project.tcl"

finn_rtllib_path = "/home/nm/FINN/hls_2020_2/finn/finn-rtllib/memstream"

ip_copy_destination_path = "/home/nm/FINN/hls_2020_2/finn/notebooks/end2end_example/cnv_w1a1_resize_regression_V5_surgery/stitched_ip_vivado_proj/vivado_stitch_proj_or5_fmik/collected_src_files/src_ips"

tmp_finn_dir = "/tmp/finn_dev_nm"

wrong_memstream_path = "/workspace/finn/finn-rtllib/memstream"



new_make_project_tcl = ""
temp_line = ""
comment = False
bd_names = []

# edit make_project.tcl into pseudo IP importer
with open(make_project_tcl_path) as fp:

	for i, line in enumerate(fp):
    
		temp_line = line
		
		if "create_bd_design" in line: # comment out line about creating block design
			temp_line = line.replace(line, "# "+line)
		
		if "create_bd_cell" in line: # get block design element names to assemble in hierarchy later
			if line.count('/') > 0:
				name = line.split()[-1] 
				name = line.split('/')[1]
			else:
				name = line.split()[-1] 
			bd_names.append(name) 
    
		if "create_project" in line: # comment out first line about creating new project
			temp_line = "#" + line
    
		if "make_wrapper" in line: # comment out all lines below and including "make wrapper..."
			comment = True
			
		if comment == True:
			temp_line = line.replace(line, "# "+line)

		new_make_project_tcl += temp_line

# fix memstream path
new_make_project_tcl = new_make_project_tcl.replace(wrong_memstream_path, finn_rtllib_path)
new_make_project_tcl = new_make_project_tcl.replace(tmp_finn_dir, ip_copy_destination_path)

# remove duplicates of bd elements in list
bd_names = list(dict.fromkeys(bd_names))

# create hierarchy with bd elements
new_make_project_tcl += "group_bd_cells finn_ip "

for name in bd_names:
	new_make_project_tcl += "[get_bd_cells " + name + "] "

new_make_project_tcl += "\nregenerate_bd_layout\nsave_bd_design"


# write the file out
with open(make_project_tcl_path.replace("make_project.tcl", "import_finn_ip.tcl"), 'w') as file:
	file.write(new_make_project_tcl)
	
print("Created: ", make_project_tcl_path.replace("make_project.tcl", "import_finn_ip.tcl"))


