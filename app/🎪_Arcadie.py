from utils import *

# Titre principal
st.set_page_config(layout="wide")
st.title("🧚 Arcadie #3 🧚")

col1, col2 = st.columns([2, 1])

# ---------------------------------------------------------------------------
# --- Description ---
# ---------------------------------------------------------------------------

col1.subheader("Amis farfadets, lutins et autres créatures des sous-bois,")
col1.text("""

L’heure est trouble, la lumière décline entre les feuillages… en cette nuit enchantée, nous vous ouvrons les portes du Cabaret des Farfadets 🧚

Après la Guinguette des Crevettes et le Bal des Étoiles, nous lançons une troisième incantation. Dans 47 jours, elle nous emportera loin du monde ordinaire, vers un refuge caché, là où la mousse est douce, les basses résonnent entre les arbres et les racines s’entrelacent 🌳

Cette conversation sera notre grimoire commun. Vous y trouverez toutes les informations pratiques et autres sortilèges utiles à notre quête : se retrouver et faire vibrer la forêt.

On a super hâte ✨
""")

# ---------------------------------------------------------------------------
# Affiche
# ---------------------------------------------------------------------------
affiche = Image.open('data/affiche_arcadie.jpeg')
col2.image(affiche, use_container_width=False)
