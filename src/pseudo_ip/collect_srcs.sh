#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
RED='\033[0;31m'


if [[ "$1" == "" ]]; then
  echo -e "${RED}Missing arguments!${NC}"
  echo "USAGE: ./collect_srcs.sh /path/to/source_file_destination_dir /path/to/make_project_tcl/ /path/to/memstream/ /tmp/finn_dev_user"
  exit
fi

if [[ "$2" == "" ]]; then
  echo -e "${RED}Missing arguments!${NC}"
  echo "USAGE: ./collect_srcs.sh /path/to/source_file_destination_dir /path/to/make_project_tcl/ /path/to/memstream/ /tmp/finn_dev_user"
  exit
fi

if [[ "$3" == "" ]]; then
  echo -e "${RED}Missing arguments!${NC}"
  echo "USAGE: ./collect_srcs.sh /path/to/source_file_destination_dir /path/to/make_project_tcl/ /path/to/memstream/ /tmp/finn_dev_user"
  exit
fi

if [[ "$4" == "" ]]; then
  echo -e "${RED}Missing arguments!${NC}"
  echo "USAGE: ./collect_srcs.sh /path/to/source_file_destination_dir /path/to/make_project_tcl/ /path/to/memstream/ /tmp/finn_dev_user"
  exit
fi



ip_folder=$1	# where to save source files, e.g. /home/user/pseudo_ip/src_ips
make_project_tcl_path=$2	# path to make_project.tcl from finn build, e.g. /home/user/finn_build_dir/make_project.tcl
finn_rtllib_path=$3	# path to memstream IP in finn installation directory, e.g. /home/user/finn/finn-rtllib/memstream/
tmp_finn_dev_path=$4

echo "Collecting FINN generated source files from /tmp/"
python3 collect_srcs.py $finn_rtllib_path $make_project_tcl_path $ip_folder


cp $make_project_tcl_path/make_project.tcl $ip_folder/make_finn_stitched.tcl

cd $ip_folder

echo "Renaming all paths pointing to finn dev /tmp/ directory - this may take a while."

replace_FS=\\\/
replace_BS=\\\\\\\/
escaped_dir=${tmp_finn_dev_path//\//$replace_FS}
double_escaped_dir=${tmp_finn_dev_path//\//$replace_BS}
temp_dir_name="\\/temp_dir_name"
escaped_temp_dir_name="\\\\\/escaped_temp_dir_name" # needed in few .json files


#point all paths with "/tmp/finn_dev_nm" to "/tmp_dir_name" instead 
#find ./ -type f -exec sed -i "s/${escaped_dir}/${temp_dir_name}/g" {} \;
find ./ -type f -exec sed -i "s/${escaped_dir}/\/temp_dir_name/g" {} \;

#point all paths with "\/tmp\/finn_dev_nm" to "\/tmp_dir_name" instead
find ./ -type f -exec sed -i "s/${double_escaped_dir}/${escaped_temp_dir_name}/g" {} \;

echo "Renaming complete."

