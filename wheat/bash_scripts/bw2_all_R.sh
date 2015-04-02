#!/bin/bash
#PBS -l walltime=1000:00:00
#PBS -l mem=24Gb
#PBS -l nodes=1:ppn=12
head_folder='/home/nenarokova/wheat/R1_2/sum_fastq_re/sorted/'
bt2_base='/mnt/lustre/nenarokova/wheat/wheat_bowtie2_index/wheat'
cd $head_folder
folder=`ls -1 | tail -n $PBS_ARRAYID | head -1`
cd $folder
cd trim_out
bowtie2 --local --very-sensitive-local -p 1 --reorder -x $bt2_base -1 paired_out_fw.fastq -2 paired_out_rv.fastq -U unpaired_out_fw.fastq,unpaired_out_rv.fastq -S ../wheat_alignment.sam
