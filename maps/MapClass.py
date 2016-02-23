import os

class Map:
    def __init__(self, mapname):
        os.chdir("maps")
        self.mapname = mapname
        f = open(self.mapname,'r')
        self.fieldname = f.readline().rstrip("\n")
        self.fielddate =[]
        self.objname = f.readline().rstrip("\n")
        self.costname = f.readline().rstrip("\n")
        f.close()
        os.chdir("../")

    def pm(self):
        os.chdir("maps")
        f = open(self.fieldname,'r')
        for line in f:
            line = line.rstrip("\n")
            self.fielddate.append(line.split(','))
        print (self.fielddate)
        f.close()
        os.chdir("../")
