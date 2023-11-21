# Advanced Coding Test: Broken String Biosciences
======
## Pipeline explanation:
This pipeline performs 4 steps:
1. Filters the provided break bedfiles located in /data/breaks/*.bed for a mapQ of >= 30
2. Intersects each sample break bedfile with the AsiSI site bed file
3. Sum(s) and normalise(s) the counts provided by bedtools
   * Sum the number of breaks per sample (provided by bedtools)
   * Normalise the number of breaks per sample (Sum of breaks/(Total Breaks/1000))
4. Collect normalised number of AsiSI breaks

## Usage guide: 
1. In order to run this you can use the pipeline by making sure you have all requirements (will make this/Dockerfile)
1. Clone the repository ```git clone https://github.com/erichards52/Broken_string_adv_test.git```
2. Pipeline uses the Nextflow workflow manager. Make sure you haven't moved any of the files present in the base level directory as all are required to be present. 
   * ```nextflow run main.nf --bed_file data/breaks/ --bed_file_intersect ./chr21_AsiSI_sites.t2t.bed```
   * If you wish to move the location of the break bedfiles you can do this by specifying with the ```--bed_file <$PATH_TO_BREAK_BEDFILES>``` or if you wish to move the location of the AsiSI site bed file, this can be done via ```--bed_file_intersect <$PATH_TO_AsiSI_SITE_BEDFILE>```
