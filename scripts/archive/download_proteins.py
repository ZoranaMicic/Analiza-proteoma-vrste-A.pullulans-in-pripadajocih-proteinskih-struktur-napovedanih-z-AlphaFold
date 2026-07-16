import pandas as pd
import requests
from pathlib import Path

# folders
metadata = Path("data/metadata/assemblies.csv")
output = Path("data/proteins")

output.mkdir(parents=True, exist_ok=True)

assemblies = pd.read_csv(metadata)

log = []

for _, row in assemblies.iterrows():

    ftp = row["FTP_GenBank"]

    if pd.isna(ftp):
        continue

    ftp = ftp.replace("ftp://", "https://")

    basename = ftp.split("/")[-1]

    url = f"{ftp}/{basename}_protein.faa.gz"

    outfile = output / f"{basename}_protein.faa.gz"

    print(f"Checking {basename}")

    try:

        r = requests.get(url, timeout=60)

        if r.status_code == 200:

            outfile.write_bytes(r.content)

            status = "downloaded"

        else:

            status = f"HTTP {r.status_code}"

    except Exception as e:

        status = str(e)

    log.append({
        "Assembly": basename,
        "Status": status
    })

pd.DataFrame(log).to_csv(
    "results/archive/download_log.csv",
    index=False
)

print("Finished.")
