Requirements for installation:
* Python 2.7
* The following Python modules:
    * django
    * django-south
    * django-haystack (version 2: http://haystacksearch.org/ )
    * markdown
    * feedparser

Installation procedure:
* Create an empty settings_local.py
* Run ./manage.py syncdb
* Run ./manage.py runserver

If you don't want elasticsearch, install whoosh for Python, and add the following to settings_local.py:

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': '.searchindex',
            'STORAGE': 'file',
        },
    }
