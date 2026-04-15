from utils import *

# ---------------------------------------------------------------------------
# --- Titre principal ---
# ---------------------------------------------------------------------------

st.set_page_config(layout="wide")
st.title("🎉 Programmation du week-end 🎉")


# ---------------------------------------------------------------------------
# --- Menu ---
# ---------------------------------------------------------------------------

st.subheader("🧑‍🍳 Menus")

menu = pd.DataFrame({
    "": ["Matin", "Midi", "Soir"],
    "Vendredi": ["", "", "Banh mi et soupe miso"],
    "Samedi": ["Confiture et pâte à tartiner", "BBQ et taboulé", "Dahl de lentille épinard & riz"],
    "Dimanche": ["Pancakes", "Restes", ""]
})

st.dataframe(
    menu,
    hide_index=True,
    use_container_width=True,
    column_config={
        "": st.column_config.TextColumn(width="small"),
        "Vendredi": st.column_config.TextColumn(width="medium"),
        "Samedi": st.column_config.TextColumn(width="medium"),
        "Dimanche": st.column_config.TextColumn(width="medium"),
    }
)

# ---------------------------------------------------------------------------
# --- TBA ---
# ---------------------------------------------------------------------------
st.divider()

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.info("""
    ### 🎁 D'autres surprises arrivent 🎁
    """)
