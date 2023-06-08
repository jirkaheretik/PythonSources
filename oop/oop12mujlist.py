class MujList:
    def __init__(self, seznam):
        self._list = seznam

    def getList(self):
        return self._list

    def __str__(self):
        return str(self._list)

    def __add__(self, seznam):
        result = []
        for idx, val in enumerate(seznam.getList()):
            result.append( self._list[idx] + val)
        return MujList(result)

    def __sub__(self, seznam):
        result = []
        for idx, val in enumerate(seznam.getList()):
            result.append(self._list[idx] - val)
        return MujList(result)

    def __mul__(self, seznam):
        result = []
        for idx, val in enumerate(seznam.getList()):
            result.append(self._list[idx] * val)
        return MujList(result)

    def __truediv__(self, seznam):
        result = []
        for idx, val in enumerate(seznam.getList()):
            result.append(self._list[idx] / val)
        return MujList(result)


# MAIN:
levy = MujList([1, 2, 3, 4, 5])
pravy = MujList([5, 4, 3, 2, 1])
print(f"{levy} + {pravy} = {levy+pravy}")
print(f"{levy} - {pravy} = {levy-pravy}")
print(f"{levy} * {pravy} = {levy*pravy}")
print(f"{levy} / {pravy} = {levy/pravy}")
