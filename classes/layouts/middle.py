import PySimpleGUI as ui


class Middle:
    def __init__(self):
        # Fields relating to URL input. Looking to add a .txt list feature some time soon.
        self.url_prompt = ui.Text('Enter URL:')
        self.url_input = ui.InputText()
        self.url_confirm = ui.Button('Get')

