# Parser accept TSPLIB format
# See more at: http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/
class Data:
    def __init__(self):
        self.x = []
        self.y = []
        self.count = 0
        self.load()
    
    def load(self,path):
        try:
            file = open(path)
            lines = file.readlines()
            for index, line in enumerate(lines):
                if (index < 8):
                    continue
                line = line.split(" ")
                self.x.append(int(line[1]))
                self.y.append(int(line[1]))
                self.count += 1
        finally:
            file.close()


    def get_point(self, i):
        return (self.x[i], self.y[i])

    def get_count(self):
        return self.count