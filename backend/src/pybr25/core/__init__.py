"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


__version__ = "20251021.0"

PACKAGE_NAME = "pybr25.core"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
