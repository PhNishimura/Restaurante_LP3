from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

LISTA_CATEGORIAS = (
    ("Brasil", "Brasil"),
    ("Mexico", "Mexico"),
    ("Arabe", "Arabe"),
    ("Japao", "Japao"),
    ("Argentina", "Argentina"),
    ("Coreia", "Coreia"),
    ("OUTROS", "Outros"),
)

MACRO_REGIOES = (
    ("AMERICA_SUL", "América do Sul"),
    ("AMERICA_NORTE", "América do Norte"),
    ("AMERICA_CENTRAL", "América Central"),
    ("ASIA", "Ásia"),
    ("AFRICA", "África"),
    ("ARABIA", "Arábia "),
    ("OUTROS", "Outros"),
)
class Regiao(models.Model):
    nome_regiao = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_regioes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=10, choices=LISTA_CATEGORIAS)
    macro_regiao = models.CharField(max_length=30, choices=MACRO_REGIOES, default='OUTROS')
    acessos = models.IntegerField(default=0)
    data_criacao=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_regiao

class Prato(models.Model):
    #Recomenda-se inserir o campo chave estrangeira como primeiro campo da classe por causa das migrações.
    regiao = models.ForeignKey("Regiao", related_name="pratos", on_delete=models.CASCADE)
    #CharField é um campo curto
    nome_prato = models.CharField(max_length=100)
    #O campo models.URLField é a definição de im link para um video.
    video = models.URLField()

    def __str__(self):
        return self.regiao.nome_regiao + " - " + self.nome_prato

# Criação da classe Usuario
class Usuario(AbstractUser):
    regioes_vistas = models.ManyToManyField("Regiao")
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []