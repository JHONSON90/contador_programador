import reflex as rx
from hojas_de_vida.components.detalles.experiencia import habilidades


def srprogramador() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text("Hola, soy Edison!!!", 
                    size="9",
                    #color= rx.color.gray,
                    ),
            rx.text("Desarrollador Full Stack apasionado por crear experiencias web únicas y memorables"),
            rx.spacer(),
            rx.hstack(
                rx.button(
                    rx.icon("at-sign", tag = "Email"),
                    "Email"
                    ),
                rx.button(
                    rx.icon("github", tag = "GitHub"),
                    "GitHub"
                )
            ),
            rx.spacer(),
            rx.hstack(
                rx.card(
                    rx.vstack(
                        rx.icon("code-xml"),
                        rx.text("Desarrollo Web"),
                        rx.text("Me especializo en crear aplicaciones web modernas y responsivas usando las últimas tecnologías")
                    )
                ),
                rx.card(
                    rx.vstack(
                        rx.icon("heart"),
                        rx.text("Diseño UI/UX"),
                        rx.text("Creo interfaces intuitivas y atractivas que mejoran la experiencia del usuario")
                    )
                ),
                rx.card(
                    rx.vstack(
                        rx.icon("coffee"),
                        rx.text("Siempre Aprendiendo"),
                        rx.text("Constantemente explorando nuevas tecnologías y mejores prácticas")
                    )
                ),
            ),
            
            rx.spacer(),
            
            rx.vstack(
                rx.text("Mejores Proyectos"),
                rx.hstack(
                    rx.card(
                        rx.image(),
                        rx.text("Segumiento a Consignaciones"),
                        rx.text("Aplicación moderna construida para gestionar y controlar las consignaciones recibidas de una empresa"),
                        rx.hstack(
                            rx.badge("Flet"),
                            rx.badge("MySQL"),
                            rx.badge("Firebase"),
                        ),
                    ),
                    rx.card(
                        rx.image(),
                        rx.text("Segumiento a PQRS"),
                        rx.text("Aplicación construida para gestionar y controlar las PQRS recibidas de un conjunto residencial"),
                        rx.hstack(
                            rx.badge("Flet"),
                            rx.badge("FastAPI"),
                            rx.badge("MySQL"),
                        ),
                    ),
                    rx.card(
                        rx.image(),
                        rx.text("TO-DO"),
                        rx.text("Aplicación construida para controlar las tareas que se tienen que realizar"),
                        rx.hstack(
                            rx.badge("React"),
                            rx.badge("Postgres"),
                            rx.badge("MySQL"),
                        ),
                    ),
                )
            ),
            rx.vstack(
                rx.text("Habilidades"),
                rx.grid(
                     rx.card(
                    habilidades("Python", 80 ),
                    height="100px",
                    width="100%"
                ),
                      rx.card(
                    habilidades("Flet", 80 ),
                    height="100px",
                    width="100%"
                ), 
                     rx.card(
                    habilidades("Reflex", 70 ),
                    height="100px",
                    width="100%"
                ),
                      rx.card(
                    habilidades("HTML/CSS", 60 ),
                    height="100px",
                    width="100%"
                ),
                     rx.card(
                    habilidades("Javascript", 60 ),
                    height="100px",
                    width="100%"
                ),
                      rx.card(
                    habilidades("React", 50),
                    height="100px",
                    width="100%"
                ),
                      columns="3",
                      spacing="4",
                      width="100%",
                ),
                width="100%"
            )
            
            
            
        ),
        height = "100%",
        width = "100%",
    )

#https://es.wallpapers.com/fondos-de-pantalla/rutinade-codificacion-minimalista-ih0aeqolwl5awdmh.html