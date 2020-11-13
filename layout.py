from .classes.layouts import Top, Middle, Bottom
from .classes.elements import Element

# Where the Layouts and Elements are handled

top = Top()
middle = Middle()
bottom = Bottom()
element = Element()


layout = [
    [
        top.title
    ],
    [
        middle.url_prompt, 
        middle.url_input,
        middle.url_confirm
    ],
    [
        element.output_element
    ],
    [
        bottom.credits,
        bottom.close_button
    ],
]
