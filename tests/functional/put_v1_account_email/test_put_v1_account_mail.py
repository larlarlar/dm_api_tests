def test_put_v1_account_mail(account_helper, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    account_helper.register_new_user(login=login, email=email, password=password)
    account_helper.user_login(login=login, password=password)
    account_helper.change_registered_email(login=login, password=password, email=email)










