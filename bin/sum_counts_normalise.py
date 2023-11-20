#! /usr/bin/env python3

# Import packages
import os
import pathlib
from pathlib import Path
from argparse import ArgumentParser
import pandas as pd

# Create parser 
parser = ArgumentParser('Sum, count and normalise DSB counts')

# Add an argument to the parser for the filtered bedfile
parser.add_argument(
'bedfile_filt', type=pathlib.Path,
help='bedfile from which to sum and normalise counts'
)

# Add an argument to the parser for the initial bedfile
parser.add_argument(
'bedfile_initial', type=pathlib.Path,
help='bedfile from which to sum and normalise counts'
)

# Create a shorthand variable for the parser to parse arguments
args = parser.parse_args()

# Get the bedfile & sample name so we can name the outputs appropriately 
bed_file_name = Path(args.bedfile_initial).stem
stripped_bed_file_name = bed_file_name.split('.', 1)[0]
sample_number_only = stripped_bed_file_name.replace('Sample', '')

# Read both bedfiles provided into a pandas dataframe
bed_file_filt_df = pd.read_csv(args.bedfile_filt, sep="\t")
bed_file_initial_df = pd.read_csv(args.bedfile_initial, sep="\t")

# Get number of total breaks from initial bedfile 
# (index + 1) and divide by 1000
total_breaks_div = (len(bed_file_initial_df.index)+1)/1000

#Sum the last (counts) column in the filtered bedfile
count_sum = bed_file_filt_df.iloc[:, 6].sum()

#Return normalised counts via count(s)/(total breaks/1000)
norm_count = round(count_sum/total_breaks_div,3)

f = open( str(sample_number_only) + '_norm_count', 'w' )
f.write( str(sample_number_only) + "\t" + str(norm_count) + "\n")
f.close()
