import time
class DataStructure:
    def __init__(self):
        self.struct = {}
        self.response = []

    def add(self, key, value):
        accessed_at = time.time()
        self.struct[key] = [value, accessed_at]

    def get(self, key):
        if key in self.struct:
            self.struct[key][1] = time.time()
            self.response.append(self.struct[key][0])
        else:
            self.response.append('-1')

    def remove(self, key):
        if key in self.struct:
            self.response.append(self.struct[key][0])
            del self.struct[key]
        else:
            self.response.append('-1')

    def evict(self):
        smallest_time = time.time()
        key = None
        for i in self.struct:
            if self.struct[i][1] <= smallest_time:
                smallest_time = self.struct[i][1]
                key = i
        del self.struct[key]
    
    def exit(self):
        return self.response


def doOperation(input):
    dataS = DataStructure()
    for element in input:
        array = element.split(' ')
        method = array[0]
        if method == 'add':
            dataS.add(array[1], array[2])
        elif method == 'get':
            dataS.get(array[1])
        elif method == 'remove':
            dataS.remove(array[1])
        elif method == 'evict':
            dataS.evict()
        else:
            return dataS.response

input = ["add 5 3", "add 1 2", "get 5", "evict","get 1", "remove 5", "exit"]
print(doOperation(input))
# string = "take me to there"
# print(string.split(' '))
