---
grand_parent: Browse Biolink Model
parent: Enums
title: biolink:druggable_gene_category_enum
layout: default
---

# Class: druggable_gene_category_enum




URI: [biolink:druggable_gene_category_enum](https://w3id.org/biolink/vocab/druggable_gene_category_enum)


## Other properties

|  |  |  |
| --- | --- | --- |

## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| Tclin | These targets have activities in DrugCentral (ie. approved drugs) with known mechanism of action. |  |  |
| Tbio | These targets have activities in ChEMBL, Guide to Pharmacology or DrugCentral that satisfy the activity thresholds detailed below. |  |  |
| Tchem | These targets do not have known drug or small molecule activities that satisfy the activity thresholds detailed below AND satisfy one or more of the following criteria: target is above the cutoff criteria for Tdark target is annotated with a Gene Ontology Molecular Function or Biological Process leaf term(s) with an Experimental Evidence code |  |  |
| Tdark | These are targets about which virtually nothing is known. They do not have known drug or small molecule activities that satisfy the activity thresholds detailed below AND satisfy two or more of the following criteria: A PubMed text-mining score from Jensen Lab less than 5, greater than or equal TO 3 Gene RIFs, or less than or equal to 50 Antibodies available according to http://antibodypedia.com. |  |  |
