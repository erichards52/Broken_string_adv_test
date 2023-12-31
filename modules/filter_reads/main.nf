process FILTER_READS {
    publishDir "${params.outdir}/filtered_bed_files/", overwrite: 'true', mode: 'copy'
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
