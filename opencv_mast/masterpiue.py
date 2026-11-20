import cv2
import os

# ==========================================
# 1. 设置你的参数
# ==========================================
video_path = 'ms.mp4'  # 🚨 你的视频文件名，记得把视频放在同一个文件夹下
output_folder = 'images_raw'  # 提取出来的图片放这个文件夹里
frame_interval = 10  # 🚨 抽帧间隔：每隔 10 帧取一张图（避免图片太多）

# 如果文件夹不存在，就自动创建一个
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ==========================================
# 2. 读取视频并开始抽帧
# ==========================================
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ 打不开视频，请检查视频名字或路径是否正确！")
    exit()

# 获取视频的总帧率和总帧数（用来显示进度）
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"🎥 视频总帧数: {total_frames}, 帧率: {fps} FPS")

count = 0  # 记录当前读到第几帧
saved_count = 0  # 记录存了多少张图片

print("开始抽帧... 按 'q' 键可以强制停止。")

while True:
    ret, frame = cap.read()

    # 视频读完了，退出循环
    if not ret:
        break

    # 判断当前帧数是否能被间隔数整除
    if count % frame_interval == 0:
        # 拼接图片名字，比如 frame_0000.jpg, frame_0010.jpg
        img_name = os.path.join(output_folder, f"frame_{count:04d}.jpg")

        # 保存图片
        cv2.imwrite(img_name, frame)
        saved_count += 1

        # 顺便在屏幕上显示一下（可以注释掉，免得闪屏）
        cv2.imshow("Extracting...", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    count += 1

    # 打印一下进度
    if count % 100 == 0:
        print(f"已处理 {count}/{total_frames} 帧，保存了 {saved_count} 张图片...")

# ==========================================
# 3. 释放资源
# ==========================================
cap.release()
cv2.destroyAllWindows()
print(f"✅ 抽帧完成！总共保存了 {saved_count} 张图片，存放在 {output_folder} 文件夹中。")
