from Bio import SeqIO
import pandas as pd


input_file = "results/clustering/A_pullulans_cdhit90.faa"


records = []

for record in SeqIO.parse(input_file, "fasta"):

    records.append({
        "Protein_ID": record.id,
        "Description": record.description,
        "Length": len(record.seq),
        "Sequence": str(record.seq)
    })


df = pd.DataFrame(records)

df.to_csv(
    "results/alphafold/representative_proteins.csv",
    index=False
)


print(df.head())
print("Proteins:", len(df))
