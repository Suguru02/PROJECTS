import cv2 as cv
from matplotlib import pyplot as plt
import os

def load_image(filename):
    """Загрузка и проверка цветного изображения"""
    if not os.path.exists(filename):
        print(f"Ошибка: Файл '{filename}' не найден!")
        return None
    
    # Загружаем цветное изображение 
    img = cv.imread(filename, cv.IMREAD_COLOR)
    
    if img is None:
        print(f"Ошибка: Не удалось загрузить изображение '{filename}'!")
        print("Проверьте, что файл является корректным изображением.")
        return None
    
    # Конвертируем из BGR в RGB
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return img_rgb

def rotate_image(img, angle):
    """Поворот изображения на заданный угол"""
    rows, cols = img.shape[:2]
    size = 1
    return cv.warpAffine(img, cv.getRotationMatrix2D((cols/2, rows/2), angle, size), (cols, rows))

def flip_image(img):
    """Отражение изображения по горизонтали и вертикали"""
    flip_horizontal = cv.flip(img, 1) # 1 - по горизонтали
    flip_vertical = cv.flip(img, 0)   # 0 - по вертикали
    return flip_horizontal, flip_vertical

def create_rotations(img):
    """Создание повернутых версий изображения"""
    return {
        'rotation30': rotate_image(img, 30),
        'rotation60': rotate_image(img, 60),
        'rotation90': rotate_image(img, 90)
    }

def display_images(original, rotations, flips):
    """Отображение всех изображений в сетке"""
    plt.figure(figsize=(12, 8))

    # Original image
    plt.subplot(231)
    plt.imshow(original)
    plt.title('Original Image')
    plt.xticks([])
    plt.yticks([])

    # Rotated images
    plt.subplot(232)
    plt.imshow(rotations['rotation30'])
    plt.title('Rotation 30')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(233)
    plt.imshow(rotations['rotation60'])
    plt.title('Rotation 60')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(234)
    plt.imshow(rotations['rotation90'])
    plt.title('Rotation 90')
    plt.xticks([])
    plt.yticks([])

    # Flipped images
    plt.subplot(235)
    plt.imshow(flips[0])
    plt.title('Horizontal Flip')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(236)
    plt.imshow(flips[1])
    plt.title('Vertical Flip')
    plt.xticks([])
    plt.yticks([])

    plt.tight_layout()
    plt.show()

def save_images(images, base_filename):
    """Сохранение всех цветных изображений в папку output"""
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for image_name, image_data in images.items():
        filename = f'{output_dir}/{base_filename}_{image_name}.jpg'
        # Конвертируем обратно из RGB в BGR для сохранения через OpenCV
        image_bgr = cv.cvtColor(image_data, cv.COLOR_RGB2BGR)
        cv.imwrite(filename, image_bgr)

def main():
    """Основная функция: чтение и запись файлов"""
    # Чтение файла
    filename = input("Введите имя файла изображения (например, image.jpg): ").strip()
    img = load_image(filename)
    
    if img is None:
        return
        
    # Создание преобразованных изображений
    rotations = create_rotations(img)
    flip_horizontal, flip_vertical = flip_image(img)
    
    # Отображение
    display_images(img, rotations, (flip_horizontal, flip_vertical))
    
    # Подготовка данных для сохранения
    all_images = {
        'original': img,
        'rotation30': rotations['rotation30'],
        'rotation60': rotations['rotation60'],
        'rotation90': rotations['rotation90'],
        'flip_horizontal': flip_horizontal,
        'flip_vertical': flip_vertical
    }
    
    # Запись файлов
    name = os.path.splitext(os.path.basename(filename))[0]
    save_images(all_images, name)
    
if __name__ == "__main__":
    main()
