students = {
    "Иванов": {"английский", "китайский", "французский"},
    "Петров": {"китайский", "немецкий"},
    "Сидоров": {"английский", "испанский"},
    "Козлов": {"китайский", "японский"},
    "Смирнов": {"английский", "китайский", "итальянский"}
}

# a) Определение всех языков
all_languages = set()
for languages in students.values():
    all_languages.update(languages)

print("Все языки:", sorted(all_languages))

# b) Студенты, знающие китайский
chinese_speakers = [student for student, languages in students.items() if "китайский" in languages]
print("Студенты, знающие китайский:", chinese_speakers)