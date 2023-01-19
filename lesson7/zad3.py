def has_uppercase(string):
    return any(c.isupper() for c in string)

print(has_uppercase("Саламатсыздарбы!"))
print(has_uppercase("1 dollar & 99 cents"))
print(has_uppercase("Дай 5"))
