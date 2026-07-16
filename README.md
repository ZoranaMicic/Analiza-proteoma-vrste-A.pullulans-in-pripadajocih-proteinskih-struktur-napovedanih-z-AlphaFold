# Proteome analysis of Aureobasidium pullulans

## Overview

This repository contains the complete bioinformatics workflow developed for the Bachelor's thsis:
**Analysis of the proteome of *Aurebasidium pullulans* and associated protein structures by AlphaFold**
The project reconstructs a non-redundant proteome from publicly available genome genome assemblies, identifies proteins with available AlphaFold structural models, and performs functional annotation using UniProt, eggoNOG-mapper and KEGG.

---

## Workflow

### 1. Genome assembly retrieval

- Retrieval of all publicly available *Aureobasidium pullulans* genome assemblies (NCBI TaxIDL 5580)
- Assembly metadata collection using the NCBI Entrez API
- Genome quality assessment

### 2. Proteom construction

- Download of predicted protein FASTA files
- Construction of a combined proteome dataset
- Removal of identical protein sequences using SeqKit

### 3. Protein quality control

- Protein length analysis
- Removal of proteins shorter than 50 amino acids

### 4. Protein clustering

- Redundancy reduction using CD-HIT (90% sequence identity)

### 5. Protein identification

- DIAMOND BLASTP search against the UniProt reference proteome
- Selection of high-confidence protein matches

### 6. AlphaFold structure identification

- Matching UniProt accessions with AlphaFold Database
- Retrieval of available AlphaFold protein models
- Structural quality assessment using pLDDT scores

### 7. Functional annotation

- UniProt annotation
- eggoNOG-mapper functional annotation
- KEGG Orthology assignment
- Functional classification of proteins

### 8. Data visualization

- Genome assembly statistics
- Protein length distributions
- DIAMOND similarity statistics
- AlphaFold confidence statistics
- Functional category summaries

---

## Data sources

- NCBI Assembly
- NCBI Genome FTP
- UniProt Reference Proteome (UP001341245)
- AlphaFold Protein Structure Database
- eggoNOG-mapper
- KEGG

---

## Software

- R 
- Python
- SeqKit
- CD-HIT
- DIAMOND BLASTP
- eggoNOG-mapper

---

## Repository structure

```
data/
results/
scripts/
R/
```

---

## Current status

✔ Genome assemblies collected

✔ Combined proteome reconstructed

✔ Redundant proteins removed

✔ Protein clustering completed

✔ UniProt mapping completed

✔ AlphaFold structures identified

✔ Functional annotation completed

✔ KEGG analysis completed

✔ R Markdown workflow completed

---

## Author

**Zorana Micić**
Bachelor thesis, University of Primorska