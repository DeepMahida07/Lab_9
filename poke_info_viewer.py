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
frm_btm_left.grid(row=1, column=0)
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

frm_input = ttk.Label(root, text=('Stat'))
frm_input.grid(row=1, column=1, padx=(20,10), pady=(10,20))

# TODO: Define button click event handler function



root.mainloop()


enter_name = ttk.Entry(frm_top)
enter_name.insert(0, 'meow')
enter_name.grid(row=0, column=1)
def handle_button_get_info():
    poke_name = enter_name.get().strip()
    if poke_name = 