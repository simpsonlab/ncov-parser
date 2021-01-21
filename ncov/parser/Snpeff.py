"""

"""

import os
import sys
import csv
import re

class Snpeff():
    """
    A class for processing annotated variants from SNPEff.
    """

    def __init__(self, file, delimiter="\t"):
        """
        Initilize the object
        """
        annotations = list()
        try:
            with open(file, 'r') as fh:
                reader = csv.DictReader(fh, delimiter=delimiter)
                for row in reader:
                    annotations.append(row)
            self.annotations = annotations
        except:
            pass


    def get_list_of_consequences(self):
        """

        """
        consequences = list()
        for var in self.annotations:
            consequences.append(var['Consequence'])
        self.consequences = consequences


    def has_frameshift(self):
        """
        Determine whether the annotated variant is frameshift
        """
        return 'frameshift_variant' in self.consequences
            

