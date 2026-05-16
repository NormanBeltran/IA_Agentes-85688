import os
from openai import OpenAI
from moviepy import ImageClip, concatenate_videoclips
import requests
from PIL import Image
from io import BytesIO
import base64
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Leer configuración externa
API_KEY = os.getenv("API_KEY_OPENAI")
MODEL_VIDEO = os.getenv("MODEL_OPENAI_VIDEO")
MODEL_IMAGEN = "gpt-5.5"

# 1. Configuración del cliente
client = OpenAI(api_key=API_KEY)

prompts = [
    "Medium resolution, standard definition. A ginger tabby cat and a tiny brown mouse cautiously sniffing each other on a bright green park lawn. Soft natural sunlight. Slow camera pan from left to right. Peaceful and playful atmosphere, highly detailed subjects.",
    "Medium resolution, standard definition. A tiny brown mouse playfully running through the tall green grass while a happy ginger cat gently chases it. The cat has a joyful expression. Dynamic tracking shot following the animals. Bright daylight, flying leaves in the background.",
    "Medium resolution, standard definition. A ginger tabby cat rolling on its back on the park grass, playfully batting its paws in the air at the little brown mouse jumping around it. Both animals look energetic and friendly. Static camera angle, joyful and comical mood.",
    "Medium resolution, standard definition. The ginger cat and the brown mouse sitting side-by-side on a wooden park bench, peacefully watching the sunset together. Warm golden hour lighting. Slow zoom out. Heartwarming and calm cinematic feel."
]

duracion_por_imagen = 3  # segundos
imagenes = []

# =========================
# GENERAR IMÁGENES
# =========================

print("1. Generando imgenes", sep="")

for i, prompt in enumerate(prompts):
    print(f"{i} ...", sep="")
    response = client.responses.create(
        model=MODEL_IMAGEN,
        input=prompt,
        tools=[{"type": "image_generation"}],
    )

    # Save the image to a file
    image_data = [
        output.result
        for output in response.output
        if output.type == "image_generation_call"
    ]
    filename = f"frame_{i}.png"        
    if image_data:
        image_base64 = image_data[0]
        with open(filename, "wb") as f:
            f.write(base64.b64decode(image_base64))

    imagenes.append(filename)

# =========================
# CREAR VIDEO
# =========================

print("\n2. Creando los clips")
clips = []

for img_path in imagenes:
    print(f"{img_path}...")
    clip = ImageClip(img_path).with_duration(duracion_por_imagen)
    clips.append(clip)

print("\n3. Concatenando clips")
video = concatenate_videoclips(clips, method="compose")

print("\n4. Guardando video")
video.write_videofile(
    "video_openai.mp4",
    fps=24
)

print("Video generado!")