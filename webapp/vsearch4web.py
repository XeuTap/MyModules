from flask import Flask, render_template, request, session, copy_current_request_context
from vsearch import search4letters
from DBcm import UseDatabase, ConnectionError, CredentialError, SQLError
from checker import check_logged_in
from time import sleep
from threading import Thread

app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }
app.secret_key = 'YouWillNeverGuessTheSecretKey'


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """ Adding some data to the SQL database """
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                value
                (%s, %s, %s, %s, %s)"""  # Могут быть проблемы с введеными данными
            sleep(15)
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res,))

    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are you results:'
    try:
        req_thread = Thread(target=log_request, args=(request, results))
        req_thread.start()
    except ConnectionError as err:
        print('Is your database switched on? Error ', str(err))
    except Exception as err:
        print('Logging failed with this error: ', str(err))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           the_title=title)


@app.route('/viewlog')
@check_logged_in
def view_log() -> 'html':
    contents = []
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """ select phrase, letters, ip, browser_string, results
                        from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
            titles = ('Phrase', 'Letters', 'Ip', 'Browser_string', 'Results')
            return render_template('viewlog.html',
                                   the_title='View Log',
                                   the_row_titles=titles,
                                   the_data=contents)
    except ConnectionError as err:
        print('Is your database switched on? Error ', str(err))
    except CredentialError as err:
        print('User-id/Passwod issues. Error:', str(err))
    except SQLError as err:
        print('Is your querry corect? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def bye() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)
