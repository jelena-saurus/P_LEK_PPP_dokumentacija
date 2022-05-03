#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#creating-custom-symbol-layer-types
# pravljenje svoje klase simbol lejera koja ce prikazivati
# feature onako kako si definisao

from qgis.core import QgsMarkerSymbolLayer
from qgis.PyQt.QtGui import QColor

# lejer mora biti aktivan 
layer = iface.activeLayer()

# Here is an example of a marker that draws red circles with specified radius
class FooSymbolLayer(QgsMarkerSymbolLayer):
    def __init__(self, radius=4.0):
        QgsMarkerSymbolLayer.__init__(self)
        self.radius = radius
        self.color = QColor(255,0,0)
    
    def layerType(self): # The layerType() method determines the name
# of the symbol layer; it has to be unique among all symbol layers
        return "FooMarker"
    
    def properties(self): # The properties() method is used for persistence of attributes
        return {'radius' : str(self.radius)}
        
    def startRender(self, context): # Finally there are rendering methods: startRender()
# is called before rendering the first feature,
        pass
    
    def stopRender(self, context): # stopRender() when the rendering is done
        pass
    
    def renderPoint(self, point, context): #and renderPoint() is called to do the rendering.
# The coordinates of the point(s) are already transformed to the output coordinates
# Rendering depends on whether the symbol is selected (QGIS >= 1.5)
# Renderovanje zavisi od toga da li je simbol izabran

        color = context.selectionColor() if context.selected() else self.color
        p = context.renderContext().painter()
        p.setPen(color)
        p.drawEllipse(point, self.radius, self.radius)
    
    def clone(self): # The properties() method is used for persistence of attributes
        return FooSymbolLayer(self.radius)

# nema odgovora 

# Usually it is convenient to add a GUI for setting attributes of the symbol layer
# type to allow users to customize the appearance: in case of our example above
# we can let user set circle radius.
# The following code implements such widget
# moze se dodati gui da bi se menjali atributi tipa simbol lejera

from qgis.gui import QgsSymbolWidget 

class FooSymbolLayerWidget(QgsSymbolLayerWidget):
    def __init__(self, parent=None):
        QgsSymbolLayerWidget.__init__(self, parent)
        self.layer = None

# setup a simple UI
# postavljanje grafickog interfejsa
        self.label = QLabel('Radius: ')
        self.spinRadius = QDoubleSpinBox()
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.spinRadius)
        self.setLayout(self.hbox)
        self.connect(
        self.spinRadius,
        SIGNAL('valueChanged(double)'),
        self.radiusChanged
        )
    
    def setSymbolLayer(self, layer):
        if layer.layerType() != 'FooMarker':
            return
        self.layer = layer
        self.spinRadius.setValue(layer.radius)
    
    def symbolLayer(self):
        return self.layer
    
    def radiusChanged(self, value):
        self.layer.radius = value
        self.emit(SIGNAL('changed()'))

# vraca greske kod svakog definisanja

# We will have to create metadata for the symbol layer
# pravljenje metapodataka za simbol lejer
        
from qgis.core import QgsSymbol, QgsSymbolLayerAbstractMetadata, QgsSymbolLayerRegistry

class FooSymbolLayerMetadata(QgsSymbolLayerAbstractMetadata):

    def __init__(self):
        super().__init__('FooMarker', 'Moj novi Foo marker', QgsSymbol.Marker)
    
    def createSymbolLayer(self, props):
        radius = float(props['radius']) if 'radius' in props else 4.0
        return FooSymbolLayer(radius)

simbol = FooSymbolLayer()
print(simbol.layerType())

fslmetapodaci = FooSymbolLayerMetadata()
QgsApplication.symbolLayerRegistry().addSymbolLayerType(fslmetapodaci)

# false
       
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
