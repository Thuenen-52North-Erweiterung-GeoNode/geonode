import os
from django.apps import AppConfig
from django.conf.urls import include, url


def run_setup_hooks(*args, **kwargs):
    from django.conf import settings
    from geonode.urls import urlpatterns
    from geonode.base.models import Menu, MenuItem, MenuPlaceholder

    LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
    settings.MAPSTORE_TRANSLATIONS_PATH += ("/static/mapstore/ea-translations",)
    settings.TEMPLATES[0]["DIRS"].insert(0, os.path.join(LOCAL_ROOT, "templates"))

    if not Menu.objects.filter(title="External Applications").exists():
        ph = MenuPlaceholder.objects.filter(name="TOPBAR_MENU_LEFT").first()
        menu = Menu.objects.create(title="External Applications", placeholder=ph, order=1)
        MenuItem.objects.create(title="External Applications", menu=menu, order=1, blank_target=False,
                                url="/catalogue/#/search/?f=externalapplication")

    urlpatterns += [url(r'^external-applications/', include('externalapplications.urls'))]


class ExternalapplicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'externalapplications'
    type = 'GEONODE_APP'
    default_model = 'ExternalApplication'

    def ready(self):
        super().ready()
        run_setup_hooks()


default_app_config = 'externalapplications.ExternalapplicationsConfig'
