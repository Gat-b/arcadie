from utils import *

# Titre principal
st.set_page_config(layout="wide")
st.markdown("""<h1 style='text-align: center;'>🚗 Comment venir ? 🚗</h1>""",
            unsafe_allow_html=True)

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

st.divider()
st.divider()

# ---------------------------------------------------------------------------
# --- Dans ma valise ---
# ---------------------------------------------------------------------------
st.markdown("""<h1 style='text-align: center;'>🧳 Dans ma valise, il y a... 🧳</h1>""",
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

valise = [
    "🎒 Un sac de couchage",
    "🔇 Des boules quies",
    "🪥 Une brosse à dent",
    "🧴 Un gel douche et un dentifrice",
    "🛁 Une serviette",
    "🌧️ Un k-way",
    "🧶 Un gros pull",
    "🏊 Un maillot de bain",
    "✨ Mon apparât de farfadet",
    "🎸 Mon tosma",
    "🍬 Mes chewing-gum",
    "🍻 Ma tease (hors bière et vin)",
    "😄 Ma bonne humeur"
]

# Split valise en deux listes
mid = len(valise) // 2
col1_valise = valise[:mid]
col2_valise = valise[mid:]

for item in col1_valise:
    col1.markdown(f"<p style='font-size: 20px;'>{item}</p>", unsafe_allow_html=True)


for item in col2_valise:
    col2.markdown(f"<p style='font-size: 20px;'>{item}</p>", unsafe_allow_html=True)


# Image après
current_file = Path(__file__)
aprem_path = current_file.parent.parent / 'data' / 'aprem.jpeg'

aprem = Image.open(aprem_path)
st.image(aprem)
