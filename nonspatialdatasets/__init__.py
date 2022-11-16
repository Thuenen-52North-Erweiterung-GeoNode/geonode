import os
from django.apps import AppConfig
from django.conf.urls import include, url


def run_setup_hooks(*args, **kwargs):
    from django.conf import settings
    from geonode.urls import urlpatterns
    from geonode.base.models import Menu, MenuItem, MenuPlaceholder

    LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
    settings.MAPSTORE_TRANSLATIONS_PATH += ("/static/mapstore/nsd-translations",)
    settings.TEMPLATES[0]["DIRS"].insert(0, os.path.join(LOCAL_ROOT, "templates"))

    title = "Non-Spatial Datasets"

    if not Menu.objects.filter(title=title).exists():
        ph = MenuPlaceholder.objects.filter(name="TOPBAR_MENU_LEFT").first()
        menu = Menu.objects.create(title=title, placeholder=ph, order=1)
        MenuItem.objects.create(title=title, menu=menu, order=1, blank_target=False,
                                url="/catalogue/#/search/?f=nonspatialdataset")

    urlpatterns += [url(r'^nonspatial/', include('nonspatialdatasets.urls'))]


class NonSpatialDatasetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nonspatialdatasets'
    type = 'GEONODE_APP'
    default_model = 'NonSpatialDataset'

    def ready(self):
        super().ready()
        run_setup_hooks()


default_app_config = 'nonspatialdatasets.NonSpatialDatasetsConfig'
