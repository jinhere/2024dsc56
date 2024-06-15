from ultralytics import YOLO

# model = YOLO('yolov8m.pt')
# # model = YOLO('sl_config.yaml')
# model.train(data='./sl_config.yaml', epochs=1)
# result = model.predict("../../sample_for_testing_ssl/train/images/20240518031454994.jpg", save=True, conf=0.1)
# print(result[0].boxes)
# # torch.save(model.state_dict(), 'sl.pt')



def predict():
    model = YOLO(model='../best.pt')
    results = model.predict( source='../../test/images', save=True)


def val():
    model = YOLO(model='../best.pt')
    metrics = model.val()


if __name__ == '__main__':
    predict()
    # val()
