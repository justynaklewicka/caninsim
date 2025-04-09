from PIL import Image, ImageDraw
import os

# Define simple color mappings
COLOR_MAP = {
    "black": "#222222",
    "gold": "#d4af37",
    "white": "#f0f0f0",
    "brown": "#8b4513",
    "gray": "#a9a9a9",
}

def generate_dog_image_from_genetics(dog):
    # Create blank canvas
    image = Image.new("RGBA", (200, 200), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Draw base circle
    base_color = COLOR_MAP.get(dog.base_color, "#777777")
    draw.ellipse([20, 20, 180, 180], fill=base_color)

    # Add markings
    if dog.marking == "blaze":
        draw.rectangle([90, 50, 110, 140], fill="white")
    elif dog.marking == "socks":
        draw.rectangle([40, 160, 70, 200], fill="white")  # left foot
        draw.rectangle([130, 160, 160, 200], fill="white")  # right foot
    elif dog.marking == "patches":
        draw.ellipse([50, 50, 90, 90], fill="white")
        draw.ellipse([110, 100, 150, 140], fill="white")
    elif dog.marking == "mask":
        draw.rectangle([60, 60, 140, 100], fill="white")

    return image
