import reflex as rx
from .style_fonts import Fonts
from .text_color import color, textColor
from .sizes import Size

STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins&display=swap",
    "https://fonts.googleapis.com/css?family=Domine&display=swap",
    "https://fonts.googleapis.com/css?family=Roboto&display=swap"    
]

BASE_STYLE = {
    "font_family": Fonts.DEFAULT.value,
    "color": textColor.BODY.value,
    "back_ground": color.BACKGROUND.value,
    
    "body": {
            "min_height": "100vh",
            "margin": "0",
            "padding": "0"
        },
    
    rx.progress: {
        "border": f"1px solid {color.BLOCKCOLOR.value}",
        "background": color.SECONDARY.value,
        
    },
    
    rx.link: {
        "font_family":Fonts.SECONDARY.value,
        "font_size": "14px",
        "color": textColor.BODY.value,
        "text_decoration": "none",
        "underline": "none",
        "_hover":{
            "color": textColor.FOOTER.value,
            "text_decoration": "none"
        },
    },
    
    rx.blockquote:{
        "font_size": "20px",
        "font_weight": "bold",
        "padding": Size.SMALL.value,
        "border_left": f"{Size.SMALL.value} solid {color.BLOCKCOLOR.value}",
        "margin": f"{Size.SMALL.value} 0",
        "line_height": "1.6",
        "border_radius": "20%",
        "color": textColor.BODY.value,
        
    },
    
    rx.text.strong:{
        "font_weight": "bold",
        "color": textColor.HEADER.value,
        "font_size":"16px",
        
    },
    
    rx.text.span:{
        "font_weight": "normal",
        "color": textColor.FOOTER.value,
        "font_size": "13px"
    },
    
    rx.card:{
        "width": "100%",
        "padding": Size.MEDIUM.value
    },
    
}