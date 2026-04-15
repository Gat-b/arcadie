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
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'data/affiche_arcadie.jpeg')

affiche = Image.open(image_path)
col2.image(affiche, use_container_width=True)

# ---------------------------------------------------------------------------
# --- Timer avec refresh ---
# ---------------------------------------------------------------------------
st.divider()

placeholder = st.empty()

while True:
    target_date = datetime(2025, 5, 29, 19, 0, 0)
    now = datetime.now()

    time_left = target_date - now
    days = time_left.days
    seconds_left = time_left.seconds
    hours = seconds_left // 3600
    minutes = (seconds_left % 3600) // 60
    seconds = seconds_left % 60

    with placeholder.container():
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("📅 Jours", f"{365 + days}")
        col2.metric("⏱️ Heures", f"{hours:02d}")
        col3.metric("⏲️ Minutes", f"{minutes:02d}")
        col4.metric("⏳ Secondes", f"{seconds:02d}")

    time.sleep(1)

st.divider()
