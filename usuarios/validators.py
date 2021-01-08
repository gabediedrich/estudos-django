import re
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class BrazilPhoneNumberValidator(validators.RegexValidator):
    '''
    Valida um número de telefone nacional, fixo (8 dígitos) ou móvel (9 dígitos), incluindo DDD (2 ou 3 dígitos)
    '''
    regex = r'\(?([1-9]{2,3})\)?([0-9]{9})'
    message = _(
        'Digite um telefone nacional válido, com DDD de 2 ou 3 dígitos '
        'e número com 9 dígitos'
    )
    flags = 0