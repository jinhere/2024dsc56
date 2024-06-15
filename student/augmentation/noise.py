import albumentations
import cv2


noise = albumentations.GaussNoise(var_limit=(5000,5000), always_apply=True, p=1.0)


def augment(image, augmentations=[noise]):
    transform_func = albumentations.Compose(augmentations)
    return transform_func(image=image)['image']


if __name__ == '__main__':
    image = cv2.imread('./test_input.jpg')
    augmented_image = augment(image=image, augmentations=[noise])
    cv2.imwrite('./result.jpg', augmented_image)
