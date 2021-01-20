'''
Suite of tests for the Consensus module
'''

import unittest
import ncov.parser

test_lineage = ncov.parser.Lineage(file='data/sample_lineages.csv')


class LineageTest(unittest.TestCase):
    def test_create_lineage_dictionary(self):
        lineage_dict = test_lineage.create_lineage_dictionary()
        self.assertEqual(lineage_dict['sampleA'], 'B.1.1.43')
        self.assertEqual(lineage_dict['sampleB'], 'B.1.36')
        self.assertEqual(lineage_dict['sampleC'], 'B.1.1.7')

