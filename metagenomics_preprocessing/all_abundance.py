import pandas as pd
from argparse import ArgumentParser

def handle_args():
    parser = ArgumentParser()
    parser.add_argument("filename", help = "Specify file to calculate abundance for (.txt for metaphlan or .tax for kraken)")
    parser.add_argument("--out", help = "Specify output dir")

    args = parser.parse_args()
    return args

args = handle_args()

## Read in file with additional preprocessing (relative abundance) for kraken
df = pd.read_csv(args.filename, sep = '	', skiprows = 3, header = 0)
df = df.iloc[1: , :]

## Get taxonomic abundance of concern
df["trim_name"] = df["#clade_name"].str.split("|").str[-1]
out = df[["trim_name","relative_abundance"]]

## Write to appropriately named file

out_dir = args.out if (args.out) else ""
if "/" in args.filename: 
    parse_filename = args.filename.split("/")[-1]
else:
    parse_filename = args.filename
out_filename = "%s" % (parse_filename.split(".")[0])
out.to_csv(out_dir + out_filename + ".txt", index = False)