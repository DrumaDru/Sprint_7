import requests
import json
import pytest
import allure
import test_data
import string
import random

class Helpers:

    @allure.step('Генерируем данные для последующей передачи их в тело запроса на регистрацию нового пользователя')
    def generate_random_data_payload(self):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        # возвращаем payload
        return payload

    @allure.step('Передаем в метод сгенерированные данные в методе generate_random_data_payload')
    def registration_user(self, payload):
        response = requests.post(f"{test_data.curl}/api/v1/courier", data=payload)
        return response


    @allure.step('Передаем сгенерированные данные в методе registration_user и выполняем запрос на первую регистрацию нового пользователя,'
                 'затем с теми же данными выполняем повторный запро на регистрацию поользователя')
    def courier_duplicate_registration(self):
        payload = self.generate_random_data_payload()
        self.registration_user(payload)
        response = self.registration_user(payload)

        return response


    @allure.step('Выполняем запрос на создание нового пользователя, в теле которого, поочередно, передаем пустое значнеия обязательно поля логин и пароль')
    def not_all_required_fields(self, payload):
        response = self.registration_user(payload)
        return response

    @allure.step('Выполняем запрос на авторизацию созданного пользователя. Даннные для тела запроса получаем из метода registration_user,'
                 'который возвращает данные зарегистрированного нового пользователя')
    def courier_login(self):
        data = self.generate_random_data_payload()
        self.registration_user(data)
        login = data['login']
        password = data['password']

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{test_data.curl}/api/v1/courier/login", data=payload)
        return response

    @allure.step('Выполяем запрос на создание авторизацию пользователя, с передачей в тело запроса пустого значения обязательного атрибута сначала для поля логин,'
                 'затем для поля пароль')
    def not_all_required_fields_login(self, payload):
        data = self.generate_random_data_payload()
        self.registration_user(data)
        login = data['login']
        password = data['password']

        if payload["login"] is None:
            payload["login"] = login
        if payload["password"] is None:
            payload["password"] = password

        response = requests.post(f"{test_data.curl}/api/v1/courier/login", data=payload)
        return response

    @allure.step('Выполяем запрос на авторизацию существуеющего пользователя, с передачей в тело запроса, некорректных значений логина или пароля')
    def incorrect_data_login(self, payload):
        data = self.generate_random_data_payload()
        self.registration_user(data)
        login = data['login']
        password = data['password']

        if payload["login"] is None:
            payload["login"] = login
        if payload["password"] is None:
            payload["password"] = password

        response = requests.post(f"{test_data.curl}/api/v1/courier/login", data=payload)
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
        response = requests.post(f"{test_data.curl}/api/v1/orders", data=payload)
        return response

    @allure.step('Выполяем запрос на получение списка заказов')
    def orders_list(self):
        response = requests.get(f"{test_data.curl}/api/v1/orders")
        return response









