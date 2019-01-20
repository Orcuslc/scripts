#! /bin/zsh

tmux new-session -s argon -n remote -d
tmux send-keys -t argon "cdg; cd Research/reduced_basis" C-m

tmux rename-window -t "init:1" Research
tmux send -t "init:Research" "cdg; cd Research/reduced_basiswq"

tmux split-window -h -t "init:Research"
