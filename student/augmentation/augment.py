import albumentations
import cv2
from os import listdir
from os.path import isfile, join

global_color_transfer = albumentations.ColorJitter(brightness=(.5,2), contrast=(.5,3), saturation=(0,4), always_apply=True, p=0.9)
cutout = albumentations.CoarseDropout(always_apply=True, p=1.0, max_holes=60, min_holes=40, max_height=30, max_width=30, min_height=20, min_width=20, fill_value=(127,127,127))
noise = albumentations.GaussNoise(var_limit=(5000,5000), always_apply=True, p=1.0)

default_augmentations = [noise]


def _augment_one_file(image, augmentations):
    transform_func = albumentations.Compose(augmentations)
    return transform_func(image=image)['image']

def augment_and_save_all(srcPath, destPath):
    filenames = [f for f in listdir(srcPath) if isfile(join(srcPath, f))]
    print(f'{len(filenames)} files. proceed?')
    input()
    print('augmenting...')
    count = 0
    total = len(filenames)
    for filename in filenames:
        filepath = join(srcPath, filename)
        image = cv2.imread(filepath)
        augmented_image = _augment_one_file(image, default_augmentations)
        cv2.imwrite(f'{join(destPath, filename)}', augmented_image)
        if count % 1000 == 0:
            print(f'{count}/{total} {count/total*100:.2f}%')
        count += 1


print('start')
augment_and_save_all('../../June5th/pseudolabeled/nonaugmented/train/images', '../../June5th/pseudolabeled/augmented_noise/train/images')
print('done')

