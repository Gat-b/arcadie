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
