
from pyscript import document

# Non-metal elements dictionary
elements = {
    "H": ["H", "Hydrogen", 1, 1.008],
    "C": ["C", "Carbon", 6, 12.011],
    "N": ["N", "Nitrogen", 7, 14.007],
    "O": ["O", "Oxygen", 8, 15.999],
    "P": ["P", "Phosphorus", 15, 30.974],
    "S": ["S", "Sulfur", 16, 32.06],
    "Se": ["Se", "Selenium", 34, 78.971],
    "F": ["F", "Fluorine", 9, 18.998],
    "Cl": ["Cl", "Chlorine", 17, 35.45],
    "Br": ["Br", "Bromine", 35, 79.904],
    "I": ["I", "Iodine", 53, 126.904],
    "He": ["He", "Helium", 2, 4.003],
    "Ne": ["Ne", "Neon", 10, 20.180],
    "Ar": ["Ar", "Argon", 18, 39.948],
    "Kr": ["Kr", "Krypton", 36, 83.798],
    "Xe": ["Xe", "Xenon", 54, 131.293],
    "Rn": ["Rn", "Radon", 86, 222]
}

# Check element details
def check_details(event):

    user_input = document.getElementById("symbol").value.strip().capitalize()

    element_checker = user_input in elements

    element_data = elements.get(user_input, ["", "", "", ""])

    display_message = {
        False: f"<b>{user_input}</b> is not a Non-Metal Element.",
        True: f"<b>Element Symbol:</b> {element_data[0]}<br><b>Element Name:</b> {element_data[1]}<br><b>Atomic Number:</b> {element_data[2]}<br><b>Atomic Weight:</b> {element_data[3]}"
    }

    document.getElementById("result").innerHTML = display_message[element_checker]

document.getElementById("btnchk").onclick = check_details