#### Senior Project: Health Data Science, KMUTT and CRA
##### Contributors

- Panitchaporn Thanyawasin [@PanitchapornT](https://github.com/PanitchapornT)
- Auripan Porat [@Thtcare](https://github.com/Thtcare)


# AMoRe

AMoRe package is a tool to analyze a bacterial genome (FASTA file), generating a comprehensive report on antimicrobial resistance (AMR). Its functionality covers strain identification, detection of AMR genes, classification of drug classes and plasmid contigs from genomic data. An exceptional feature of this package is its ability to generate detailed reports, providing comprehensive statistics sourced directly from our database.

We specifically designed the AMoRe package for deployment on Linux systems using Docker.


## Required Dependencies

- pandas
- numpy
- sqlite3
- sys
- os
- subprocess
- SeqIO
- datetime
- matplotlib
- plotly
- mpld3


## Installation (Linux only)

1. Pull a docker image.

``` bash
% docker pull panitchapornt/amore:1
```

2. Download AMoRe package.

``` bash
% gdown https://drive.google.com/uc?id=1W5q50iVssznDh3JlY7uKmvJEMCx0vZT6
% unzip amore.zip
```

3. Download databases. You have the option to download all databases or only select ones for specific functions. You can download it from this [link](https://drive.google.com/drive/folders/17IaCfBIuaXXan8pNAY_eI69QwNEoe4bH?usp=drive_link) or download all databases using the following command:

``` bash
% gdown https://drive.google.com/uc?id=1UMSrH3nvxq4FUDLlH7AbeItwTZ69jMph
% unzip amore_db.zip
```

4. Start your Docker desktop application to run the Docker image.
5. AMoRe package is ready to use.
** If Python cannot locate your package, try this command:

``` python
$ import sys
$ sys.path.append(path to directory before AMoRe package folder)
```
6. Demo is available [here](https://drive.google.com/drive/folders/126y4laDeYza6fyz5A1d2vUJOQDxbwvQ0?usp=sharing).

``` bash
% gdown --folder https://drive.google.com/drive/folders/1JO52N3_91rnbbSz6P2QK8uQrljD08awn
```

---

## Assembly Quality Control Module

### input_qc

This module comes with an **'input_qc'** function for checking the quality of genome assembly. It offers 10 different measures to evaluate. There are:
- Number of contigs
- Sequence length
- Average sequence length
- Minimal sequence length
- Maximal sequence length
- GC%
- N50
- L50
- N75
- L75

#### Usage

``` bash
$ from amore import assembly_qc
$ assembly_qc.input_qc(input_path, output_name)
```
- input_path: Your genome path
- output_name: Output name (.tsv)

#### Example

``` bash
$ from amore import assembly_qc
$ assembly_qc.input_qc(input_path="amore_demo/GCA_013778425.1_ASM1377842v1_genomic.fna", output_name='amore_demo/amore_qc.tsv')
```

#### Output
| Number of contigs | Sequence length | Average sequence length | Minimal sequence length | Maximal sequence length | GC%   | N50    | L50 | N75    | L75 |
|-------------------|-----------------|-------------------------|-------------------------|-------------------------|-------|--------|-----|--------|-----|
| 68                | 3910877         | 57512.9                 | 524                     | 349398                  | 38.92 | 118544 | 12  | 118544 | 12  |

---

## Sequence Typing Module

This module has 2 funtions:

### mlst
- Multilocus sequence typing (MLST) is an unambiguous procedure for characterising isolates of bacterial species using the sequences of internal fragments of (usually) seven house-keeping genes. 

- Scan contig files against traditional PubMLST typing schemes. **This function is tool from [tseeman](https://github.com/tseemann/mlst).

#### Usage

``` bash
$ from amore import sequence_typing
$ sequence_typing.mlst(input_path, output_name)
```
- input_path: Your genome path
- output_name: Output name (.tsv) ** If your genome is *Acinetobacter baumannii* or *Escherichia coli*, you will recieve 2 outputs.

#### Example

``` bash
$ from amore import sequence_typing
$ sequence_typing.mlst(input_path="amore_demo/GCA_013778425.1_ASM1377842v1_genomic.fna", output_name="amore_demo/amore_mlst.tsv")
```
#### Output
| FILE                                   | SCHEME       | ST | Pas_cpn60 | Pas_fusA | Pas_gltA | Pas_pyrG | Pas_recA | Pas_rplB | Pas_rpoB |
|----------------------------------------|--------------|----|-----------|----------|----------|----------|----------|----------|----------|
| GCA_000173395.1_ASM17339v1_genomic.fna | abaumannii_2 | 49 | 3         | 3        | 6        | 2        | 3        | 1        | 5        |

#
### cgmlst
- Core genome multilocus sequence typing (cgMLST) is a molecular typing method based on core genomes to construct high-resolution species typing results and analyze the population structure and genetic evolution of strains.
- Determine the allelic profiles of a set of genomes.
**This function is AlleleCall function from [chewBBACA](https://chewbbaca.readthedocs.io/en/latest/index.html)


#### Usage

``` bash
$ from amore import sequence_typing
$ sequence_typing.cgmlst(input_path, scheme_path, output_name)
```
- input_path: Your genome path
- scheme_path: cgMLST scheme folder path
- output_name: Output folder name

** We have 7 cgMLST schemes that are available to download. There are *Acinetobacter baumannii*, *Enterococcus faecium*, *Escherichia coli*, *Pseudomonas aeruginosa*, *Klebsiella pneumoniae*, *Staphylococcus aureus* and *Streptococcus pneumoniae*. These cgMLST schemes are from [PubMLST](https://pubmlst.org/) and [Ridom cgMLST](https://www.cgmlst.org/ncs) and were prepared by using the [PrepExternalSchema](https://chewbbaca.readthedocs.io/en/latest/user/modules/PrepExternalSchema.html) function from chewBBACA. If you want to create your own scheme, use the same [PrepExternalSchema](https://chewbbaca.readthedocs.io/en/latest/user/modules/PrepExternalSchema.html) that we used.

#### Example

``` bash
$ from amore import sequence_typing
$ sequence_typing.cgmlst(input_path="amore_demo/GCA_013778425.1_ASM1377842v1_genomic.fna", scheme_path="amore_db/cgmlst/cgmlst_abaumannii", output_name="amore_demo/amore_cgmlst")
```

#### Output
OutputFolderName

├── cds_coordinates.tsv

├── invalid_cds.txt

├── loci_summary_stats.tsv

├── results_statistics.tsv

├── results_contigsInfo.tsv

├── results_alleles.tsv

├── paralogous_counts.tsv

├── paralogous_loci.tsv

└── logging_info.txt

The important output file is **results_alleles.tsv**, which contains cgMLST's allelic profiles. Details about other output files can be found at this [link](https://chewbbaca.readthedocs.io/en/latest/user/modules/AlleleCall.html).

---

## Plasmid Module

This module was created to classify plasmids and chromosomes from the FASTA file. There are 2 functions:
### mobsuite 
- This function is MOB-recon function from [MOB-suite](https://github.com/phac-nml/mob-suite). 

#### Usage

``` bash
$ from amore import plasmid
$ plasmid.mobsuite(input_path, output_name)
```

- input_path: Your genome path
- output_name: Output folder name

#### Example

``` bash
$ from amore import plasmid
$ plasmid.mobsuite(input_path="amore_demo/GCA_013778425.1_ASM1377842v1_genomic.fna", output_name="amore_demo/amore_mobsuite")
```

#### Output
OutputFolderName

├── contig_report.txt

├── mge.report.txt

├── chromosome.fasta

├── plasmid_(X).fasta

└── mobtyper_results.txt


|        File       |                                           Description                                           |
|:-----------------:|:-----------------------------------------------------------------------------------------------:|
| contig_report.txt | This file describes the assignment of the contig to chromosome or a particular plasmid grouping |
| mge.report.txt    | Blast HSP of detected MGE's/repetitive elements with contextual information                     |
| chromosome.fasta  | Fasta file of all contigs found to belong to the chromosome                                     |
| plasmid_(X).fasta | Each plasmid group is written to an individual fasta file which contains the assigned contigs   |
| mobtyper_results  | Aggregate MOB-typer report files for all identified plasmid                                     |


#
### plasme
- This function is a PLASMe tool from [HubertTang](https://github.com/HubertTang/PLASMe). To use this function, you must first download a PLASMe folder from our provided database.

#### Usage

``` bash
$ from amore import plasmid
$ plasmid.plasme(input_path, db_path, output_name)
```

- input_path: Your genome path
- db_path: PLASMe folder path
- output_name: Prefix of output name

#### Example

``` bash
$ from amore import plasmid
$ plasmid.plasme(input_path="amore_demo/GCA_013778425.1_ASM1377842v1_genomic.fna", db_path="amore_db/PLASMe", output_name="amore_demo/amore_plasme")
```

#### Output
- Fasta file of all predicted plasmid contigs
- Report file of the description of the identified plasmid contigs (.tsv)

|    Field   |                      Description                      |
|:----------:|:-----------------------------------------------------:|
| contig     | Sequence ID of the query contig                       |
| length     | Length of the query contig                            |
| reference  | The best-hit aligned reference plasmid                |
| order      | Assigned order                                        |
| evidence   | BLASTn or Transformer                                 |
| score      | The prediction score (applicable only to Transformer) |
| amb_region | The ambiguous regions*                                |

*The ambiguous regions refer to regions that may be shared with the chromosomes. If a query contig contains a large proportion of ambiguous regions, caution must be exercised as it could potentially originate from a chromosome.

|     contig     | length | reference     | order            | evidence    | score              | amb_region  |
|--------------|------|---------------|------------------|-------------|--------------------|-------------|
| ABXK01000015.1 | 110638 | NZ_CP072497.1 | Enterobacterales | Transformer | 0.5862023234367371 | 54283-55061 |
| ABXK01000006.1 | 130480 | CP074266.1    | Enterobacterales | Transformer | 0.8918898105621338 | 31026-31283 |
| ...            | ...    | ...           | ...              | ...         | ...                | ...         |
---

## AMR Module

### amrfinderplus

This module was created to identify the AMR gene and drug class by using [NCBI Antimicrobial Resistance Gene Finder (AMRFinderPlus)](https://github.com/ncbi/amr) via **'amrfinderplus'** function. 

#### Usage

``` bash
$ from amore import amr
$ amr.amrfinderplus(input_path, output_name)
```

- input_path: Your genome path
- output_name: Output name (.tsv)

#### Example

``` bash
$ from amore import amr
$ amr.amrfinderplus(input_path="amore_demo/GCA_013778425.1_ASM1377842v1_genomic.fna", output_name="amore_demo/amore_amr.tsv")
```

#### Output

| Protein identifier |    Contig id   | Start | Stop  | Strand | Gene symbol | Sequence name                                                      | Scope | Element type | Element subtype | Class       | Subclass      | Method  | Target length | Reference sequence length | % Coverage of reference sequence | % Identity to reference sequence | Alignment length | Accession of closest sequence | Name of closest sequence                                           | HMM id | HMM description |
|:------------------:|:--------------:|-------|-------|--------|-------------|--------------------------------------------------------------------|-------|--------------|-----------------|-------------|---------------|---------|---------------|---------------------------|----------------------------------|----------------------------------|------------------|-------------------------------|--------------------------------------------------------------------|--------|-----------------|
| NA                 | ABXK01000010.1 | 94136 | 94957 | +      | blaOXA-98   | OXA-51 family carbapenem-hydrolyzing class D beta-lactamase OXA-98 | core  | AMR          | AMR             | BETA-LACTAM | CARBAPENEM    | ALLELEX | 274           | 274                       | 100.00                           | 100.00                           | 274              | WP_001021777.1                | OXA-51 family carbapenem-hydrolyzing class D beta-lactamase OXA-98 | NA     | NA              |
| NA                 | ABXK01000012.1 | 96619 | 97767 | +      | blaADC-241  | extended-spectrum class C beta-lactamase ADC-241                   | core  | AMR          | AMR             | BETA-LACTAM | CEPHALOSPORIN | ALLELEX | 383           | 383                       | 100.00                           | 100.00                           | 383              | WP_001211198.1                | extended-spectrum class C beta-lactamase ADC-241                   | NA     | NA              |
| ...                | ...            | ...   | ...   | ...    | ...         | ...                                                                | ...   | ...          | ...             | ...         | ...           | ...     | ...           | ...                       | ...                              | ...                              | ...              | ...                           | ...                                                                | ...    | ...             |

---

## Report Module

### amr_analysis_report

You can use this module to create a report that contains output from all modules in this package via **'amr_analysis_report'** function. Additionally, this module will summarize the statistics relative to your data from our database. That will be beneficial information to understand overall.

#### Usage

``` bash
$ from amore import report
$ report.amr_analysis_report(asm_qc, mlst, cgmlst, plasme, amr, output_name, db, mlst2=False, input_metadata=False)
```

- asm_qc: Path to the output of assembly_qc.input_qc
- mlst: Path to the output of sequence_typing.mlst
- cgmlst: Path to results_alleles.tsv, the output of sequence_typing.cgmlst
- plasme: Path to the PLASMe report (.tsv), output of plasmid.plasme
- amr: Path to the output of amr.amrfinderplus
- output_name: Prefix of output name
- db: Path to AMoRe_mini_DB.db
- mlst2: Path to the output of sequence_typing.mlst ** If you have 2 outputs from analyzed *Acinetobacter baumannii* and *Escherichia coli*. (default=False)
- input_metadata: (default=False) You can add the metadata to your report. 
    - Filename
    - Isolate name
    - Species name
    - Isolation source
    - Country
    - City
    - Collection date
    - Collection by

#### Example

``` bash
$ from amore import report
$ report.amr_analysis_report(asm_qc='amore_demo/amore_qc.tsv', mlst='amore_demo/amore_mlst.tsv', cgmlst='amore_demo/amore_cgmlst/results_alleles.tsv', plasme='amore_demo/amore_plasme_report.tsv', amr='amore_demo/amore_amr.tsv', output_name='amore_demo/amore_report', db='amore_db/AMoRe_mini_DB.db')
```

#### Output
- Report contains 6 parts:
    - Metadata
        - Filename
        - Isolate name
        - Species name
        - Isolation source
        - Country
        - City
        - Collection date
        - Collection by
    - Assembly stats
        - Number of contigs
        - Sequence length
        - Average sequence length
        - Minimal sequence length
        - Maximal sequence length
        - GC%
        - N50
        - L50
        - N75
        - L75
        - A box plot of sequence length and GC% compared to our database.
    - MLST
        - MLST table
        - A bar chart showing the countries and years where the same ST was found in our database.
    - AMR analysis
        - A table shows the AMR genes found in plasmids or chromosomes, as well as the drug classes to which they are resistant.
    - Plasmid typing
        - A bar chart showing the countries and years in which the same plasmid was discovered in our database.
    - Closest genome
        - The table shows the top 10 closest genomes with no more than 100 different loci for the cgMLST scheme.

---

The AMoRe package was created for educational purposes. There is no intention to infringe on copyright.