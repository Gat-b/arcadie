from utils import *

# ---------------------------------------------------------------------------
# --- Menu ---
# ---------------------------------------------------------------------------

st.markdown("<h1 style='text-align: center;'>🍽️ Menus du week-end 🍽️</h1>", unsafe_allow_html=True)

st.markdown("""
    <h2 style='text-align: left;'>Vendredi soir </h2>
    <h3 style='text-align: left;'>🌴 La forêt enchantée devient tropicale 🌴</h3>
    <div style='text-align: left;'>

    **Banh mi végétariens** croustillants garnis de légumes pickles et tofu caramélisé

    **Bouillon clair** parfumé gingembre et menthe
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <h2 style='text-align: right;'>Samedi midi </h2>
    <h3 style='text-align: right;'>🌲 Détour dans les forêts de cèdres du Levant 🌲</h3>
    <div style='text-align: right;'>

    **Taboulé printanier** gorgé de persil et de menthe

    **Brochettes de légumes grillés** au feu
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <h2 style='text-align: left;'>Samedi soir </h2>
    <h3 style='text-align: left;'>🐊 Passage dans les mangroves du Kerala 🐊</h3>
    <div style='text-align: left;'>

    **Grand dahl** aux lentilles corail et épinards

    Servi avec du **riz**
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <h2 style='text-align: right;'>Dimanche midi</h2>
    <h3 style='text-align: right;'>🍃 Ramassage de feuilles 🍃</h3>
    <div style='text-align: right;'>

    **Pancakes**, restes et litres de café
    </div>
    """, unsafe_allow_html=True)



# current_file = Path(__file__)
# image_path = current_file.parent.parent / 'data' / 'menus.jpeg'


# affiche = Image.open(image_path)
# st.image(affiche, use_container_width=True)

# ---------------------------------------------------------------------------
# --- Programme du samedi ---
# ---------------------------------------------------------------------------
st.divider()
st.markdown("<h1 style='text-align: center;'>☀️ Programme du samedi ☀️</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

activites = [
    "🎯 Pétanque",
    "🎳 Molki",
    "🏐 Spike ball",
    "🏊 Piscine",
    "🎵 Music live",
    "🪕 Bal folk",
    "🎹 Atelier MAO",
    "🗺️ Chasse au trésor",
    "✨ Stand paillette",
    "👨‍🍳 Cuisine collaborative",
    "🎲 Jeux de sociétés",
    "🎉 Et tout ce que vous allez ramener !"
]

# Split activités en deux listes
mid = len(activites) // 2
col1_activites = activites[:mid]
col2_activites = activites[mid:]


for activite in col1_activites:
    col1.markdown(f"<p style='font-size: 20px;'>{activite}</p>", unsafe_allow_html=True)


for activite in col2_activites:
    col2.markdown(f"<p style='font-size: 20px;'>{activite}</p>", unsafe_allow_html=True)

### Image : etoiles

current_file = Path(__file__)
etoiles_path = current_file.parent.parent / 'data' / 'etoiles.jpeg'

etoiles = Image.open(etoiles_path)
st.image(etoiles, use_container_width=True)
