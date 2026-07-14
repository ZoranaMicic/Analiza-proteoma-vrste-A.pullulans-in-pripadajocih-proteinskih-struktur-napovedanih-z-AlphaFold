import requests
import pandas as pd
import time


input_file = "results/alphafold_uniprot_ids.txt"
output_file = "results/alphafold/alphafold_availability.csv"


ids = pd.read_csv(
    input_file,
    header=None,
    names=["UniProt_accession"]
)


results = []


for i, accession in enumerate(ids["UniProt_accession"]):

    url = f"https://alphafold.ebi.ac.uk/api/prediction/{accession}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()[0]

            results.append({
                "UniProt_accession": accession,
                "AlphaFold_model": True,
                "pLDDT": data.get("globalMetricValue")
            })

        else:

            results.append({
                "UniProt_accession": accession,
                "AlphaFold_model": False,
                "pLDDT": None
            })

    except Exception:

        results.append({
            "UniProt_accession": accession,
            "AlphaFold_model": False,
            "pLDDT": None
        })


    if i % 100 == 0:
        print(i, "/", len(ids))


    time.sleep(0.05)


df = pd.DataFrame(results)

df.to_csv(output_file, index=False)

print("Finished")
