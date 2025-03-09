import requests


def get_historical_facts(city):
    # URL API (пример для Historical Events API)
    url = "https://history.muffinlabs.com/date"  # Бесплатный API, ключ не требуется

    try:
        # Отправляем GET-запрос
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос успешен
        data = response.json()  # Парсим JSON-ответ

        # Выводим данные
        if "data" in data:
            events = data["data"]["Events"]
            print(f"Исторические факты для {city}:")
            for event in events[:2]:  # Выводим первые два события
                print(f"- {event['year']}: {event['text']}")
        else:
            print("Ошибка: данные не получены.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")


# Пример использования
city = "Moscow"
get_historical_facts(city)