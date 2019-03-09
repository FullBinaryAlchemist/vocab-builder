from django.template.defaultfilters import register


@register.filter(name='get_value')
def get_value(tot_words, key):
    print(tot_words.get(key))
    return tot_words.get(key)
