
"""
fileUnderReplacer.py
"""

import os.rename
import glob
files = glob.glob('*(*).*')
print(files)
for file in files:
    new_name = file.replace("(", "")
    new_name2 = new_name.replace(")", "")
    print(new_name2)
    os.rename(file, new_name2)
