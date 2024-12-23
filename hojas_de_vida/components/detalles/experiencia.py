import reflex as rx
from hojas_de_vida.style.sizes import Size

def titulos (titulo:str) -> rx.Component:
    return rx.box(
            rx.blockquote(
                titulo,
                size="3",
                weight="medium",
                color_scheme="gray"
                ),
    ),
    
def habilidades(habilidad:str, valor:int) -> rx.Component:    
       return rx.box(
                rx.vstack(
                    rx.progress(value=valor,
                                max=100,
                                color_scheme="gray",
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
                            rx.badge(rx.text(fecha_inicial, size="1"),
                                radius="large",
                                margin=Size.DEFAULT.value,
                                variant="surface",
                                size="3",
                                color_scheme="gray",
                                ),
                            rx.text("Hasta", size="1"),
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
                    rx.text(cargo),
                    spacing="0",
                ),                
                content= metas,
            ),
            collapsible=True,
            variant="ghost",
            width= "100%",
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
                rx.icon(icono),
                radius="full",
                variant="outline",
                color_scheme="gray",
            ),
            rx.text(hobbie),
            
        ),
        padding=Size.SMALL.value,
        width="100%",
    )
    