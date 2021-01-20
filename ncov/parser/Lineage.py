import csv
import re

class Lineage():
    """
    A class for handling Pangolin lineage reports.
    """

    def __init__(self, file, delimiter=','):
        self.file = file
        self.delimiter = delimiter


    def get_sample_name(self, row):
        """
        The sample name is obtained from the 'taxon' field.  Note that ONT
        consensus FASTA files are generated as "<sample>/ARTIC/nanopolish"
        whereas Illumina runs (iVar) use "Consensus_<sample>"
        """
        samplename = row['taxon'].split('/')[0]
        if samplename.startswith('Consensus_'):
            samplename = re.sub('Consensus_', '', samplename)
        return samplename
            

    def get_lineage(self, row):
        """
        Return the lineage value
        """
        return row['lineage']

    
    def create_lineage_dictionary(self):
        """
        Create a dictionary containing sample names as key and their lineage as
        the value
        """
        lineage_dict = dict()
        with open(self.file, 'r') as fh:
            reader = csv.DictReader(fh, delimiter=self.delimiter)
            for row in reader:
                sample = self.get_sample_name(row=row)
                lineage = self.get_lineage(row=row)
                lineage_dict[sample] = lineage
        self.lineage_dict = lineage_dict
        return lineage_dict

