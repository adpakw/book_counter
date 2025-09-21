import os

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image


def plot_res_images_slice(
    images_folder: str, start: int = 0, end: int = 10, max_cols: int = 10
):
    image_files = [
        f for f in os.listdir(images_folder) if f.endswith((".jpg", ".jpeg", ".png"))
    ]

    image_files.sort(key=lambda x: int(x.split(".")[0].split("_")[0]))

    image_files = image_files[start:end]
    n = len(image_files)

    if n == 0:
        print("Нет изображений в указанном диапазоне")
        return

    cols = min(max_cols, n)
    rows = (n + cols - 1) // cols

    fig_width = min(20, cols * 3)
    fig_height = rows * 3

    fig, axes = plt.subplots(rows, cols, figsize=(fig_width, fig_height))

    if rows == 1 and cols == 1:
        axes = [[axes]]
    elif rows == 1:
        axes = axes.reshape(1, -1)
    elif cols == 1:
        axes = axes.reshape(-1, 1)

    for i in range(rows):
        for j in range(cols):
            index = i * cols + j
            if index < n:
                img_path = os.path.join(images_folder, image_files[index])

                with Image.open(img_path) as img:
                    width, height = img.size

                img_display = mpimg.imread(img_path)

                axes[i, j].imshow(img_display)
                axes[i, j].set_title(f"{image_files[index]}", fontsize=8, pad=2)
                axes[i, j].axis("off")
            else:
                axes[i, j].axis("off")

    plt.subplots_adjust(
        wspace=0.02, hspace=0.04, left=0.03, right=0.97, bottom=0.04, top=0.99
    )
    plt.show()


def plot_two_images_side_by_side(
    image_path1: str,
    image_path2: str,
    title1: str = "Image 1",
    title2: str = "Image 2",
):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    if os.path.exists(image_path1):
        img1 = mpimg.imread(image_path1)
        ax1.imshow(img1)
        ax1.set_title(title1, fontsize=14, pad=10)
        ax1.axis("off")
    else:
        ax1.text(
            0.5,
            0.5,
            f"Image not found:\n{image_path1}",
            ha="center",
            va="center",
            transform=ax1.transAxes,
        )
        ax1.set_title("Error", fontsize=14, pad=10)
        ax1.axis("off")

    if os.path.exists(image_path2):
        img2 = mpimg.imread(image_path2)
        ax2.imshow(img2)
        ax2.set_title(title2, fontsize=14, pad=10)
        ax2.axis("off")
    else:
        ax2.text(
            0.5,
            0.5,
            f"Image not found:\n{image_path2}",
            ha="center",
            va="center",
            transform=ax2.transAxes,
        )
        ax2.set_title("Error", fontsize=14, pad=10)
        ax2.axis("off")

    plt.subplots_adjust(wspace=0.1)

    plt.show()
