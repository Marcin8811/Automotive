import requests
import time

time.sleep(5)

class Test_new_location():
    """Работа с новой локацией"""

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

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print("Ответ от POST-запроса:")
        check_post = result_post.json()
        print(check_post)
        print("Статус код : " + str(result_post.status_code))

        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Успешно!!! Создана новая локация")
        else:
            print("Провал! Запрос ошибочный")

        check_info_post = check_post.get("status")
        print("Статус код ответа : " + check_info_post)
        assert check_info_post == "OK"
        print("Статус ответа верен")

        place_id = check_post.get("place_id")
        print("Place_id : " + place_id)

        """Проверка создания новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print("GET URL:", get_url)

        result_get = requests.get(get_url)
        print("Ответ от GET-запроса:")
        print(result_get.json())
        print("Статус код : " + str(result_get.status_code))

        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Проверка создания новой локации прошла успешно!")
        else:
            print("Провал! Запрос ошибочный")

        # https: // rahulshettyacademy.com / maps / api / place / update / json?key = qaclick123

        """Изменение новой локации"""

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print("PUT URL:", put_url)

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU"
        }

        result_put = requests.put(put_url, json=json_for_update_new_location)

        # Печатаем сырое содержимое ответа от PUT-запроса
        print("Ответ от PUT-запроса (raw):", result_put.text)
        print("Код статуса от PUT-запроса:", result_put.status_code)

        # Проверяем, что запрос прошел успешно
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("Изменение новой локации")

            # Проверяем, что ответ от PUT-запроса содержит корректный JSON
            try:
                response_json = result_put.json()
                print("Ответ от PUT-запроса (JSON):", response_json)
                # Если сообщение об успешном обновлении есть, выводим его
                if 'msg' in response_json:
                    print("Сообщение об успешном обновлении:", response_json['msg'])
                else:
                    print("Сообщение 'msg' не найдено в ответе.")
            except ValueError:
                print("Ответ от PUT-запроса не является JSON. Ответ:", result_put.text)
        else:
            print("Провал! Запрос ошибочный")

            """Проверка изменения новой локации"""

            result_get = requests.get(get_url)
            print("Ответ от GET-запроса:")
            print(result_get.json())
            print("Статус код : " + str(result_get.status_code))

            assert 200 == result_get.status_code
            if result_get.status_code == 200:
                print("Проверка изменения новой локации прошла успешно!")
            else:
                print("Провал! Запрос ошибочный")
            check_address = result_get.json()
            check_address_info = check_address.get("address")
            print("Сообщение : " + check_address_info)
            assert check_address_info == "100 Lenina street, RU"
            print("Сообщение верно")


# Запуск теста
new_place = Test_new_location()
new_place.test_create_new_location()
