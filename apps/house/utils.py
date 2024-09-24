from PIL import Image
import io
from django.core.files.base import ContentFile

def add_watermark(self, image_file):
    watermark_path = 'House.kg/core/base_media/logo.png'

    base_image = Image.open(image_file).convert("RGBA")
    watermark = Image.open(watermark_path).convert("RGBA")
    watermark = watermark.resize((50, 50))

    position = (base_image.width - watermark.width, base_image.height - watermark.height)

    base_image.paste(watermark, position, watermark)

    image_io = io.BytesIO()
    base_image.save(image_io, format='PNG')
    return ContentFile(image_io.getvalue(), name=image_file.name)