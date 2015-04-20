#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l mem=2Gb
#PBS -l nodes=1:ppn=1

head_folder='/home/nenarokova/wheat/R1_2/sum_fastq_re/sorted/'
bt2_base='/home/nenarokova/wheat/bw2_base_v2.2_transcripts/wheat'
cd $head_folder
folder=`ls -1 | tail -n $PBS_ARRAYID | head -1`
cd $folder
cd trim_out
bowtie2 -p 1  --local --ma 1 --mp 0,0 --rdg 0,0 --rfg 0,0 --score-min L,0,0.85 --reorder -x $bt2_base -1 paired_out_fw.fastq -2 paired_out_rv.fastq -U unpaired_out_fw.fastq,unpaired_out_rv.fastq -S ../wheat_alignment_transcripts_strict.sam