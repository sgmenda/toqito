"""Tests for tile function."""
import unittest
import numpy as np

from toqito.core.ket import ket
from toqito.states.states.tile import tile


class TestTile(unittest.TestCase):
    """Unit test for tile."""

    def test_tile_0(self):
        r"""Generate the Tile state for index = 0:
        .. math::
            |\psi_0 \rangle = \frac{1}{\sqrt{2}} |0 \rangle
            \left(|0\rangle - |1\rangle \right).
        """
        e_0, e_1 = ket(3, 0), ket(3, 1)
        expected_res = 1 / np.sqrt(2) * e_0 * (e_0 - e_1)
        res = tile(0)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_tile_1(self):
        r"""Generate the Tile state for index = 1:
        .. math::
            |\psi_1\rangle = \frac{1}{\sqrt{2}}
            \left(|0\rangle - |1\rangle \right) |2\rangle
        """
        e_0, e_1, e_2 = ket(3, 0), ket(3, 1), ket(3, 2)
        expected_res = 1 / np.sqrt(2) * (e_0 - e_1) * e_2
        res = tile(1)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_tile_2(self):
        r"""Generate the Tile state for index = 2:
        .. math::
            |\psi_2\rangle = \frac{1}{\sqrt{2}} |2\rangle
            \left(|1\rangle - |2\rangle \right)
        """
        e_1, e_2 = ket(3, 1), ket(3, 2)
        expected_res = 1 / np.sqrt(2) * e_2 * (e_1 - e_2)
        res = tile(2)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_tile_3(self):
        r"""Generate the Tile state for index = 3:
        .. math::
            |\psi_3\rangle = \frac{1}{\sqrt{2}}
            \left(|1\rangle - |2\rangle \right) |0\rangle
        """
        e_0, e_1, e_2 = ket(3, 0), ket(3, 1), ket(3, 2)
        expected_res = 1 / np.sqrt(2) * (e_1 - e_2) * e_0
        res = tile(3)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_tile_4(self):
        r"""Generate the Tile state for index = 4:
        .. math::
            |\psi_4\rangle = \frac{1}{3}
            \left(|0\rangle + |1\rangle + |2\rangle)\right)
            \left(|0\rangle + |1\rangle + |2\rangle.
        """
        e_0, e_1, e_2 = ket(3, 0), ket(3, 1), ket(3, 2)
        expected_res = 1 / 3 * (e_0 + e_1 + e_2) * (e_0 + e_1 + e_2)
        res = tile(4)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_tile_invalid(self):
        """Ensures that an integer above 4 is error-checked."""
        with self.assertRaises(ValueError):
            tile(5)


if __name__ == "__main__":
    unittest.main()
