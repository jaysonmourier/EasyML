from textx import metamodel_from_file

easyml_meta = metamodel_from_file('easyml.tx')
easy_model = easyml_meta.model_from_file('main.easyml')

a =  easy_model.fichier.name


print(a)