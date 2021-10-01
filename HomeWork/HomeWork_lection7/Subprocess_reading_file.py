import subprocess
import os

directory = os.getcwd()
util = "type "
filename = r"\Subprocess_file.txt"
filepath = util + directory + filename


def subproc_reading_file(f_filepath):
    file = subprocess.run(f_filepath, shell=True)
    return file


print(subproc_reading_file(filepath))
