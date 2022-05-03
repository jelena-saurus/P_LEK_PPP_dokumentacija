# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#creating-custom-renderers

# Creating Custom Renderers

# It might be useful to create a new renderer implementation if you would
# like to customize the rules how to select symbols for rendering of features.
# Some use cases where you would want to do it: symbol is determined from a
# combination of fields,
# size of symbols changes depending on current scale etc

import random
from qgis.core import (
QgsWkbTypes, 
QgsSymbol, 
QgsFeatureRenderer,
QgsRendererAbstractMetadata,
QgsRendererRegistry,
QgsApplication
)
from qgis.gui import QgsRendererWidget, QgsColorButton

layer = iface.activeLayer()

class RandomRenderer(QgsFeatureRenderer):
    def __init__(self, syms=None):
        super().__init__('RandomRenderer')
        self.syms = syms if syms else [
         QgsSymbol.defaultSymbol(QgsWkbTypes.geometryType(QgsWkbTypes.Point)),
         QgsSymbol.defaultSymbol(QgsWkbTypes.geometryType(QgsWkbTypes.Point)),
        ]
        
    def symbolForFeature(self, feature, context):
        return random.choice(self.syms)
    
    def startRender(self, context, fields):
        super().startRender(context, fields)
        for s in self.syms:
            s.startRender(context)
    
    def usedAttributes(self, context):
        return []
    
    def clone(self):
        return RandomRenderer(self.syms)
        

class RandomRendererWidget(QgsRendererWidget):
    def __init__(self, layer, style, renderer):
        super().__init__(layer, style)
        if renderer is None or renderer.type() != 'RandomRenderer':
            self.r = RandomRenderer()
        else:
            self.r = renderer
            
#setup UI        
#namestanje grafickog interfejsa
        self.btn1 = QgsColorButton()
        self.btn1.setColor(self.r.syms[0].color())
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn1)
        self.setLayout(self.vbox)
        self.btn1.colorChanged.connect(self.setColor1)
        
    def setColor1(self):
        color = self.btn1.color()
        if not color.isValid():
            return self.r.syms[0].setColor(color)
    
    def renderer(self):
        return self.r


class RandomRendererMetadata(QgsRendererAbstractMetadata):
    
    def __init__(self):
        super().__init__('RandomRenderer', 'Random renderer')
    
    def createRenderer(self, element):
        return RandomRenderer()
    
    def createRendererWidget(self, layer, style, renderer):
        return RandomRendererWidget(layer, style, renderer)

rrmetadata = RandomRendererMetadata()
QgsApplication.rendererRegistry().addRenderer(rrmetadata)
        
        
        
        
        
        
        
        
        
        
        
        
        
        











        

