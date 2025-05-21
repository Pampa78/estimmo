import streamlit as st
import pandas as pd
import joblib

# Chargement du modèle
model = joblib.load("model_xgb.pkl")

st.title("🏠 Estimation de la Valeur Foncière d’un Bien Immobilier")

st.markdown("**Remplissez les informations ci-dessous pour estimer la valeur foncière d’un bien en Île-de-France.**")

# Interface utilisateur
nature_mutation = st.selectbox("Nature de la mutation", ["Vente"])
code_postal = st.number_input("Code postal", min_value=1000, max_value=99999, value=95150)
commune = st.text_input("Commune", value="TAVERNY")
code_departement = st.selectbox("Code département", [75, 77, 78, 91, 92, 93, 94, 95], index=7)
type_local = st.selectbox("Type de bien", ["Maison", "Appartement"])
surface_bati = st.number_input("Surface réelle bâtie (m²)", min_value=10, max_value=1000, value=95)
nombre_pieces = st.number_input("Nombre de pièces principales", min_value=1, max_value=20, value=4)
surface_terrain = st.number_input("Surface du terrain (m²)", min_value=0, max_value=5000, value=137)
jour = st.slider("Jour", 1, 31, 1)
mois = st.slider("Mois", 1, 12, 12)
annee = st.number_input("Année", min_value=2000, max_value=2100, value=2023)
moyenne_taux = st.number_input("Taux moyen du crédit immobilier (%)", min_value=0.0, max_value=10.0, value=4.265)

# Construction du DataFrame
ligne = pd.DataFrame([{
    "Nature_mutation": nature_mutation,
    "Code_postal": code_postal,
    "Commune": commune,
    "Code_departement": code_departement,
    "Type_local": type_local,
    "Surface_reelle_bati": surface_bati,
    "Nombre_pieces_principales": nombre_pieces,
    "Surface_terrain": surface_terrain,
    "Jour": jour,
    "Mois": mois,
    "Année": annee,
    "Moyenne_Taux": moyenne_taux
}])

# Conversion des colonnes catégorielles
categorical_cols = ["Nature_mutation", "Commune", "Type_local"]
for col in categorical_cols:
    ligne[col] = ligne[col].astype("category")

# Prédiction
if st.button("🔮 Estimer la valeur foncière"):
    prediction = model.predict(ligne)
    st.success(f"💰 Valeur foncière estimée : {int(prediction[0]):,} €".replace(",", " "))
