import os 

directory_path = "/users/hp/OneDrive/Documents/"

contents = os.listdir(directory_path)

# If you want to list files in a vertical manner
for item in contents:
    print(item)

# If you want to list files in a horizontal manner
print(contents)