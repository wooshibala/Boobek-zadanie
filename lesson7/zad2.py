def has_special_char(string):
    special_chars = "№#%!$@&*"
    return any(c in special_chars for c in string)

print(has_special_char("Саламатсыздарбы!"))
print(has_special_char("1 dollar & 99 cents"))
print(has_special_char("Дай 5"))
