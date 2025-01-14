#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from geonode.catalogue.backends.generic import CatalogueBackend as GenericCatalogueBackend


class CatalogueBackend(GenericCatalogueBackend):
    """pycsw HTTP CSW backend"""

    def __init__(self, *args, **kwargs):
        """initialize pycsw HTTP CSW backend"""
        GenericCatalogueBackend.__init__(CatalogueBackend, self, *args, **kwargs)
        self.catalogue.formats = ["Atom", "DataCite", "DIF", "Dublin Core", "ebRIM", "FGDC", "ISO"]
