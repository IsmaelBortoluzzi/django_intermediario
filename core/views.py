from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from core.models import Produto, Contato
from core.forms import ContatoForm, ProdutoModelForm

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


class Produto(FormView):
    model = Produto
    template_name = 'produto.html'
    form_class = ProdutoModelForm
    success_url = '/produto'

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            produto = form.save(commit=False)
            messages.success(request, 'produto salvado com sucesso!')
            # form = ProdutoModelForm()

            return self.form_valid(form)
        else:
            messages.error(request, 'erro no envio!')
            return self.form_invalid(form)

