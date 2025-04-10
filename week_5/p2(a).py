# 2.a Using os and sys Modules:
# Write a Python program that prints the current working directory, lists files in a directory, and prints the Python version.

import os
import sys

print("Current Working Directory:", os.getcwd())
print()
print("Files in Directory:", os.listdir('.'))
print()
print("Python Version:", sys.version)
