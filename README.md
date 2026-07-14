# Proteome analysis of Aureobasidium pullulans

## Overview

This project aims to identify proteins from *Aureobasidium pullulans*
with available or predicted 3D structures and perform downstream
functional analysis.

## Workflow

1. Genome and protein data collection
2. Proteome construction and redundancy reduction
3. Protein length filtering
4. Protein clustering using CD-HIT
5. Homology search against UniProt reference proteome using DIAMOND BLASTP
6. Identification of candidate proteins with AlphaFold models
7. Structural quality filtering using pLDDT scores
8. Functional pathway analysis

## Data sources

- NCBI Genome database
- UniProt reference proteome UP001341245
- AlphaFold Protein Structure Database

## Current status

Protein sequences were mapped against the *A. pullulans*
reference proteome using DIAMOND BLASTP.
AlphaFold model identification is currently being validated.
