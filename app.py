import PySimpleGUI as ui
import main

# Top

title = ui.Text('Youtube to MP3')

top = [
    [title]
]

# Middle

url_prompt = ui.Text('Enter URL')
url_input = ui.InputText()
url_confirm = ui.Button('Get')

url_row = [
    [url_prompt, url_input, url_confirm]
]

middle = [
    ui.Text(),
    url_row
]

# Bottom

close_button = ui.Button("Close")

bottom = [
    [close_button]
]

layout = [
    [title],
    [url_prompt, url_input, url_confirm],
    [ui.Output(size=(80, 10))],
    [close_button]
]


def App():
    window = ui.Window("YT2MP3", layout)

    while True:
        event, values = window.read(timeout=100)
        if event == "Get":
            try:
                link = url_input.Get()
                print("Getting MP3...")
                main.main(link)
                print("Finished!")
                window.Refresh()
            except Exception as e:
                print(e)

        if event in (window.WasClosed, 'Close'):
            break
        window.Refresh()

    window.close()