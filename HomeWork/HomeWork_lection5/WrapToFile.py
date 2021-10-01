import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            temp = open(self.filepath, "r")
            temp_text = temp.read()
            temp.close()
            return temp_text
        except FileNotFoundError:
            return "File not found"

    @content.setter
    def content(self, value):
        try:
            temp = open(self.filepath, "w")
            temp_text = temp.write(value)
            temp.close()
        except FileExistsError:
            print("Couldn't write into file")

    @content.deleter
    def content(self):
        os.remove(self.filepath)


WSTF = WrapStrToFile()
print(WSTF.content)
WSTF.content = 'test str'
print(WSTF.content)
WSTF.content = 'text'
print(WSTF.content)
del WSTF.content
