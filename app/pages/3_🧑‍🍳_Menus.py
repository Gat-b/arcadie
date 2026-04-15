from utils import *

menu = pd.DataFrame({
    "": ["Matin", "Midi", "Soir"],
    "Vendredi": ["", "", "Banh mi et soupe miso"],
    "Samedi": ["Confiture et pâte à tartiner", "BBQ et taboulé", "Dahl de lentille épinard & riz"],
    "Dimanche": ["Pancakes", "Restes", ""]
})


st.dataframe(menu, hide_index=True)
