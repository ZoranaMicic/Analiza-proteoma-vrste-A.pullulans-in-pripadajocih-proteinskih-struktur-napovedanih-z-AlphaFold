import pandas as pd
import requests
import time


input_file = "results/alphafold/archive/alphafold_matches.csv"

output_file = "results/alphafold/archive/alphabet_plddt.csv"


df = pd.read_csv(
    input_file,
    header=None
)

df.columns = [
    "accession",
    "version",
    "length",
    "model_id",
    "db_version"
]


results=[]


for acc in df["accession"]:

    url = f"https://alphafold.ebi.ac.uk/api/prediction/{acc}"

    r = requests.get(url)

    if r.status_code == 200:

        data=r.json()[0]

        results.append({
            "accession":acc,
            "pLDDT":data["globalMetricValue"],
            "model":data["modelEntityId"]
        })

    time.sleep(0.1)


out=pd.DataFrame(results)

out.to_csv(output_file,index=False)

print(out)
