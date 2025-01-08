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
    
    
def create_icon(
    icon_color, icon_height, icon_tag, icon_width
):
    """Create an icon component with specified color, height, tag, and width."""
    return rx.icon(
        tag=icon_tag,
        height=icon_height,
        color=icon_color,
        width=icon_width,
    )


def fondo_about_me():
    """Create the main page layout with background elements and profile content."""
    return rx.box(
        rx.box(
            class_name="bg-gradient-to-r from-white to-black",
            position="absolute",
            top="0",
            bottom="0",
            right="0",
            width="50%",
        ),
        # rx.flex(
        #     create_profile_layout(),
        #     position="absolute",
        #     display="flex",
        #     top="0",
        #     right="0",
        #     bottom="0",
        #     left="0",
        #     align_items="center",
        #     justify_content="center",
        # ),
        rx.box(
            create_icon(
                icon_color="#D1D5DB",
                icon_height="100%",
                icon_tag="triangle",
                icon_width="100%",
            ),
            position="absolute",
            height="16rem",
            left="0",
            opacity="0.1",
            top="0",
            width="16rem",
        ),
        rx.box(
            create_icon(
                icon_color="#D1D5DB",
                icon_height="100%",
                icon_tag="circle",
                icon_width="100%",
            ),
            class_name="transform",
            position="absolute",
            bottom="0",
            height="16rem",
            opacity="0.1",
            right="0",
            transform="rotate(180deg)",
            width="16rem",
        ),
        background_color="#ffffff",
        height="100vh",
        overflow="hidden",
        position="relative",
        width="100%",
    )