#!/usr/bin/python3
# Copyright (c) 2021 Xilinx, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of Xilinx nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


"""
from keras.datasets import mnist
(train_x, train_y), (test_x, test_y) = mnist.load_data()
#print('X_test:  '  + str(test_x.shape))


for i in range(20):
  for j in range(28):
    for k in range(27,-1,-1):
      print('{:02X}'.format(test_x[i][j][k]),end='');
    print('')

  print('ffffffffffffffffffffffffffffffffffffffffffffffffffffff{:02X}'.format(0));
"""


import numpy as np
import cv2
import os

one_img_dir = "/home/nm/Downloads/VOCdevkit/VOC2012/single_or_no_person_dataset/single_person_images"
one_txt_dir = "/home/nm/Downloads/VOCdevkit/VOC2012/single_or_no_person_dataset/single_person_txt"

read_folder = one_img_dir + '/'
label_folder = one_txt_dir + '/'

dims = (256,256)
#fs = 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'

its = 0
for filename in os.listdir(read_folder):
  img = cv2.imread(os.path.join(read_folder,filename),1) # read img
  img = cv2.resize(img, dims, interpolation = cv2.INTER_AREA)# resize img to fit dims
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # this converts it into RGB
  for j in range(256):
    for k in range(256):
      for l in range(3):
        print('{:02X}'.format(img[j][k][l].astype('uint8')),end='');
    print('')


  f = open(label_folder + filename.replace('.jpg','.txt'), "r")
  temp_label = (f.read().split(","))
  hex_label = ''
  for k in range (4):
    temp_label[k] = round(float(temp_label[k]) / 5) # 0-100 label
    hex_label += '{:02X}'.format(temp_label[k])
  f.close()

  print('FFFFFFFFFFFFF' + hex_label)

  its += 1
  if its == 20:
    break