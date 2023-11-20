process COMBINE_OUTPUT {
    publishDir "${params.outdir}/results/combined_outputs/", overwrite: 'true'
    errorStrategy 'retry'

    input:
    path norm_counts

    output:
    path "combined_out.txt"

    """
    cat ${norm_counts} > combined_out.txt
    """
}
