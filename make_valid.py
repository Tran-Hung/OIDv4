import glob2
import math  
import os
import numpy as np
 
files = []
for ext in ["*.png", "*.jpeg", "*.jpg"]:
  image_files = glob2.glob(os.path.join("/home/team28_2/OIDv4_ToolKit/OID/Dataset/images/", ext))
  files += image_files
 
nb_val = math.floor(len(files)*0.2)
rand_idx = np.random.randint(0, len(files), nb_val)

print(len(files)) 

with open("./OID/Dataset/train.txt", "w") as f:
  for idx in np.arange(len(files)):
    # if (os.path.exists(files[idx][:-3] + "txt")):
      f.write(files[idx]+'\n')

with open("./OID/Dataset/valid.txt", "w") as f:
  for idx in np.arange(len(files)):
    if (idx in rand_idx):
      f.write(files[idx]+'\n')
