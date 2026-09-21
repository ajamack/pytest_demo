"""
test_boggle_solver.py

Black-box unit tests for Boggle (boggle_solver.py), built using the
Category Partition Method.
"""

import unittest
from boggle_solver import Boggle


class TestBoggleSolver(unittest.TestCase):

    def test_empty_dictionary(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        solver = Boggle(grid, [])
        self.assertEqual(solver.getSolution(), [])

    def test_empty_grid(self):
        solver = Boggle([], ["cat"])
        self.assertEqual(solver.getSolution(), [])

    def test_single_word_reachable(self):
        grid = [["C", "A", "T"]]
        solver = Boggle(grid, ["cat"])
        self.assertEqual(solver.getSolution(), ["cat"])

    def test_word_not_in_grid(self):
        grid = [["D", "O", "G"]]
        solver = Boggle(grid, ["cat"])
        self.assertEqual(solver.getSolution(), [])

    def test_words_too_short(self):
        grid = [["A", "B"]]
        solver = Boggle(grid, ["ab"])
        self.assertEqual(solver.getSolution(), [])
    def test_multiple_words(self):
        grid = [["C", "A"], ["T", "S"]]
        solver = Boggle(grid, ["cat", "cats"])
        self.assertEqual(solver.getSolution(), ["cat", "cats"])
    def test_qu_tile(self):
      grid = [["Qu", "A"]]
      solver = Boggle(grid, ["qua"])
      self.assertEqual(solver.getSolution(), ["qua"])
    def test_st_tile(self):
      grid = [["St", "A", "R"]]
      solver = Boggle(grid, ["star"])
      self.assertEqual(solver.getSolution(), ["star"])
    def test_no_reuse_cell(self):
      grid = [["A", "B"]]
      solver = Boggle(grid, ["aba"])
      self.assertEqual(solver.getSolution(), [])
    def test_all_same_letter(self):
      grid = [["A", "A"], ["A", "A"]]
      solver = Boggle(grid, ["aaa"])
      self.assertEqual(solver.getSolution(), ["aaa"])

if __name__ == "__main__":
  unittest.main()