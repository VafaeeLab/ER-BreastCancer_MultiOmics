import pandas as pd
import glob, os

from argparse import ArgumentParser

def get_names():
    genera = []
    sample_names = []
    if (args.input): os.chdir(os.getcwd()+"/"+args.input)
    for file in glob.glob("*.txt"):
        file_details = file.split('_')
        sample_names.append("_".join(file_details[:-1]))

        sample = pd.read_csv(file)
        for entry in sample["trim_name"]:
            if entry not in genera: genera.append(entry)

    return genera, sample_names

def build_table(genera, sample_names):
    data = []
    for file in glob.glob("*.txt"):
        data.append(build_row(file, genera))

    genera.append('Response')

    return pd.DataFrame(data, columns = genera, index = sample_names)


def build_row(file, genera):
    
    sample = pd.read_csv(file)
    row = []

    for genus in genera:
        abundance = sample[sample["trim_name"] == genus]

        if not abundance.empty:
            row.append(abundance["relative_abundance"].values[0])
        else: row.append(0)

    if "control" in file: row.append(0)
    else: row.append(1)

    return row

parser = ArgumentParser()
parser.add_argument("--input", help= "Txt files to collate")
args = parser.parse_args()

genera, sample_names = get_names()
table = build_table(genera,sample_names)

print(f"../{args.input}.csv")
table.to_csv(f"../{args.input}.csv")