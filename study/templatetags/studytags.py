from django.template.defaultfilters import register


@register.filter(name='get_value')
def get_value(tot_words, key):
    return tot_words.get(str(key))  # since type(key)=<class 'study.models.List'>
