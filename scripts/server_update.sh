# Run this to initialize the server with newly pulled data.

set -e

./scripts/migrate_db.sh
./manage.py collectstatic
service uwsgi reload
