from utils import *

# Affiche
affiche = Image.open('data/affiche_arcadie.jpeg')
st.image(affiche, use_container_width=False)

st.set_page_config(
    page_title="Arcadie #3",
    page_icon="🎪",
)

st.markdown("""# Amis farfadets, lutins et autres créatures des sous-bois,

L’heure est trouble, la lumière décline entre les feuillages… en cette nuit enchantée, nous vous ouvrons les portes du Cabaret des Farfadets 🧚

Après la Guinguette des Crevettes et le Bal des Étoiles, nous lançons une troisième incantation. Dans 47 jours, elle nous emportera loin du monde ordinaire, vers un refuge caché, là où la mousse est douce, les basses résonnent entre les arbres et les racines s’entrelacent 🌳

Cette conversation sera notre grimoire commun. Vous y trouverez toutes les informations pratiques et autres sortilèges utiles à notre quête : se retrouver et faire vibrer la forêt.

On a super hâte ✨""")
