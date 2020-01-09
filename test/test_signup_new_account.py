

def test_signup_new_account(app):
    username = "user1"
    password = "test"
    app.james.ensure_user_exists(username, password)

# для вызова и провреки в cmd (вход) - telnet localhost 4555.
# log и pas root.
# если не работает telnet - Программы и компоненты - Включение/отключение компонентов Win - поставить галочку.

