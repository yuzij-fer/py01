import cv2
import numpy as np

chessboard_size = (7, 7)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

objpoints = []
imgpoints = []

# ==========================================
# 2. 打开摄像头，实时抓拍
# ==========================================
cap = cv2.VideoCapture(0)
print("📷 摄像头已启动！")
print("👉 请把打印好的棋盘格放在镜头前。")
print("👉 当屏幕上出现【彩色连线】时，按键盘上的 's' 键抓拍一张。")
print("👉 请变换至少 10-15 个不同的角度、距离，多按几次 's'。")
print("👉 拍够之后，按 'q' 键退出并开始计算。")

w=int(cap.get(3))
h=int(cap.get(4))
print(w, h)


count = 0  # 记录抓拍的张数

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 实时寻找角点
    ret_corners, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    # 显示画面
    display_frame = frame.copy()

    if ret_corners:
        # 如果找到了，画出彩色的角点
        cv2.drawChessboardCorners(display_frame, chessboard_size, corners, ret_corners)
        cv2.putText(display_frame, "FOUND! Press 'S' to save", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.putText(display_frame, f"Saved: {count}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Calibration - Press S to Save, Q to Quit", display_frame)

    key = cv2.waitKey(1) & 0xFF

    # 按 s 键抓拍
    if key == ord('s') and ret_corners:
        # 精细化角点
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        objpoints.append(objp)
        imgpoints.append(corners2)
        count += 1
        print(f"✅ 抓拍成功！目前已保存 {count} 张。")
        # 保存图片到本地（方便以后备查）
        cv2.imwrite(f"calib_{count}.jpg", frame)
        # 闪一下白屏作为拍照提示
        cv2.rectangle(display_frame, (0, 0), (display_frame.shape[1], display_frame.shape[0]), (255, 255, 255), -1)
        cv2.imshow("Calibration - Press S to Save, Q to Quit", display_frame)
        cv2.waitKey(100)

    # 按 q 键退出
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# ==========================================
# 3. 开始计算标定参数
# ==========================================
if count >= 5:
    print(f"\n正在用 {count} 张照片计算参数，请稍候...")
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    print("\n" + "=" * 40)
    print("🎉 标定成功！")
    print("=== 相机内参矩阵 (mtx) ===")
    print(mtx)
    print("\n=== 畸变系数 (dist) ===")
    print(dist)
    print("=" * 40)
    print("⚠️ 请把上面这两串数字抄下来，写进你的视觉主程序里！")
else:
    print("\n❌ 抓拍数量太少（不到 5 张），无法计算！请重新运行。")