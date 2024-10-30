import copy


class HashTable:
    def __init__(self):
        self._array = [None, None, None, None, None, None, None, None, None, None]
        self._counter = 0

    def _hash_function(self, value, arr):
        num_value = hash(value)
        length = len(arr)
        index = num_value % length

        return index


    def insert(self, value):
        if self.load_factor(self._counter, len(self._array))[1]:
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

    def load_factor(self, counter: int, length: int) -> tuple:
        factor = counter / length

        if factor >= 0.7:
            return factor, True
        else:
            return factor, False