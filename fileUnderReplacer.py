
"""
fileUnderReplacer.py
"""

import os.rename
import glob
files = glob.glob('*_*')
for file in files:
    new_name = file.replace("_", " ")
    os.rename(file, new_name)
