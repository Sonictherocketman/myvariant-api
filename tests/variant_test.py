""" Tests for the variants module. """

import unittest
import sys

sys.path.insert(0, '../')
from myvariant.variant import Variant


class VariantTest(unittest.TestCase):

    def test_find_by(self):
        res = Variant.find_by(query='chr1:69000-70000')
        self.assertEqual(len(res), 3)
        for r in res:
            self.assertEqual(r.cadd['chrom'], 1)

    def test_get(self):
        res = Variant.get('chr1:g.35367G>A')
        self.assertTrue(res is not None)
        self.assertEqual(res.cadd['chrom'], 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(VariantTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
