# -*- coding: cp1252 -*-
# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/expressions.html
# evaluating-expressions

# 11.2.1. https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/expressions.html
#basic-expressions

# This basic expression evaluates a simple arithmetic operation:
#osnovni izrazi
izraz = QgsExpression('2*3')
print(izraz)
print(izraz.evaluate())
"""6"""

# Expression can also be used for comparison, evaluating to 1 (True) or 0 (False)
# takodje se mogu koristiti za uporedjivanje: 1 je True, 0 je False
izraz = QgsExpression('1+1=2')
print(izraz.evaluate())
"""1"""


# 11.2.2. https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/expressions.html
#expressions-with-features

"""To evaluate an expression against a feature, a QgsExpressionContext object has to be
created and passed to the evaluate function in order to allow the expression to
access the feature’s field values."""

# kreira atribut 'povrs_ha', koji se odnosi na povrsinu u hektarima
atributi = QgsFields()
atribut = QgsField('Kolona')
atributi.append(atribut)
feature = QgsFeature()
feature.setFields(atributi)
feature.setAttribute(0, 99)

izraz = QgsExpression('"Kolona"')
context = QgsExpressionContext()
context.setFeature(feature)
print(izraz.evaluate(context))


# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/expressions.html
#expressions-with-features

from qgis.PyQt.QtCore import QVariant

# create a vector layer
# v1- vektor lejer, pr -, my data - moji podaci, rec - podatak, pt - tacka, f-feature

v1 = QgsVectorLayer('Point?crs=epsg:6316', 'Companies', 'memory')
pr = v1.dataProvider()
pr.addAttributes([QgsField('Name', QVariant.String),
                    QgsField('Employees', QVariant.Int),
                    QgsField('Revenue', QVariant.Int),
                    QgsField('Sum', QVariant.Int),
                    QgsField('Fun', QVariant.Int)])

my_data = [{'x': 7459186, 'y':4973535, 'name': 'ABC', 'emp': 19572, 'rev': 141},
            {'x': 7453475, 'y':4971713, 'name': 'DEF', 'emp': 5151, 'rev': 131},
            {'x': 7466452, 'y':4976748, 'name': 'GHI', 'emp': 4276, 'rev': 107}]

for rec in my_data:
    f = QgsFeature()
    pt = QgsPointXY(rec['x'], rec['y'])
    f.setGeometry(QgsGeometry.fromPointXY(pt))
    f.setAttributes([rec['name'], rec['emp'], rec['rev']])
    pr.addFeature(f)

v1.updateExtents()
QgsProject.instance().addMapLayer(v1)

# napravljen je privremeni lejer sa tri tacke sa atributima koji su se naknadno
# upisali mozda upotrebom komande  #v1.updateFeature(f)

# sl. skripta za upisivanje novih atributnih polja ne radi i daje gresku pri stampi 

# The first expression computes the revenue per employee.
# The second one computes the sum of all revenue values in the layer.
# The final third expression doesn’t really make sense but illustrates
# the fact that we can use a wide range of expression functions, such
# as area and buffer in our expressions:

expression1 = QgsExpression('"Revenue"/"Employees"')
expression2 = QgsExpression('sum("Revenue")')
expression3 = QgsExpression('area(buffer($geometry,"Employees"))')

# QgsExpressionContextUtils.globalProjectLayerScopes() is a convenience
# function that adds the global, project, and layer scopes all at once.
# Alternatively, those scopes can also be added manually. In any case,
# it is important to always go from “most generic” to “most specific”
# scope, i.e. from global to project to layer

context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(v1))

with edit(v1):
    for f in v1.getFeatures():
        context.setFeature(f)
        f['Rev. per employee'] = expression1.evaluate(context)
        f['Sum'] = expression2.evaluate(context)
        v1.updateFeature(f)

print(f['Rev. per employee'])
print(f['Sum'])



