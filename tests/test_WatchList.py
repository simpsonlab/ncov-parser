"""
Suite of tests for the WatchList module
"""

import unittest
import ncov.parser

test_watch = ncov.parser.WatchList(file='data/testrun_ncov_watch_variants.tsv')
expected_mutation_string = 'S:del69-70,S:del144,S:A570D,S:P681H,S:T716I,S:S982A'

class WatchListTest(unittest.TestCase):
    def test_get_mutation_string(self):
        self.assertEqual(test_watch.get_mutation_string(sample='sampleA'),
                         expected_mutation_string)
