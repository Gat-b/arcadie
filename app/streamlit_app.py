from utils import *

# Liste des pages
PAGES = {
    "🎪 Arcadie": "app/pages/1_🎪_Arcadie.py",
    "🎧 Line-up": "app/pages/2_🎧_Line-up.py",
    "🚗 Comment venir": "app/pages/3_🚗_Comment_venir.py",
    "🎉 Programmation": "app/pages/4_🎉_Programmation.py",
}

# NAVBAR FIXE
cols = st.columns(len(PAGES))

for i, (name, path) in enumerate(PAGES.items()):
    with cols[i]:
        if st.button(name, use_container_width=True):
            st.switch_page(path)

st.markdown("---")

# Navigation native Streamlit (IMPORTANT)
pg = st.navigation([
    st.Page(p) for p in PAGES.values()
])

pg.run()
