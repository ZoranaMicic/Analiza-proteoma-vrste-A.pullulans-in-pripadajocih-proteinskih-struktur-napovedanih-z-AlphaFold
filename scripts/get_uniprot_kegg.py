import requests
import pandas as pd
import time


input_file = "results/alphafold/final_alphafold_proteins.csv"

output_file = "results/alphafold/uniprot_kegg_annotations.csv"


df = pd.read_csv(input_file)


results = []


for acc in df["UniProt_accession"]:

    url = f"https://rest.uniprot.org/uniprotkb/{acc}.txt"

    r = requests.get(url)

    kegg = None
    ec = None
    function = None

    if r.status_code == 200:

        text = r.text


        for line in text.split("\n"):

            if line.startswith("DR   KEGG;"):
                kegg = line.split(";")[1].strip()


            if line.startswith("DE   EC="):
                ec = line.split("=")[1].split(";")[0]


            if line.startswith("CC   -!- FUNCTION:"):
                function = line.replace(
                    "CC   -!- FUNCTION:",
                    ""
                ).strip()


    results.append({
        "UniProt_accession": acc,
        "KEGG": kegg,
        "EC": ec,
        "Function": function
    })


    time.sleep(0.2)


out = pd.DataFrame(results)

out.to_csv(
    output_file,
    index=False
)

print(out)
