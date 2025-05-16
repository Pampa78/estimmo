import streamlit as st
import pandas as pd
import joblib

# Sauvegarder le modèle
joblib.dump(model_xgb, "model_xgb.pkl")

# Chargement du modèle
model = joblib.load("model_xgb.pkl")

st.title("Prédiction de la valeur foncière")

# Interface utilisateur
surface = st.number_input("Surface réelle bâtie (m²)", min_value=10, max_value=500, value=100)
pieces = st.number_input("Nombre de pièces principales", min_value=1, max_value=10, value=3)
terrain = st.number_input("Surface terrain", min_value=0, max_value=2000, value=100)
code_dep = st.selectbox("Code département", [78, 91, 92, 93, 94, 95, 27])
type_local = st.selectbox("Type de bien", ["Maison", "Appartement"])

# Création d’un DataFrame d’entrée
ligne = pd.DataFrame([{
    "Surface_reelle_bati": surface,
    "Nombre_pieces_principales": pieces,
    "Surface_terrain": terrain,
    "Code_departement": code_dep,
    "Type_local": type_local,
    # ajoute ici les autres colonnes attendues par le modèle
}])

# Conversion en category si besoin
ligne["Type_local"] = ligne["Type_local"].astype("category")

# Prédiction
if st.button("Prédire"):
    prediction = model.predict(ligne)
    st.success(f"Valeur foncière estimée : {int(prediction[0]):,} €")