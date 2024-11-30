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
            rx.spacer(spacing="6", direction="row"),
            experiencia("01-2021","08-2024", "Proinsalud S.A", "Coordinador de Costos", "Realizar un análisis de costos exhaustivo, cubriendo el 95% de los costos y gastos totales, con una distribución por unidad funcional y centro de costo. Además, determinar el costo del 70% de los procedimientos."),
            rx.spacer(spacing="3", direction="row"),
            experiencia("02-2017","11-2017", "Cooperativa Multiactiva Social Mayorista","Contador","Control y seguimiento exhaustivo al 100% de los movimientos contables, garantizando la precisión en la presentación de informes a la junta directiva y a entidades regulatorias. Elaboración oportuna de ajustes contables, reduciendo el margen de error a 7%." ),
            rx.spacer(spacing="3", direction="row"),
            experiencia("02-2017", "11-2017","Carnes del Sebastián (SUMAR)","Auxiliar Contable", "Realizar un control exhaustivo del 100% del inventario en la planta de producción y en los 3 puntos de venta, actualizando los registros diariamente. Esto incluye inventario de materias primas, productos en proceso, productos terminados."),
            rx.spacer(spacing="3", direction="row"),
            experiencia("01-2009","12-2015","Proinsalud S.A.", "Coordinador de suministros", "Acompañamiento activo en las actividades logísticas y operativas, optimizando procesos a través de la gestión documental eficiente, elaboración de planes de compras estratégicos, control de inventarios preciso y presentación de informes que permitan la toma de decisiones basadas en datos. Impulsar la mejora continua en los procesos de adquisición de insumos y equipos médicos."),
            #experiencia()
            width="33%",
            spacing="6",
            
            margin="4px",
            padding="4px" 
        ),
        rx.box(
            titulos("ESTUDIOS"),
            estudios("CONTADOR PUBLICO","Fundación Universitaria San Martín"),
            estudios("ESPECIALISTA EN GERENCIA FINANCIERA", "Fundación Universitaria del Area Andina"),
            
            titulos("HOBBIES"),
            rx.spacer(spacing="2", direction="row"),
            hobies("book-open-check", "Leer"),
            hobies("dribbble","Jugar Futbol"),
            hobies("music", "Escuchar música"),
            hobies("code-xml", "Aprender a programar"),
            hobies("dumbbell", "Hacer ejercicio"),
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