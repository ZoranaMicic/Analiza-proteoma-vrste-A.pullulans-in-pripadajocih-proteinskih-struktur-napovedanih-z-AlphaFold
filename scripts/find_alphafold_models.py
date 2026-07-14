import csv

input_ids = "results/alphafold/A_pullulans_candidate_uniprot_ids.txt"
alphafold_db = "data/alphafold/accession_ids.csv"
output_file = "results/alphafold/alphafold_matches.csv"

# učitaj naših 8224 UniProt accession-a
with open(input_ids) as f:
    ids = set(line.strip() for line in f if line.strip())

print(f"Loaded {len(ids)} candidate proteins.")

matches = 0

with open(alphafold_db, newline="") as infile, \
     open(output_file, "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:

        if not row:
            continue

        accession = row[0]

        if accession in ids:
            writer.writerow(row)
            matches += 1

print(f"Found {matches} AlphaFold models.")
print(f"Results saved to {output_file}")