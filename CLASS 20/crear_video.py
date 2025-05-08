from moviepy import ImageSequenceClip, AudioFileClip, CompositeVideoClip

# Paso 1: Cargar imágenes (ordenadas)
imagenes = [
    "imagenes/imagen1.png",
    "imagenes/imagen2.png",
    "imagenes/imagen3.png",
    "imagenes/imagen4.png",
    # Agrega más si tienes
]

# Paso 2: Crear clip de video con duración total de 5 segundos
clip = ImageSequenceClip(imagenes, durations=[5 / len(imagenes)] * len(imagenes))

# Paso 3: Cargar audio de fondo (debe durar al menos 5 segundos)
audio = AudioFileClip("musica/fondo.m4a").subclipped(0, 5)

# Paso 4: Combinar video con audio
video_final = clip.with_audio(audio)

# Paso 5: Exportar el video
video_final.write_videofile("video_final.mp4", fps=24)
