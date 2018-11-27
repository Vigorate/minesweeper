import os
import random

# Go through already existing names, and renaming the current one as a vacant name

path = "C:/Users/alexl/Desktop/e/"
files = os.listdir(path)
for file in files:
    print(file)
disp_name = []
for i in range(1, len(files) + 1):
    disp_name.append(i)
for file in files:
    idx = random.randint(1, len(disp_name) - 1)
    new_name = str(disp_name[idx]) + "." + file.split(".")[1]
    print(file, "New Name", new_name)
    while new_name in files:
        print(str(disp_name[idx]) + "." + file.split(".")[1], "Already Existed")
        idx = random.randint(1, len(disp_name) - 1)
        new_name = str(disp_name[idx]) + "." + file.split(".")[1]
    os.rename(path + file, path + str(disp_name[idx]) + "." + file.split(".")[1])
    del disp_name[idx]


# path = "C:/Users/alexl/Desktop/e/"
# files = os.listdir(path)
# disp_name = []
# for i in range(1, len(files) + 1):
#     disp_name.append(i)
# for file in files:
#     idx = random.randint(1, len(disp_name) - 1)
#     new_name = str(disp_name[idx]) + "." + file.split(".")[1]
#     print(file, "New Name", new_name)
#     while new_name in files:
#         print(str(disp_name[idx]) + "." + file.split(".")[1], "Already Existed")
#         idx = random.randint(1, len(disp_name) - 1)
#         new_name = str(disp_name[idx]) + "." + file.split(".")[1]
#     os.rename(path + file, path + str(disp_name[idx]) + "." + file.split(".")[1])
#     del disp_name[idx]
