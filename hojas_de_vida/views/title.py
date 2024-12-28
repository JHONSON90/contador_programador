import reflex as rx
from hojas_de_vida.style.sizes import Size

def indice () -> rx.Component:
    return rx.box(
            rx.heading("Jhon Edison Portilla",
                       font_weight="800",
                        margin_bottom="1.5rem",
                        font_size="4.5rem",
                        line_height="1",
                        color="#ffffff",
                        letter_spacing="-0.05em",
                        as_="h1"
                        ),    
            rx.hstack(
                rx.button(
                        rx.link(
                            "Contador Publico", href="/hvcontador",
                            underline="hover",
                            color_scheme="gray"
                        ),
                        class_name="bg-gradient-to-r from-cyan-400 hover:from-cyan-500 hover:to-blue-600 to-blue-500 transform",
                        transition_duration="300ms",
                        font_weight="700",
                        _hover={"transform": "scale(1.05)"},
                        padding_left="2rem",
                        padding_right="2rem",
                        padding_top="0.75rem",
                        padding_bottom="0.75rem",
                        border_radius="9999px",
                        color="#ffffff",
                        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                    ),
                    rx.button(
                        rx.link(
                            "Programador Web", href="/programadorsr",
                            underline="hover",
                            color_scheme="gray"
                            ),
                        class_name="bg-gradient-to-r from-cyan-400 hover:from-cyan-500 hover:to-blue-600 to-blue-500 transform",
                        transition_duration="300ms",
                        font_weight="700",
                        _hover={"transform": "scale(1.05)"},
                        padding_left="2rem",
                        padding_right="2rem",
                        padding_top="0.75rem",
                        padding_bottom="0.75rem",
                        border_radius="9999px",
                        color="#ffffff",
                        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                        ),
                    align="center",
                    justify="center",
                    width="100%",
            ),  
         text_align="center",  
         justify_content="center" 
        )