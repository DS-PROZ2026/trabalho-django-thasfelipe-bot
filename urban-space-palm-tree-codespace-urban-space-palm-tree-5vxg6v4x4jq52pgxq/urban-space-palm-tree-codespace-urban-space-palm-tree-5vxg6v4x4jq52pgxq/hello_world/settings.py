"""
Django settings for hello_world project.
Projeto preparado para GitHub Codespaces e execução local.
"""

import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# Chave de desenvolvimento. Pode ser substituída por SECRET_KEY no ambiente.
SECRET_KEY = config("SECRET_KEY", default="django-insecure-gestao-ativos-2026-codespace")
DEBUG = config("DEBUG", default=True, cast=bool)

# Aceita acesso local e o domínio de preview do GitHub Codespaces.
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "[::1]",
    ".app.github.dev",
]

# O navegador interno do Codespaces pode enviar a origem como localhost.
# Mantemos as origens local e app.github.dev confiáveis para os formulários POST.
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "https://localhost:8000",
    "https://*.app.github.dev",
]

# Também adiciona explicitamente a URL deste Codespace quando as variáveis existem.
codespace_name = os.environ.get("CODESPACE_NAME")
codespace_domain = os.environ.get("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")
if codespace_name and codespace_domain:
    codespace_origin = f"https://{codespace_name}-8000.{codespace_domain}"
    if codespace_origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(codespace_origin)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_browser_reload",
    "meu_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "hello_world.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "hello_world" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hello_world.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "hello_world" / "static"]
STATIC_ROOT = BASE_DIR / "hello_world" / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "hello_world" / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"
