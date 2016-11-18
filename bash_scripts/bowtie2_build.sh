#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60
bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
cd /home/nenarokova/genomes/novymonas/assembly/wt_all_spades/
$bw2_dir'bowtie2-build' --threads 60 contigs.fasta wt_novymonas
