from ultralytics import YOLO


def train():
    model = YOLO(model='../../June5th/best.pt')
    results = model.train(data='./ssl_config.yaml', epochs=300)

def val():
    model = YOLO(model='./runs/detect/train/weights/best.pt')
    metrics = model.val()


def predict():
    model = YOLO(model='./runs/detect/train_90_cutout/weights/best.pt')
    results = model.predict(source='../../test/images', save=True, show=True)


# train()
# val()
predict()

