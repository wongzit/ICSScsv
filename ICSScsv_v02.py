# ICSSplt
# 2021-04-22, Wang Zhe

with open("benzene.log", 'r') as originalOutput:
	outputLines = originalOutput.readlines()

# Read Bq coordinates and shielding tensor
coorBq = []
shielTensor = []

for line in outputLines:
	if ' Bq    ' in line and line.count('.') == 3:
		coorBq.append(line.rstrip())
	elif 'Isotropic =' in line:
		shielTensor.append(line.rstrip())
	elif ('XX=' in line) and ('YX=' in line) and ('ZX=' in line):
		shielTensor.append(line.rstrip())
	elif ('XY=' in line) and ('YY=' in line) and ('ZY=' in line):
		shielTensor.append(line.rstrip())
	elif ('XZ=' in line) and ('YZ=' in line) and ('ZZ=' in line):
		shielTensor.append(line.rstrip())

#print(coorBq)
#print(shielTensor)

# Define range
#bqatomNum = len(coorBq)
#print(bqatomNum)
x_all = []
y_all = []
z_all = []

for atomNum in range(len(coorBq)):
	x_all.append(float(coorBq[atomNum].split()[1]))
	y_all.append(float(coorBq[atomNum].split()[2]))
	z_all.append(float(coorBq[atomNum].split()[3]))

#print(x_all)
#print(y_all)
#print(z_all)

x_set = sorted(set(x_all))
y_set = sorted(set(y_all))
z_set = sorted(set(z_all))

#print(x_set)
print(y_set)
#print(z_set)

'''
shieldingFile = open("shieldingFile.gjf", 'w')
for line2 in shielTensor:
	shieldingFile.write(f"{line2}\n")
shieldingFile.close()
'''

x_max, x_min = max(x_set), min(x_set)
y_max, y_min = max(y_set), min(y_set)
z_max, z_min = max(z_set), min(z_set)

#print(x_max, x_min)
#print(y_max, y_min)
#print(z_max, z_min)

#check plane
planeFlag = 0

if len(x_set) == 1:
	planeFlag = 3    #YZ plane
	y_step = y_set[1] - y_set[0]
	z_step = z_set[1] - z_set[0]
	print(f"ICSS will be mapped on YZ plane in Y[{y_min} {y_max}, {round(y_step, 2)}], Z[{z_min} {z_max}, {round(z_step, 2)}].\n")
elif len(y_set) == 1:
	planeFlag = 2    #XZ plane
	x_step = x_set[1] - x_set[0]
	z_step = z_set[1] - z_set[0]
	print(f"ICSS will be mapped on XZ plane in X[{x_min} {x_max}, {round(x_step, 2)}], Z[{z_min} {z_max}, {round(z_step, 2)}].\n")
elif len(z_set) == 1:
	planeFlag = 1    #XY plane
	x_step = x_set[1] - x_set[0]
	y_step = y_set[1] - y_set[0]
	print(f"ICSS will be mapped on XY plane in X[{x_min} {x_max}, {round(x_step, 2)}], Y[{y_min} {y_max}, {round(y_step, 2)}].\n")

# How many atoms
totalNum = int(len(shielTensor) / 4)
tarMolNum = int(totalNum - len(coorBq))
#print(totalNum, tarMolNum)

# For reading isotropic case
isotropicValue = []
for isotropicLine in shielTensor:
	if 'Isotropic =' in isotropicLine:
		isotropicValue.append(- float(isotropicLine.split()[4]))
del isotropicValue[:tarMolNum]

#print(isotropicValue)

# For reading anisotropy case
anisotropyValue = []
for anisotropyLine in shielTensor:
	if 'Anisotropy =' in anisotropyLine:
		anisotropyValue.append(- float(anisotropyLine.split()[7]))
del anisotropyValue[:tarMolNum]

#print(anisotropyValue)

# For reading XX, YX, ZX tensor
xxValue = []
yxValue = []
zxValue = []
for xxLine in shielTensor:
	if 'XX=' in xxLine:
		xxValue.append(- float(xxLine.split()[1]))
		yxValue.append(- float(xxLine.split()[3]))
		zxValue.append(- float(xxLine.split()[5]))

del xxValue[:tarMolNum]
del yxValue[:tarMolNum]
del zxValue[:tarMolNum]

#print(xxValue)
#print(yxValue)
#print(zxValue)

# For reading XY, YY, ZY tensor
xyValue = []
yyValue = []
zyValue = []
for yyLine in shielTensor:
	if 'YY=' in yyLine:
		xyValue.append(- float(yyLine.split()[1]))
		yyValue.append(- float(yyLine.split()[3]))
		zyValue.append(- float(yyLine.split()[5]))

del xyValue[:tarMolNum]
del yyValue[:tarMolNum]
del zyValue[:tarMolNum]

#print(xyValue)
#print(yyValue)
#print(zyValue)

# For reading XZ, YZ, ZZ tensor
xzValue = []
yzValue = []
zzValue = []
for zzLine in shielTensor:
	if 'ZZ=' in zzLine:
		xzValue.append(- float(zzLine.split()[1]))
		yzValue.append(- float(zzLine.split()[3]))
		zzValue.append(- float(zzLine.split()[5]))

del xzValue[:tarMolNum]
del yzValue[:tarMolNum]
del zzValue[:tarMolNum]

#print(xzValue)
#print(yzValue)
#print(zzValue)

# Tensor type defined from user
nicsTensor = "aniso"

mapValue = anisotropyValue

# write output file
icssOutput = open("ICSS_output.csv", 'w')

# For ICSS map on XY plane
if planeFlag == 1:
	icssOutput.write("XY,")

	for x_axis in x_set:
		icssOutput.write(f"{x_axis},")
	icssOutput.write("\n")

	y_count = 0
	for n_x in range(len(x_set)):
		if y_count < len(y_set):
			icssOutput.write(f"{y_set[y_count]},")
		for n_y in range(len(y_set)):
			icssOutput.write(f"{mapValue[n_x + len(y_set) * n_y]},")
		y_count += 1
		icssOutput.write("\n")

elif planeFlag == 2:
	icssOutput.write("XZ,")

	for x_axis in x_set:
		icssOutput.write(f"{x_axis},")
	icssOutput.write("\n")

	z_count = 0
	for n_x in range(len(x_set)):
		if z_count < len(z_set):
			icssOutput.write(f"{z_set[z_count]},")
		for n_z in range(len(z_set)):
			icssOutput.write(f"{mapValue[n_x + len(y_set) * n_z]},")
		z_count += 1
		icssOutput.write("\n")

elif planeFlag == 3:
	icssOutput.write("YZ,")

	for y_axis in y_set:
		icssOutput.write(f"{y_axis},")
	icssOutput.write("\n")

	z_count = 0
	for n_y in range(len(y_set)):
		if z_count < len(z_set):
			icssOutput.write(f"{z_set[z_count]},")
		for n_z in range(len(z_set)):
			icssOutput.write(f"{mapValue[n_y + len(y_set) * n_z]},")
		z_count += 1
		icssOutput.write("\n")

icssOutput.close()

