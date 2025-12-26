import allure
import requests

@allure.title("Проверка получения списка пользователей")
@allure.description("Отправляет GET-запрос к JSONPlaceholder, проверяет статус 200 и наличие данных")
def test_get_users():
    with allure.step("Отправить GET-запрос к /users"):
        response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    with allure.step("Проверить статус-код"):
        assert response.status_code == 200

    with allure.step("Проверить, что в ответе есть пользователи"):
        data = response.json()
        assert len(data) > 0
        assert "name" in data[0]

