# Dependencies

* Python 2.7
* The following Python modules:
    * markdown
    * feedparser
    * icalendar
    * django 1.4.3+
    * django-south
    * django-haystack (version 2: [http://haystacksearch.org/]())
    * django-widget-tweaks
    * django-extensions
    * django-ical

The Python modules can be installed with:

    pip install markdown feedparser icalendar django==1.4.6 south \
      django-haystack==2 django-widget-tweaks django-extensions django-ical


# Setup

0. Create "settings_local.py" from "settings_local_template.py"
1. Run ./manage.py syncdb
2. Run ./manage.py migrate
3. Run ./manage.py runserver

If you want Elasticsearch instead of Whoosh, add the following to your
"settings_local.py":

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'dikutal',
        },
    }


# Server updating

When pulling new code and data on the server, run this to restart the webserver
with the new data:

    ./script/data_update.sh

