from utils import *

# ----------------------------------------------------------------------------
# --- Google Sheet ---
# ----------------------------------------------------------------------------

st.markdown("""

    ### Veuillez remplir le Google Sheet que vous veniez en train ou en covoiturage

""")

col1, col2, col3 = st.columns(3)
col2.markdown("""
    ### [📁 Sheet](GOOGLE_SHEET_COVOIT)

""")

# ----------------------------------------------------------------------------
# --- Train ---
# ----------------------------------------------------------------------------

st.divider()
col1, col2, col3 = st.columns(3)
col2.markdown("""
    # Train
""")

col1, col2 = st.columns(2)

col1.markdown("""
## Aller

🚉 Paris Montparnasse → La Loupe : TER (toutes les 30min jusqu'à 19h, ~24€) \n
🚐 La Loupe → Gîte : navette (8min)
""")

col2.markdown("""
## Retour

🚐 Gite →  la gare de Verneuil-sur-Avre : navette (28min)  \n
🚉 Verneuil-sur-Avre → Paris : TER (11h, 16h ou 18h, ~15€) \n
⚠️ Gare différente de l'aller ⚠️

""")

# ----------------------------------------------------------------------------
# --- Adresse & Maps ---
# ----------------------------------------------------------------------------
st.divider()
col1, col2, col3 = st.columns(3)
col2.markdown("""
    # Covoit
""")
st.markdown("""
    ## Gîte de l'Orée du Bois
    11 bis Rue du Château, 28240 Manou
""")

gite_adresse = pd.DataFrame({
    'latitude': [48.52193898339119],
    'longitude': [0.9811073892840328]
})

st.map(gite_adresse, zoom=12)

# ----------------------------------------------------------------------------
# --- Image ---
# ----------------------------------------------------------------------------
st.divider()
gite = Image.open('data/gite_arcadie.jpeg')
st.image(gite, use_container_width=False)
