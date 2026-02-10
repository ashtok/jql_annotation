#!/bin/bash
#SBATCH --job-name=JQL-Part0
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=42G
#SBATCH --time=24:00:00
#SBATCH --output=logs/part0-%j.out
#SBATCH --error=logs/part0-%j.err

cd /data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/JQL-Annotation-Pipeline
source .venv/bin/activate
export PYTHONPATH=/data/42-julia-hpc-rz-wuenlp/s472389/jql_annotation/JQL-Annotation-Pipeline/src

echo "Starting part 0 at $(date)"
srun python -u annotate_part0.py
echo "Completed part 0 at $(date)"
