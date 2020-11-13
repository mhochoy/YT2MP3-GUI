import PySimpleGUI as ui
from .layout import layout

window = ui.Window("YT2MP3", layout)


def change_layout(_layout: list):
    # Soon to be depreciated!
    window.Layout(_layout)
