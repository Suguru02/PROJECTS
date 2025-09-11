import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

def main():

    # Получаем имя файла
    filename = input("Введите имя файла изображения (например, image.jpg): ").strip()
    
    # Проверяем есть ли такой файл
    if not os.path.exists(filename):
        print(f"Ошибка: Файл '{filename}' не найден!")
        return


    img = cv.imread(filename, 0) # загружаем картинку

    # Проверяем загрузилось ли изображение
    if img is None:
        print(f"Ошибка: Не удалось загрузить изображение '{filename}'!")
        print("Проверьте, что файл является корректным изображением.")
        return


    rows, cols = img.shape
    # Поворачиваем на 30 60 90
    M = np.float32([[1,  0, 0], [0, -1, rows], [0,  0, 1]])
    img_rotation30 = cv.warpAffine(img, cv.getRotationMatrix2D((cols/2, rows/2), 30, 1), (cols, rows))
    img_rotation60 = cv.warpAffine(img, cv.getRotationMatrix2D((cols/2, rows/2), 60, 1), (cols, rows))
    img_rotation90 = cv.warpAffine(img, cv.getRotationMatrix2D((cols/2, rows/2), 90, 1), (cols, rows))

    # Отражаем по горизонтали и вертикали
    img_flip_gor = cv.flip(img, 1)
    img_flip_vert = cv.flip(img, 0)

    # Делаем сетку и помещаем туда оригинал и повернутые изображения
    plt.figure(figsize=(12, 8))

    plt.subplot(231)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(232)
    plt.imshow(img_rotation30, cmap='gray')
    plt.title('Rotation30 Image')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(233)
    plt.imshow(img_rotation60, cmap='gray')
    plt.title('Rotation60 Image')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(234)
    plt.imshow(img_rotation90, cmap='gray')
    plt.title('Rotation90 Image')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(235)
    plt.imshow(img_flip_gor, cmap='gray')
    plt.title('Flip_gorizontal Image')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(236)
    plt.imshow(img_flip_vert, cmap='gray')
    plt.title('Flip_vertikal Image')
    plt.xticks([])
    plt.yticks([])

    plt.tight_layout()
    plt.show()
    
    # Создаем папку для выходных файлов, если её нет
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Сохраняем преобразованные изображения
    base_name = os.path.splitext(os.path.basename(filename))[0]
    
    cv.imwrite(f'{output_dir}/{base_name}_rotation30.jpg', img_rotation30)
    cv.imwrite(f'{output_dir}/{base_name}_rotation60.jpg', img_rotation60)
    cv.imwrite(f'{output_dir}/{base_name}_rotation90.jpg', img_rotation90)
    cv.imwrite(f'{output_dir}/{base_name}_flip_horizontal.jpg', img_flip_gor)
    cv.imwrite(f'{output_dir}/{base_name}_flip_vertical.jpg', img_flip_vert)

if __name__ == "__main__":
    main()
