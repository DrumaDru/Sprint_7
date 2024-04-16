import pytest
import allure
from helpers import Helpers

class TestOrderCreation:
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["BLACK", "GREY"],
            []
        ]
    )
    @allure.title('Проверка, что можно указать один из цветов — BLACK или GREY, оба цвета, без цветов,'
                  'и что тело ответа содержит track')
    @allure.description('Проверяем, что если в методе order_create_colors, выполнить запрос на создание закзаа, с указанием различных вариантов'
                        'заполнения поля "Цвет", то будет возвращаться код 201 и тело овтета будет содержать track номер закзаа')
    def test_order_colors(self, color):
        helpers = Helpers()
        response = helpers.order_create_colors(color)
        assert response.status_code == 201 and response.json()['track'] !=0



