import os 

directory_path = "/users/hp/OneDrive/Documents/"

contents = os.listdir(directory_path)

for item in contents:
    print(item)