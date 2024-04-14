import pytest
import allure
from helpers import Helpers




class TestCourierCreation:

    @allure.title('Проверка создания курьера.')
    @allure.description('Проверяем, что при создании нового курьреа, метод фикстуры register_new_courier_and_return_login_password, '
                        'добавляет данные о новоом пользователе в список result, если приходит код ответа 201.')
    def test_courier_creation(self, register_new_courier_and_return_login_password):
        result = register_new_courier_and_return_login_password
        assert len(result) != 0

    @allure.title('Проверка, что нельзя создать второго курьера с таким же логином и что возвращается ошибка')
    @allure.description('Проверяем, что если в методе courier_duplicate_registration, использовать повторно для регистрации данные,'
                        'которые уже были использованы при создании пользователя в методе register_new_courier_and_return_login_password')
    def test_courier_duplicate(self,register_new_courier_and_return_login_password):
         helpers = Helpers()
         response = helpers.courier_duplicate_registration(register_new_courier_and_return_login_password)
         assert  response.status_code == 409 and response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Проверка, что для создания курьера нужно передать все обязательные данные')
    @allure.description('Проверяем, что если при создани курьера,в методе not_all_required_fields, передать не все заполненные,'
                        'обязательные поля, то ответ будет содержать код 400 и сообщение в теле')
    def test_not_all_required_fields(self, register_new_courier_and_return_login_password):
        helpers = Helpers()
        response = helpers.not_all_required_fields(register_new_courier_and_return_login_password)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Проверка, что запрос возвращает правильный код ответа')
    @allure.description('Проверяем, что в методе correct_status_code, при отправке запроса на создании нового пользователя, '
                        'с валидными данными, придет код ответа 201.')
    def test_correct_status_code(self, return_random_data):
        helpers = Helpers()
        response = helpers.correct_status_code(return_random_data)
        assert response.status_code == 201

    @allure.title('Проверка, что запрос возвращает правильный текст ответа')
    @allure.description('Проверяем, что в методе correct_status_code, при отправке запроса на создании нового пользователя,'
                        'тело ответа содержит {"ok":true}')
    def test_correct_text_answer(self, return_random_data):
         helpers = Helpers()
         response = helpers.correct_status_code(return_random_data).text
         result = '{"ok":true}'
         assert response == result


    @allure.title('Проверка, что если одного из полей нет, запрос возвращает ошибку')
    @allure.description('Проверяем, что если в методе not_all_required_fields_exist, передать запрос на создание нового пользователя, с отсутствующим обязательным полем,'
                        'то в отвтете вернется код 400 и тело ответа будет содержать сообщение.')
    def test_not_all_required_fields_exist(self, register_new_courier_and_return_login_password):
        helpers = Helpers()
        response = helpers.not_all_required_fields_exist(register_new_courier_and_return_login_password)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи'

