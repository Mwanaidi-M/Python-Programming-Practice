def greet(language):
    """
    Think of a way to store the languages as a database (e.g. an object).

    Write a 'welcome' function that takes a parameter 'language' (always a string),
    and returns a greeting - if you have it in your database. It should default to
    English if the language is not in the database, or in the event of an invalid input.

    """

    lang_db = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }

    welcome_msg = ''

    if lang_db.get(language) is None:
        welcome_msg = lang_db['english']
    else:
        welcome_msg = lang_db[language]

    # alternative technique
    # return lang_db.get(language, "Welcome")

    return welcome_msg
