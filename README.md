# Advanced Coding Test: Broken String Biosciences
### Answers to questions posed from the original GitLab repo can be found at the bottom of this REAMDE

## Pipeline explanation:
This pipeline performs 4 steps:
1. Filters the provided break bedfiles for a mapQ of >= 30

2. Intersects each sample break bedfile with the AsiSI site bed file

3. Sum(s) and normalise(s) the counts provided by bedtools
   * Sum the number of breaks per sample (provided by bedtools)
   * Normalise the number of breaks per sample (Sum of breaks/(Total Breaks/1000))

4. Collect normalised number of AsiSI breaks

## Usage guide: 
1. In order to run this you can use the pipeline by making sure you have all requirements (will make this/Dockerfile)

2. Clone the repository ```git clone https://github.com/erichards52/Broken_string_adv_test.git```

3. Pipeline can be run using: 
```nextflow run main.nf --bed_file data/breaks/ --bed_file_intersect ./chr21_AsiSI_sites.t2t.bed```
   * Pipeline uses the Nextflow workflow manager. Make sure you haven't moved any of the files present in the base level directory as all are required to be present. 
   * If you wish to move the location of the break bedfiles you can do this by specifying with the ```--bed_file <$PATH_TO_BREAK_BEDFILES>``` or if you wish to move the location of the AsiSI site bed file, this can be done via ```--bed_file_intersect <$PATH_TO_AsiSI_SITE_BEDFILE>```

4. Output files as well as pipeline meta information can be found in the ```results_<$yyyy-MM-dd_HH-mm-ss>``` directory, which contains individual directories (named appopriately) containing outputs for each individual parallel process as well as a directory named ```pipeline_meta``` which contains a DAG, trace, as well as two viewable HTML reports (timeline and report)

## N.B./Additional Info
* (Python) Scripts used within processes can be found in the ```/bin``` directory

* All analysis was done from within the ```/analysis``` directory (```analysis_script.py```) after having copied the final output of the pipeline (```combined_out.txt```) into the ```/analysis``` directory

* Whilst timing decorators are not found within the pipeline inside individual processes, the trace files as well as HTMLs produced via Nextflow can be used to view an extensive number of traits from each parallel process' undertaken by the pipeline during each run

## Answers to original repo questions:
1. Which of the samples are likely to be controls or treated?
   * Samples 1-8 are likely to be controls and samples 9,10,12,15 and 16 are likely to be the treated

2. Are there any you are uncertain of?
   * I am uncertain as to whether samples 11,13 and 14 are treated or a control as they exhibit the greatest distance from the cluster's centroid

3. Can you explain the samples in the uncertain group?
   * There are a number of reasons for each sample potentially belonging to the control group or the treated group:
      1.  