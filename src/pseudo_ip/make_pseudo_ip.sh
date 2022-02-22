#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
RED='\033[0;31m'


if [[ "$1" == "" ]]; then
  echo -e "${RED}Missing arguments!${NC}"
  echo "USAGE: ./collect_srcs.sh /path/to/source_ips_unpack_dir /path/to/pseudo_ip_install_dir /path/to/memstream"
  exit
fi

if [[ "$2" == "" ]]; then
  echo -e "${RED}Missing arguments!${NC}"
  echo "USAGE: ./collect_srcs.sh /path/to/source_ips_unpack_dir /path/to/pseudo_ip_install_dir /path/to/memstream"
  exit
fi

if [[ "$3" == "" ]]; then
  echo -e "${RED}Missing arguments!${NC}"
  echo "USAGE: ./collect_srcs.sh /path/to/source_ips_unpack_dir /path/to/pseudo_ip_install_dir /path/to/memstream"
  exit
fi



ip_folder=$1	# where source files have been unpacked, e.g. /home/user/src_ips
install_dir=$2	# where to install pseudo ip
finn_rtllib_path=$3	# path to memstream IP in finn installation directory, e.g. /home/user/finn/finn-rtllib/memstream/
make_project_tcl_path=$ip_folder/make_finn_stitched.tcl

echo "Copying files into installation directory"
cp -rf $ip_folder/* $install_dir


cd $install_dir

echo "Renaming all paths to point to installation directory - this may take a while."

replace_FS=\\\/
replace_BS=\\\\\\\/
escaped_install_dir=${install_dir//\//$replace_FS}
double_escaped_install_dir=${install_dir//\//$replace_BS}
temp_dir_name="\\/temp_dir_name"
escaped_temp_dir_name="\\\\\/escaped_temp_dir_name" # needed in few .json files


#point all paths with "/tmp/finn_dev_nm" to "/tmp_dir_name" instead 
find ./ -type f -exec sed -i "s/${temp_dir_name}/${escaped_install_dir}/g" {} \;

#point all paths with "\/tmp\/finn_dev_nm" to "\/tmp_dir_name" instead
find ./ -type f -exec sed -i "s/${escaped_temp_dir_name}/${double_escaped_install_dir}/g" {} \;

echo "Renaming complete."



echo "Creating pseudo IP TCL script (usage in Vivado Tcl console: source /path/to/import_finn_ip.tcl"
cd $SCRIPT_DIR
python3 make_pseudo_ip.py $finn_rtllib_path $make_project_tcl_path $install_dir
