import requests
import json
import pytest
import allure

class Helpers:
    @allure.step('Для каждого атрибута данных пользователя для регистрации, вызывает метод register_new_courier_and_return_login_password'
                 'и извлекаем значения зарегистрированного пользовтеля из списка. Затем выполняем запрос на создание пользователя с данными,'
                 'уже зарегистрированного пользователя.')
    def courier_duplicate_registration(self, register_new_courier_and_return_login_password):
        login = register_new_courier_and_return_login_password[0]
        password = register_new_courier_and_return_login_password[1]
        first_name = register_new_courier_and_return_login_password[2]

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        if response.status_code == 409:
            return response

    @allure.step('Выполняем запрос на создание нового пользователя, в теле которого передаем пустое значнеия обязательно поля')
    def not_all_required_fields(self, register_new_courier_and_return_login_password):
        password = register_new_courier_and_return_login_password[1]
        first_name = register_new_courier_and_return_login_password[2]

        payload = {
            "login": '',
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        if response.status_code == 400:
            return response

    @allure.step('Выполняем запрос на создание нового пользователя, в теле которого отсутствует обязательно поля')
    def not_all_required_fields_exist(self, register_new_courier_and_return_login_password):
        password = register_new_courier_and_return_login_password[1]
        first_name = register_new_courier_and_return_login_password[2]

        payload = {
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        if response.status_code == 400:
            return response

    @allure.step('Выполняем запрос на создание нового пользователя с использованием метода фикстуры return_random_data, для передачи в тело запроса случайных данных')
    def correct_status_code(self, return_random_data):
        payload = return_random_data
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        return response

    @allure.step('Выполняем запрос на авторизацию созданного пользователя. Даннные для тела запроса получаем из метода фикстуры register_new_courier_and_return_login_password,'
                 'которая возвращает данные зарегистрированного нового пользователя')
    def courier_login(self, register_new_courier_and_return_login_password):
        login = register_new_courier_and_return_login_password[0]
        password = register_new_courier_and_return_login_password[1]

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

        if response.status_code == 200:
            return response

    @allure.step('Выполяем запрос на авторизацию существущего пользователя, с передачей в тело запроса пустое значение обязательного атрибута')
    def not_all_required_fields_login(self, register_new_courier_and_return_login_password):
        password = register_new_courier_and_return_login_password[1]

        payload = {
            "login": "",
            "password": password
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

        if response.status_code == 400:
            return response

    @allure.step('Выполяем запрос на авторизацию существущего пользователя, с отсутствующим обязательным полем в теле запроса.')
    def not_all_required_fields_login_exist(self, register_new_courier_and_return_login_password):
        password = register_new_courier_and_return_login_password[1]

        payload = {
            "password": password
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

        if response.status_code == 400:
            return response

    @allure.step('Выполяем запрос на авторизацию нового пользователя, с передачей в тело запроса, невалидных значений логина и пароля')
    def incorret_data_login(self, register_new_courier_and_return_login_password):
        login = register_new_courier_and_return_login_password[0]

        payload = {
            "login": login,
            "password": 12345
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

        if response.status_code == 404:
            return response

    @allure.step('Выполняем запрос на создание нового заказа, с передачей данных в тело запроса, трех разных вариантов значений поля "Цвет".')
    def order_create_colors(self, color):
        data = {
            "firstName": "Leonid",
            "lastName": "Yakubobich",
            "address": "Ostankino, 142",
            "metroStation": 4,
            "phone": "+7 985 355 35 35",
            "rentTime": 5,
            "deliveryDate": 2024 - 12 - 31,
            "comment": "Saske, come back to Konoha",
            "color": [
                color
            ]
        }

        payload = json.dumps(data)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)

        return response

    @allure.step('Выполяем запрос на получение списка заказов')
    def orders_list(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        if response.status_code == 200:
            return response









