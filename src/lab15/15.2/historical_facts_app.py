import requests


def get_historical_facts(city):
    # URL API (пример для Historical Events API)
    url = f"https://history.muffinlabs.com/date"  # Бесплатный API, ключ не требуется

    # Отправляем запрос
    response = requests.get(url)
    data = response.json()

    # Выводим данные
    if "data" in data:
        events = data["data"]["Events"]
        print(f"Исторические факты для {city}:")
        for event in events[:2]:  # Выводим первые два события
            print(f"- {event['year']}: {event['text']}")
    else:
        print("Ошибка: данные не получены.")


# Пример использования
city = "Moscow"
get_historical_facts(city)