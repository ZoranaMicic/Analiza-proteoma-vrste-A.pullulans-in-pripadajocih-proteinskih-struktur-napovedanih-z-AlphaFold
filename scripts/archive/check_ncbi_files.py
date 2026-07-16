import pandas as pd
import requests
from pathlib import Path
from bs4 import BeautifulSoup


assemblies = pd.read_csv(
    "data/metadata/assemblies.csv"
)

results = []


for i, row in assemblies.iterrows():

    assembly = row["Assembly"]
    ftp = row["FTP_GenBank"]

    print(f"{i+1}/{len(assemblies)} {assembly}")

    url = ftp.replace(
        "ftp://",
        "https://"
    ) + "/"

    try:

        r = requests.get(url, timeout=60)

        soup = BeautifulSoup(
            r.text,
            "html.parser"
        )

        files = [
            x.text
            for x in soup.find_all("a")
        ]

        protein = [
            f for f in files
            if f.endswith("_protein.faa.gz")
        ]

        gbff = [
            f for f in files
            if f.endswith("_genomic.gbff.gz")
        ]


        if protein:

            status = "protein_fasta"
            file = protein[0]

        elif gbff:

            status = "genbank_annotation"
            file = gbff[0]

        else:

            status = "no_protein_annotation"
            file = ""


    except Exception as e:

        status = str(e)
        file = ""


    results.append({

        "Assembly": assembly,
        "Status": status,
        "File": file,
        "FTP": ftp

    })


pd.DataFrame(results).to_csv(
    "results/annotation_availability.csv",
    index=False
)


print("Finished")
