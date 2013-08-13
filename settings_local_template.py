DEBUG = True

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': '.searchindex',
        'STORAGE': 'file',
    },
}
