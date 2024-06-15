srun \
--gres=gpu:1 \
--cpus-per-gpu=8
--mem-per-gpu=29G
-p debug_ugrad
-w aurora-g7
--pty $SHELL
