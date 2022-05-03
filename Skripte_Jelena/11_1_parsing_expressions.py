#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/expressions.html
#expressions-filtering-and-calculating-values

"""Parsing Expressions
Evaluating Expressions
Basic Expressions
Expressions with features
Filtering a layer with expressions
Handling expression errors"""

# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/expressions.html
#parsing-expressions

# The following example shows how to check if a given expression
# can be parsed correctly
exp = QgsExpression('1 + 1 = 2')
assert(not exp.hasParserError())

exp = QgsExpression('1 + 1 = ')
assert(exp.hasParserError())

# assert(exp.parserErrorString() == '\nsyntax error, unexpected $end')
# ukoliko zelimo da proverimo da li izraz moze biti uspesno rastavljen
# odnosno da li je ispravan; ukoliko nije, bice izbacen AssertionError





























