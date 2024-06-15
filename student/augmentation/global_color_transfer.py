import albumentations
import cv2


global_color_transfer = albumentations.ColorJitter(brightness=(.5,2), contrast=(.5,3), saturation=(0,4), always_apply=True, p=0.9)


def augment(image, augmentations=[global_color_transfer]):
    transform_func = albumentations.Compose(augmentations)
    return transform_func(image)['image']


if __name__ == '__main__':
    image = cv2.imread('./test_input.jpg')
    augmented_image = augment(image, [global_color_transfer])
    cv2.imwrite('./result.jpg', augmented_image)
