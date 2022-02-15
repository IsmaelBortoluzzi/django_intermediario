from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from core.models import Produto, Contato
from core.forms import ContatoForm


class Index(TemplateView):
    template_name = 'index.html'
    produtos = Produto.objects.all()

    def get_context_data(self, **kwargs):
        context = {
            'produtos': self.produtos,
        }
        return context


class Contato(FormView):
    model = Contato
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = '/contato'

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'email enviado com sucesso!')
            form = ContatoForm()

            return self.form_valid(form)
        else:
            messages.error(request, 'erro no envio!')
            return self.form_invalid(form)


class Produto(ListView):
    model = Produto
    template_name = 'produto.html'
    context_object_name = 'produto'

