process COMBINE_OUTPUT {
    publishDir "${params.outdir}/combined_outputs/", overwrite: 'true', mode: 'copy'
    errorStrategy 'retry'

    input:
    path norm_counts

    output:
    path "combined_out.txt"

    """
    cat ${norm_counts} | sort -k1 -n > combined_out.txt
    """
}
