import pytest
import allure
from helpers import Helpers
import test_data

class TestCourierCreation:

    @allure.title('Проверка создания нового курьера.')
    @allure.description('Проверяем, что при создании нового курьреа, метод  registration_user, '
                        'выполняет запрос на создание нового курьера и возвращает код ответа 201, а в тело ответ содержит {"ok":true}')
    def test_courier_creation(self):
        helpers = Helpers()
        payload = helpers.generate_random_data_payload()
        response = helpers.registration_user(payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка, что нельзя создать второго курьера с таким же логином и что возвращается ошибка')
    @allure.description('Проверяем, что передать в метод registration_user, данные для регистрации нового пользователя,'
                        'а заетем эти же данные использовать повторно, то ответ возвращает код 409 и тело ответа содержит сообщение')
    def test_courier_duplicate(self):
        helpers = Helpers()
        response = helpers.courier_duplicate_registration()
        assert response.status_code == 409 and response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Проверка, что для создания курьера нужно передать все обязательные данные')
    @allure.description('Проверяем, что если при создани курьера,в методе not_all_required_fields, передать не все заполненные,'
                        'обязательные поля, то ответ будет содержать код 400 и сообщение в теле')
    @pytest.mark.parametrize("payload", [
        {"login": '', "password": test_data.password, "firstName": test_data.firstName},  # Первый объект без значения поля логин
        {"login": test_data.login, "password": '', "firstName": test_data.firstName} # Второй объект без значения поля пароль

    ])
    def test_not_all_required_fields(self, payload):
        helpers = Helpers()
        response = helpers.not_all_required_fields(payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи'

