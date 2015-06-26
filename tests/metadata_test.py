""" Tests for the metadata module. """

import unittest
import sys

sys.path.insert(0, '../')
from myvariant.metadata import Metadata


class MetadataTest(unittest.TestCase):

    def test_get_metadata(self):
        result = Metadata.get_metadata()
        self.assertTrue(result is not None)
        self.assertTrue(result.stats['cadd'] > 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MetadataTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
