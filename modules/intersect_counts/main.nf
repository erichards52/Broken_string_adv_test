process INTERSECT_COUNTS {
    publishDir "${params.outdir}/results/filtered_intersect_count_bed_files/", overwrite: 'true'
    errorStrategy 'retry'

    input:
    each filt_bed_file
    path bed_file_intersect

    output:
    path "*intersect_counts.bed", emit: filt_intersect_count_bed_files

    script:
    """
    filt_file_name="\$(basename -- ${filt_bed_file})"
    bedtools intersect -c -a ${filt_bed_file} -b ${bed_file_intersect} > \${filt_file_name}_intersect_counts.bed
    """
}
