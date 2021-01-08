from django.db import models
from django.contrib.auth.models import User
from .validators import BrazilPhoneNumberValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class UserInfo(User):
    """
    Extende o modelo base de usuário (username, password, first_name,
    last_name, email)    
    """
    profile_pic = models.ImageField(upload_to="media/",             #todo Como realizar o upload de arquivos?
                                    blank=True,
                                    default="media/default.jpg", 
                                    verbose_name="Foto de Perfil",
                                    help_text=_("Selecione uma imagem para ser sua foto pública de perfil"))
    phone_number = models.CharField(max_length=12, 
                                    validators=[BrazilPhoneNumberValidator],  
                                    verbose_name=_("Número de Telefone"),
                                    help_text=_("Um número de telefone nacional com o DDD e os 9 dígitos"))
    description = models.CharField(blank=True,
                                   max_length=100,  
                                   verbose_name=_("descrição"),
                                   help_text=_("Descrição breve"))


    def __str__(self):
        return self.username

    #def get_absolute_url(self):  #todo URL para o perfil do usuário
    #    return reverse('perfil', kwargs={'pk': self.id})
