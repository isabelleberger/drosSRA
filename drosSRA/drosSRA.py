# -*- coding: utf-8 -*-

"""Main module."""

import argparse
import sys
import pandas as pd


def arguments(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--pubmed_id", dest="pubmed", nargs='*', type=float, action="store")
    parser.add_argument("-s", "--sex", dest="sex", nargs='*', type=str, action="store")
    parser.add_argument("-d", "--dev_stage", dest="devstage", nargs='*', type=str, action="store")
    parser.add_argument("-t", "--tissue", dest="tissue", nargs='*', type=str, action="store")
    parser.add_argument("-c", "--cell_type", dest="celltype", nargs='*', type=str, action="store")

    args = parser.parse_args(argv)
    return args


def main(argv=None):
    args = arguments(argv)
    meta = pd.read_table('drosSRA/rnaseq_metadata.tsv')
    sample_ids = []
    if (len(sys.argv)==1 and argv==None):
        sys.exit("One or more flags are necessary to identify tracks of interest")

    if args.pubmed:
        for ids in args.pubmed:
            sample_ids.extend(meta[meta.pubmed == ids].sample_name.values)

    if args.sex:
        for sexes in args.sex:
            #print(sexes)
            sample_ids.extend(meta[meta.sex == sexes].sample_name.values)

    if args.devstage:
        for stages in args.devstage:
            sample_ids.extend(meta[meta['developmental stage'] == stages].sample_name.values)

    if args.tissue:
        for tis in args.tissue:
            sample_ids.extend(meta[meta.tissue == tis].sample_name.values)

    if args.celltype:
        for types in args.celltype:
            sample_ids.extend(meta[meta['cell type'] == types].sample_name.values)
    GO = 'https://www.ncbi.nlm.nih.gov/genome/gdv/browser/?context=GEO&acc='
    url = GO + '%2C'.join(sample_ids)
    print(url)


if __name__ == '__main__':
    main()

