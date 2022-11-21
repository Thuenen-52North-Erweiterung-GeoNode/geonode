import os
from django.apps import AppConfig
from django.conf.urls import include, url
import logging

from .database.database import create_catalog_table

logger = logging.getLogger(__name__)


def insert_base_data():
    logger.info("Loading non-spatial static data")
    from django.conf import settings
    from geonode.urls import urlpatterns
    from geonode.base.models import Menu, MenuItem, MenuPlaceholder

    try:
        create_catalog_table()
        
        LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
        settings.MAPSTORE_TRANSLATIONS_PATH += ("/static/mapstore/nsd-translations",)
        settings.TEMPLATES[0]["DIRS"].insert(0, os.path.join(LOCAL_ROOT, "templates"))

        title = "Non-Spatial Datasets"

        if not Menu.objects.filter(title=title).exists():
            if (not MenuPlaceholder.objects.filter(name="TOPBAR_MENU_LEFT").first()):
                logger.info(f"MenuPlaceholder not yet created. Skipping")
                return

            ph = MenuPlaceholder.objects.filter(name="TOPBAR_MENU_LEFT").first()        
            menu = Menu.objects.create(title=title, placeholder=ph, order=1)
            MenuItem.objects.create(title=title, menu=menu, order=1, blank_target=False,
                                    url="/catalogue/#/search/?f=nonspatialdataset")

        urlpatterns += [url(r'^nonspatial/', include('nonspatialdatasets.urls'))]
        logger.info("Non-spatial datasets contrib module loaded")
    except Exception as e:
        logger.exception(e)

class NonSpatialDatasetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nonspatialdatasets'
    type = 'GEONODE_APP'
    default_model = 'NonSpatialDataset'

    def ready(self):
        super().ready()
        insert_base_data()

default_app_config = 'nonspatialdatasets.NonSpatialDatasetsConfig'
