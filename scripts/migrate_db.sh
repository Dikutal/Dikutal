#!/bin/sh

for app in attachments jobs news planet
do
    echo "Migrating app $app..."
    ./manage.py migrate $app && \
        ./manage.py schemamigration $app --auto && \
        ./manage.py migrate $app
    echo "$app migrated."
    echo
done
