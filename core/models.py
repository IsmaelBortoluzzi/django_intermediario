from django.db import models


class Produto(models.Model):
    nome = models.CharField('nome', max_length=128)
    preco = models.DecimalField('preco', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('qtd_em_estoque')

    def __str__(self):
        return f'{self.nome}'


class Contato(models.Model):
    nome = models.CharField('nome', max_length=128)
    sobrenome = models.CharField('sobrenome', max_length=128)
    email = models.EmailField('email', max_length=128)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
