#!/bin/bash
export FLASK_CONFIG=development
export FLASK_APP=run.py
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
done
flask db upgrade
exec gunicorn run:app -b0.0.0.0:5000