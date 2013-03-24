#!/usr/bin/env python2

import sys
import django
from news.models import Article
import util.formats as formats

# title: text
# author: text
# teaser: html
# content: html
# published: YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
# slug: text
def import_legacy_article(title, author, teaser, content, published, slug):
    article = Article(title=title,
                      author_id=1,
                      teaser=teaser,
                      content='<p><em>By %s</em></p>\n%s' % (author, content),
                      content_format=formats.HTML,
                      published=published,
                      slug=slug)
    article.save()

if __name__ == '__main__':
    try:
        with open(sys.argv[3]) as f:
            teaser = f.read()
        with open(sys.argv[4]) as f:
            content = f.read()
        import_legacy_article(sys.argv[1],
                              sys.argv[2],
                              teaser,
                              content,
                              sys.argv[5],
                              sys.argv[6])
    except IndexError:
        print '''\
Usage: %s TITLE AUTHOR TEASER_FILE CONTENT_FILE PUBLISHED SLUG
TITLE: plain text
AUTHOR: plain text
TEASER_FILE: file in html
CONTENT_FILE: file in html
PUBLISHED: YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
SLUG: plain text\
''' % sys.argv[0]
