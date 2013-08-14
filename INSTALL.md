# Dependencies

* Python 2.7
* The following Python modules:
    * django (1.4.(3--5) guaranteed to work, probably all 1.4.* versions)
    * django-south
    * django-haystack (version 2: [http://haystacksearch.org/]())
    * django-widget-tweaks
    * django-extensions
    * markdown
    * feedparser

The Python modules can be installed with:

    pip install django==1.4.5 south django-haystack==2 django-widget-tweaks django-extensions markdown feedparser


# Installation

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

