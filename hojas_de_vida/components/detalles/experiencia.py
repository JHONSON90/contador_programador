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
                    rx.text(habilidad),
                    rx.progress(value=valor,
                            color_scheme="gray",
                            size="1",
                            radius="medium"
                            ),
                    width="100%"
                        ),
                )
       
def habilidades_personales(habilidad:str)-> rx.Component:
    return rx.box(
        rx.text(habilidad)
    )
    
def experiencia(fecha_inicial:str, fecha_final:str, empresa:str, cargo:str) ->rx.Component:
    return rx.box(
        rx.hstack(
                rx.badge(
                    rx.vstack(
                        rx.text(fecha_inicial),
                        rx.text("Hasta"),
                        rx.text(fecha_final),
                    ),
                    radius="full",
                    margin=Size.DEFAULT.value,
                    variant="outline",
                    color_scheme="gray",
                    ),
                rx.text(
                    rx.text.strong(empresa)
                ),
                rx.text(cargo),
        ),
    )
    
def estudios(titulo:str, institucion:str)-> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                    rx.text.strong(titulo)
                ),
                rx.text(institucion),
        )
    )

def hobies(icono:str, hobbie:str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.badge(
                rx.icon(icono),
                radius="full",
                margin=Size.DEFAULT.value,
                variant="outline",
                color_scheme="gray",
            ),
            rx.text(hobbie),
        )
    )
    