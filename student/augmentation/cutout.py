import albumentations
import cv2


cutout = albumentations.CoarseDropout(always_apply=True, p=1.0, max_holes=60, min_holes=40, max_height=30, max_width=30, min_height=20, min_width=20, fill_value=(127,127,127))


def augment(image, augmentations=[cutout]):
    transform_func = albumentations.Compose(augmentations)
    return transform_func(image=image)['image']


if __name__ == '__main__':
    image = cv2.imread('./test_input.jpg')
    augmented_image = augment(image=image, augmentations=[cutout])
    cv2.imwrite('./result.jpg', augmented_image)
