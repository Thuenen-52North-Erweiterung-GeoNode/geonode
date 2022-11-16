from importlib.resources import Resource
from django.db import models
from geonode.geoapps.models import GeoApp




# Create your models here.
class NonSpatialDataset(GeoApp):
    url = models.URLField(max_length=2000, null=False, blank=False, help_text="Link to the external application")

    def get_absolute_url(self):
        return f"/nonspatial/{self.pk}"
        