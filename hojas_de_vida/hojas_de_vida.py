"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from hojas_de_vida.views.navbar import navbar
from hojas_de_vida.components.carta_presentacion.presentacion import componente_carta
from hojas_de_vida.views.title import  indice
from hojas_de_vida.views.contador import contador


from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
    #     navbar(), 
    #     rx.vstack(
    #         componente_carta(),
    #    ),
    indice(),
        width="100%",
        #size="4"
        
    )
    
def about() -> rx.Component:
    return rx.box(
                navbar(), 
        rx.vstack(
            componente_carta(),
       ),
    )
    
def programador() -> rx.Component:
        return rx.box(
                navbar(), 
        rx.vstack(
          
       ),
    )

def hvcontador() -> rx.Component:
        return rx.box(
                navbar(), 
                contador()
    )


app = rx.App()
app.add_page(index)
app.add_page(about)
app.add_page(hvcontador)
app.add_page(programador)
