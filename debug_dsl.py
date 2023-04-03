from textx import metamodel_from_str
import easyml

m = metamodel_from_str(easyml.grammar)
model = m.model_from_file('example.dsl')
