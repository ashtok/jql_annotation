import sys
sys.path.insert(0, '/data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/JQL-Annotation-Pipeline/src')

from datatrove_jql_annotator import JQLAnnotator, stats_adapter
from datatrove.pipeline.readers import JsonlReader
from datatrove.executor import LocalPipelineExecutor
from datatrove.pipeline.writers import JsonlWriter

# Paths
input_path = '/data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/data'
output_base = '/data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/outputs'

print(f"Input: {input_path}/synthdata_sample.jsonl")
print(f"Output: {output_base}")

pipeline = [
    JsonlReader(
        data_folder=input_path,
        glob_pattern='synthdata_sample.jsonl',
        text_key='raw_content',  # Adjust based on your data structure
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
        output_folder=f'{output_base}/annotated_data'
    ),
]

executor = LocalPipelineExecutor(
    pipeline,
    tasks=1,
    local_tasks=1,
    local_rank_offset=0,
    logging_dir=f'{output_base}/logs'
)

print("Running pipeline...")
executor.run()
print("Pipeline completed!")
