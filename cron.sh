#!/bin/sh

PATH="cd /Users/michaelherman/repos/realpython/daily-commit/venv/bin/:$PATH"
export PATH
cd /Users/michaelherman/repos/realpython/daily-commit
source venv/bin/activate
source env.sh
python ping.py
