import requests
import time

class TestNewLocation:
    """Тестирование работы с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com"
        key = "?key=qaclick123"

        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key
        print("POST URL:", post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        # Отправляем POST-запрос для создания локации
        result_post = requests.post(post_url, json=json_for_create_new_location)
        print("Ответ от POST-запроса:")
        print(result_post.text)
        print("Статус код : " + str(result_post.status_code))

        # Проверка успешности запроса
        assert 200 == result_post.status_code, f"Ошибка при создании локации, код ответа: {result_post.status_code}"

        check_post = result_post.json()
        assert check_post.get("status") == "OK", "Ответ от сервера не содержит статус OK"
        print("Статус ответа верен")

        place_id = check_post.get("place_id")
        print("Place_id : " + place_id)

        # Проверка, что place_id не пустой
        assert place_id is not None, "place_id не найден!"

        """Проверка создания новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print("GET URL:", get_url)

        result_get = requests.get(get_url)
        print("Ответ от GET-запроса:")
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))

        assert 200 == result_get.status_code, f"Ошибка при проверке локации, код ответа: {result_get.status_code}"
        print("Проверка создания новой локации прошла успешно!")

        """Изменение новой локации"""

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print("PUT URL:", put_url)

        json_for_update_new_location = {
            "place_id": place_id,  # Используем правильный place_id
            "address": "100 Lenina street, RU",
            "name": "Updated Frontline House",  # Добавим новое имя, если требуется
            "phone_number": "(+91) 983 893 3938"  # Обновим телефонный номер
        }

        # Выполнение PUT-запроса
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print("Ответ от PUT-запроса (raw):", result_put.text)
        print("Код статуса от PUT-запроса:", result_put.status_code)

        # Проверка успешности PUT-запроса
        if result_put.status_code == 200:
            try:
                # Попробуем декодировать ответ в JSON, если он не пустой
                if result_put.text:
                    put_response_json = result_put.json()
                    print("Ответ от PUT-запроса в формате JSON:", put_response_json)
                else:
                    print("Ответ PUT-запроса пустой.")
            except ValueError as e:
                print(f"Ошибка при декодировании JSON: {e}")
                print("Ответ от PUT-запроса (raw):", result_put.text)
        else:
            print(f"Ошибка PUT-запроса! Код статуса: {result_put.status_code}")
            print("Ответ от PUT-запроса (raw):", result_put.text)

        # Добавляем небольшой таймаут для обновления данных на сервере
        print("Ожидаем 10 секунд для обновления данных на сервере...")
        time.sleep(10)  # Увеличено время ожидания до 10 секунд

        """Проверка изменения новой локации"""
        result_get = requests.get(get_url)
        print("Ответ от GET-запроса после PUT:")
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))

        assert 200 == result_get.status_code, f"Ошибка при проверке обновленного адреса, код ответа: {result_get.status_code}"

        check_address = result_get.json()
        check_address_info = check_address.get("address")
        print("Адрес после PUT-запроса : " + check_address_info)

        # Проверка на правильность обновленного адреса
        assert check_address_info == "100 Lenina street, RU", f"Адрес не обновился! Получен адрес: {check_address_info}"
        print("Адрес верно обновлен")

        """Удаление новой локации"""

        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        print("Статус код : " + str(result_delete.status_code))

        assert 200 == result_delete.status_code, f"Ошибка при удалении локации, код ответа: {result_delete.status_code}"
        print("Удаление прошло успешно!")

        # Проверка статуса удаления
        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print("Сообщение : " + check_status_info)
        assert check_status_info == "OK", f"Ошибка при удалении локации, сообщение от сервера: {check_status_info}"

        """Проверка удаления новой локации"""

        result_get = requests.get(get_url)
        print("Ответ от GET-запроса после удаления:")
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))

        # Проверка, что локация действительно была удалена
        assert 404 == result_get.status_code, f"Локация не была удалена, код ответа: {result_get.status_code}"

        print("Тест завершен успешно.")

        print("Тестирование TestNewLocation завершено успешно")

# Создаём объект теста
new_place = TestNewLocation()
# Запускаем тест
new_place.test_create_new_location()
