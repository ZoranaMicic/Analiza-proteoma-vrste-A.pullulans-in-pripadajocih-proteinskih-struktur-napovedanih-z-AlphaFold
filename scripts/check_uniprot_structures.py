import requests
import pandas as pd
import time


input_file = "results/alphafold/reference_uniprot_ids.txt"
output_file = "results/alphafold/uniprot_structure_annotations.csv"


ids = pd.read_csv(
    input_file,
    header=None,
    names=["accession"]
)


results = []


for i, acc in enumerate(ids["accession"]):

    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"

    try:
        r = requests.get(url)

        if r.status_code == 200:

            data = r.json()

            pdbs = []

            for ref in data.get("uniProtKBCrossReferences", []):
                if ref["database"] == "PDB":
                    pdbs.append(ref["id"])

            results.append({
                "accession": acc,
                "organism": data["organism"]["scientificName"],
                "pdb_count": len(pdbs),
                "pdb_ids": ";".join(pdbs)
            })

        else:

            results.append({
                "accession": acc,
                "organism": None,
                "pdb_count": 0,
                "pdb_ids": None
            })


    except Exception:

        results.append({
            "accession": acc,
            "organism": None,
            "pdb_count": 0,
            "pdb_ids": None
        })


    if i % 100 == 0:
        print(i, "/", len(ids))

    time.sleep(0.05)


df = pd.DataFrame(results)

df.to_csv(output_file, index=False)

print("Finished")
