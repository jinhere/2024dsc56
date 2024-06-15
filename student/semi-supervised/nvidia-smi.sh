ssh aurora-g7 nvidia-smi --query-gpu=timestamp,name,utilization.gpu,memory.used --format=csv -l 1
