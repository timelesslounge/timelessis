from timeless import create_app
"""@todo #48:30min Setup a pre-commit git hook, to forbid single-quoted
    Strings. Generally, the Strings in our codebase should be double-quoted 
    (see README: https://github.com/timelesslounge/timelessis#development-guidelines)
    More on git hooks here: https://githooks.com/
"""

app = create_app("config.DevelopmentConfig")

