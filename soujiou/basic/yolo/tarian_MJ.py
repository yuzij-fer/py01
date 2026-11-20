from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8n.pt')
    model.train(
        data='data.yaml',
        epochs=50,#训练次数
        imgsz=960,#图片训练尺寸
        batch=8,#每次多少图片
        device='cpu',#用GPU
        name='MJ_train' ,)
