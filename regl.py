import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def train(file, features, target, std, model):
    # Charger les données à partir du fichier CSV
    data = pd.read_csv(file)
    
    # Sélectionner les colonnes utiles et la colonne cible
    X = data[features]
    y = data[target]

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardiser les données si nécessaire
    if std:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    # Entraîner le modèle
    model.fit(X_train, y_train)

    # Retourner le modèle pré-entraîné
    return model

if __name__ == "__main__":
    pass