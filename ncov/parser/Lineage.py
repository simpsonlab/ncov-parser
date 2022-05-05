import csv
import re

class Lineage():
    """
    A class for handling Pangolin lineage reports.
    """

    def __init__(self, file, delimiter=',', pangolin_ver='3'):
        self.file = file
        self.delimiter = delimiter
        self.pangolin_ver = pangolin_ver
        if pangolin_ver == '3':
            self.notes_col = 'note'
        elif pangolin_ver == "4":
            self.notes_col = 'scorpio_notes'
        else:
            self.notes_col = 'scorpio_notes'



    def get_sample_name(self, row):
        """
        The sample name is obtained from the 'taxon' field.  Note that ONT
        consensus FASTA files are generated as "<sample>/ARTIC/nanopolish"
        whereas Illumina runs (iVar) use "Consensus_<sample>"
        """
        sample_name = row['taxon']
        sample_name = re.sub('^Consensus_', '', sample_name) # added by ivar
        sample_name = re.sub('.primertrimmed.consensus_threshold_0.75_quality_20', '', sample_name) # added by ivar
        sample_name = re.sub('_MN908947.3', '', sample_name) # added by pangolin
        sample_name = re.sub('/ARTIC/nanopolish', '', sample_name) # added by ARTIC
        sample_name = re.sub('/ARTIC/medaka', '', sample_name) # added by ARTIC
        return sample_name
            

    def get_lineage(self, row):
        """
        Return the lineage value
        """
        return row['lineage']


    def get_notes(self, row):
        """
        Return the notes that pangolin added to the lineage assignment
        """
        n = row[self.notes_col]
        if n.startswith('scorpio call'):
            n_dict = n.split(' ')
            alt = re.sub(';', '', n_dict[4])
            ref = re.sub(';', '', n_dict[7])
            amb = re.sub(';', '', n_dict[10])
            tag = 'alt/ref/amb:'
            value = '/'.join([alt, ref, amb])
            return ''.join([tag, value])
        else:
            return "none"


    def get_scorpio_call(self, row, colname='scorpio_call'):
        """
        Return the scorpio_call value
        """
        return row[colname]

    
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
                notes = self.get_notes(row=row)
                scorpio_call = self.get_scorpio_call(row=row)
                lineage_dict[sample] = { "lineage":lineage, "notes":notes, "scorpio_call": scorpio_call }
        self.lineage_dict = lineage_dict
        return lineage_dict

