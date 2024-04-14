import pytest
import allure
from helpers import Helpers

class TestCourierLogin:
    @allure.title('Проверка, что курьер может авторизоваться и что успешный запрос возвращает id')
    @allure.description('Проверяем, что если в методе courier_login, выполнить запрос с данными нового пользователя, после успешной регистрации,'
                        'то можно авторизоваться и тело ответа будет содержать id авторизованного пользователя.')
    def test_courier_login(self, register_new_courier_and_return_login_password):
        helpers = Helpers()
        response = helpers.courier_login(register_new_courier_and_return_login_password)
        assert response.status_code == 200 and response.json()['id'] != 0

    @allure.title('Проверка, что для авторизации нужно передать все обязательные поля ')
    @allure.description('Проверяем, что если в методе not_all_required_fields_login, при отправке запроса на авторизацию,'
                        'не все обязательные поля будут заполнены, то вернется код 400, а в тело ответа будет содержать сообщение.')
    def test_not_all_required_fields_login(self, register_new_courier_and_return_login_password):
        helpers = Helpers()
        response = helpers.not_all_required_fields_login(register_new_courier_and_return_login_password)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'


    @allure.title('Проверка, что система вернёт ошибку, если неправильно указать логин или пароль.')
    @allure.description('Проверить, что если в методе incorret_data_login, отправтиь запрос на атворизацию с невалидными значениями логина и пароля,'
                        'то вернется код 400 и тело ответа будет содержать сообщение')
    def test_incorrect_data_login(self, register_new_courier_and_return_login_password):
        helpers = Helpers()
        response = helpers.incorret_data_login(register_new_courier_and_return_login_password)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка, если какого-то поля нет, запрос возвращает ошибку')
    @allure.description('Проверить, что если в методе incorret_data_login, отправтиь запрос на атворизацию, с отсутствующим обязательным полем, '
                        'то вернется код 400 и тело ответа будет содержать сообщение')
    def test_not_all_required_fields_login_exist(self, register_new_courier_and_return_login_password):
        helpers = Helpers()
        response = helpers.not_all_required_fields_login_exist(register_new_courier_and_return_login_password)
        assert response.status_code == 400  and response.json()['message'] == 'Недостаточно данных для входа'



