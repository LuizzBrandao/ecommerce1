from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    # Rotas principais do carrinho
    path('', views.detalhe_carrinho, name='detalhe'),
    path('adicionar/<int:produto_id>/', views.adicionar_carrinho, name='adicionar'),
    path('remover/<int:produto_id>/', views.remover_carrinho, name='remover'),
    path('limpar/', views.limpar_carrinho, name='limpar'),

    # Rotas para requisições AJAX
    path('ajax/adicionar/<int:produto_id>/', views.adicionar_carrinho_ajax, name='adicionar_ajax'),
]
