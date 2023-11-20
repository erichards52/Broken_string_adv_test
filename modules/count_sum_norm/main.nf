process COUNT_SUM_NORM {
    publishDir "${params.outdir}/results/count_sum_norm/", overwrite: 'true'
    errorStrategy 'retry'

    input:
    tuple path(filt_bed), path(bed)

    output:
    path "*_norm_count", emit: norm_counts

    """
    sum_counts_normalise.py ${filt_bed} ${bed}
    """
}


