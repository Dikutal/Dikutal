Requirements for installation:
* Python 2.7
* The following Python modules:
    * django (1.4.(3--5) guaranteed to work, probably all 1.4.* versions)
    * django-south
    * django-haystack (version 2: http://haystacksearch.org/ )
    * django-widget-tweaks
    * django-extensions
    * markdown
    * feedparser

Installation procedure:
* Create "settings_local.py" from "settings_local_template.py"
* Run ./manage.py syncdb
* Run ./manage.py migrate
* Run ./manage.py runserver

If you want elasticsearch, add the following to your "settings_local.py":

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'dikutal',
        },
    }
