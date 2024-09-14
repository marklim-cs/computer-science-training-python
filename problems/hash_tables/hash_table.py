import copy


class HashTable:
    def __init__(self):
        self._array = [None, None, None, None, None, None, None, None, None, None]
        self._counter = 0

    def _hash_function(self, value, arr):
        length = len(arr)
        sum_ord = 0
        for char in value:
            sum_ord += ord(char)

        index = sum_ord % length
        return index

    def insert(self, value):
        if self._counter / len(self._array) > 0.7:
            self._resize()

        index = self._hash_function(value, self._array)

        if self._array[index] is None:
            self._array[index] = []
            self._array[index].append(value)
            self._counter += 1
        else:
            self._array[index].append(value)
            self._counter += 1

    def _resize(self):
        large_array = [None for _ in range(len(self._array) * 2)]

        for bucket in self._array:
            if bucket is not None:
                for value in bucket:
                    index = self._hash_function(value, large_array)
                    if large_array[index] is None:
                        large_array[index] = []
                    large_array[index].append(value)

        self._array = large_array

        return self._array

    def items(self):
        copied_arr = copy.deepcopy(self._array)
        return copied_arr