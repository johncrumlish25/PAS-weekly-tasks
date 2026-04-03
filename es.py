# es.py
# Reads in a text file and outputs the number of e's it contains
# Author: John Crumlish

import sys # Reads arguments from the command line
import os  # Checks does file exist

# Check if a file name was given - found sys module on W3Schools
if len(sys.argv) < 2: # if it is less than 2 then the file doesn't exist
    print("Error: No filename given")
else:
    FILENAME = sys.argv[1]

    # Check if file exists
    if os.path.exists(FILENAME):
        f = open(FILENAME, "r")
        text = f.read()
        print(text.count("e"))
        f.close()
    else:
        print("Error: File does not exist")