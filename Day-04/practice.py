import sys
import os

# Accessing command-line arguments using sys.argv
script_name = sys.argv[0]
arguments = sys.argv[1:]

# Getting the absolute path of the script using os.path
script_path = os.path.abspath(script_name)

print(f'Script Name:', script_name)
print(f'Arguments:', arguments)
print(f'Script Path:', script_path)