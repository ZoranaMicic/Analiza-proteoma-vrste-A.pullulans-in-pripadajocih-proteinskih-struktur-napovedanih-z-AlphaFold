from Bio import SeqIO
import pandas as pd


fasta = "data/uniprot/UP001341245_5580.fasta"
models = "results/alphafold/archive/alphafold_matches.csv"


# učitaj proteome
proteins = {}

for record in SeqIO.parse(fasta, "fasta"):
    acc = record.id.split("|")[1]
    proteins[acc] = {
        "length": len(record.seq),
        "description": record.description
    }


# učitaj AlphaFold rezultate
df = pd.read_csv(
    models,
    header=None
)

df.columns = [
    "accession",
    "version",
    "length",
    "model_id",
    "db_version"
]


df["in_reference_proteome"] = df["accession"].isin(proteins)

df["description"] = df["accession"].map(
    lambda x: proteins.get(x, {}).get("description")
)


df.to_csv(
    "results/alphafold/archive/validated_models.csv",
    index=False
)


print(df)
