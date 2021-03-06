"""Tests for kraus_to_choi function."""
import unittest
import numpy as np

from toqito.channels.operations.kraus_to_choi import kraus_to_choi


class TestKrausToChoi(unittest.TestCase):
    """Unit test for kraus_to_choi."""

    def test_max_ent_2(self):
        """Choi matrix of the transpose map is the swap operator."""
        kraus_1 = np.array([[1, 0], [0, 0]])
        kraus_2 = np.array([[1, 0], [0, 0]]).conj().T
        kraus_3 = np.array([[0, 1], [0, 0]])
        kraus_4 = np.array([[0, 1], [0, 0]]).conj().T
        kraus_5 = np.array([[0, 0], [1, 0]])
        kraus_6 = np.array([[0, 0], [1, 0]]).conj().T
        kraus_7 = np.array([[0, 0], [0, 1]])
        kraus_8 = np.array([[0, 0], [0, 1]]).conj().T

        kraus_ops = [
            [kraus_1, kraus_2],
            [kraus_3, kraus_4],
            [kraus_5, kraus_6],
            [kraus_7, kraus_8],
        ]

        choi_res = kraus_to_choi(kraus_ops)
        expected_choi_res = np.array(
            [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
        )

        bool_mat = np.isclose(choi_res, expected_choi_res)
        self.assertEqual(np.all(bool_mat), True)


if __name__ == "__main__":
    unittest.main()
