#!/usr/bin/python
from Bio import SeqIO

l = [
"NODE_2_length_844906_cov_870.704",
"NODE_822_length_1318_cov_1863.76",
"NODE_346_length_5920_cov_1555.3",
"NODE_121_length_88224_cov_845.318",
"NODE_106_length_108046_cov_858.69",
"NODE_104_length_108845_cov_889.343"
]
fasta = '/home/anna/bioinformatics/novymonas/wt_scaffolds.fasta'
results = []

for record in SeqIO.parse(fasta, "fasta"):
  if record.id not in l:
    results.append(record)

outpath = '/home/anna/bioinformatics/novymonas/novymonas_no_pand_scaffolds.fasta'

SeqIO.write(results, outpath, "fasta")
