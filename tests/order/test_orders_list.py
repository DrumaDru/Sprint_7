import pytest
import allure
from helpers import Helpers

class TestOrderList:
    @allure.title('Проверка, что в тело ответа возвращается список заказов.')
    @allure.description('Проверить, что если в методе orders_list, выполнить запрос на получение списка заказов,'
                        'то вернется код 200, а тело запроса будет содержать массив данных с заказами Orders')
    def test_orders_list(self):
        helpers = Helpers()
        response = helpers.orders_list()
        assert response.status_code == 200  and 'orders' in response.text



