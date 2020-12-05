import pandas as pd
import os
import numpy as np

f=pd.read_csv("./OID/csv_folder/validation-annotations-bbox.csv")
# print(f.info())

#For multiple classes use the below, adding as many new LabelNames as needed
#this one is beer[0] cat[1] banana[2] in that order
numClasses = ['/m/01940j','/m/01g317'] #backpack


u = f.loc[f['LabelName'].isin(numClasses)]
keep_col = ['LabelName','ImageID','XMin','XMax','YMin','YMax']

new_f = u[keep_col]

new_f['ClassNumber'] = new_f['LabelName']

# print(new_f.info())

# # adding a new column for Classnumber and setting the values based on LabelName
# # so, for this, it's beer[0] cat[1] banana[2] in that order
new_f.loc[new_f['LabelName'] == '/m/01940j', 'ClassNumber'] = 0
new_f.loc[new_f['LabelName'] == '/m/01g317', 'ClassNumber'] = 1
# # new_f.loc[new_f['LabelName'] == '/m/09qck', 'ClassNumber'] = 2
# print(new_f.head(3))
new_f['width'] = new_f['XMax'] - new_f['XMin']
new_f['height'] = new_f['YMax'] - new_f['YMin']
new_f['x'] = (new_f['XMax'] + new_f['XMin'])/2
new_f['y'] = (new_f['YMax'] + new_f['YMin'])/2
keep_col = ['ClassNumber','ImageID','x','y','width','height']
new_f_2 = new_f[keep_col]

print(new_f_2.head(3))
new_f_2['ImageID'] = new_f_2['ImageID'].astype(str)
print(new_f_2.info())

for root, dirs, files in os.walk("."):  
	for filename in files:

		if filename.endswith(".jpg"):
			fn = filename[:-4]
			# print(fn)
			nf = new_f_2.loc[new_f_2['ImageID'] == fn]
			keep_col = ['ClassNumber','x','y','width','height']
			new_nf = nf[keep_col]
			# print(new_nf)
			imgpath = "./OID/Dataset/labels/" + fn + ".txt"
			# print(imgpath)
			new_nf.to_csv(imgpath, index=False, header=False, sep=' ')
			# print(nf.info())
			# np.savetxt(imgpath, new_nf.values,fmt='%s')


