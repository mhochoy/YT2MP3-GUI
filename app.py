import main
import layout
import options
import window


def App():
    # Building window according to layout, which contains a List of Elements. 
    app_window = window.window

    while True:
        # This program runs Asynchronously
        event, values = app_window.read(timeout=100)

        # On event confirming conversion request
        if event == "Get":
            try:
                link = layout.middle.url_input.Get()
                print("Getting MP3...")
                main.grab(link)

            # Must change
            except Exception as e:
                print(e)
        
        # On event confirming close of window
        if event in ('Close'):
            break
        app_window.Refresh()

    app_window.close()