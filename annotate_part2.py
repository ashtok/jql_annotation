import sys
sys.path.insert(0, '/data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/JQL-Annotation-Pipeline/src')

from datatrove_jql_annotator import JQLAnnotator, stats_adapter
from datatrove.pipeline.readers import JsonlReader
from datatrove.executor import LocalPipelineExecutor
from datatrove.pipeline.writers import JsonlWriter

def main():
    output_base = '/data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/outputs_part2'
    
    pipeline = [
        JsonlReader(
            data_folder='/data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/data_splits',
            glob_pattern='part_2.jsonl',
            text_key='raw_content',
        ),
        JQLAnnotator(
            embedder_model_id='Snowflake/snowflake-arctic-embed-m-v2.0',
            batch_size=100,
            stats_writer=JsonlWriter(
                output_folder=f'{output_base}/stats',
                adapter=stats_adapter,
                expand_metadata=True,
            ),
        ),
        JsonlWriter(
            output_folder=f'{output_base}/annotated_data',
            compression='gzip',
        ),
    ]

    executor = LocalPipelineExecutor(
        pipeline,
        tasks=1,
        local_tasks=1,
        local_rank_offset=0,
        logging_dir=f'{output_base}/logs'
    )

    print("Processing part 2...")
    executor.run()
    print("Part 2 completed!")

if __name__ == '__main__':
    main()
