from os import path

def createFile(dest):
    if not(path.isfile(dest)):
        f = open(dest,'w')
        f.write('Welcome to python scripting.')
        f.close()

dest = 'D:\\VS Code\\Python\\Simplilearn-Python for Beginners\\sample.txt'
createFile(dest)

print("File created")