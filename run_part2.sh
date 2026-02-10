#!/bin/bash
#SBATCH --job-name=JQL-Part2
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=42G
#SBATCH --time=24:00:00
#SBATCH --output=logs/part2-%j.out
#SBATCH --error=logs/part2-%j.err

cd /data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/JQL-Annotation-Pipeline
source .venv/bin/activate
export PYTHONPATH=/data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/JQL-Annotation-Pipeline/src

echo "Starting part 2 at $(date)"
srun python -u annotate_part2.py
echo "Completed part 2 at $(date)"
