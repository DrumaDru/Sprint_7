import pytest
import allure
from helpers import Helpers
import test_data

class TestCourierLogin:
    @allure.title('Проверка, что курьер может авторизоваться и что успешный запрос возвращает id')
    @allure.description('Проверяем, что если в методе courier_login, выполнить запрос с данными нового пользователя, после успешной регистрации,'
                        'то можно авторизоваться и тело ответа будет содержать id авторизованного пользователя.')
    def test_courier_login(self):
        helpers = Helpers()
        response = helpers.courier_login()
        assert response.status_code == 200 and response.json()['id'] != 0

    @allure.title('Проверка, что для авторизации нужно передать все обязательные поля ')
    @allure.description('Проверяем, что если в методе not_all_required_fields_login, при отправке запроса на авторизацию,'
                        'не все обязательные поля будут заполнены, то вернется код 400, а в тело ответа будет содержать сообщение.')
    @pytest.mark.parametrize("payload", [
        {"login": '', "password": None},  # Первый объект без значения поля логин
        {"login": None, "password": ''}  # Второй объект без значения поля пароль
    ])
    def test_not_all_required_fields(self, payload):
        helpers = Helpers()
        response = helpers.not_all_required_fields_login(payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'


    @allure.title('Проверка, что система вернёт ошибку, если неправильно указать логин или пароль.')
    @allure.description('Проверить, что если в методе incorret_data_login, отправтиь запрос на атворизацию с невалидными значениями логина и пароля,'
                        'то вернется код 400 и тело ответа будет содержать сообщение')
    @pytest.mark.parametrize("payload", [
        {"login": None, "password": test_data.password},  # Первый объект c невалидным значениям поля пароль
        {"login": test_data.login, "password": None}  # Второй объект с невалидным значением поля логин
    ])
    def test_incorrect_data_login(self, payload):
        helpers = Helpers()
        response = helpers.incorrect_data_login(payload)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'




