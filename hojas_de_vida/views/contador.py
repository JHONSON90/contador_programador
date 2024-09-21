import reflex as rx
from hojas_de_vida.components.detalles.experiencia import titulos, experiencia, estudios, habilidades, habilidades_personales, hobies
from hojas_de_vida.style.sizes import Size

def contador()->rx.Component:
    return rx.flex(
        rx.box(
            rx.vstack(
            titulos("HABILIDADES DE SOFTWARE"),
            habilidades("Excel", 80),
            habilidades("Python", 60),
            habilidades("Pandas", 60),
            habilidades("Numpy", 50),
            habilidades("Power Bi", 70),
            habilidades("SQL", 70),
            ),
            rx.vstack(
            titulos("LENGUAJES"),
            habilidades("Español", 99),
            habilidades("Ingles", 60),
            ),
            rx.vstack(
            titulos("VALORES"),
            habilidades_personales("- Responsabilidad"),
            habilidades_personales("- Integridad"),
            habilidades_personales("- Objetividad"),
            habilidades_personales("- Confidencialidad"),
            habilidades_personales("- Proactividad"),
            habilidades_personales("- Aprendizaje continuo"),            
            ),
            width="100%"            
        ),
    spacing="4",
    padding="1em",
    flex_direction=["column", "column", "row"],
    height="600px",
    width="100%",
    )