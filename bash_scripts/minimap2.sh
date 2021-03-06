#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40
outdir="/home/users/Myxozoa_exchange/genome_workshop/mapping/"
reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/raw_reads_min_qual_7.fq.gz"
ref="/home/users/Myxozoa_exchange/Anush/carp_pbjelly.fa"
aln=$outdir"aln.sam"
module load minimap

minimap2 -ax map-ont -t 40 $ref $reads > $aln