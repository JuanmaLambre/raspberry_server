from os import listdir
from os.path import isfile, join


FILES_FOLDER = 'files/'


def get_files():
    fileslist = [f for f in listdir(FILES_FOLDER) if isfile(join(FILES_FOLDER, f))]
    return sorted(fileslist)

def create_file(filename, data):
    fileslist = get_files()
    if file_exists(filename):
        raise Exception("File {} already exists".format(filename))
    newfile = open('files/'+filename, 'w')
    newfile.write(data)
    newfile.close()

def file_exists(filename):
    return filename in get_files()

def get_path(filename=''):
    return FILES_FOLDER + filename
