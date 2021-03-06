# -*- coding: utf-8 -*-
# Copyright 2017-2019 ControlScan, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
"""

"""

# third party
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

# local
from cyphon.models import GetByNameManager
from parsers.models import StringParser
from sifter.condensers.models import Condenser, Fitting


class LogParser(StringParser):
    """

    """
    objects = GetByNameManager()


class LogCondenser(Condenser):
    """

    """
    objects = GetByNameManager()


class LogFitting(Fitting):
    """

    """
    CONDENSER = models.Q(app_label='logcondensers', model='logcondenser')
    PARSER = models.Q(app_label='logcondensers', model='logparser')
    CONTENT_TYPES = PARSER | CONDENSER

    condenser = models.ForeignKey(LogCondenser, related_name='fittings',
                                  related_query_name='fitting')
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to=CONTENT_TYPES,
                                     verbose_name=_('parser type'))

