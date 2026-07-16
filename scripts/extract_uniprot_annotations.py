from Bio import SeqIO
import pandas as pd
import re


input_fasta = "data/uniprot/UP001341245_5580.fasta"

output = "results/alphafold/uniprot_annotations.csv"


records = []


for record in SeqIO.parse(input_fasta, "fasta"):

    header = record.description

    # accession
    accession = record.id.split("|")[1]

    # protein name
    protein_name = header.split(" OS=")[0]
    protein_name = protein_name.split("|")[-1].strip()

    # remove entry name if needed
    protein_name = protein_name.split(" ",1)[1] if " " in protein_name else protein_name


    # gene
    gene_match = re.search(r"GN=([^\s]+)", header)

    if gene_match:
        gene = gene_match.group(1)
    else:
        gene = None


    records.append({
        "UniProt_accession": accession,
        "Protein_name": protein_name,
        "Gene": gene,
        "Length": len(record.seq)
    })


df = pd.DataFrame(records)

df.to_csv(output, index=False)

print(df.head())
print("Saved:", output)
