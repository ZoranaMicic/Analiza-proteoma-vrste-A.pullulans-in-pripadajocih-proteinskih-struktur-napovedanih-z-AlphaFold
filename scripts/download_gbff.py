import pandas as pd
import requests
from pathlib import Path

log_file = Path("results/download_log.csv")

output = Path("data/gbff")
output.mkdir(parents=True, exist_ok=True)

log = pd.read_csv(log_file)

missing = log[log["Status"] == "HTTP 404"]

results = []

for i, row in missing.iterrows():

    assembly = row["Assembly"]

    print(f"Downloading GBFF {assembly}")

    parts = assembly.split("_")

    accession = parts[0]

    # napravi FTP path
    url = (
        "https://ftp.ncbi.nlm.nih.gov/genomes/all/"
        f"{accession[0:3]}/"
        f"{accession[4:7]}/"
        f"{accession[7:10]}/"
        f"{accession[10:13]}/"
        f"{assembly}/"
        f"{assembly}_genomic.gbff.gz"
    )

    outfile = output / f"{assembly}_genomic.gbff.gz"

    try:

        r = requests.get(url, timeout=60)

        if r.status_code == 200:
            outfile.write_bytes(r.content)
            status = "downloaded"
        else:
            status = f"HTTP {r.status_code}"

    except Exception as e:
        status = str(e)

    results.append({
        "Assembly": assembly,
        "Status": status
    })


pd.DataFrame(results).to_csv(
    "results/gbff_download_log.csv",
    index=False
)

print("Finished")
