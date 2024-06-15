#!/usr/bin/bash

#SBATCH -J yechan2468-augmentation
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=32G
#SBATCH -p batch_ugrad
#SBATCH -w aurora-g7
#SBATCH -t 15:0
#SBATCH -o logs/slurm-%A.out

python ./augment.py


