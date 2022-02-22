from distutils.dir_util import copy_tree
import copy
import os 
import sys


cur_dir_path = os.path.dirname(os.path.realpath(__file__))



make_project_tcl_path = sys.argv[2]

finn_rtllib_path = sys.argv[1]

ip_installation_path = sys.argv[3]

tmp_finn_dir = "/temp_dir_name"

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
new_make_project_tcl = new_make_project_tcl.replace(tmp_finn_dir, ip_installation_path)

# remove duplicates of bd elements in list
bd_names = list(dict.fromkeys(bd_names))

# create hierarchy with bd elements
new_make_project_tcl += "group_bd_cells finn_ip "

for name in bd_names:
	new_make_project_tcl += "[get_bd_cells " + name + "] "

new_make_project_tcl += "\nregenerate_bd_layout\nsave_bd_design"


# write the file out
with open((cur_dir_path+"/import_finn_ip.tcl"), 'w') as file:
	file.write(new_make_project_tcl)
	
print("Created: ", (cur_dir_path+"/import_finn_ip.tcl"))


