import unittest
from src.bubble_sort import bubble_sort
from src.insertion_sort import insertion_sort
from src.merge_sort import merge_sort
from src.quick_sort import quick_sort
from src.geraVetor import geraVetor

class TestAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        vetor = geraVetor(10000)
        sorted_vetor = sorted(vetor)
        bubble_sort(vetor)
        self.assertEqual(vetor, sorted_vetor)

    def test_insertion_sort(self):
        vetor = geraVetor(10000)
        sorted_vetor = sorted(vetor)
        insertion_sort(vetor)
        self.assertEqual(vetor, sorted_vetor)

    def test_merge_sort(self):
        vetor = geraVetor(10000)
        sorted_vetor = sorted(vetor)
        merge_sort(vetor)
        self.assertEqual(vetor, sorted_vetor)

    def test_quick_sort(self):
        vetor = geraVetor(10000)
        sorted_vetor = sorted(vetor)
        vetor = quick_sort(vetor)
        self.assertEqual(vetor, sorted_vetor)

if __name__ == '__main__':
    unittest.main()