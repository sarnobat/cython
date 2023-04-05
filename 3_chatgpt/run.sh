#!/bin/sh

#----------------------------------------------------------------------------
# DESCRIPTION		
# DATE				[:VIM_EVAL:]strftime('%Y-%m-%d')[:END_EVAL:]
# AUTHOR			ss401533@gmail.com                                           
#----------------------------------------------------------------------------

set -o errexit

test $# -gt 0 && echo "args given" || echo "no args"

cat <<EOF | batcat --plain --paging=never --language sh --theme TwoDark
PYTHONPATH=/Volumes/numerous/2022/usr/local/homebrew/lib/python3.10/site-packages  python3 main.py
EOF



