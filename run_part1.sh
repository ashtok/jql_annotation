#!/bin/bash
#SBATCH --job-name=JQL-Part1
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=42G
#SBATCH --time=24:00:00
#SBATCH --output=logs/part1-%j.out
#SBATCH --error=logs/part1-%j.err

cd /data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/JQL-Annotation-Pipeline
source .venv/bin/activate
export PYTHONPATH=/data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/JQL-Annotation-Pipeline/src

echo "Starting part 1 at $(date)"
srun python -u annotate_part1.py
echo "Completed part 1 at $(date)"
