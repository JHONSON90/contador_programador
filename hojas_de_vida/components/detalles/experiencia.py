import reflex as rx
from hojas_de_vida.style.sizes import Size
from hojas_de_vida.style.text_color import color, textColor

def titulos (titulo:str) -> rx.Component:
    return rx.box(
            rx.blockquote(
                titulo,
                # size="3",
                # weight="medium",
                #color_scheme="gray"
                ),
    ),
    
def habilidades(habilidad:str, valor:int) -> rx.Component:    
       return rx.box(
                rx.vstack(
                    rx.progress(value=valor,
                                max=100,
                                color_scheme="gray",
                                high_contrast= True,
                                size="1",
                                radius="large",
                                variant="soft"
                            ),
                    rx.text(habilidad),
                    width="80%",
                    spacing="0"
                    ),
                    width="100%",
                    padding=Size.SMALL.value
                )
       
def habilidades_personales(habilidad:str)-> rx.Component:
    return rx.box(
        rx.text(habilidad),
        padding=Size.SMALL.value
    )
    
def experiencia(fecha_inicial:str, fecha_final:str, empresa:str, cargo:str, metas:str) ->rx.Component:
    return rx.accordion.root(
            rx.accordion.item(
                header= rx.vstack(
                    rx.hstack(
                            rx.badge(rx.text(fecha_inicial, size="1",),
                                radius="large",
                                margin=Size.DEFAULT.value,
                                variant="surface",
                                size="3",
                                color_scheme="gray",
                                ),
                            rx.text("Hasta", 
                                    size="1",
                                    color_scheme="gray",
                                    high_contrast=True
                                    ),
                            rx.badge(rx.text(fecha_final, size="1"),
                                radius="large",
                                margin=Size.DEFAULT.value,
                                variant="surface",
                                size="3",
                                color_scheme="gray",
                            ),
                            spacing="0",
                            align="center",
                            justify="center"
                        ),
                    rx.text(rx.text.strong(empresa)),
                    rx.text(cargo,
                            size="3",
                            color_scheme="gray",
                            high_contrast=True
                            ),
                    spacing="0",
                ),                
                content= metas,
                color_scheme="gray",
                high_contrast=True
            ),
            collapsible=True,
            variant="ghost",
            width= "100%",
            color_scheme="cyan",
            
        ),
    
def estudios(titulo:str, institucion:str)-> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                    rx.text.strong(titulo)
                ),
                rx.text(institucion),
                spacing="0"
        ),
        padding=Size.DEFAULT.value,
        width="100%",
    )

def hobies(icono:str, hobbie:str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.badge(
                rx.icon(icono, 
                        size=30,
                        color= rx.color("indigo",11)),
                radius="full",
                variant="outline",
                color_scheme="gray",
            ),
            rx.text(hobbie, 
                    weight="bold",
                    ),
            
        ),
        padding=Size.SMALL.value,
        width="100%",
    )
    