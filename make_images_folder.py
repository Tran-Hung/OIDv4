import glob
import shutil
import os

src_dir = "./OID/Dataset/validation/Backpack"
dst_dir = "./OID/Dataset/images"
for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
    shutil.copy(jpgfile, dst_dir)

src_dir2 = "./OID/Dataset/validation/Person"
dst_dir2 = "./OID/Dataset/images"
for jpgfile in glob.iglob(os.path.join(src_dir2, "*.jpg")):
    shutil.copy(jpgfile, dst_dir2)
