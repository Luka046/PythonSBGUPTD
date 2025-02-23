def is_rare_word(word):
    return "ф" in word.lower()

def check_rare_word():
    word = input("Введите слово: ")
    if is_rare_word(word):
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

check_rare_word()