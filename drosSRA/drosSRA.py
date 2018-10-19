# -*- coding: utf-8 -*-

"""Main module."""

import argparse
import sys
import pandas as pd


def arguments(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--pubmed_id", dest="pubmed", nargs='?', type=float, action="store")
    parser.add_argument("-s", "--sex", dest="sex", nargs='?', type=str, action="store")
    parser.add_argument("-d", "--dev_stage", dest="developmental stage", nargs='?', type=str, action="store")
    parser.add_argument("-t", "--tissue", dest="tissue", nargs='?', type=str, action="store")
    parser.add_argument("-c", "--cell_type", dest="cell type", nargs='?', type=str, action="store")

    args = parser.parse_args(argv)
    return args


def main(argv=None):
    args = arguments(argv)
    meta = pd.read_table('drosSRA/rnaseq_metadata.tsv')
    
    #need to handle plural somehow too
    #actually (need to check with justin) dont think we'll have any plurals
    

    
    dictargs = vars(args)
    if all(val==None for val in dictargs.values()):
        sys.exit("One or more flags are necessary to identify tracks of interest")
    
    use = {k: v for k, v in dictargs.items() if v is not None}
    
    search = ':'.join(map(str, use.values()))
    #use search to find sample names
    funct = lambda x:':'.join(map(str, [getattr(x, col) for col in use]))
    meta['merged'] = meta.apply(funct, axis=1)
    sample_ids = meta[meta['merged'] == search].sample_name.values
    #build url
    GO = 'https://www.ncbi.nlm.nih.gov/genome/gdv/browser/?context=GEO&acc='
    url = GO + '%2C'.join(sample_ids)
    print(url)

if __name__ == '__main__':
    main()

