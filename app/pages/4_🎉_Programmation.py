from utils import *

# ---------------------------------------------------------------------------
# --- Titre principal ---
# ---------------------------------------------------------------------------

st.set_page_config(layout="wide")
st.title("🎉 Programmation du week-end 🎉")


# ---------------------------------------------------------------------------
# --- Menu ---
# ---------------------------------------------------------------------------

# st.header("🧑‍🍳 Menus & Recettes")

# menu = pd.DataFrame({
#     "": ["Matin", "Midi", "Soir"],
#     "Vendredi": ["", "", "Banh mi et soupe miso"],
#     "Samedi": ["Confiture et pâte à tartiner", "BBQ et taboulé", "Dahl de lentille épinard & riz"],
#     "Dimanche": ["Pancakes", "Restes", ""]
# })

# st.dataframe(menu)

# st.subheader("Vendredi Soir : Banh mi & Soupe miso", divider=True)

# st.subheader("Samedi matin : Tartine de confiture et pâte à tartiner", divider=True)

# st.subheader("Samedi midi : BBQ de légumes et taboulé", divider=True)

# st.subheader("Samedi soir : Dahl de lentille épinard & riz", divider=True)

# st.subheader("Dimanche matin : Pancakes", divider=True)

# st.subheader("Dimanches midi : Restes + pâtes", divider=True)



# ---------------------------------------------------------------------------
# --- TBA ---
# ---------------------------------------------------------------------------
st.divider()

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown("### 🎁 Les surprises arrivent soon 🎁", text_alignment="center")
