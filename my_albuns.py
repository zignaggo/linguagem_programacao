from tkinter import *
from tkinter import ttk
import domain

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


def render_albuns(tree_view: ttk.Treeview, albuns):
    album: dict
    for album in albuns:
        tree_view.insert('', END, values=(
            album['author'], album['album'], album['year'], album['release']))


def clean_albuns(tree_view: ttk.Treeview):
    for line in tree_view.get_children():
        tree_view.delete(line)


   

def on_submit(author: ttk.Entry, date: ttk.Combobox, date_time: IntVar, label_message: ttk.Label, tree_view: ttk.Treeview, albuns: list, button: ttk.Button):
    author_value = author.get()
    date_time_value = date_time.get()
    date_value = date.get()
    filtered_albuns = albuns
    print(date_value)
    if not author_value and not date_value:
        label_message.configure(text="Nenhum filtro selecionado")
    elif author_value:
        filtered_albuns = domain.get_all_albuns_by('author', author_value, albuns)
    elif date_time_value:
        if date_time_value == 1:
            filtered_albuns = domain.get_album_previous_year(date_value, albuns)
        elif date_time_value == 2:
            filtered_albuns = domain.get_album_same_year(date_value, albuns)
        elif date_time_value == 3:
            filtered_albuns = domain.get_album_later_year(date_value, albuns)
    clean_albuns(tree_view)
    render_albuns(tree_view, filtered_albuns)
    def clean_label():
        label_message.configure(text='', foreground=ERROR)
    button.after(1500, clean_label)


def open_my_albuns_screen(_event):

    # Create my albuns window.
    window_width = 700
    window_height = 550
    root = Toplevel()
    root.title("Deezer - Meus albuns")
    root.iconbitmap('assets/icon.ico')
    root.resizable(False, False)
    root.attributes('-topmost', 1)

    # Center window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root.geometry(
        f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    # Variables
    data = [str(i) for i in range(1900, domain.CURRENT_YEAR, 4)]
    time_date = IntVar()
    time_date.set(1)
    albuns = domain.get_albuns()


    list_section = ttk.Frame(root)
    columns = ('author', 'album', 'year', 'release')
    tree_view = ttk.Treeview(
        list_section, columns=columns, show='headings', height=300
    )
    # Create and positioning elements
    # Title Section
    title_section = ttk.Frame(root)
    title_section.pack(side='top', anchor='w', padx=24, pady=16)

    # Title and Subtitle
    back_button = ttk.Button(title_section, text="Voltar",
                             padding=(8, 4), command=root.destroy)
    back_button.pack(anchor="w")
    title_body = ttk.Label(title_section, text="Meus albuns", font=(
        'Roboto', 24, 'bold'),  foreground=TITLE)
    title_body.pack(anchor="w")
    subtitle_body = ttk.Label(title_section, text="Veja todos os albuns filtrando por Autor e Ano de lançamento", font=(
        'Roboto', 16, "normal"),  foreground=SUBTITLE)
    subtitle_body.pack(anchor="w")

    # Filter by Autor Section
    inputs_section = ttk.Frame(root)
    inputs_section.pack(side='top', anchor='w', padx=24, pady=4)
    author_label = ttk.Label(inputs_section, text="Filtrar por Autor", font=(
        'Roboto', 12, "normal"),  foreground=TITLE)
    author_input = ttk.Entry(inputs_section, name="author", width=INPUT_WIDTH)
    author_label.pack(anchor="w", pady=2)
    author_input.pack(anchor="w", pady=INPUT_PY)
    label_message = ttk.Label(inputs_section, font=('Roboto', 8, "normal"),  foreground=ERROR)
    label_message.pack(anchor="w", pady=2)

    # Filter by Date Section
    radio_section = ttk.Frame(root)
    radio_section.pack(side='top', anchor='w', padx=24, pady=4)
    radio_previous = ttk.Radiobutton(
        radio_section, text="Anterior a", variable=time_date, value=1)
    radio_previous.grid(column=0, row=0)
    radio_equals = ttk.Radiobutton(
        radio_section, text="Igual a", variable=time_date, value=2)
    radio_equals.grid(column=1, row=0)
    radio_next = ttk.Radiobutton(
        radio_section, text="Posterior a", variable=time_date, value=3)
    radio_next.grid(column=2, row=0)
    date_input = ttk.Combobox(radio_section, values=data)
    date_input.grid(column=3, row=0, padx=8)
    filter_button = ttk.Button(
        radio_section, text='Filtrar', style='Accent.TButton')
    def bind_on_submit(_event):
        on_submit(author_input, date_input, time_date, label_message, tree_view, albuns, filter_button)
    filter_button.grid(column=5, row=0)
    filter_button.bind('<Button-1>', bind_on_submit)

    # Tree_view Section
    
    list_section.pack(side='top', anchor='w', padx=24, pady=4)

    tree_view.heading('author', text='Autor')
    tree_view.heading('album', text='Album')
    tree_view.heading('year', text='Ano')
    tree_view.heading('release', text='É lançamento?')
    tree_view.column('year', width=160, anchor='center')
    tree_view.column('album', width=160, anchor='center')
    tree_view.column('author', width=160, anchor='center')
    tree_view.column('release', width=120, anchor='center')
    render_albuns(tree_view, albuns)

    tree_view.pack(side='top', anchor='w')
