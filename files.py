# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 05/09/2019
# PROGRAM: TO DELETE THE COMMON FILES IN TWO FOLDERS
import os  # PYTHON OS CONTAINS MODULES, PATH, ESCAPE CHARS
original_folder = r"/media/sameer/New Volume/redmi y1/mp3"  # PATH OF A ORIGINAL FOLDER
files = os.listdir(original_folder)

copy_folder = r"/media/sameer/New Volume/music"  # PATH OF FOLDER THAT CONTAINS COMMON FILES
copy_files = os.listdir(copy_folder)
for file in files:
    if file in copy_files:
        common_file = os.path.join("/media/sameer/New Volume/music", file)
        os.remove(common_file)  # REMOVING OF FILES
print("SUCCESSFULLY DELETED COMMON FILES")
