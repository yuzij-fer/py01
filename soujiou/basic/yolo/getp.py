import cv2
import os

video_path ='test.mp4' #视频文件
output_folder = 'images_raw' #保存的文件夹
frame_interval = 10  #间隔帧数

if not os.path.exists(output_folder):
    os.makedirs(output_folder) #创建文件夹

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ 打不开视频，请检查视频名字或路径是否正确！")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"🎥 视频总帧数: {total_frames}, 帧率: {fps} FPS")

count = 0  #当前帧数
saved_count = 0 #图片数目

print("开始抽帧... 按 'q' 键可以强制停止。")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if count % frame_interval == 0:#保存图片
        img_name = os.path.join(output_folder, f"frame_{count:04d}.jpg")

        cv2.imwrite(img_name, frame)
        saved_count += 1

        cv2.imshow("Extracting...", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    count += 1

    if count % 100 == 0:
        print(f"已处理 {count}/{total_frames} 帧，保存了 {saved_count} 张图片...")

cap.release()
cv2.destroyAllWindows()
print(f"✅ 抽帧完成！总共保存了 {saved_count} 张图片，存放在 {output_folder} 文件夹中。")
