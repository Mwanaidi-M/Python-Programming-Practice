import pathlib
import os
import fnmatch
import tempfile
import zipfile
import fileinput


with open('seen.txt', 'w') as m_writer:
    m_writer.write(f"Email Slicer is a simple tool that will take an email address.\n")
    m_writer.write(f"as input and slice it to produce the username and the domain associated with it.\n")
    m_writer.write(f"The email must be divided into two strings by using ‘@’ as the separator.\n")


# os.scandir() creates an iterator that you can use to loop through the iterator and get contents in the path
# with os.scandir(r"C:\my_pathmy_path") as m_reader:
#     for entry in m_reader:
#         print(entry.name)


# pathlib.Path() is another alternative, it has an iterdir() method that returns an iterator
# the iterator can be used to loop over the contents in the path
with pathlib.Path(r"C:\my_path") as m_viewer:
    for entry in m_viewer.iterdir():
        pass

# check if the entries in the path are subdirectories i.e. filter out directories only
with pathlib.Path(r"C:\my_path") as m_viewer:
    for entry in m_viewer.iterdir():
        # if entry.is_file():
        if entry.is_dir():
            pass

# check if the entries in the path are files i.e. filter out files only
with os.scandir(r"C:\my_path") as m_entries:
    for entry in m_entries:
        if entry.is_file():
            pass

# view file attributes in a given path
with pathlib.Path(r"C:\my_path") as m_viewer:
    for entry in m_viewer.iterdir():
        # print(entry.stat().st_mtime_ns)
        pass

# create a single directory
with pathlib.Path(r"C:\my_path\polsa") as m_viewer:
    m_viewer.mkdir(exist_ok=True)

# create a nested directory path
os.makedirs(r"m1\m_child\m_grand_child", exist_ok=True)


# view files that match a certain pattern in this case, files that start with 's'
with os.scandir(r"C:\my_path") as m_viewer:
    for entry in m_viewer:
        if entry.name.startswith(r"s"):
            # print(entry.name)
            pass

# view files that match a certain pattern in this case, all files ending with .jpg
with pathlib.Path(r"C:\my_path") as m_viewer:
    for entry in m_viewer.iterdir():
        if entry.name.endswith('.jpg'):
            # print(entry.name)
            pass

# view files ending with .png using the fnmatch module
with pathlib.Path(r"C:\my_path") as m_viewer:
    for entry in m_viewer.iterdir():
        if fnmatch.fnmatch(entry.name, '*.png'):
            # print(entry.name)
            pass


# view files that have an extension beginning with 'p' using the glob method
with pathlib.Path(r"C:\my_path") as m_viewer:
    for entry in m_viewer.glob("*.p*"):
        # print(entry.name)
        pass


# traversing a path/directory tree to get its contents
for dirpath, dirnames, filenames in os.walk(r"C:\my_path"):
    # print(f"{dirpath}-----{dirnames}------{filenames}")
    pass


# creating a temporary file, write into it then get its name & location
with tempfile.TemporaryFile('w+t') as m_temp:
    # m_temp.write('There you go.\nHave a nice day.\nLorem.\nIpsum.')
    # print(f"Temprary File created: {m_temp.name}")
    # m_temp.seek(0)
    # print(m_temp.read())
    pass


# create a temporary directory, show its location & name & also confirm that its present in the os
with tempfile.TemporaryDirectory() as tmpdir:
    # print(f"Temprary Directory created: {tmpdir}")
    # print(os.path.exists(tmpdir))
    pass


with tempfile.NamedTemporaryFile('w+t') as mr:
    # mr.write('There is somethin')
    # print(f"File created: {mr.name}")
    # mr.seek(0)
    # print(mr.read())
    pass

# give a file path
file_path = r'free3.txt'

# check if the path give is of an actual file then delete the file if so.
if os.path.isfile(file_path):
    os.unlink(file_path)
else:
    print("The file is not there")

# does the same operation as above
if pathlib.Path(file_path).is_file():
    pathlib.Path(file_path).unlink(missing_ok=True)
else:
    print("The file is not there")


file_dest = r'D:\Python_Pracs\m_backup'

# rename the folder using any of the methods below.
pathlib.Path(file_dest).rename('my_backup')

os.rename(r'D:\Python_Pracs\my_backup', 'new_backup')


# To read contents from a zip file, create a ZipFile object
# To get a list of files in the archive, call namelist() on the ZipFile object.
with zipfile.ZipFile(r"C:\my_path\amcharts_weather_icons_1.0.0.zip", "r") as my_zip:
    print(my_zip.namelist())
    # To get/show specific info on the contents in the zip file
    for entry in my_zip.infolist():
        print(f"{entry.filename} ----- {entry.file_size}")


# To extract all the contents from a zipfile to a certain path
print(zipfile.ZipFile(r"C:\my_path\amcharts_weather_icons_1.0.0.zip", "r").extractall(r"D:\my_path"))

# To extract a particular file in the zip file to another location.
print(zipfile.ZipFile(r"C:\my_path\mysqlsampledatabase.zip", "r").extract("mysqlsampledatabase.sql", r"D:\my_path\m1"))


# To create a zip file, open the ZipFile object in 'w'/write mode
# you can create a list of your files that you want to zip
# loop through the files list and write them to the ZipFile object
file_list = ['seen.txt', 'mysqlsampledatabase.sql', 'sample3.txt']
with zipfile.ZipFile('testing_zip.zip', 'w') as zip_writer:
    for fl in file_list:
        zip_writer.write(fl)


# To add files to an existing zip file, open the ZipFile object in 'a'/append mode & add the files.
with zipfile.ZipFile('testing_zip.zip', 'a') as zip_writer:
    zip_writer.write('restaurant.py')


# create an instance of the FileInput class, which can be iterated.
files = fileinput.input()

# loop through the instance and print each line in the file
for line in files:
    if fileinput.isfirstline():
        # Return the name of the file currently being read.
        print(f"---------- Reading from {fileinput.filename()}--------------")
    print(f"-> {line}")
print()

