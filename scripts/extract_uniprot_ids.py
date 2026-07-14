import pandas as pd

diamond = pd.read_csv(
    "results/diamond/cdhit_vs_reference.tsv",
    sep="\t",
    header=None
)

diamond.columns = [
    "Query",
    "Subject",
    "Identity",
    "Length",
    "Evalue",
    "Bitscore"
]

diamond["UniProt_accession"] = (
    diamond["Subject"]
    .str.split("|")
    .str[1]
)

diamond["UniProt_accession"].drop_duplicates().to_csv(
    "results/alphafold/reference_uniprot_ids.txt",
    index=False,
    header=False
)

print("Unique proteins:",
      diamond["UniProt_accession"].nunique())
