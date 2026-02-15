from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fichas/', views.lista_fichas, name='lista_fichas'),
    path('ficha/<int:ficha_id>/', views.visualizar_ficha, name='visualizar_ficha'),
    path('ficha/<int:ficha_id>/editar/', views.editar_ficha, name='editar_ficha'),
    path('ficha/<int:ficha_id>/deletar/', views.deletar_ficha, name='deletar_ficha'),
    path('ficha/<int:ficha_id>/download-pdf/', views.download_pdf, name='download_pdf'),
    path('ficha/<int:ficha_id>/download-word/', views.download_word, name='download_word'),
]
