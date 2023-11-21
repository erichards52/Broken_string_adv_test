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

======================================================

## Usage guide: 
1. In order to run this you can use the pipeline by making sure you have all requirements (will make this/Dockerfile)

2. Clone the repository ```git clone https://github.com/erichards52/Broken_string_adv_test.git```

3. Pipeline can be run using: 
```nextflow run main.nf --bed_file data/breaks/ --bed_file_intersect ./chr21_AsiSI_sites.t2t.bed```
   * Alternatively, the pipeline can be run with the Dockerfile present within the repo after building it via ```docker build . -t broken_string_dockfile``` and then running the pipeline as above with the additional parameter: ```-with-docker broken_string_dockfile``` at the end
   * Pipeline uses the Nextflow workflow manager. Make sure you haven't moved any of the files present in the base level directory as all are required to be present. 
   * If you wish to move the location of the break bedfiles you can do this by specifying with the ```--bed_file path/to/break/bedfiles``` or if you wish to move the location of the AsiSI site bed file, this can be done via ```--bed_file_intersect path/to/AsiSI/sites/bedfile```

4. Output files as well as pipeline meta information can be found in the ```results_<$yyyy-MM-dd_HH-mm-ss>``` directory, which contains individual directories (named appopriately) containing outputs for each individual parallel process as well as a directory named ```pipeline_meta``` which contains a DAG, trace, as well as two viewable HTML reports (timeline and report)

======================================================

## N.B./Additional Info
* (Python) Scripts used within processes can be found in the ```/bin``` directory

* All analysis was done from within the ```/analysis``` directory (```analysis_script.py```) after having copied the final output of the pipeline (```combined_out.txt```) into the ```/analysis``` directory

* Whilst timing decorators are not found within the pipeline inside individual processes, the trace files as well as HTMLs produced via Nextflow can be used to view an extensive number of traits from each parallel process' undertaken by the pipeline during each run

======================================================

## Answers to original repo questions:
1. Which of the samples are likely to be controls or treated?
   * Samples 1-8 are likely to be controls and samples 9-12,15 and 16 are likely to be the treated
   * A KMean Clustering scatterplot can be found and viewed in the ```analysis``` directory in the repo above along with an "Elbow Method" plot along with a text file named ```Cluster_Info.txt``` which dictates which samples belong to which cluster(s) as well as their distance from the KMeans clustering centroid(s)

2. Are there any you are uncertain of?
   * I am uncertain as to whether samples 13 and 14 are treated or a control as they exhibit the an abnormal distance from their (respective) cluster's centroid and their placing is somewhat ambiguous

3. Can you explain the samples in the uncertain group?
   * There are a number of reasons for each (uncertain) sample potentially belonging to the control group or the treated group. It could be that some of the cells were treated with a greater amount of 4OHT than other samples (as might be the case with sample 11) or treated with less 4OHT than other samples (as could be the case for samples 13 and 14).

   * Furthermore, it could be the case that one or more of the controls exhibited a naturally occurring DSB break at one or more AsiSI site(s) (as might be the case for sample 13), leading to a control seemingly belonging to the treated group. In the same vein, one of the treated samples might have exhibited a naturally occuring DSB break at one or more AsiSI site(s) (such as sample 11), leading to a treated group appearing as if it had been treated with a greater amount of 4OHT, despite this (potentially) not being the case.

4. Of all the possible AsiSI sites described in the chr21_AsiSI_sites.t2t.bed file what is the maximum percentage observed in a single sample?
   * The answer is Sample 11 with 0.48%
   * Intermediate files used for this analysis can be found in ```/analysis```
   * By using bedtools intersect with the ```-wo``` parameter, which gives us the total overlapping bases per defined region, and dividing the resulting sum of overlap(s) by the total number of base pairs present within each break bedfile, we can achieve this. It appears that all break bedfiles provided have the same number of features as total base pairs, but I used AWK just to be safe. I approached this by doing the following:

   Bedtools intersect each breakend:
   ```for file in $(ls *breakends*); do bedtools intersect -wo -a ${file} -b ../chr21_AsiSI_sites.t2t.bed > ${file}.overlap; done```

   Sum total overlaps into individual txts:
   ```for file in $(ls *.overlap); do cat ${file} | cut -f10 | paste -sd+ | bc > ${file}_total_overlap; done```

   Get total base pairs per breakend Sample:
   ```for file in $(ls *breakends.bed); do awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}' ${file} > ${file}_bp.txt; done```

   Perform division (Base pair(s) overlap/total base pairs)*100:
   
   Sample1: None

   Sample2: None

   Sample3: 1 out of 3734 = 0.03%

   Sample4: None

   Sample5: None

   Sample6: None

   Sample7: None

   Sample8: None

   Sample9: 5 out of 1826 = 0.27%

   Sample10: 10 out of 2961 = 0.34%

   Sample11: 10 out of 2076 = 0.48%

   Sample12: 5 out of 2283 = 0.22%

   Sample13: 2 out of 1629 = 0.12%

   Sample14: 7 out of 3564 = 0.20%

   Sample15: 15 out of 4859 = 0.31%

   Sample16: 18 out of 5347 = 0.34%