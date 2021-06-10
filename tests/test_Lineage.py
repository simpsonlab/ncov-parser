'''
Suite of tests for the Consensus module
'''

import unittest
import ncov.parser

test_lineage = ncov.parser.Lineage(file='data/test_lineages.csv')


class LineageTest(unittest.TestCase):
    def test_create_lineage_dictionary(self):
        lineage_dict = test_lineage.create_lineage_dictionary()
        self.assertEqual(lineage_dict['sampleA']['lineage'], 'B.1.1.7')
        self.assertEqual(lineage_dict['sampleA']['notes'], 'alt/ref/amb:18/3/0')
        self.assertEqual(lineage_dict['sampleB']['lineage'], 'B.1.1.7')
        self.assertEqual(lineage_dict['sampleC']['lineage'], 'B.1.1.7')
        self.assertEqual(lineage_dict['sampleC']['scorpio_call'], 'cB.1.1.7')
    def test_get_sample_name(self):
        sample_row = {'taxon' : 'sampleA/ARTIC/nanopolish',
                      'lineage' : 'B.1.1.43',
                      'probability' : 1.0,
                      'pangoLEARN_version' : '2021-01-06',
                      'passed_qc' : 'passed_qc'}
        expected_sample_name = 'sampleA'
        sample_name = test_lineage.get_sample_name(row=sample_row)
        self.assertEqual(sample_name, expected_sample_name)
