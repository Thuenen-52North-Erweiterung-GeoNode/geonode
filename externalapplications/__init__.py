from django.apps import AppConfig

class ExternalapplicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'externalapplications'
    type = 'GEONODE_APP'
    default_model = 'ExternalApplication'

default_app_config = 'externalapplications.ExternalapplicationsConfig'
