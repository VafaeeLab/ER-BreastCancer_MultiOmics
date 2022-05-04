import glob
from argparse import ArgumentParser

def handle_args():
    parser = ArgumentParser()
    parser.add_argument("response", help= "Good, intermediate or poor?", type = str.lower)

    args = parser.parse_args()
    return args

args = handle_args()

for file in glob.glob("*clean_1.fastq"):
    filename = file.split("_")
    job_name = filename[1] + ".pbs"
    f = open(job_name, "w")

    f.write("#!/bin/bash\n#PBS -l select=1:ncpus=16:mem=12gb\n#PBS -l walltime=15:00\n#PBS -M michael@c47.com\n#PBS -m ae\n#PBS -j oe\n")
    f.write("#PBS -o /srv/scratch/z5160180\n\ncd $PBS_O_WORKDIR\nsource /srv/scratch/z5160180/miniconda3/etc/profile.d/conda.sh\n")
    f.write("conda activate metaphlan3\nmodule load bowtie/2.3.5.1\n")

    metaphlan_command = "metaphlan " + file + "," + '_'.join(filename[0:-2]) + "_clean_2.fastq --nproc 16 --bowtie2out " + '_'.join(filename[0:-4]) + ".bowtie2.bz2" + \
                        " --bowtie2db /srv/scratch/z5160180/metaphlan_database --input_type fastq -o " + '_'.join(filename[0:-5]) + "_" + args.response + ".txt"
    
    f.write(metaphlan_command)

    f.close()