from textx import metamodel_from_str
from grammar2 import grammar
import easyml

m = metamodel_from_str(grammar)
model = m.model_from_file('example2.dsl')

def object_exists(obj, path):
    try:
        parts = path.split('.')
        for part in parts:
            obj = getattr(obj, part)
        return True
    except AttributeError:
        return False

if object_exists(model, 'model.option.test_size'):
    print(model.model.option.test_size)
else:
    print("L'objet n'existe pas.")