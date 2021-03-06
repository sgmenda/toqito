"""Tests for is_commuting function."""
import unittest
import numpy as np

from toqito.linear_algebra.properties.is_commuting import is_commuting


class TestIsCommuting(unittest.TestCase):
    """Unit test for is_commuting."""

    def test_is_commuting_false(self):
        """Test if non-commuting matrices return False."""
        mat_1 = np.array([[0, 1], [0, 0]])
        mat_2 = np.array([[1, 0], [0, 0]])
        self.assertEqual(is_commuting(mat_1, mat_2), False)

    def test_is_commuting_true(self):
        """Test commuting matrices return True."""
        mat_1 = np.array([[1, 0, 0], [0, 1, 0], [1, 0, 2]])
        mat_2 = np.array([[2, 4, 0], [3, 1, 0], [-1, -4, 1]])
        self.assertEqual(is_commuting(mat_1, mat_2), True)


if __name__ == "__main__":
    unittest.main()
