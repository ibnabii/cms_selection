"""
Django settings for cms_selection project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3m6%oig4dun!0lha7x$(+@&tua4&&arzg=o@6#na!3fn@5a-_)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "djangocms_admin_style",  # required by django-cms, it has to be before django.contrib.admin
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # required by django-cms
    "cms",  # required by django-cms
    "menus",  # required by django-cms
    "treebeard",  # required by django-cms
    "sekizai",  # required by django-cms
    "djangocms_versioning",  # required by django-cms (recommended)
    "djangocms_alias",  # required by django-cms (recommended)
    "wagtail.contrib.forms",  # required by wagtail
    "wagtail.contrib.redirects",  # required by wagtail
    "wagtail.embeds",  # required by wagtail
    "wagtail.sites",  # required by wagtail
    "wagtail.users",  # required by wagtail
    "wagtail.snippets",  # required by wagtail
    "wagtail.documents",  # required by wagtail
    "wagtail.images",  # required by wagtail
    "wagtail.search",  # required by wagtail
    "wagtail.admin",  # required by wagtail
    "wagtail",  # required by wagtail
    "modelcluster",  # required by wagtail
    "taggit",  # required by wagtail
    "wagtail_home",  # sample wagtail app
]

SITE_ID = 1  # required by django-cms

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # required by django-cms
    "cms.middleware.utils.ApphookReloadMiddleware",  # required by django-cms (actually recommended)
    "cms.middleware.user.CurrentUserMiddleware",  # required by django-cms
    "cms.middleware.page.CurrentPageMiddleware",  # required by django-cms
    "cms.middleware.toolbar.ToolbarMiddleware",  # required by django-cms
    "cms.middleware.language.LanguageCookieMiddleware",  # required by django-cms
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",  # required by wagtail
]

ROOT_URLCONF = "cms_selection.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",  # required by django-cms
                "sekizai.context_processors.sekizai",  # required by django-cms
                "cms.context_processors.cms_settings",  # required by django-cms (by cms check)
            ],
        },
    },
]

WSGI_APPLICATION = "cms_selection.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "pl"
LANGUAGES = [
    ("pl", "Polski"),
    # ("en", "English"),
]
TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "static_files"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# django-cms
CMS_CONFIRM_VERSION4 = True
X_FRAME_OPTIONS = "SAMEORIGIN"
CMS_TEMPLATES = [
    ("django_cms_home.html", "Home page template"),
]


# wagtail
WAGTAIL_SITE_NAME = "Przykładowa strona"
WAGTAILADMIN_BASE_URL = "http://127.0.0.1:8000/wagtail/cms"
# If this setting is not present, Wagtail will fall back to request.site.root_url or to the hostname of the request.
# Although this setting is not strictly required, it is highly recommended because leaving it out may produce
# unusable URLs in notification emails.
# WAGTAILADMIN_BASE_URL = "http://zobaczymy"

# Add a WAGTAILDOCS_EXTENSIONS setting to specify the file types that Wagtail will allow to be uploaded as documents.
# This can be omitted to allow all file types, but this may present a security risk if untrusted users are allowed
# to upload documents - see User Uploaded Files.
# WAGTAILDOCS_EXTENSIONS = ['csv', 'docx', 'key', 'odt', 'pdf', 'pptx', 'rtf', 'txt', 'xlsx', 'zip']
