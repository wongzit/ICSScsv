# ICSScsv v1.0
![ICSScsv_full](https://user-images.githubusercontent.com/41381763/115954588-ceb45180-a52c-11eb-9aac-94099a09b8e7.png)
A program for extracting magnetic shielding tensor from ICSS calculation output.

**ICSScsv homepage** https://www.wangzhe95.net/program-icsscsv

First released at 2021-04-23.

Last updated at 2021-04-24.

Author: Zhe Wang

## Update history
### 2021-04-26
ICSS map of benzene created by ICSScsv and Origin Pro 2021 has been uploaded into **example** folder.

### v1.0 (2021-04-24): Main feature
1. Improved output file reading.
2. Executable file for macOS/Linux/Microsoft Windows are released.
3. User can choose isotropic, anisotropy, and other component for ICSS map.

### v0.2 (2021-04-23)
1. First beta release!

## Platform
### For all platform
Python source code is provided, if your computer already installed Python IDE, you can run ICSSgen with:

`python3 ICSScsv_v10_source.py`

Executable files for macOS/Linux/Windows are in **execufiles.zip**.

**NOTICE:** Python 3.7 or newer is recommended, ICSScsv may not work normally under Python 2.

### For macOS
Executable file **ICSScsv_v10_mac** has been tested on macOS Catalina 10.15.7 (Intel Mac) and Big Sur 11.2.3 (Intel/M1 Mac).

### For Linux
Before running for the first time, you may need to add permission by:
`chmod +x ./path_to_ICSScsv/ICSScsv_v10_linux`

Add following command to environmental variables (for bash):
`alias icsscsv=./path_to_ICSScsv/ICSScsv_v10_linux`
and you can run ICSSgen by `icsscsv`.

### For Microsoft Windows
Executable file **ICSScsv_v10_win.exe** has been tested on Windows 10 Education (x64) with Intel Core i7-10700. Double click to run it.

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
