DANISH = 'DA'
ENGLISH = 'EN'
OTHER = '**'

LANGUAGES = (
    (DANISH, 'Dansk'),
    (ENGLISH, 'English'),
    (OTHER, 'Other/Unspecified'),
)

DEFAULT = ENGLISH

lang_filter = {
    'da': 'DA',
    'en': 'EN'
}

def filter_with_lang(objs, lang):
    try:
        lang = lang_filter[lang]
        objs = objs.filter(language=lang)
    except KeyError:
        pass
    return objs
