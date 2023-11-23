import os
import shutil

src = "C:\\Users\\sackuma3\\Desktop\\sachin"
dest = "C:\\Users\\sackuma3\\Desktop\\Sachin\\Test\\"

for (root, directories, files) in os.walk(src):
    for file in files:
        if ".py" in file and ".pyc" not in file:
            try:
                shutil.copy(os.path.join(root, file), dest)
            except shutil.SameFileError as err:
                print(err)



