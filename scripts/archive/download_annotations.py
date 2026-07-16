import pandas as pd
import requests
from pathlib import Path


input_file = "results/annotation_availability.csv"

protein_dir = Path("data/proteins")
gbff_dir = Path("data/gbff")

protein_dir.mkdir(parents=True, exist_ok=True)
gbff_dir.mkdir(parents=True, exist_ok=True)


df = pd.read_csv(input_file)

results = []


for i, row in df.iterrows():

    assembly = row["Assembly"]
    status = row["Status"]
    ftp = row["FTP"].replace("ftp://", "https://")
    filename = row["File"]

    print(f"{i+1}/{len(df)} {assembly}")


    url = f"{ftp}/{filename}"


    if status == "protein_fasta":

        outfile = protein_dir / filename

    elif status == "genbank_annotation":

        outfile = gbff_dir / filename

    else:

        continue


    try:

        r = requests.get(
            url,
            timeout=120
        )

        if r.status_code == 200:

            outfile.write_bytes(r.content)
            result = "downloaded"

        else:

            result = f"HTTP {r.status_code}"


    except Exception as e:

        result = str(e)


    results.append({
        "Assembly": assembly,
        "File": filename,
        "Status": result
    })


pd.DataFrame(results).to_csv(
    "results/final_download_log.csv",
    index=False
)


print("Finished")
