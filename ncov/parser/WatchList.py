"""
WatchList module
"""

import csv
import os
import sys
import re


class WatchList():
    """
    A class for handling the watch list report generated in the ncov-tools
    pipeline.
    """

    watch_list = dict()

    def __init__(self, file, delimiter='\t'):
        """
        Initialize the WatchList object and construct the watch_list dictionary
        attribute from the provided file.
        """
        watch = dict()
        samplename = str()
        with open(file, 'r') as fh:
            reader = csv.DictReader(fh, delimiter=delimiter)
            for row in reader:
                samplename = re.sub('.variants.tsv', '', row['sample'])
                if samplename in watch:
                    watch[samplename].append(row)
                else:
                    watch[samplename] = [row]
        self.watch_list = watch


    def get_mutation_string(self, sample, delimiter=','):
        """
        Returns a comma separated string of the watch list mutations.
        """
        mutations = list()
        for samplename in self.watch_list:
            if sample == samplename:
                for item in self.watch_list[samplename]:
                    mutations.append(item['mutation'])
            else:
                continue

        return delimiter.join(mutations)

