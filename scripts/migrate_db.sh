#!/bin/sh

for app in news jobs planet attachments
do
    echo "Migrating app $app..."
    ./manage.py migrate $app && ./manage.py schemamigration $app --auto && ./manage.py migrate $app
    echo "$app migrated."
done
