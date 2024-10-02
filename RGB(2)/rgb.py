import numpy as np
import imageio.v3 as img

image_path = "C:\gambar\daun kenikir.jpg"
image = img.imread(image_path)

if len(image.shape) < 3 or image.shape[2] != 3:
    print("Format Gambar Harus RGB")
    exit()

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

image_red = np.zeros_like(image)
image_red[:,:,0] = red

image_green = np.zeros_like(image)
image_green[:,:,1] = green

image_blue = np.zeros_like(image)
image_blue[:,:,2] = blue

gray = 0.2 * red + 0.5 * green + 0.3 * blue
image_gray = np.zeros_like(image)
image_gray[:,:,0] = gray
image_gray[:,:,1] = gray
image_gray[:,:,2] = gray

threshold = 100
image_bw = np.zeros_like(image)

for i in range(0, len(gray)):
    for j in range(0, len(gray[i])):
        if (gray[i,j] > threshold):
            image_bw[i,j] = 255
        else:
            image_bw[i,j] = 0


image = img.imwrite("image_red.jpg", image_red)
image = img.imwrite("image_green.jpg", image_green)
image = img.imwrite("image_blue.jpg", image_blue)
image = img.imwrite("image_gray.jpg", image_gray)
image = img.imwrite("image_bw.jpg", image_bw)

print("Proses Berhasil")