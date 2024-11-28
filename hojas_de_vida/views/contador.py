import reflex as rx
from hojas_de_vida.components.detalles.experiencia import titulos, experiencia, estudios, habilidades, habilidades_personales, hobies
from hojas_de_vida.style.sizes import Size

def contador()->rx.Component:
    return rx.flex(
        rx.box(
            rx.vstack(
            titulos("HABILIDADES DE SOFTWARE"),
            rx.spacer(spacing="2", direction="row"),
            habilidades("Excel", 80),
            habilidades("Python", 70),
            habilidades("Pandas", 60),
            habilidades("Numpy", 50),
            habilidades("Power Bi", 70),
            habilidades("SQL", 70),
            ),
            rx.vstack(
                rx.spacer(spacing="4", direction="row"),
            titulos("LENGUAJES"),
            rx.spacer(spacing="2", direction="row"),
            habilidades("Español", 99),
            habilidades("Ingles", 60),
            rx.spacer(spacing="2", direction="row"),
            ),
            rx.vstack(
                rx.spacer(spacing="4", direction="row"),
            titulos("VALORES"),
            rx.spacer(spacing="2", direction="row"),
            habilidades_personales("- Responsabilidad"),
            habilidades_personales("- Integridad"),
            habilidades_personales("- Objetividad"),
            habilidades_personales("- Confidencialidad"),
            habilidades_personales("- Proactividad"),
            habilidades_personales("- Aprendizaje continuo"),
            spacing="1"            
            ),
            width="33%",
            spacing="4",
            margin="4px",
            padding="4px"            
        ),
        rx.box(
            titulos("EXPERIENCIA LABORAL"),
            rx.spacer(spacing="4", direction="row"),
            experiencia("01-2021","08-2024", "Proinsalud S.A", "Coordinador de Costos", "Conseguir el reporte del 95% de los costos generados por la empresa y distribuirlos por cada unidad funcional como tambien por centro de costo"),
            #experiencia()
            width="33%",
            spacing="4",
            margin="4px",
            padding="4px" 
        ),
        rx.box(
            titulos("ESTUDIOS"),
            rx.spacer(spacing="4", direction="row"),
            estudios("CONTADOR PUBLICO","Fundacion Universitaria San Martin"),
            width="33%",
            spacing="4",
            margin="4px",
            padding="4px" 
            
        
        ),
    spacing="4",
    padding="1em",
    flex_direction=["column", "column", "row"],
    height="600px",
    width="100%",
    )