import string
import random


#-------------------------------------------------9.4
def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_signup_new_account(app):
    username = random_username("user_", 10)
    email = username + "@localhost"
    password = "test"
    app.james.ensure_user_exists(username, password)
    # для пароля почтового сервера и регистрации в системе mantis
    app.signup.new_user(username, email, password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()


#------------------------------------------9.3
#def test_signup_new_account(app):
#    username = "user1"
#    password = "test"
#    app.james.ensure_user_exists(username, password)

# для вызова и провреки в cmd (вход) - telnet localhost 4555.
# log и pas root.
# если не работает telnet - Программы и компоненты - Включение/отключение компонентов Win - поставить галочку.

