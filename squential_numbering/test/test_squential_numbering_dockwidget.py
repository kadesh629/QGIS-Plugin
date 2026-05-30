# coding=utf-8
"""DockWidget tests for SequentialNumberingDockWidget."""

import pytest
from qgis.PyQt.QtWidgets import QDockWidget

from squential_numbering_dockwidget import SequentialNumberingDockWidget


@pytest.fixture
def dockwidget(qgis_app):
    widget = SequentialNumberingDockWidget(None)
    yield widget
    widget.close()


def test_dockwidget_is_qdockwidget(dockwidget):
    """The generated dockwidget is a QDockWidget instance."""
    assert isinstance(dockwidget, QDockWidget)


def test_dockwidget_has_closing_signal(dockwidget):
    """The dockwidget exposes a closingPlugin signal."""
    assert hasattr(dockwidget, "closingPlugin")
