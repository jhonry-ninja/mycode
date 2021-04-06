#!/usr/bin/env python3

# import additional code to complete our task
import shutil # The shutil (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs.
import os # The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.

# move into the working directory
os.chdir("/home/student/mycode/") # This will allow the user to run the program from any location on the system, and our script still always start at /home/student/mycode/




# copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy") # This will copy the file at the path source to the folder at the path destination

# copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/") # This will copy an entire folder and every folder and file contained in it

