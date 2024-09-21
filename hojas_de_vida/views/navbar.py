import reflex as rx

from hojas_de_vida.components.navbar_components.nav_link_components import navbar_link
from hojas_de_vida.style.sizes import Size as size

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width=size.EXTRA.value,
                        height="100%",
                        border_radius="15%",
                    ),
                    rx.heading(
                        "", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("Contador Publico", "/hvcontador"),
                    navbar_link("Programador","/programador"),
                    navbar_link("Acerca de mi", "/about"),
                            # rx.menu.item("Service 3"),
                    #navbar_link("Pricing", "/#"),
                    #TODO: revisar como hacer el contactarme y pasarle el correo al contactarme que ya esta hecho
                    #navbar_link("Contactactame", "/#"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
                width="100%",
                height="25%"
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Edison Portilla", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        #TODO COLOCAR EL ENLACE AL HOME
                        rx.menu.item(
                                rx.link("Contador Publico", href="/contador"),
                                ),
                        rx.menu.item(
                                rx.link("Programador", href="/programador")),
                                #rx.menu.item("Service 3"),  
                        rx.menu.item(
                                rx.link("Acerca de mi", href="/about")),                     
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
            width="100%"
        ),
        bg=rx.color("black", 3),
        padding=size.DEFAULT.value,
        direction= "left",
        #justify="between",
        align_items="center",
        position="left",
        top=size.MEDIUM.value,
        z_index="5",
        width="auto",
        
    )