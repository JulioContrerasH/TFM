import matplotlib.pyplot as plt
import pathlib
from PIL import Image

# Ruta de la imagen
img_path = pathlib.Path("images/news/SR_allen.png")

# Leer la imagen usando Pillow
img = Image.open(img_path)
plt.figure(figsize=(10, 10))
# Mostrar la imagen con matplotlib
plt.imshow(img)
plt.axis('off')  # Opcional: Quita los ejes para que no se vean
plt.savefig("images/news/SR.png", bbox_inches="tight", pad_inches=0)


