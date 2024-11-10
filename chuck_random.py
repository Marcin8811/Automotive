import requests

class TestNewJoke:
    """Создание новой шутки"""

    def test_create_new_random_categories_joke(self):
        """Создание случайной шутки на определенную тему"""
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("Статус код : " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успех! Мы получили новую шутку!")
        else:
            print("Что-то пошло не так, давай по новой.")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("Категория верна")

if __name__ == "__main__":
    # Запуск теста
    test_instance = TestNewJoke()
    test_instance.test_create_new_random_categories_joke()
