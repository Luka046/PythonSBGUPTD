def mix_colors(color1, color2):
    if color1 not in ["красный", "синий", "желтый"] or color2 not in ["красный", "синий", "желтый"]:
        return "Ошибка: введен неверный цвет"
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        return "Фиолетовый"
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        return "Оранжевый"
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        return "Зеленый"
    else:
        return "Ошибка: одинаковые цвета"

color1 = input("Введите первый цвет: ").lower()
color2 = input("Введите второй цвет: ").lower()
print(mix_colors(color1, color2))