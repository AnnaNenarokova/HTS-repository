#!/bin/bash
bw2_dir="/home/nenarokova/tools/bowtie2-2.2.9/"
fasta="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/TriTrypDB-33_LseymouriATCC30220_Genome.fasta"
bt2_base="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/mapping/lseymouri_genome"
$bw2_dir"bowtie2-build" --threads 30 $fasta $bt2_base

base_name="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/mapping/lseymouri_23_1_rna"
r1="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/reads/L_seymouri_23_1_trimmed_paired_forward.fastq.gz"
r2="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/reads/L_seymouri_23_1_trimmed_paired_reverse.fastq.gz"

alignment=$base_name".sam"
report=$base_name".txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted_file=$base_name"_sorted.bam"

samtools view -bS -@ 30 $samfile > $bamfile
samtools sort -o $sorted_file -@ 30 $bamfile
samtools index -b $sorted_file

base_name="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/mapping/lseymouri_23_2_rna"
r1="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/reads/L_seymouri_23_2_trimmed_paired_forward.fastq.gz"
r2="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/reads/L_seymouri_23_2_trimmed_paired_reverse.fastq.gz"

alignment=$base_name".sam"
report=$base_name".txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted_file=$base_name"_sorted.bam"

samtools view -bS -@ 30 $samfile > $bamfile
samtools sort -o $sorted_file -@ 30 $bamfile
samtools index -b $sorted_file

base_name="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/mapping/lseymouri_35_1_rna"
r1="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/reads/L_seymouri_35_1_trimmed_paired_forward.fastq.gz"
r2="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/reads/L_seymouri_35_1_trimmed_paired_reverse.fastq.gz"

alignment=$base_name".sam"
report=$base_name".txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted_file=$base_name"_sorted.bam"

samtools view -bS -@ 30 $samfile > $bamfile
samtools sort -o $sorted_file -@ 30 $bamfile
samtools index -b $sorted_file

base_name="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/mapping/lseymouri_35_2_rna"
r1="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/reads/L_seymouri_35_2_trimmed_paired_forward.fastq.gz"
r2="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/reads/L_seymouri_35_2_trimmed_paired_reverse.fastq.gz"

alignment=$base_name".sam"
report=$base_name".txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $bt2_base -1 $r1 -2 $r2 -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted_file=$base_name"_sorted.bam"

samtools view -bS -@ 30 $samfile > $bamfile
samtools sort -o $sorted_file -@ 30 $bamfile
samtools index -b $sorted_file