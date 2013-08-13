DEBUG = True

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': '.searchindex',
        'STORAGE': 'file',
    },
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '..................................................'
