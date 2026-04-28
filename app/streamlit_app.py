from utils import *

# Liste des pages
PAGES = {
    "🎪 Arcadie": "pages/1_🎪_Arcadie.py",
    "🎧 Line-up": "pages/2_🎧_Line-up.py",
    "🚗 Comment venir": "pages/3_🚗_Comment_venir.py",
    "🎉 Programmation": "pages/4_🎉_Programmation.py",
    #"Qui est-ce": "pages/5_Qui_est_ce.py"
}

# NAVBAR FIXE
cols = st.columns(len(PAGES))

for i, (name, path) in enumerate(PAGES.items()):
    with cols[i]:
        if st.button(name, use_container_width=True):
            st.switch_page(path)

st.markdown("---")

# Navigation native Streamlit
pg = st.navigation([
    st.Page(p) for p in PAGES.values()
])

pg.run()
