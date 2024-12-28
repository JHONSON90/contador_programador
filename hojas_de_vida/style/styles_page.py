import reflex as rx
from hojas_de_vida.style.text_color import color as Color
from hojas_de_vida.style.sizes import Size

def global_styles():
    return rx.el.style(
        """
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-30px) rotate(5deg); }
        }
        @keyframes pulse {
            0%, 100% { opacity: 0.4; transform: scale(1); }
            50% { opacity: 0.8; transform: scale(1.1); }
        }
        .animate-float {
            animation: float 8s ease-in-out infinite;
        }
        .animate-pulse {
            animation: pulse 6s ease-in-out infinite;
        }
        .cube:nth-child(2n) {
            animation-delay: 2s;
        }
        .pyramid:nth-child(3n) {
            animation-delay: 3s;
        }
        .sphere:nth-child(4n) {
            animation-delay: 4s;
        }
        .line:nth-child(5n) {
            animation-delay: 1s;
        }
        .data-point:nth-child(2n) {
            animation-delay: 1.5s;
        }
        """
    )


def create_pulsating_dot(
    horizontal_position, vertical_position
):
    return rx.box(
        class_name="animate-ping bg-cyan-400 data-point",
        top=vertical_position,
        background_color="#446074",
        left=horizontal_position,
        position="absolute",
        height="0.75rem",   
        border_radius="9999px",
        width="0.75rem",
    )


def create_background_shapes():
    """Generate a collection of animated background shapes including cube, pyramid, sphere, and lines."""
    return rx.box(
        rx.box(
            class_name="animate-float border-cyan-400 cube",
            top="10%",
            left="20%",
            position="absolute",
            border_width="4px",
            height="6rem",
            opacity="0.4",
            width="6rem",
        ),
        rx.box(
            class_name="animate-float border-b-40 border-b-green-400 border-l-24 border-r-24 pyramid",
            top="30%",
            left="60%",
            position="absolute",
            border_color="transparent",
            height="0",
            opacity="0.4",
            width="0",
        ),
        rx.box(
            class_name="animate-float sphere",
            top="70%",
            left="40%",
            position="absolute",
            background_color="#006466",
            height="5rem",
            opacity="0.4",
            border_radius="9999px",
            width="5rem",
        ),
        rx.box(
            class_name="animate-pulse line",
            top="25%",
            left="0",
            transform="rotate(45deg)",
            position="absolute",
            background_color="#F472B6",
            height="0.25rem",
            opacity="0.4",
            width="12rem",
        ),
        rx.box(
            class_name="animate-pulse bg-orange-400 line",
            top="75%",
            left="70%",
            transform="rotate(-45deg)",
            position="absolute",
            height="0.25rem",
            opacity="0.4",
            width="12rem",
        ),
        create_pulsating_dot(
            horizontal_position="85%",
            vertical_position="15%",
        ),
        create_pulsating_dot(
            horizontal_position="35%",
            vertical_position="35%",
        ),
        create_pulsating_dot(
            horizontal_position="15%",
            vertical_position="80%",
        ),
        
        create_pulsating_dot(
            horizontal_position="65%",
            vertical_position="80%",
        ),
        position="absolute",
        top="0",
        right="0",
        bottom="0",
        left="0",
    )



# def index():
#     """Render the complete portfolio page with styles, hero section, and background."""
#     return rx.fragment(
#         rx.el.link(
#             href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
#             rel="stylesheet",
#         ),
#         rx.el.style(
#             """
#         @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
#         body {
#             font-family: 'Inter', sans-serif;
#         }
#         @keyframes float {
#             0%, 100% { transform: translateY(0) rotate(0deg); }
#             50% { transform: translateY(-30px) rotate(5deg); }
#         }
#         @keyframes pulse {
#             0%, 100% { opacity: 0.4; transform: scale(1); }
#             50% { opacity: 0.8; transform: scale(1.1); }
#         }
#         .animate-float {
#             animation: float 8s ease-in-out infinite;
#         }
#         .animate-pulse {
#             animation: pulse 6s ease-in-out infinite;
#         }
#         .cube:nth-child(2n) {
#             animation-delay: 2s;
#         }
#         .pyramid:nth-child(3n) {
#             animation-delay: 3s;
#         }
#         .sphere:nth-child(4n) {
#             animation-delay: 4s;
#         }
#         .line:nth-child(5n) {
#             animation-delay: 1s;
#         }
#         .data-point:nth-child(2n) {
#             animation-delay: 1.5s;
#         }
#     """
#         ),
#         rx.box(create_hero_section()),
#     )

def create_star(left_position, top_position):
    """Create a single star element with the specified position."""
    return rx.box(
        class_name="animate-twinkle star",
        top=top_position,
        left=left_position,
        position="absolute",
        background_color="#ffffff",
        height="0.25rem",
        border_radius="9999px",
        width="0.25rem",
    )


def create_starfield():
    return rx.box(
        create_star(
            left_position="20%", top_position="10%"
        ),
        create_star(
            left_position="40%", top_position="15%"
        ),
        create_star(
            left_position="60%", top_position="25%"
        ),
        create_star(
            left_position="80%", top_position="35%"
        ),
        create_star(
            left_position="10%", top_position="45%"
        ),
        create_star(
            left_position="30%", top_position="55%"
        ),
        create_star(
            left_position="50%", top_position="65%"
        ),
        create_star(
            left_position="70%", top_position="75%"
        ),
        create_star(
            left_position="90%", top_position="85%"
        ),
        create_star(left_position="95%", top_position="5%"),
        create_star(
            left_position="75%", top_position="20%"
        ),
        create_star(
            left_position="55%", top_position="30%"
        ),
        create_star(
            left_position="35%", top_position="40%"
        ),
        create_star(
            left_position="15%", top_position="50%"
        ),
        create_star(
            left_position="85%", top_position="60%"
        ),
        create_star(left_position="5%", top_position="70%"),
        create_star(
            left_position="45%", top_position="80%"
        ),
        create_star(
            left_position="25%", top_position="90%"
        ),
        create_star(
            left_position="65%", top_position="95%"
        ),
        create_star(
            left_position="88%", top_position="12%"
        ),
        position="absolute",
        top="0",
        right="0",
        bottom="0",
        left="0",
    )

def create_cosmos_layout():
    """Create the main layout for the cosmos-themed page, including starfield and welcome message."""
    return rx.box(
        create_starfield(),
        rx.flex(
            position="absolute",
            display="flex",
            top="0",
            right="0",
            bottom="0",
            left="0",
            align_items="center",
            justify_content="center",
        ),
        class_name="bg-gradient-to-b from-gray-800 to-black",
        height="100vh",
        overflow="hidden",
        position="relative",
        width="100%",
    )


def index():
    """Render the complete cosmos-themed page with layout and CSS animations."""
    return rx.fragment(
        rx.box(
            create_cosmos_layout(),
            rx.el.style(
                """
  @keyframes twinkle {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.2; }
  }
  .animate-twinkle {
    animation: twinkle 3s infinite;
  }
  .star:nth-child(2n) {
    animation-delay: 0.5s;
  }
  .star:nth-child(3n) {
    animation-delay: 1s;
  }
  .star:nth-child(4n) {
    animation-delay: 1.5s;
  }
  .star:nth-child(5n) {
    animation-delay: 2s;
  }
"""
            ),
        )
    )