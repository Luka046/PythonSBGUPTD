days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
weekend_count = int(input("Сколько выходных на неделе вы хотите? "))

weekend_days = days[-weekend_count:]
work_days = days[:-weekend_count]

print("Ваши выходные дни:", ", ".join(weekend_days))
print("Ваши рабочие дни:", ", ".join(work_days))