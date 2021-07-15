import Data
data = Data()
data.load('fra1488.tsp')

for i in data.get_count():
    print(data.get_point(i))
