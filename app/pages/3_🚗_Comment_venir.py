from utils import *

# Titre principal
st.set_page_config(layout="wide")
st.title("🚗 Comment venir ? 🚗")

# ---------------------------------------------------------------------------
# --- Google Sheet ---
# ---------------------------------------------------------------------------

st.markdown("""
Pour coordonner les trajets, merci de remplir le Google Sheet selon votre mode de transport :
""")

col1, col2, col3 = st.columns([1, 4, 1])
GOOGLE_SHEET_COVOIT = st.secrets["GOOGLE_SHEET_COVOIT"]
with col2:
    st.link_button("📋 Remplir le formulaire de covoiturage & train", GOOGLE_SHEET_COVOIT, use_container_width=True)

st.divider()

# ---------------------------------------------------------------------------
# --- Train ---
# ---------------------------------------------------------------------------

st.header("🚂 En train")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### Aller
    - 🚉 **Paris Montparnasse** → La Loupe : TER (toutes les 30 min jusqu'à 19h), ~24€
    - 🚐 La Loupe → Gîte : navette (10 min)
    """,
    text_alignment="center")

with col2:
    st.markdown("""
    #### Retour
    - 🚐 Gîte → Verneuil-sur-Avre : navette (30 min)
    - 🚉 **Verneuil-sur-Avre** → Paris : TER (11h, 16h ou 18h), ~15€ \n
    ⚠️ **Gare différente de l'aller !** ⚠️
    """,
    text_alignment="center")

st.info("💡 Pensez à vérifier les horaires exacts sur SNCF Connect")

st.divider()

# ---------------------------------------------------------------------------
# --- Covoiturage ---
# ---------------------------------------------------------------------------
st.header("🚗 En covoiturage")

# Adresse et carte
st.markdown("""
### 📍 Gîte de l'Orée du Bois
11 bis Rue du Château \n
28240 Manou
""",
text_alignment="center")
st.link_button("📍 Voir sur Google Maps",
                "https://maps.google.com/?q=48.52193898339119,0.9811073892840328",
                use_container_width=True)


# gite_adresse = pd.DataFrame({
#     'latitude': [48.52193898339119],
#     'longitude': [0.9811073892840328]
# })
# st.map(gite_adresse, zoom=12)

# st.divider()
