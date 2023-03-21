import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_data_from_csv(fichier, separateur=',', en_tete=0, index_col=None, noms_colonnes=None, encodage='utf-8', skip_blank_lines=True, na_values=None, dtype=None):
    """
    Charger un fichier CSV en un DataFrame avec différentes options pour minimiser les erreurs.

    Paramètres:
    fichier (str): Chemin du fichier CSV à charger.
    separateur (str, optional): Séparateur utilisé pour séparer les champs du fichier CSV. Par défaut ','.
    en_tete (int, list, optional): Ligne(s) à utiliser comme en-tête. Par défaut 0 (première ligne).
    index_col (int, str, optional): Colonne à utiliser comme index du DataFrame. Par défaut None.
    noms_colonnes (list, optional): Liste des noms de colonnes. Par défaut None.
    encodage (str, optional): Encodage du fichier CSV. Par défaut 'utf-8'.
    skip_blank_lines (bool, optional): Ignorer les lignes vides. Par défaut True.
    na_values (scalar, str, list, or dict, optional): Valeurs supplémentaires à considérer comme NaN. Par défaut None.
    dtype (dict, optional): Dictionnaire de types de données pour chaque colonne. Par défaut None.

    Retour:
    DataFrame: DataFrame chargé à partir du fichier CSV.
    """

    dataframe = pd.read_csv(
        fichier,
        sep=separateur,
        header=en_tete,
        index_col=index_col,
        names=noms_colonnes,
        encoding=encodage,
        skip_blank_lines=skip_blank_lines,
        na_values=na_values,
        dtype=dtype
    )

    return dataframe


def train(file, features, target, std, model):
    try:
        # Charger les données à partir du fichier CSV
        data = pd.read_csv(file)
    except FileNotFoundError:
        print("Erreur : fichier non trouvé.")
        return

    if set(features + [target]).issubset(data.columns):
        # Sélectionner les colonnes utiles et la colonne cible
        X = data[features]
        y = data[target]
    else:
        print("Erreur : certaines colonnes sont manquantes.")
        return

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardiser les données si nécessaire
    if std:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    try:
        # Entraîner le modèle
        model.fit(X_train, y_train)
    except Exception as e:
        print("Erreur lors de l'entraînement du modèle :", e)
        return

    # Retourner le modèle pré-entraîné
    return model

if __name__ == "__main__":
    pass