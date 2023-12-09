from tkinter import *
from tkinter import ttk
from datetime import date
from domain import save_album, CURRENT_YEAR
from my_albuns import open_my_albuns_screen

# Variables
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500


# Styles
INPUT_WIDTH = 300
INPUT_PY = 4
SUBTITLE = "#909090"
TITLE = "#333333"
ERROR = "#f14"
SUCCESS = "#0f9f0f"
WARNING = "#FF0"


# Window Config
root = Tk()
root.title("Deezer")
root.iconbitmap('assets/icon.ico')
root.resizable(False, False)
root.attributes('-topmost', 0)
# Center window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (WINDOW_WIDTH/2))
y_cordinate = int((screen_height/2) - (WINDOW_HEIGHT/2))
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_cordinate}+{y_cordinate}")
# Theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")
isReleased = BooleanVar()


# Create and positioning elements
# Title Section
title_section = ttk.Frame(root)
title_section.pack(side='top', anchor='w', padx=24, pady=16)

# Title and Subtitle
title_body = ttk.Label(title_section, text="Cadastro", font=('Roboto', 24, 'bold'),  foreground=TITLE)
title_body.pack(anchor="w")
subtitle_body = ttk.Label(title_section, text="Cadastre albuns na plataforma", font=('Roboto', 16, "normal"),  foreground=SUBTITLE)
subtitle_body.pack(anchor="w")

# Inputs Section
inputs_section = ttk.Frame(root)
inputs_section.pack(side='top', anchor='w', padx=24, pady=8)

author_label = ttk.Label(inputs_section, text="Autor", font=('Roboto', 12, "normal"),  foreground=TITLE)
author_label.pack(anchor="w", pady=2)

author_input = ttk.Entry(inputs_section, name="author", width=INPUT_WIDTH)
author_input.pack(anchor="w", pady=INPUT_PY)

album_label = ttk.Label(inputs_section, text="Nome do Album", font=('Roboto', 12, "normal"),  foreground=TITLE)
album_label.pack(anchor="w", pady=2)

album_input = ttk.Entry(inputs_section, name="album", width=INPUT_WIDTH)
album_input.pack(anchor="w", pady=INPUT_PY)

year_label = ttk.Label(inputs_section, text="Ano de lançamento", font=('Roboto', 12, "normal"),  foreground=TITLE)
year_label.pack(anchor="w", pady=2)

year_input = ttk.Spinbox(inputs_section, name="year", from_=1900, to=date.today().year, width=INPUT_WIDTH)
year_input.pack(anchor="w", pady=INPUT_PY)

release_label = ttk.Label(inputs_section, text="É lançamento?", font=('Roboto', 12, "normal"),  foreground=TITLE )
release_label.pack(anchor="w", pady=2, side='left')

release_checkbox = ttk.Checkbutton(inputs_section, variable=isReleased, style='Switch.TCheckbutton')
release_checkbox.pack(anchor="w", pady=INPUT_PY)


message_label = ttk.Label(root, font=('Roboto', 12, "normal"), foreground=ERROR)
message_label.pack(anchor='w', padx=24, pady=8)

# Buttons
create_button = ttk.Button(root, text='Criar Album', width=INPUT_WIDTH, style='Accent.TButton')
create_button.pack(anchor="w", padx=24, pady=8)
list_button = ttk.Button(root, text='Meus albuns', width=INPUT_WIDTH)
list_button.pack(anchor="w", padx=24, pady=8, side='top')


# Events Functions
def clean_label():
    message_label.configure(text='', foreground=ERROR)


def clean_inputs():
    author_input.delete(0, END)
    album_input.delete(0, END)
    year_input.delete(0, END)
    isReleased.set(False)
    clean_label()


def validateInputs():
    if not author_input.get() or not album_input.get() or not year_input.get() or int(year_input.get()) > CURRENT_YEAR:
        message_label.configure(text="Algum campo está incorreto ou vazio!")
        return False
    clean_label()
    return True


def bind_on_submit(_event):
    is_realized_value = 'Sim' if isReleased.get() else 'Nao'
    if validateInputs():
        save_album(author_input.get(),
                   album_input.get(),
                   year_input.get(),
                   is_realized_value)
        message_label.configure(text="Album cadastrado!!", foreground=SUCCESS)
        create_button.after(1500, clean_inputs)
    else:
        create_button.after(2000, clean_label)


# Listen Events
create_button.bind('<Button-1>', bind_on_submit)
list_button.bind('<Button-1>', open_my_albuns_screen)

if __name__ == "__main__":
    root.mainloop()
