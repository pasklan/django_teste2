from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def index(request):
  context = {
    'produtos': Produto.objects.all()
  }
  return render(request, 'index.html', context)

# lida com envio de e-mail do formulário contato
def contato(request):
  form = ContatoForm(request.POST or None) # formulario pode conter dados, durante o POST ou não, durante o GET
  if str(request.method) == 'POST':
    # se os dados do formulário forem válidos
    if form.is_valid():
      form.send_mail()          
       
      messages.success(request, 'E-mail enviado com sucesso!')
      form = ContatoForm()
    else:
      messages.error(request, 'Erro ao enviar e-mail')

  context = {
    'form': form
  }
  return render(request, 'contato.html', context)


# lida com cadastro de produtos
def produto(request):
  if str(request.user) != 'AnonymousUser':
    
    if str(request.method) == 'POST':
      form = ProdutoModelForm(request.POST, request.FILES)
      if form.is_valid():
        form.save() # commit = False para apenas visualizar os dados
              
        messages.success(request, 'Produto salvo com sucesso')
        form = ProdutoModelForm()
      else:
        messages.error(request, 'Erro ao salvar produto')
    else:
      form = ProdutoModelForm()
    
    context = {
      'form' : form
    }
    return render(request, 'produto.html', context)
  else:
    return redirect(index)