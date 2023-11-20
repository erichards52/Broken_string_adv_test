/* 
 * Enable DSL 2 syntax
 */
nextflow.enable.dsl = 2


////////////////////////////////////////////////////
/* --    IMPORT LOCAL MODULES/SUBWORKFLOWS     -- */
////////////////////////////////////////////////////

include { FILTER_READS            } from './modules/filter_reads/main'
include { INTERSECT_COUNTS        } from './modules/intersect_counts/main'
include { COUNT_SUM_NORM          } from './modules/count_sum_norm/main'
include { COMBINE_OUTPUT          } from './modules/combine_outputs/main'

////////////////////////////////////////////////////
/* --           RUN MAIN WORKFLOW              -- */
////////////////////////////////////////////////////

workflow {
    ch_bed_file = Channel.fromPath(params.bed_file + '/*.bed')
    ch_intersect_bed_file = Channel.fromPath(params.bed_file_intersect)

    FILTER_READS(ch_bed_file)

    INTERSECT_COUNTS(FILTER_READS.out.filt_bed_file, ch_intersect_bed_file)

    ch_bed_files_temp = ch_bed_file.map { tuple( it.simpleName, it ) }
        .groupTuple().set { bed_files }

    ch_bed_filt_comb = INTERSECT_COUNTS.out.filt_intersect_count_bed_files.map { tuple( it.simpleName - ~/_Sample$/, it ) }
        .combine( bed_files, by: 0 )
        .transpose( by: 2 )
        .map { sample, filt_bed, bed -> tuple( filt_bed, bed ) }

    COUNT_SUM_NORM(ch_bed_filt_comb)

    COMBINE_OUTPUT(COUNT_SUM_NORM.out.norm_counts.collect(sort:true))
}