import os

# Import a function from a module
from os import chdir

# Import multiple function from a module
from os import getcwd, chdir

# Using an os function
os.getcwd()

# Assign to a variable
work_dir = os.getcwd()

# Changing directory
os.chdir("/home/alimansour")

# Check the current directory
os.getcwd()

# Get the local environment
print(os.environ)
