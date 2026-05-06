from utils import *

st.set_page_config(page_title="Line Up", layout="wide")

st.set_page_config(page_title="Line Up", layout="wide")

# Charger les données depuis Google Sheets
GOOGLE_SHEET_DJS = st.secrets["GOOGLE_SHEET_DJS"]

@st.cache_data
def load_dj_data():
    conn = st.connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=GOOGLE_SHEET_DJS)
    return data

# CSS pour l'effet flip card
st.markdown("""
<style>
.flip-container {
    width: 100%;
    height: 280px;
    perspective: 1000px;
    margin: 10px 0;
}

.flip-card {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.6s;
    transform-style: preserve-3d;
}

.flip-card.flipped {
    transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.flip-card-front {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    font-size: 24px;
    font-weight: bold;
}

.flip-card-back {
    background: linear-gradient(135deg, #2c3e50 0%, #3d566e 100%);
    color: white;
    transform: rotateY(180deg);
    padding: 20px;
    overflow-y: auto;
    text-align: center;
}

.flip-card-back h3 {
    margin: 0 0 15px 0;
    font-size: 20px;
}

.flip-card-back .info-row {
    margin: 8px 0;
    font-size: 14px;
}

.flip-card-back .description {
    font-size: 12px;
    margin-top: 10px;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

try:
    dj_data = load_dj_data()
except Exception as e:
    st.error(f"❌ Erreur lors du chargement des données: {e}")
    st.stop()

st.title("🎵 Line Up")
st.divider()

# Initialiser session state
if 'flipped_cards' not in st.session_state:
    st.session_state.flipped_cards = [False] * len(dj_data)

# Afficher les cartes en grille
cols = st.columns(4)

for idx, (_, row) in enumerate(dj_data.iterrows()):
    col = cols[idx % 4]

    with col:
        # Bouton pour retourner la carte
        if st.button(f"{row['nom']}", key=f"btn_{idx}", use_container_width=True):
            st.session_state.flipped_cards[idx] = not st.session_state.flipped_cards[idx]

        # Affichage de la carte
        is_flipped = st.session_state.flipped_cards[idx]

        if is_flipped:
            # Verso (description)
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #2c3e50 0%, #3d566e 100%);
                        color: white; padding: 20px; border-radius: 10px;
                        min-height: 280px; display: flex; flex-direction: column;
                        justify-content: center; text-align: center;">
                <h3 style="margin: 0 0 15px 0;">{row['nom']}</h3>
                <div style="font-size: 14px; margin: 8px 0;"><b>Horaire:</b> {row['horaire']}</div>
                <p style="font-size: 12px; margin-top: 15px; line-height: 1.5;">{row['description']}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Recto (image ou placeholder)
            if pd.notna(row['image']) and str(row['image']).strip():
                st.image(row['image'], use_column_width=True)
            else:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            color: white; padding: 60px 20px; border-radius: 10px;
                            min-height: 280px; display: flex; flex-direction: column;
                            justify-content: center; align-items: center; text-align: center;">
                    <div style="font-size: 48px; margin-bottom: 10px;">🎧</div>
                    <h2 style="margin: 0; font-size: 22px;">{row['nom']}</h2>
                    <p style="margin: 5px 0; font-size: 14px; opacity: 0.9;">Cliquez pour plus d'infos</p>
                </div>
                """, unsafe_allow_html=True)
