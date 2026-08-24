"""Rotas principais do projeto.

Por escolha do trabalho, todas as URLs do sistema estão centralizadas neste arquivo.
Não é necessário usar um arquivo meu_app/urls.py.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from hello_world.core import views as core_views
from meu_app import views as app_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="meu_app/login.html"), name="login"),
    path("cadastro/", app_views.cadastro_usuario, name="cadastro_usuario"),
    path("sair/", auth_views.LogoutView.as_view(), name="logout"),
    path("perfil/", app_views.perfil, name="perfil"),
    path("", app_views.dashboard, name="dashboard"),
    path("equipamentos/", app_views.lista_equipamentos, name="lista_equipamentos"),
    path("equipamentos/cadastrar/", app_views.cadastrar_equipamento, name="cadastrar_equipamento"),
    path(
        "equipamento/<int:id>/",
        app_views.detalhes_equipamento,
        name="detalhes_equipamento"
    ),
    path(
        "equipamento/<int:id>/excluir/",
        app_views.excluir_equipamento,
        name="excluir_equipamento"
    ),
    path("pagina-original/", core_views.index, name="pagina_original"),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
