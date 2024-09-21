import reflex as rx
from hojas_de_vida.style.sizes import Size

def indice () -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.center(
                rx.box(
                    rx.vstack(
                        rx.image(
                        src="/logo.jpg",
                        width="50em",
                        height="auto",
                        border_radius="10%"
                        
                    ),
                    rx.hstack(
                    rx.button(
                        rx.link(
                            "Contador Publico", href="/hvcontador"
                        ),
                        variant="outline",
                        color_scheme="gray",
                        position="relative",
                        
                    ),
                    rx.button(
                        rx.link(
                            "Programador Web", href="/programador"
                            ),
                        variant="outline",
                        color_scheme="gray",
                        position="relative",
                       
                        ),
                        top="70%",
                        left="30%",
                        position="absolute"
                    ),
                ),
                    position="relative",
                    margin=Size.MEDIUM.value
                    ),
                    
                ),
        ),
        rx.mobile_and_tablet(
            rx.flex(
                rx.box(
                    rx.vstack(
                        rx.image(
                        src="/logo.jpg",
                        width="40em",
                        height="auto",
                        border_radius="10%"
                    ),
                        rx.hstack(
                        rx.button(
                            rx.link(
                                "Contador Publico", href="/contador",
                                weight="light",
                                size="1"
                            ),
                            variant="outline",
                            color_scheme="gray",   
                            margin= Size.MEDIUM.value
                            
                        ),
                        rx.button(
                            rx.link(
                                "Programador Web", href="/programador",
                                weight="light",
                                size="1"
                                ),
                            variant="outline",
                            color_scheme="gray",    
                            margin= Size.MEDIUM.value
                            ),
                        position="absolute",
                        top="70%",
                        left="5%",
                        ),
                ),
                    position="relative",
                    
                    ),
                    direction="column",
                    spacing="2",
                    align="center",
                    align_items="center",
                    margin= Size.EXTRA.value
                    
                ),
        ),
            
        )