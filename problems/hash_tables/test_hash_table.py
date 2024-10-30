import unittest
from .hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_insert(self):
        arr = HashTable()
        arr.insert("Alla")
        arr.insert("Camil")
        arr.insert("Doo")
        self.assertEqual(arr.items(), [['Doo'], None, None, None, None, None, ['Camil'], None, ['Alla'], None])

    def test_insert_same_index(self):
        arr = HashTable()
        arr.insert("Alla")
        arr.insert("Lisa")
        arr.insert("Doo")
        arr.insert("Stuart")
        arr.insert("Adelle")
        arr.insert("Bob")
        arr.insert("Thomas")
        self.assertEqual(arr.items(), [['Doo', 'Thomas'], None, None, ['Lisa', 'Stuart', 'Adelle'], None, ['Bob'], None, None, ['Alla'], None])

    def test_insert_same_index1(self):
        arr = HashTable()
        arr.insert(1)
        arr.insert(3)
        arr.insert(4)
        arr.insert(3)
        arr.insert(6)
        arr.insert(0)
        self.assertEqual(arr.items(), [[0], [1], None, [3, 3], [4], None, [6], None,  None, None])

    def test_resize(self):
        arr = HashTable()
        arr.insert("Alla") #378
        arr.insert("Lisa") #393
        arr.insert("Doo") #290
        arr.insert("Stuart") #663
        arr.insert("Adelle") #683
        arr.insert("Bob") #275
        arr.insert("Thomas") #620
        arr.insert("Kate") #389
        self.assertEqual(arr.items(), [['Thomas'], None, None, ['Stuart', 'Adelle'], None, None, None, None, None, ['Kate'], ['Doo'], None, None, None, ['Bob'], None, None, ['Alla'], None])


if __name__ == '__main__':
    unittest.main()