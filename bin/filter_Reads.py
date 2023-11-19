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
help='bedfile from which to filter mapQ score'
)

# Create a shorthand variable for the parser to parse arguments
args = parser.parse_args()

# Get the bedfile name so we can name the outputs appropriately 
bed_file_name = Path(args.bedfile).stem

# Read the bedfile provided into a pandas dataframe
bed_file_df = pd.read_csv(args.bedfile, sep="\t")

# Filter the bedfile for a mapping quality of >= 30
filt_bed_file_df = bed_file_df[bed_file_df.iloc[:, 4] >= 30]

# Write the filtered bedfile into a new bedfile
filt_bed_file_df.to_csv(bed_file_name + "_filtered.bed", sep="\t",index=False)
