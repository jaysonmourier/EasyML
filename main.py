from textx import metamodel_from_file
from textx.scoping.providers import RelativeName, FQN
from textx.export import model_export
import regl
from sklearn.svm import SVC

meta_model = metamodel_from_file('easyml.tx')


model = meta_model.model_from_file('main.easyml')


file= model.Fichiers.name+".csv"
target = model.Cibles.name
std = model.Standardizers.state
modeluse = model.Modeles.name
features = []

for i in model.Features.names:
    features.append(i.name) ## nom des colonnes


print("le fichier sélectionné est : "+file)
print("\n les colonnes utilisées sont : ")
print(features)

if(std):
    print("\n l'expresion linéaire sera standardisé ")
else:
    print("\n l'expresion linéaire ne sera pas standardisé ")

print("la cible est : "+target)



# mo = regl.train(file,features,target,std,SVC(gamma='auto'))
# print(mo.predict([[10, 123]]))
