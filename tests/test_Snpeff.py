"""
Suite of tests for the Snpeff module
"""

import unittest
import ncov.parser

test_snpeff = ncov.parser.Snpeff(file='data/sampleA_aa_table.tsv')
test_snpeff.get_list_of_consequences()

class SnpeffTest(unittest.TestCase):
    def test_has_frameshift(self):
        self.assertTrue(test_snpeff.has_frameshift())

