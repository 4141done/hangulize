from __future__ import with_statement
import sys
import os
libpath = os.path.abspath('lib')
for dirname in os.listdir(libpath):
    sys.path.insert(0, os.path.join(libpath, dirname))
sys.path.insert(0, libpath)
import re
import random
from google.appengine.ext.webapp.util import run_wsgi_app
from flask import *
from flaskext.babel import Babel, gettext
from hangulize import hangulize, LanguageError


LOCALES = ['ko', 'en']


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'ko'
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Returns a best matched language. It finds a language from the GET
    arguments, the cookie values, and the HTTP ``Accept-Language`` header.
    """
    try:
        return request.args["locale"]
    except KeyError:
        pass
    try:
        return request.cookies["locale"]
    except KeyError:
        return request.accept_languages.best_match(LOCALES)


@app.route("/locale", methods=["post"])
def set_locale():
    """Sets a language to the cookie values."""
    locale = request.form["locale"]
    response = redirect(url_for("index"))
    response.set_cookie("locale", locale, 60 * 60 * 24 * 14)
    return response


def get_langs():
    """Returns the allowed languages in :mod:`hangulize`."""
    import hangulize.langs
    def iter():
        for code in hangulize.langs.get_list():
            yield code, gettext(code)
    def compare(x, y):
        return cmp(x[1], y[1])
    return sorted(iter(), cmp=compare)


@app.route('/favicon.ico')
def favicon():
    """Sends the favicon file."""
    return app.send_static_file('favicon.ico')


@app.route('/')
def index():
    """The index page."""
    word = request.args.get('word', '')
    lang = request.args.get('lang', 'it')
    context = dict(word=word, lang=lang,
                   langs=get_langs(), locale=get_locale())
    if word and lang:
        def get_context(word, lang):
            try:
                result = hangulize(unicode(word), lang)
                return dict(success=True, result=result)
            except LanguageError, e:
                return dict(success=False, reason=str(e))
        if request.is_xhr:
            return jsonify(**get_context(word, lang))
        else:
            context.update(**get_context(word, lang));
            return render_template('result.html', **context)
    else:
        return render_template('index.html', **context)


@app.route('/shuffle.js')
def shuffle():
    """Sends a JavaScript code which fills a random language and word to the
    form of the index page.
    """
    lang = request.args.get('lang') or random.choice(list(get_langs()))[0]
    test_path = os.path.join(libpath, 'hangulize', 'tests',
                             lang.replace('.', '_') + '.py')
    assertion_pattern = re.compile("assert u'(?P<want>.+)' == " \
                                   "self\.hangulize\(u'(?P<word>.+)'\)")
    with open(test_path) as f:
        test_code = ''.join(f.readlines())
        assertion = random.choice(list(assertion_pattern.finditer(test_code)))
    context = dict(lang=lang, word=assertion.group('word'))
    return render_template('shuffle.js', **context)


if __name__ == '__main__':
    run_wsgi_app(app)
