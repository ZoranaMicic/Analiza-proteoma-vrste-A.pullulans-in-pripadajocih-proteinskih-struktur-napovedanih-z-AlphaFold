from Bio import SeqIO
import requests
import pandas as pd
import time


fasta = "data/uniprot/UP001341245_5580.fasta"

output = "results/alphafold/all_reference_alphafold.csv"


accessions=[]


for record in SeqIO.parse(fasta,"fasta"):

    acc = record.id.split("|")[1]
    accessions.append(acc)


print("Total proteins:", len(accessions))


results=[]


for i,acc in enumerate(accessions):

    url=f"https://alphafold.ebi.ac.uk/api/prediction/{acc}"

    r=requests.get(url)


    if r.status_code==200:

        data=r.json()[0]

        results.append({
            "accession":acc,
            "model":data["modelEntityId"],
            "pLDDT":data["globalMetricValue"]
        })


    if i%100==0:
        print(i,"/",len(accessions))


    time.sleep(0.05)



df=pd.DataFrame(results)

df.to_csv(output,index=False)


print("Models found:",len(df))
