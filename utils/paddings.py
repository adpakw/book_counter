from typing import Literal

import cv2


def add_padding(
    image,
    padding_percent: int = 10,
    padding_type: Literal["reflective", "replicate", "constant"] = "reflective",
):
    """
    Добавляет паддинг к изображению с выбором типа.

    Args:
        image: входное изображение (numpy array)
        padding_percent: Размер паддинга равный проценту от размера изображения
        padding_type: тип паддинга:
            - "reflective": зеркальное отражение краев
            - "replicate": повторение крайних пикселей
            - "constant": заполнение постоянным цветом

    Returns:
        изображение с паддингом
    """
    height, width = image.shape[:2]
    pad_w = int(width * padding_percent / 100)
    pad_h = int(height * padding_percent / 100)

    if padding_type == "reflective":
        return cv2.copyMakeBorder(
            image,
            top=pad_h,
            bottom=pad_h,
            left=pad_w,
            right=pad_w,
            borderType=cv2.BORDER_REFLECT_101,
        )

    elif padding_type == "replicate":
        return cv2.copyMakeBorder(
            image,
            top=pad_h,
            bottom=pad_h,
            left=pad_w,
            right=pad_w,
            borderType=cv2.BORDER_REPLICATE,
        )

    elif padding_type == "constant":
        return cv2.copyMakeBorder(
            image,
            top=pad_h,
            bottom=pad_h,
            left=pad_w,
            right=pad_w,
            borderType=cv2.BORDER_CONSTANT,
            value=(0, 0, 0),
        )

    return image
