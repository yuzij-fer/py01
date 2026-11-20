

import cv2
import numpy as np



# cap=cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
# cap.set(cv2.CAP_PROP_FPS,30)
# cap.set(cv2.CAP_PROP_BRIGHTNESS,100)
# while True:
#     ret,img=cap.read()
#     if not ret:
#         break
#     cv2.imshow('img', img)
#
#     if cv2.waitKey(1)& 0xFF==ord('q'):
#         break
# kernel=np.ones((5,5),np.uint8)
# img=cv2.imread('xs.png')
# img_Gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# new_img_Gray = cv2.resize(img_Gray,(640,480))
# cv2.imshow('Grayimg',new_img_Gray)
# cv2.waitKey(0)
# img_blur = cv2.GaussianBlur(new_img_Gray,(5,5),0)
# img_canny = cv2.Canny(img_blur,100,100)
# img_dilated = cv2.dilate(img_canny,kernel,iterations = 3)
# img_eroded = cv2.erode(img_dilated,kernel,iterations = 3)
#
#
# img=np.zeros((300,300,3),np.uint8)
# print(img)
# img[:]=255,0,0
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),5)
# cv2.rectangle(img,(0,0),(150,100),(0,255,0),cv2.FILLED)
# cv2.circle(img,(150,100),50,(255,255,0),5)
# cv2.putText(img,'CVOPEN',(80,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# ps1=np.float32([[0,0],[100,0],[0,100],[100,100]])
# ps2=np.float32([[0,0],[300,0],[0,300],[300,300]])
# matrix=cv2.getPerspectiveTransform(ps1,ps2)
# imgput=cv2.warpPerspective(img,matrix,(300,300))
# cv2.imshow('imgput',imgput)
# cv2.waitKey(0)
# img_cropped=img[0:300,200:300]
# cv2.imshow('img_cropped',img_cropped)
# cv2.waitKey(0)
# img2 = cv2.imread('xs.png')
# img1 = cv2.resize(img2, (800, 600))
# hsv_img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
# a=np.hstack((hsv_img,img1))
# b=np.vstack((hsv_img,img1))
# def empty(a):
#     pass
# cv2.namedWindow('image')
# cv2.resizeWindow('image', 600, 300)
# cv2.createTrackbar('Hue_min', 'image', 0, 180, empty)
# cv2.createTrackbar('Hue_max', 'image', 180, 180, empty)
# cv2.createTrackbar('Sat_min', 'image', 0, 255, empty)
# cv2.createTrackbar('Sat_max', 'image', 255, 255, empty)
# cv2.createTrackbar('Val_min', 'image', 0, 255, empty)
# cv2.createTrackbar('Val_max', 'image', 255, 255, empty)
# while True:
#     h1=cv2.getTrackbarPos('Hue_min', 'image')
#     h2=cv2.getTrackbarPos('Hue_max', 'image')
#     s1=cv2.getTrackbarPos('Sat_min', 'image')
#     s2=cv2.getTrackbarPos('Sat_max', 'image')
#     v1=cv2.getTrackbarPos('Val_min', 'image')
#     v2=cv2.getTrackbarPos('Val_max', 'image')
#     lower = np.array([h1, s1, v1])
#     upper = np.array([h2,s2, v2])
#     mask = cv2.inRange(hsv_img, lower, upper)
#     result=cv2.bitwise_and(img1,img1,mask=mask)
#     cv2.imshow('image_hsv',hsv_img)
#     cv2.imshow('result',result)
#     cv2.imshow("mask",mask)
#     cv2.waitKey(1)
# def getContours(img):
#     contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 500:
#             cv2.drawContours(img_new, cnt, -1, (255, 0, 0), 3)
#             peri = cv2.arcLength(cnt,True)
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)
#             objCor=(len(approx))
#             x,y,w,h = cv2.boundingRect(approx)
#             X=(x+w)/2
#             Y=(y+h)/2
#             test=f"{X},{Y}"
#
#             cv2.rectangle(img_new,(x,y),(x+w,y+h),(0,255,0),3)
#             cv2.putText(img_new,test,(x+(w//2)-30,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),1)
#
#
#
#
#
# img_=cv2.imread('ps.jpg')
# img=cv2.resize(img_,(500,500))
# img_new=img.copy()
# img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img_blur=cv2.GaussianBlur(img_gray,(7,7),1)
# img_canny=cv2.Canny(img_blur,100,100)
# getContours(img_canny)
# cv2.imshow('img1',img_canny)
# cv2.imshow('img_new',img_new)
# cv2.waitKey(0)


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