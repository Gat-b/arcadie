from utils import *

# Titre principal
st.set_page_config(
    page_title="Arcadie",
    page_icon="🧚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===========================
# BARRE DE NAVIGATION HORIZONTALE
# ===========================

# Définir les pages disponibles
PAGES = {
    "🎪 Arcadie": "pages/1_🎪_Arcadie.py",
    "🚗 Comment venir": "pages/2_🚗_Comment_venir.py",
    "🎉 Programmation": "pages/3_🎉_Programmation.py",
    "🎧 Line-up": "pages/4_🎧_Line-up.py"
}

# CSS pour la barre de navigation horizontale scrollable
st.markdown("""
    <style>
    /* Barre de navigation sticky en haut */
    .navbar {
        background: linear-gradient(135deg, #1f77b4 0%, #2c8ccd 100%);
        padding: 0.8rem 1rem;
        margin: -2rem -2rem 2rem -2rem;
        position: sticky;
        top: 0;
        z-index: 999;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        overflow-x: auto;
        overflow-y: hidden;
        white-space: nowrap;
        scrollbar-width: thin;
        scrollbar-color: rgba(255,255,255,0.4) transparent;
    }

    .navbar::-webkit-scrollbar {
        height: 4px;
    }

    .navbar::-webkit-scrollbar-track {
        background: transparent;
    }

    .navbar::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.4);
        border-radius: 2px;
    }

    .navbar::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.6);
    }

    /* Conteneur des boutons */
    .nav-buttons {
        display: flex;
        gap: 0.6rem;
        padding: 0.2rem 0;
    }

    /* Style des boutons de navigation */
    .stButton > button {
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 0.5rem 1.2rem !important;
        border-radius: 6px !important;
        white-space: nowrap !important;
        transition: all 0.3s ease !important;
        font-size: 15px !important;
    }

    .stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.25) !important;
        border-color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
    }

    /* Bouton actif */
    .stButton > button:focus, .stButton > button:active {
        background-color: rgba(255, 255, 255, 0.95) !important;
        color: #1f77b4 !important;
        border-color: white !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
    }

    /* Mode mobile */
    @media (max-width: 768px) {
        .navbar {
            margin: -2rem -1.5rem 2rem -1.5rem;
            padding: 0.6rem 0.8rem;
        }

        .stButton > button {
            padding: 0.6rem 1rem !important;
            font-size: 13px !important;
        }
    }

    /* Masquer la sidebar */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Initialiser la session pour tracker la page actuelle
if "current_page" not in st.session_state:
    st.session_state.current_page = "🎪 Arcadie"

st.title("🧚 Arcadie #3 🧚")

# Créer la barre de navigation
navbar_container = st.container()
with navbar_container:
    cols = st.columns(len(PAGES))

    for idx, (page_name, page_path) in enumerate(PAGES.items()):
        with cols[idx]:
            if st.button(
                page_name,
                key=f"nav_{page_name}",
                use_container_width=True,
                help=f"Accéder à {page_name}"
            ):
                st.session_state.current_page = page_name
                st.rerun()

st.markdown("---")

# ===========================
# CHARGER LA PAGE SÉLECTIONNÉE
# ===========================

def load_page(page_path):
    """Charge et exécute le fichier Python de la page"""
    spec = importlib.util.spec_from_file_location("page_module", page_path)
    page_module = importlib.util.module_from_spec(spec)
    sys.modules["page_module"] = page_module
    spec.loader.exec_module(page_module)

# Vérifier que le fichier existe et le charger
page_file = PAGES.get(st.session_state.current_page)

if page_file:
    page_path = Path(page_file)
    if page_path.exists():
        load_page(page_path)
    else:
        st.error(f"❌ Erreur : Le fichier {page_file} n'existe pas")
        st.info("Assurez-vous que le fichier existe à ce chemin")
else:
    st.error(f"❌ Erreur : La page '{st.session_state.current_page}' n'est pas définie dans PAGES")
