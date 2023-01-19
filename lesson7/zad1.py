def has_digit(string):
    return any(c.isdigit() for c in string)

print(has_digit("Саламатсыздарбы!"))
print(has_digit("1 dollar & 99 cents"))
print(has_digit("Дай 5"))
