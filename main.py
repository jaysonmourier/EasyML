from textx import metamodel_from_file
from textx.scoping.providers import RelativeName, FQN
from textx.export import model_export


meta_model = metamodel_from_file('easyml.tx')


model = meta_model.model_from_file('main.easyml')

a= model.Fichiers.name+".csv"

print(model.Cibles.name)
print(model.Standardizers.state)
print(model.Modeles.name)
print(a)