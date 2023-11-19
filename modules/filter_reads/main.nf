process FILTER_READS {
    publishDir "${params.outdir}/results/filtered_bed_files/", overwrite: 'true'
    errorStrategy 'retry'

    input:
    path bed_file

    output:
    path "*_filtered.bed", emit: filt_bed_file

    script:
    """
    filter_Reads.py ${bed_file}
    """
}
