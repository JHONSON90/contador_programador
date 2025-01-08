import reflex as rx
from hojas_de_vida.components.detalles.experiencia import habilidades
from hojas_de_vida.style.sizes import Size

def srprogramador() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.vstack(
            rx.heading("Hola, soy Edison!!!", 
                    size="9",
                    weight="bold",
                    
                    #color= rx.color.gray,
                    ),
            rx.text.strong("Desarrollador Full Stack apasionado por crear experiencias web únicas y memorables", 
                    #size="6"
                    ),
            rx.hstack(
                rx.button(
                    rx.icon("at-sign", tag = "Email"),
                    "Email",
                    variant="ghost",
                    size="2",
                    color_scheme="gray",
                    high_contrast=True,
                    on_click= rx.redirect("mailto:edisonportillal@gmail.com", external=True)
                    ),
                rx.button(
                    rx.icon("github", tag = "GitHub", size=30),
                    "GitHub",
                    size="2",
                    variant="ghost",
                    color_scheme="gray",
                    high_contrast=True,
                    on_click= rx.redirect("https://github.com/JHONSON90", external=True)
                ),
                align="center",
                justify="center",
                spacing="6",
                widht="50%",
            ),
            align="center",
            justify="center",
            #margin_top = "30%",
            width= "100%",
            height= "100vh",
            text_align="center"
        ),
            rx.vstack(
                rx.heading("Sobre Mi", 
                    size="9",
                    margin_top = "0%",
                    margin_bottom= Size.LARGE.value
                    #color= rx.color.gray,
                    ),
                rx.hstack(
                rx.card(
                    rx.vstack(
                        rx.icon("code-xml", size=60, color= rx.color("indigo",11)),
                        rx.text("Desarrollo Web",
                        weight="bold",
                        size="7",
                        color_scheme="gray",
                        high_contrast=True,
                        margin_top= Size.MEDIUM.value
                        ),
                        rx.text.strong("Me especializo en crear aplicaciones web modernas y responsivas usando las últimas tecnologías")
                    ), 
                ),
                rx.card(
                    rx.vstack(
                        rx.icon("heart", size=60,color= rx.color("indigo",11)),
                        rx.text("Diseño UI/UX",
                        weight="bold",
                        size="7",
                        color_scheme="gray",
                        high_contrast=True,
                        margin_top= Size.MEDIUM.value
                        ),
                        rx.text.strong("Creo interfaces intuitivas y atractivas que mejoran la experiencia del usuario")
                    ),
                ),
                rx.card(
                    rx.vstack(
                        rx.icon("coffee", size=60, color= rx.color("indigo",11)),
                        rx.text("Siempre Aprendiendo",
                        weight="bold",
                        size="7",
                        color_scheme="gray",
                        high_contrast=True,
                        margin_top= Size.MEDIUM.value
                        ),
                        rx.text.strong("Constantemente explorando nuevas tecnologías y mejores prácticas")
                    )
                ),
            ),
                align="center",
                justify="center",
                padding = Size.SMALL.value,
                #margin_top = "30%",
                width= "100%",
                height= "100vh",
                text_align="center"
            ),
            
            rx.vstack(
                rx.heading("Mejores Proyectos",
                           size="9",
                           margin_top = "0%",
                           margin_bottom= Size.LARGE.value
                           ),
                rx.hstack(
                    rx.card(
                        rx.image(),
                        rx.text("Segumiento a Consignaciones",
                                weight="bold",
                                size="6",
                                color_scheme="gray",
                                high_contrast=True,
                                ),
                        rx.text.span("Aplicación moderna construida para gestionar y controlar las consignaciones recibidas de una empresa",
                                ),
                        rx.hstack(
                            rx.badge("Flet",
                                     color_scheme="indigo", variant="outline", high_contrast=True
                                     ),
                            rx.badge("MySQL",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("Firebase",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                        ),
                    ),
                    rx.card(
                        rx.image(),
                        rx.text("Segumiento a PQRS",
                                weight="bold",
                                size="6",
                                color_scheme="gray",
                                high_contrast=True,
                                ),
                        rx.text.span("Aplicación construida para gestionar y controlar las PQRS recibidas de un conjunto residencial"),
                        rx.hstack(
                            rx.badge("Flet",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("FastAPI",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("MySQL",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                        ),
                    ),
                    rx.card(
                        rx.image(),
                        rx.text("TO-DO",
                                weight="bold",
                                size="6",
                                color_scheme="gray",
                                high_contrast=True,
                                ),
                        rx.text("Aplicación construida para controlar las tareas que se tienen que realizar"),
                        rx.hstack(
                            rx.badge("React",   
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("Postgres",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                            rx.badge("MySQL",
                                     color_scheme="indigo", variant="outline", high_contrast=True,
                                     ),
                        ),
                    ),
                ),
                align="center",
                justify="center",
                #margin_top = "30%",
                width= "100%",
                height= "100vh",
                text_align="center"
            ),
            rx.vstack(
                rx.heading("Habilidades",
                           size="9",
                           margin_top = "0%",
                           margin_bottom = Size.LARGE.value,
                ),
                rx.grid(
                     rx.card(
                         rx.center(
                             rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg",
                                 width = "40px",
                                 height = "40px"),
                             habilidades("Python", 80 ),    
                             width = "100%",
                             height = "100%",
                         ),
                    height="100px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                      rx.card(
                          rx.center(
                              rx.image(src="/assets/FLET_LOGO.png",
                                 width = "40px",
                                 height = "40px"),
                              habilidades("Flet", 80 ),
                                    width = "100%",
                             height = "100%",),
                    height="100px",
                    width="100%",
                    padding=Size.EXTRA.value
                ), 
                     rx.card(
                         rx.center(
                             rx.image(src="/assets/REFLEX_LOGO.png",
                                 width = "40px",
                                 height = "40px"),
                             habilidades("Reflex", 70 ),
                                   width = "100%",
                             height = "100%",
                                   ),
                    height="100px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                      rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg",
                                 width = "40px",
                                 height = "40px"),
                        habilidades("HTML/CSS", 60 ),
                              width = "100%",
                             height = "100%",
                             ),
                    height="100px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                     rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg",
                                 width = "40px",
                                 height = "40px"),
                        habilidades("Javascript", 60 ),
                              width = "100%",
                             height = "100%",
                             ),
                    height="100px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                      rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg",
                                 width = "40px",
                                 height = "40px"),
                        habilidades("React", 50),
                              width = "100%",
                             height = "100%",
                              ),
                    height="100px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                      rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg",
                                 width = "40px",
                                 height = "40px"),
                        habilidades("Postgress", 50),
                              width = "100%",
                             height = "100%",
                              ),
                    height="100px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                       rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg",
                                 width = "40px",
                                 height = "40px"),
                        habilidades("FastApi", 50),
                              width = "100%",
                             height = "100%",
                              ),
                    height="100px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                        rx.card(
                    rx.center(
                        rx.image(src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg",
                                 width = "40px",
                                 height = "40px"),
                        habilidades("MySQL", 50),
                              width = "100%",
                             height = "100%",
                              ),
                    height="100px",
                    width="100%",
                    padding=Size.EXTRA.value
                ),
                      columns="3",
                      spacing="4",
                      width="100%",
                      margin= Size.MEDIUM.value
                ),
            
                align="center",
                justify="center",
                #margin_top = "30%",
                width= "100%",
                height= "100vh",
                text_align="center"
            ),
        ),
        width = "100%",
        spacing="4em",
        margin = Size.DEFAULT.value
    )
#https://es.wallpapers.com/fondos-de-pantalla/rutinade-codificacion-minimalista-ih0aeqolwl5awdmh.html