from qgis.gui import QgsMapTool
from qgis.core import (
    QgsFeatureRequest,
    QgsRectangle
)


class NumberingMapTool(QgsMapTool):

    def __init__(self, canvas, dockwidget):
        super().__init__(canvas)

        self.canvas = canvas
        self.dockwidget = dockwidget

    def canvasReleaseEvent(self, event):

        layer = self.dockwidget.get_selected_layer()

        if not layer:
            return

        point = self.toMapCoordinates(event.pos())

        tolerance = self.canvas.mapUnitsPerPixel() * 5

        rect = QgsRectangle(
            point.x() - tolerance,
            point.y() - tolerance,
            point.x() + tolerance,
            point.y() + tolerance
        )

        request = QgsFeatureRequest()
        request.setFilterRect(rect)

        feature = None

        for feat in layer.getFeatures(request):
            feature = feat
            break

        if feature is None:
            print("No feature found")
            return

        print("Feature Found:", feature.id())