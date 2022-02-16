from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('nome', max_length=128)
    preco = models.DecimalField('preco', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('qtd_em_estoque')
    imagem = StdImageField('imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('slug', max_length=128, blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.nome}'


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)


class Contato(models.Model):
    nome = models.CharField('nome', max_length=128)
    sobrenome = models.CharField('sobrenome', max_length=128)
    email = models.EmailField('email', max_length=128)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
