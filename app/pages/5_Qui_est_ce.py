from utils import *

# Titre principal
st.set_page_config(
    page_title="Qui est-ce ?",
    page_icon="❓",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.title("❓Qui est-ce ?")

# ---------------------------------------------------------------------------
# 1. DICTIONNAIRE DES PERSONNESs
# ---------------------------------------------------------------------------
personnes = {
    "Anto" : "photos/anto.jpeg",
    "Felix" : "photos/felix.jpeg",
    "FX" : "photos/fx.jpeg",
    "Joaq" : "photos/joaq.jpeg",
    "Maud" : "photos/maud.jpeg",
    "Sarah" : "photos/sarah.jpeg"
}


# ---------------------------------------------------------------------------
# 2. INITIALISER L'ÉTAT DU JEU
# ---------------------------------------------------------------------------
if "personne_actuelle" not in st.session_state:
    st.session_state.personne_actuelle = random.choice(list(personnes.keys()))
    st.session_state.photos_melangees = []

personne_actuelle = st.session_state.personne_actuelle
photo_correcte = personnes[personne_actuelle]

# ---------------------------------------------------------------------------
# 3. GÉNÉRER LES 4 PHOTOS (1 correcte + 3 fausses)
# ---------------------------------------------------------------------------
if not st.session_state.photos_melangees:
    # Récupérer toutes les autres photos (fausses)
    autres_prenoms = [p for p in personnes.keys() if p != personne_actuelle]
    photos_fausses = [personnes[p] for p in autres_prenoms]

    # Choisir 3 fausses photos aléatoirement
    trois_fausses = random.sample(photos_fausses, 3)

    # Mélanger : 1 correcte + 3 fausses
    toutes_les_photos = [photo_correcte] + trois_fausses
    random.shuffle(toutes_les_photos)

    st.session_state.photos_melangees = toutes_les_photos

# ---------------------------------------------------------------------------
# 4. AFFICHER LA QUESTION
# ---------------------------------------------------------------------------
st.subheader(f"❓ Qui est **{personne_actuelle}** ?")

# ============================================
# 5. AFFICHER LES 4 PHOTOS
# ============================================
cols = st.columns(4)
for i, photo in enumerate(st.session_state.photos_melangees):
    with cols[i]:
        st.image(photo, width=200)
        if st.button(f"Réponse #{i+1}", key=f"btn_{i}", use_container_width=True):
            if photo == photo_correcte:
                st.success("✅ Correct !")
                st.balloons()
                st.session_state.reponse_donnee = True
            else:
                st.error("❌ Mauvaise réponse... Réessayez !")
                st.session_state.reponse_donnee = True

# Afficher le bouton "Jouer de nouveau" après une réponse
if st.session_state.get("reponse_donnee", False):
    st.divider()
    if st.button("🔄 Jouer de nouveau 🔄", use_container_width=True):
        st.session_state.personne_actuelle = random.choice(list(personnes.keys()))
        st.session_state.photos_melangees = []
        st.session_state.reponse_donnee = False
        st.rerun()
