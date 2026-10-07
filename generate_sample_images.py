import os
from PIL import Image, ImageDraw, ImageFont

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), "sample_images")
os.makedirs(SAMPLE_DIR, exist_ok=True)

def create_food_sample_image(filename, bg_color, inner_shapes, label_text, subtext=""):
    """Generates a high quality visual representation of a food sample for offline testing."""
    img = Image.new("RGB", (400, 400), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw background container/plate circle
    draw.ellipse([30, 30, 370, 370], fill=(240, 240, 240), outline=(180, 180, 180), width=6)
    draw.ellipse([50, 50, 350, 350], fill=bg_color, outline=(200, 200, 200), width=2)
    
    # Draw food textures/shapes
    for shape in inner_shapes:
        stype = shape.get("type")
        coords = shape.get("coords")
        color = shape.get("color")
        if stype == "ellipse":
            draw.ellipse(coords, fill=color)
        elif stype == "rectangle":
            draw.rectangle(coords, fill=color)
        elif stype == "line":
            draw.line(coords, fill=color, width=shape.get("width", 3))
        elif stype == "polygon":
            draw.polygon(coords, fill=color)
            
    # Add Text Label
    try:
        font = ImageFont.truetype("arial.ttf", 22)
        font_sub = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        
    # Draw dark banner at bottom
    draw.rectangle([0, 320, 400, 400], fill=(20, 30, 45))
    draw.text((20, 330), label_text, fill=(255, 255, 255), font=font)
    draw.text((20, 362), subtext, fill=(180, 220, 255), font=font_sub)
    
    file_path = os.path.join(SAMPLE_DIR, filename)
    img.save(file_path)
    return file_path

def generate_all_samples():
    samples = [
        ("leftover_rice.jpg", (250, 248, 240), [
            {"type": "ellipse", "coords": [70, 70, 330, 330], "color": (255, 255, 250)},
            {"type": "ellipse", "coords": [100, 120, 140, 145], "color": (230, 230, 220)},
            {"type": "ellipse", "coords": [180, 150, 220, 175], "color": (235, 235, 225)},
            {"type": "ellipse", "coords": [220, 220, 260, 245], "color": (240, 240, 230)},
        ], "Leftover Rice", "Traditional Food | Freshness: 92%"),

        ("boiled_milk.jpg", (255, 255, 255), [
            {"type": "ellipse", "coords": [60, 60, 340, 340], "color": (245, 248, 255)},
            {"type": "ellipse", "coords": [120, 120, 280, 280], "color": (255, 255, 250)},
        ], "Boiled Milk", "Dairy | Freshness: 98% (Fresh)"),

        ("chicken_curry.jpg", (180, 60, 20), [
            {"type": "ellipse", "coords": [60, 60, 340, 340], "color": (160, 50, 15)},
            {"type": "polygon", "coords": [(120, 150), (180, 120), (210, 180)], "color": (110, 35, 10)},
            {"type": "polygon", "coords": [(200, 220), (270, 200), (250, 270)], "color": (120, 40, 12)},
            {"type": "ellipse", "coords": [150, 210, 180, 240], "color": (80, 160, 40)} # coriander garnish
        ], "Chicken Curry", "Traditional Leftover | Freshness: 88%"),

        ("veg_curry.jpg", (210, 120, 30), [
            {"type": "ellipse", "coords": [60, 60, 340, 340], "color": (190, 100, 20)},
            {"type": "rectangle", "coords": [120, 130, 160, 170], "color": (240, 200, 50)}, # Paneer/potato block
            {"type": "ellipse", "coords": [200, 140, 240, 180], "color": (40, 160, 50)}, # Peas
            {"type": "ellipse", "coords": [170, 210, 210, 250], "color": (220, 50, 40)}, # Tomato piece
        ], "Veg Curry / Sabzi", "Traditional Food | Freshness: 90%"),

        ("sambar.jpg", (200, 110, 30), [
            {"type": "ellipse", "coords": [60, 60, 340, 340], "color": (185, 95, 20)},
            {"type": "ellipse", "coords": [100, 160, 140, 200], "color": (230, 140, 30)},
            {"type": "polygon", "coords": [(190, 130), (240, 120), (220, 180)], "color": (60, 140, 50)},
        ], "Sambar", "Traditional Leftover | Freshness: 85%"),

        ("rasam.jpg", (190, 70, 20), [
            {"type": "ellipse", "coords": [60, 60, 340, 340], "color": (175, 55, 15)},
            {"type": "ellipse", "coords": [130, 130, 270, 270], "color": (195, 65, 25)},
            {"type": "ellipse", "coords": [160, 180, 180, 200], "color": (30, 140, 30)},
        ], "Rasam", "Traditional Leftover | Freshness: 94%"),

        ("curd_dahi.jpg", (250, 250, 245), [
            {"type": "ellipse", "coords": [60, 60, 340, 340], "color": (245, 245, 238)},
            {"type": "ellipse", "coords": [100, 100, 300, 300], "color": (255, 255, 250)},
        ], "Curd / Dahi", "Traditional Dairy | Freshness: 96%"),

        ("dosa_batter.jpg", (245, 242, 230), [
            {"type": "ellipse", "coords": [60, 60, 340, 340], "color": (238, 235, 220)},
            {"type": "ellipse", "coords": [110, 110, 290, 290], "color": (248, 245, 235)},
        ], "Dosa / Idli Batter", "Traditional Batter | Freshness: 95%"),

        ("fresh_apple.jpg", (220, 40, 40), [
            {"type": "ellipse", "coords": [90, 80, 310, 310], "color": (200, 30, 30)},
            {"type": "ellipse", "coords": [110, 100, 160, 160], "color": (240, 80, 80)}, # shine
            {"type": "rectangle", "coords": [190, 50, 210, 90], "color": (80, 50, 20)}, # stem
            {"type": "ellipse", "coords": [205, 55, 240, 80], "color": (50, 160, 40)}, # leaf
        ], "Fresh Apple", "Fresh Fruit | Freshness: 96% (Fresh)"),

        ("fresh_tomato.jpg", (230, 50, 30), [
            {"type": "ellipse", "coords": [80, 80, 320, 320], "color": (220, 40, 20)},
            {"type": "ellipse", "coords": [110, 110, 150, 150], "color": (250, 100, 80)}, # gloss
            {"type": "polygon", "coords": [(180, 70), (220, 70), (200, 100)], "color": (40, 160, 30)}, # calyx
        ], "Fresh Tomato", "Fresh Vegetable | Freshness: 94%"),

        ("spinach.jpg", (40, 150, 40), [
            {"type": "ellipse", "coords": [70, 70, 330, 330], "color": (30, 130, 30)},
            {"type": "ellipse", "coords": [110, 110, 230, 230], "color": (50, 170, 50)},
            {"type": "ellipse", "coords": [180, 170, 300, 290], "color": (25, 120, 25)},
        ], "Spinach / Leafy Greens", "Fresh Vegetable | Freshness: 91%"),

        ("packaged_milk.jpg", (30, 100, 200), [
            {"type": "rectangle", "coords": [100, 70, 300, 310], "color": (240, 245, 255)},
            {"type": "rectangle", "coords": [120, 120, 280, 180], "color": (30, 100, 220)},
            {"type": "line", "coords": [130, 240, 270, 240], "color": (10, 10, 10), "width": 8},
            {"type": "line", "coords": [130, 260, 270, 260], "color": (10, 10, 10), "width": 8},
        ], "Packaged Amul Milk 1L", "OCR / Barcode: 8901262010115 | Exp: 3 Days"),
    ]
    
    generated_paths = []
    for name, bg, shapes, label, sub in samples:
        path = create_food_sample_image(name, bg, shapes, label, sub)
        generated_paths.append(path)
    print(f"Generated {len(generated_paths)} sample test images.")

if __name__ == "__main__":
    generate_all_samples()
