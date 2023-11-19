#! /usr/bin/env python3

# Import packages
import os
import pathlib
from pathlib import Path
from argparse import ArgumentParser
import pandas as pd

# Create parser 
parser = ArgumentParser('Filter Reads')

# Add an argument to the parser for the bedfile
parser.add_argument(
'bedfile', type=pathlib.Path,
help='bedfile from which to sum and normalise counts'
)

# Create a shorthand variable for the parser to parse arguments
args = parser.parse_args()

# Get the bedfile name so we can name the outputs appropriately 
bed_file_name = Path(args.bedfile).stem

# Read the bedfile provided into a pandas dataframe
bed_file_df = pd.read_csv(args.bedfile, sep="\t")

#Sum the last (counts) column
count_sum = bed_file_df.iloc[:, 6].sum()

print(count_sum/1000)
