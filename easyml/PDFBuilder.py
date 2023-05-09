import io
import os
from reportlab.pdfgen import canvas
from PyPDF3 import PdfFileWriter, PdfFileReader
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def creation_plot(filename:str,var, target):
    # Charger les données du fichier CSV
    data = pd.read_csv(filename)

    # Tracer un pairplot
    g = sns.pairplot(data, vars=var, hue=target)
    g.savefig("Image.png")


def plot(filename, feature, model, target, test):

    creation_plot(filename, feature, target)
    # Créer un nouveau fichier PDF
    output = PdfFileWriter()

    # chargement image
    img = Image.open('Image.png')
    img_path = os.path.abspath('Image.png')
    test= str(test*100)
    # Écrire "Hello World!" sur une page
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    can.setFont("Helvetica-Bold", 18)
    can.setFillColorRGB(1, 0, 0)
    can.drawString(130, 450, "Compte rendu de l'entrainement du modèle")
    can.save()
    packet.seek(0)

    # Ajouter la page au fichier PDF de sortie
    new_pdf = PdfFileReader(packet)
    output.addPage(new_pdf.getPage(0))

    # Écrire sur la nouvelle page
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    can.drawString(40, 750, "Vous venez d'entrainer votre jeu de données à l'aide de l'outil EasyML.")
    can.drawString(40, 730, "Pour se faire vous avez utilisé les différentes Features :")
    ligne=710
    for f in feature:
        can.drawString(60, ligne, "- "+f)
        ligne=ligne-20

    can.setFont("Helvetica-Bold", 12)
    can.drawString(40, ligne, "Le modèle que vous avez sélectionner est le modèle  "+model+".")
    can.setFont("Helvetica", 12) # arrêter la mise en gras
    ligne= ligne-20
    if model == "SVM":
        can.drawString(40, ligne, "Il s'agit d'un algorithme d'apprentissage supervisé utilisé pour la classification et la régression.") 
        ligne= ligne-20
        can.drawString(40, ligne, "L'objectif de l'algorithme SVM est de trouver la meilleure séparation possible entre les différentes") 
        ligne= ligne-20
        can.drawString(40, ligne, "classes dans un ensemble de données. Il s'agit d'une méthode très puissante pour la classification ")
        ligne= ligne-20
        can.drawString(40, ligne, "binaire, mais elle peut également être étendue à la classification multiclasse.")
    elif model == "XGBoost":
        can.drawString(40, ligne, "Il s'agit une bibliothèque open source d'apprentissage automatique basée sur l'algorithme de gradient ") 
        ligne= ligne-20
        can.drawString(40, ligne, "boosting,qui est utilisépour la classification et la régression. L'algorithme de gradient boosting")
        ligne= ligne-20
        can.drawString(40, ligne, "consiste à entraîner plusieurs modèles simples (généralement des arbres de décision) en séquence, où ")
        ligne= ligne-20
        can.drawString(40, ligne, "chaque modèle est entraîné pour corriger les erreurs de prédiction du modèle précédent.")
    elif model == "Logistic":
        can.drawString(40, ligne, " Le modèle de régression logistique est un algorithme d'apprentissage supervisé utilisé pour la")
        ligne= ligne-20
        can.drawString(40, ligne, "classification binaire. C'est l'un des algorithmes de classification les plus couramment utilisés en ")
        ligne= ligne-20
        can.drawString(40, ligne, "apprentissage automatique.Le modèle de régression logistique estime la probabilité que l'entrée")
        ligne= ligne-20
        can.drawString(40, ligne, "appartienne à une classe particulière en utilisant une fonction logistique. La fonction logistique ")
        ligne= ligne-20
        can.drawString(40, ligne, "est une fonction sigmoïde qui prend en entrée la somme pondérée des caractéristiques d'entrée et ")
        ligne= ligne-20
        can.drawString(40, ligne, "produit une valeur de sortie entre 0 et 1, qui peut être interprétée comme une probabilité. ")
        ligne= ligne-20
        can.drawString(40, ligne, "Si la probabilité est supérieure à un seuil prédéfini, l'entrée est classée comme appartenant à la ")
        ligne= ligne-20
        can.drawString(40, ligne, "classe positive, sinon elle est classée comme appartenant à la classe négative.")
    ligne= ligne-20
    can.drawString(40, ligne, "Vous trouverez ci-dessous une représentation de votre modèle entrainer ")
    ligne= ligne-20
    can.drawImage(img_path, 100, ligne-325, width=400, height=300)
    ligne= ligne-325
    can.drawString(40, ligne-40, "Votre modèle a été entrainé avec une couverture de test de "+test+"%")
    can.setFont("Helvetica-Bold", 12)
    can.drawString(210, ligne-100, "Merci d'avoir utiliser EasyML")
    can.save()
    packet.seek(0)

    new_pdf = PdfFileReader(packet)
    output.addPage(new_pdf.getPage(0))

    os.remove('Image.png')

    # Enregistrer le fichier PDF de sortie sur le disque
    with open("output/Compte rendu.pdf", "wb") as f:
        output.write(f)


