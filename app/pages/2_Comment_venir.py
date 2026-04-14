from utils import *

# Image
gite = Image.open('data/gite_arcadie.jpeg')
st.image(gite, use_container_width=False)


# Maps

st.markdown("""
    ## Gîte de l'Orée du Bois
    11 bis Rue du Château, 28240 Manou
""")

gite_adresse = pd.DataFrame({
    'latitude': [48.52193898339119],
    'longitude': [0.9811073892840328]
})

st.map(gite_adresse, zoom=12)

# Lien Google Sheet

st.markdown("""
    ### [Google Sheet Train & Covoiturage](https://docs.google.com/spreadsheets/d/11nlYVrzULCtokI5QsRXU5TBGfkA1y9ruVCqx_SBTplg/edit?usp=sharing)

""")

# Train

st.markdown("""
    # Train
""")

col1, col2 = st.columns(2)

col1.markdown("""
## Aller

Paris Montparnasse → La Loupe : TER (toutes les 30min jusqu'à 19h, ~24€) \n
La Loupe → Gîte : navette (8min)
""")

col2.markdown("""
## Retour

Gite →  la gare de Verneuil-sur-Avre : navette (28min)  \n
Verneuil-sur-Avre → Paris : TER (11h, 16h ou 18h, ~15€) \n
⚠️ gare différente de l'aller ⚠️

""")

# Covoiturage

st.markdown("""
    # Covoiturage

    1h40 depuis Porte d'Auteuil jusqu'au Gîte de l'Orée du Bois. \n
""")
