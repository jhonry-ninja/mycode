#!/usr/bin/env python3

import shutil # The shutil (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs.
import os # The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.

os.chdir('/home/student/mycode/') # allows the user to run the program from any location on the system

shutil.move('raynor.obj', 'ceph_storage/') # moves the file or folder at the path source to the path destination and will return a string of the absolute path of the new location. If destination points to a folder, the source file gets moved into destination and keeps its current filename.
# NOTE: If there had been a raynor.obj file already in the destination folder ~/home/student/mycode/ceph_storage/, it would have been overwritten. Since it’s easy to accidentally overwrite files in this way, you should take some care when using move().

xname = input('What is the new name for kerrigan.obj? ') # Promptthe user for a new name for the kerrigan.obj file.

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # Renames the current kerrigan.obj file.
