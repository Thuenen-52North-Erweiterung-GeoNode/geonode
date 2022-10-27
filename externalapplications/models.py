from importlib.resources import Resource
from django.db import models
from geonode.geoapps.models import GeoApp




# Create your models here.
class ExternalApplication(GeoApp):
    url = models.URLField(max_length=2000, null=False, blank=False, help_text="Link to the external application")