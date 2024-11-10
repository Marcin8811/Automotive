import requests


class Test_new_location():
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com"  # базовая URL
        key = "?key=qaclick123"  # параметр для всех запросов

        """Создание новой локации"""

        post_resource = "/maps/api/place/add/json"  # ресурс метода POST

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

        # Выполняем POST-запрос
        result_post = requests.post(post_url, json=json_for_create_new_location)
        print("Ответ от POST-запроса:")
        check_post = result_post.json()  # Получаем ответ как JSON
        print(check_post)  # Печатаем весь ответ
        print("Статус код : " + str(result_post.status_code))

        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Успешно!!! Создана новая локация")
        else:
            print("Провал! Запрос ошибочный")

        # Проверка статуса ответа
        check_info_post = check_post.get("status")
        print("Статус код ответа : " + check_info_post)
        assert check_info_post == "OK"
        print("Статус ответа верен")

        # Получаем place_id
        place_id = check_post.get("place_id")
        print("Place_id : " + place_id)

        """Проверка создания новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print("GET URL:", get_url)

        result_get = requests.get(get_url)
        print("Ответ от GET-запроса:")
        print(result_get.json())  # Печатаем весь ответ от GET-запроса
        print("Статус код : " + str(result_get.status_code))

        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Проверка создания новой локации прошла успешно!")
        else:
            print("Провал! Запрос ошибочный")


# Запуск теста
new_place = Test_new_location()
new_place.test_create_new_location()
