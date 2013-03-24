#!/bin/sh

set -e # Die on error.

# Import articles into the database.  Uses import_legacy_article.py.
# Uses little error checking, be careful.  Note that
# import_legacy_article.py must be in the current directory (which
# must also be the root directory of the Dikutal source code).  The
# input directory must contain articles of the format created by
# extract.hs.

if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory containing articles>"
    exit 1
fi

for article in $1/*; do
    slug=$(basename $article)
    echo $slug:
    ./import_legacy_article.py "$(cat $article/title)" "$(cat $article/author)" $article/teaser $article/content "$(cat $article/date)" "$slug"
done
