import os
for folder, subfolder, file in os.walk("c:\\Users\\Maunish dave\\desktop\\doing boring stuff with python"):
    print("current folder is{}".format(folder))
    for sub in subfolder:
        print("subfolder is {}".format(sub))
    for f in file:
        print("file is {}".format(file))
