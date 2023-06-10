from PIL import Image, ImageDraw
from math import floor

# Input file path
INPUT_FILE = "image.jpg"

# Output file path
OUTPUT_FILE = "newImage.png"

# Space between the painted dots (in pixels)
SPACE_BETWEEN_DOTS = 30
# Border size (in pixels)
BORDER_SIZE = 100
# Input image grid cell surface to dot ratio
PIXEL_DOT_RATIO = 30
# Output image rescale (keep int)
IMAGE_SIZE_MODIFIER = 4


initialImage = Image.open(INPUT_FILE)
initialSizeX, initialSizeY = initialImage.size

numberDotsX = floor(initialSizeX / PIXEL_DOT_RATIO)
numberDotsY = floor(initialSizeY / PIXEL_DOT_RATIO)

newSizeX = 2 * BORDER_SIZE + IMAGE_SIZE_MODIFIER * numberDotsX * PIXEL_DOT_RATIO + (numberDotsX - 1) * SPACE_BETWEEN_DOTS
newSizeY = 2 * BORDER_SIZE + IMAGE_SIZE_MODIFIER * numberDotsY * PIXEL_DOT_RATIO + (numberDotsY - 1) * SPACE_BETWEEN_DOTS
newSize = newSizeX, newSizeY

newImage = Image.new("RGB", newSize, "black")
draw = ImageDraw.Draw(newImage)

offsetX = BORDER_SIZE
for i in range(0, numberDotsX):
    offsetY = BORDER_SIZE
    for j in range(0, numberDotsY):
        startX = (offsetX + i * PIXEL_DOT_RATIO * IMAGE_SIZE_MODIFIER)
        startY = (offsetY + j * PIXEL_DOT_RATIO * IMAGE_SIZE_MODIFIER)
        endX = (startX + PIXEL_DOT_RATIO * IMAGE_SIZE_MODIFIER)
        endY = (startY + PIXEL_DOT_RATIO * IMAGE_SIZE_MODIFIER)

        colorCoords = i * PIXEL_DOT_RATIO + PIXEL_DOT_RATIO / 2, j * PIXEL_DOT_RATIO + PIXEL_DOT_RATIO / 2
        color = initialImage.getpixel(colorCoords)

        elipseCoords = startX, startY, endX, endY
        draw.ellipse(elipseCoords, color)

        offsetY += SPACE_BETWEEN_DOTS

    offsetX += SPACE_BETWEEN_DOTS

newImage.save(OUTPUT_FILE)