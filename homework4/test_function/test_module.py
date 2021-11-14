
class TestFunction:
    """Реализуйте в отдельном модуле (файле) тестовую функцию которая будет принимать 2 параметра:
url - должно быть значение по умолчанию https://ya.ru
status_code - значение по умолчанию 200
Параметры должны быть реализованы через pytest.addoption.
Можно положить фикcтуру и тестовую функцию в один файл.
Основная задача чтобы ваш тест проверял по переданному урлу статус ответа тот который передали,
т.е. по адресу https://ya.ru/sfhfhfhfhfhfhfhfh должен быть валидным ответ 404
пример запуска pytest test_module.py --url=https://mail.ru --status_code=200"""

    def test_url(self, module_client):
        response = module_client.get_unauthorized(url=module_client.url, uri='')
        assert response.status_code == int(module_client.status_code)
