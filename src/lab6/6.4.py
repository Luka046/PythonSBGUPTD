def is_lucky_ticket(ticket):
    half = len(ticket) // 2
    first_half = sum(map(int, ticket[:half]))
    second_half = sum(map(int, ticket[half:]))
    return first_half == second_half

ticket = input("Введите номер билета: ")
if is_lucky_ticket(ticket):
    print("Билет счастливый!")
else:
    print("Билет не счастливый.")