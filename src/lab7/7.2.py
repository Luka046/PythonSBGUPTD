def find_duplicates(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

items = [1, 2, 3, 2, 4, 5, 3]
duplicates = find_duplicates(items)
print("Повторяющиеся элементы:", duplicates)