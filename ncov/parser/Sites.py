'''
A set of classes and functions to handle parsing a set of positions
and locating them inside a VCF file for annotation.
'''
import vcf
import csv

class Sites():
    '''
    A class for handling genomic sites from a VCF file.
    '''

    def __init__(self):
        '''
        initialize the object
        '''
        pass

def import_sites(file, safe_list=None):
    '''
    Import a file containing positions or regions to annotate.
    '''
    vcf_reader = vcf.Reader(filename=file)
    sites = dict()
    for var in vcf_reader:
        var_alt = list()
        for _alt in var.ALT:
            var_alt.append(str(_alt))
        var_alt_string = ''.join(var_alt)            
        if safe_list:
            if str(var.POS) in safe_list:
                print("position found in safe list, skipping...")
                continue
        if var.CHROM not in sites:
            sites[var.CHROM] = {str(var.POS) : {'ref': var.REF, 'alt': var_alt_string}}
        else:
            sites[var.CHROM].update({str(var.POS) : {'ref': var.REF, 'alt': var_alt_string}})
    return sites


def convert_vcf_to_bed(file, safe_list=None):
    '''

    '''
    bed = list()
    sites = import_sites(file=file, safe_list=safe_list)
    name = 'prob_sites'
    score = '100'
    strand = '+'
    for item in sites:
        for pos in sites[item]:
            bed.append([item, pos, str(int(pos) + 1), name, score, strand])
    return bed


def filter_variants(file, vcf, safe_list=None):
    '''

    '''
    sites = import_sites(file=vcf, safe_list=safe_list)
    with open(file, 'r') as file_p:
        reader = csv.DictReader(file_p, delimiter='\t')
        for line in reader:
            if str(line['POS']) in sites['MN908947.3']:
                print("Found in problematic site list, skipping...")
                continue
            else:
                print(line)


def is_variant_problematic(pos, sites):
    '''
    Returns a boolean depending on whether the variant is found in the
    problematic sites file.
    '''
    