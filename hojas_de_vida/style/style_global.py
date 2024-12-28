import reflex as rx
from .style_fonts import Fonts
from .text_color import color, textColor

STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins&display=swap",
    "https://fonts.googleapis.com/css?family=Domine&display=swap",
    "https://fonts.googleapis.com/css?family=Roboto&display=swap"    
]

BASE_STYLE = {
    "font_family": Fonts.DEFAULT.value,
    "color": textColor.BODY.value,
    "back_ground": color.BACKGROUND.value,
    
    rx.progress: {
        "color_scheme": color.SECONDARY.value,
        
    },
    
    rx.link: {
        "font_family":Fonts.SECONDARY.value,
        "font_size": "14",
        "color": textColor.BODY.value,
        "text_decoration": "None",
        "underline": False,
        "hover":{
            "color": textColor.FOOTER.value,
            "text_decoration": "none"
        }
    },
    
    
}