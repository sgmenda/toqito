"""Tests for gen_bell function."""
import unittest
import numpy as np

from toqito.states.states.bell import bell
from toqito.states.states.gen_bell import gen_bell


class TestGenBell(unittest.TestCase):
    """Unit test for gen_bell."""

    def test_gen_bell_0_0_2(self):
        """Generalized Bell state for k_1 = k_2 = 0 and dim = 2."""
        dim = 2
        k_1 = 0
        k_2 = 0

        expected_res = bell(0) * bell(0).conj().T

        res = gen_bell(k_1, k_2, dim)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_gen_bell_0_1_2(self):
        """Generalized Bell state for k_1 = 0, k_2 = 1 and dim = 2."""
        dim = 2
        k_1 = 0
        k_2 = 1

        expected_res = bell(1) * bell(1).conj().T

        res = gen_bell(k_1, k_2, dim)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_gen_bell_1_0_2(self):
        """Generalized Bell state for k_1 = 1, k_2 = 0 and dim = 2."""
        dim = 2
        k_1 = 1
        k_2 = 0

        expected_res = bell(2) * bell(2).conj().T

        res = gen_bell(k_1, k_2, dim)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_gen_bell_1_1_2(self):
        """Generalized Bell state for k_1 = 1, k_2 = 1 and dim = 2."""
        dim = 2
        k_1 = 1
        k_2 = 1

        expected_res = bell(3) * bell(3).conj().T

        res = gen_bell(k_1, k_2, dim)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)


if __name__ == "__main__":
    unittest.main()
