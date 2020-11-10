import PySimpleGUI as ui
import layout

window = ui.Window("YT2MP3", layout.layout)

def change_layout(layout: list):
    # Soon to be depreciated!
    window.Layout(layout)