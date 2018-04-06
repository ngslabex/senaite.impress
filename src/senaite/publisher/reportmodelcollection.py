# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.PUBLISHER
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from senaite.publisher.interfaces import IReportModelCollection
from zope.interface import implements


class ReportModelCollection(list):
    """Collection of Report Models
    """
    implements(IReportModelCollection)
