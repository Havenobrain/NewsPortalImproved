from django import template
register = template.Library()



@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Это не слово!")

    bad_words = ('москвичи', 'пожары', 'также', 'Путин', 'ветер', 'запах')


    for word in bad_words:
        value = value.replace(word[1:], '*'*(len(word)-1))

    return "".join(value)