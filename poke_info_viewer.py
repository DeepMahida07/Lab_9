""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info

# Create the main window
root = Tk()
root.title("Pokemon Information")

# TODO: Create the frames
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2)

frm_btm_left = ttk.Frame(root)
frm_btm_left.grid(row=1, column=1)
frm_btm_right = ttk.Frame(root)
frm_btm_right.grid(row=1, column=1)

#frm_input = ttk.Frame(root, text=('Info'))
#frm_input.grid(row=1, column=0, padx=(20,10), pady=(10,20))

#frm_input = ttk.Frame(root, text=('Stat'))
#frm_input.grid(row=1, column=1, padx=(20,10), pady=(10,20))

# TODO: Populate the user input frame with widgets
lbl_name = ttk.Label(frm_top, text='Pokemon name:')
lbl_name.grid(row=0, column=0, padx=15, pady=20)
ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=(20,5), pady=(20,20))

frm_input = ttk.Label(root, text=('Info'))
frm_input.grid(row=1, column=0, padx=(20,10), pady=(10,20))

#Getting info table 
enter_name = ttk.Entry(frm_top)
#enter_name.insert(0, 'meow')
#enter_name.grid(row=0, column=1)

def handle_button_get_info():
    poke_name = enter_name.get().strip()
    if poke_name == '': return
    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        label_height_value = [text] = str(poke_info['Height']) + ' dm'
        label_weight_value = [text] = str(poke_info['Weight']) + ' hg'
        
label_height = ttk.Label(frm_input, text='Height:')
label_height.grid(row=3, column=0, padx=(10,5), pady=(10,5), sticky=E)
label_height_value = ttk.Label(frm_input, width=20)
label_height_value.grid(row=1, column=1, padx=(0,10), pady=(10,5), sticky=W)

#label_weight = ttk.Label(frm_input, text='Weight:')
#label_weight.grid(row=5, column=0, padx=(10,5), pady=(10,5), sticky=E)
#label_weight_value = ttk.Label(frm_input, width=20)
#label_weight_value.grid(row=3, column=1, padx=(0,10), pady=(10,5), sticky=W)





frm_input = ttk.Label(root, text=('Stat'))
frm_input.grid(row=1, column=1, padx=(20,10), pady=(10,20))

# TODO: Define button click event handler function
get_button = ttk.Button(frm_top, text='Get Info')
get_button.grid(row=0, column=2, padx=10, pady=5)
root.mainloop()
