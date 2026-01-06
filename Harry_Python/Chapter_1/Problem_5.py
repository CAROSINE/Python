import os

# Select the directory whose  content I want to list
directory_path = '/New folder'

# Use the os module to list the directory content
contents = os.listdir(directory_path)

# Print the contents of the directory 
for item in contents:
    print(item)