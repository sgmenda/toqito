"""Tests for apply_map function."""
import unittest
import numpy as np

from toqito.channels.operations.apply_map import apply_map
from toqito.perms.swap_operator import swap_operator


class TestApplyMap(unittest.TestCase):
    """Unit test for apply_map."""

    def test_apply_map_choi(self):
        """
        The swap operator is the Choi matrix of the transpose map.

        The following test is a (non-ideal, but illustrative) way of computing
        the transpose of a matrix.
        """
        test_input_mat = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

        expected_res = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        res = apply_map(test_input_mat, swap_operator(3))

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_apply_map_kraus(self):
        """
        Apply Kraus map.

        The following test computes PHI(X) where X = [[1, 2], [3, 4]] and
        where PHI is the superoperator defined by:
        Phi(X) = [[1,5],[1,0],[0,2]] X [[0,1][2,3][4,5]].conj().T -
        [[1,0],[0,0],[0,1]] X [[0,0][1,1],[0,0]].conj().T
        """
        test_input_mat = np.array([[1, 2], [3, 4]])

        kraus_1 = np.array([[1, 5], [1, 0], [0, 2]])
        kraus_2 = np.array([[0, 1], [2, 3], [4, 5]])
        kraus_3 = np.array([[-1, 0], [0, 0], [0, -1]])
        kraus_4 = np.array([[0, 0], [1, 1], [0, 0]])

        expected_res = np.array([[22, 95, 174], [2, 8, 14], [8, 29, 64]])

        res = apply_map(test_input_mat, [[kraus_1, kraus_2], [kraus_3, kraus_4]])

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)


if __name__ == "__main__":
    unittest.main()
