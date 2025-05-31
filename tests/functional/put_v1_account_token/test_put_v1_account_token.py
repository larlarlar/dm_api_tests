from json import loads
from tests.functional.post_v1_account.test_post_v1_account import get_activation_token_by_login
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration
from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True,
        )
    ],
)


def test_put_v1_account_token():
    mailhog_configuration = MailhogConfiguration(host='http://5.63.153.31:5025')
    dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)

    account = DMApiAccount(configuration=dm_api_configuration)
    mailhog = MailHogApi(configuration=mailhog_configuration)

    login = 'tset6'
    password = 'BertillippoBertillippo'
    email = f'{login}@mail.ru'
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    # Регистрация
    response = account.account_api.post_v1_account(json_data=json_data)
    assert response.status_code == 201, f'Пользователь не был создан {response.json()}'

    # Получить письма из почтового сервера
    response = mailhog.mailhog_api.get_api_v2_messages()
    assert response.status_code == 200, 'Письма не были получены'

    # Получить активационный токен
    token = get_activation_token_by_login(login, response)
    assert token is not None, f'Токен для пользователя {login} не был получен'

    # Активация пользователя
    response = account.account_api.put_v1_account_token(token=token)
    assert response.status_code == 200, f'Пользователь не был активирован'
