# ICSScsv v3.1
![ICSScsv_icon](ICSScsv_icon.png)

Extract magnetic shielding tensor from ICSS calculation output.

**Homepage** https://www.wangzhe95.net/program-icsscsv

First released at 2021-04-23

Last updated at 2021-05-24

Author: Zhe Wang

ORCiD: [0000-0002-9996-586X](https://orcid.org/0000-0002-9996-586X)

## Statement of need
2D isochemical shielding surface (2D-ICSS) maps, also known as 2D-NICS (nuclear independent
chemical shift) maps, are useful tools for investigating the aromaticity of cyclic molecules.
A large number of ghost atoms, in addition to the target molecules, must be included in the
input file for 2D-ICSS calculations. After completing the calculations, the magnetic shielding
tensors of all ghost atoms must be extracted from the output files. This process is a huge and
tiresome task; therefore, we present ICSSgen and ICSScsv, two open-source, highly efficient,
and user-friendly Python programs, to easily generate 2D-ICSS maps.

More information about ICSSgen, please check [ICSSgen](https://github.com/wongzit/ICSSgen)

## Update history
### v3.1 (2021-07-14)
1. Now ICSScsv would show the 2D-ICSS map after processing the output file, and the .png file would be saved in the same folder.
2. Example updated. ICSScsv relies on the external library *numpy* and *matplotlib*. Make sure you have installed these lib if you plan to run ICSScsv with source code.
4. Executable files were removed due to the large file size excessed the limitation of GitHub. Please download from [here](https://www.wangzhe95.net/program-icsscsv).
5. Older version could be download from release page.

### v2.2 (2021-05-24)
Bug fixed.

### v2.0 (2021-05-11)
Minor bugs fix.

### v1.0 (2021-04-24): Main feature
1. Improved output file reading.
2. Executable file for macOS/Linux/Microsoft Windows are released.
3. User can choose isotropic, anisotropy, and other component for ICSS map.

### v0.2 (2021-04-23)
First beta release!

## How to run
For detail information, please check the user manual.

### For all platform
Python source code is provided, if your computer already installed Python IDE, you can run ICSScsv with:

`python3 ICSScsv_vxx_source.py`

Executable files for macOS/Linux/Windows are in **execufiles.zip**.

**NOTICE:** Python 3.7 or newer is recommended, ICSScsv may not work normally under Python 2.

### For macOS
1. Double click the executable file **ICSScsv_vxx_mac**.
2. Package with source code. If for some reason the (1) could not work, you can package 
ICSScsv by yourself. For more information, please check the manual.

### For Linux
Before running for the first time, you may need to add permission by:
`chmod +x ./path_to_ICSScsv/ICSScsv_vxx_linux`

Add following command to environmental variables (for bash):
`alias icsscsv=./path_to_ICSScsv/ICSScsv_vxx_linux`
and you can run ICSScsv by `icsscsv`.

### For Microsoft Windows
Executable file **ICSScsv_vxx_win.exe** has been tested, Double click to run it.

## How to use
1. Run ICSScsv.
2. Drag the ICSS output file to the command windows, and press enter.
3. Choose which component will be used for ICSS map.
'''
      1 - Isoptropic       2 - Anisotropy
      3 - XX component     4 - YX component     5 - ZX component
      6 - XY component     7 - YY component     8 - ZY component
      9 - XZ component    10 - YZ component    11 - ZZ component
'''

4. A .csv file including shielding tensor would be generated in the same dictionary as the output file.

## From author
If you found any bugs, please contact me (wongzit@yahoo.co.jp).

More information about me, please check my [personal website](https://www.wangzhe95.net).

 **Hope you enjoy this program!**
