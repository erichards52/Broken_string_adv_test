/* 
 * Enable DSL 2 syntax
 */
nextflow.enable.dsl = 2


////////////////////////////////////////////////////
/* --    IMPORT LOCAL MODULES/SUBWORKFLOWS     -- */
////////////////////////////////////////////////////

include { FILTER_READS            } from './modules/filter_reads/main'
include { INTERSECT_COUNTS        } from './modules/intersect_counts/main'

////////////////////////////////////////////////////
/* --           RUN MAIN WORKFLOW              -- */
////////////////////////////////////////////////////

workflow {
    ch_bed_file = Channel.fromPath(params.bed_file + '/*.bed')
    ch_intersect_bed_file = Channel.fromPath(params.bed_file_intersect)

FILTER_READS(ch_bed_file)

INTERSECT_COUNTS(FILTER_READS.out.filt_bed_file, ch_intersect_bed_file)
}