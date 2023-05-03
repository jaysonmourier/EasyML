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
    can.drawString(40, ligne, "Le modèle que vous avez sélectionner est le modèle  "+model)

    can.setFont("Helvetica", 12) # arrêter la mise en gras
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

    # Enregistrer le fichier PDF de sortie sur le disque
    with open("Compte rendu.pdf", "wb") as f:
        output.write(f)


