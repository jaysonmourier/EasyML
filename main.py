# from textx import metamodel_from_file

# easyml_meta = metamodel_from_file('easyml.tx')
# easy_model = easyml_meta.model_from_file('main.easyml')

# a =  easy_model.fichier.name


# print(a)


from textx import metamodel_from_file
from textx.scoping.providers import RelativeName, FQN
from textx.export import model_export
# ------------------------------------
# GRAMMAR
#
meta_model = metamodel_from_file('easyml.tx')


# ------------------------------------
# EXAMPLE
#
model = meta_model.model_from_file('main.easyml')

a= model.Fichiers.name+".csv"

print(model.Cibles.name)
print(model.Standardizers.state)
print(model.Modeles.name)
print(a)