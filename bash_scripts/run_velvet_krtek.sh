#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=32

reads1="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq/E262_1.fastq.gz"
reads2="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq/E262_2.fastq.gz"
reads3="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/with_endosym_trimmed/wt_S2_L001_trimmed_1U.fq"
reads4="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/with_endosym_trimmed/wt_S2_L001_trimmed_2U.fq"

outdir="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/with_endosym_trimmed/velvet/"

/home/nenarokova/tools/VelvetOptimiser-2.2.5/VelvetOptimiser.pl -s 27 -e 27 -f '-shortPaired -fastq $reads1 -shortPaired2 -fastq $reads2' -t 32
