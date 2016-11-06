#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=32

reads1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/with_endosym_trimmed/wt_S2_L001_trimmed_1P.fq"
reads2="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/with_endosym_trimmed/wt_S2_L001_trimmed_2P.fq"
reads3="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/with_endosym_trimmed/wt_S2_L001_trimmed_1U.fq"
reads4="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/with_endosym_trimmed/wt_S2_L001_trimmed_2U.fq"

outdir="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/with_endosym_trimmed/velvet/"

/home/nenarokova/tools/VelvetOptimiser-2.2.5/VelvetOptimiser.pl -s 27 -e 31 -f '-shortPaired -fastq -separate $reads1 $reads2 -short -fastq $reads3 -short -fastq $reads4' -d $outdir -g 31 -t 32
