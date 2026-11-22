# 全局配置 —— 所有"标定出来的数"只在这里出现一次
# ══════════════════════════════════════════════════════════════════
import numpy as np


# ── 1. 相机采集 ────────────────────────────────────────────────
WIDTH = 640
HEIGHT = 480
FPS = 30
CAP_ID = 0


# ── 2. 相机内参 ────────────────────────────────────────────────
# 标定出来的原始数字，全工程只出现这一次。换相机就只改这五行。
_FX = 945.15025581
_FY = 786.09360996
_CX = 431.22090007
_CY = 261.05788457
_DIST = (-1.36251624, 6.68606376, 0.0873288483, -0.00284729744, -9.19749936)


class Intrinsics:
    """一组内参 + 它所属的分辨率，打包成一个对象。
    约定：对象建好之后不要再改它的属性。改了 fx，已经算好的 matrix
    不会跟着变 —— 要换内参就新建一个 Intrinsics。
    """

    def __init__(self, width, height, fx, fy, cx, cy, dist):
        self.width = width        # 多宽的画面
        self.height = height      # 多高的画面
        self.fx = fx              # X 方向焦距（像素），配"用宽度算距离"
        self.fy = fy              # Y 方向焦距（像素），配"用高度算距离"
        self.cx = cx              # 光心 x（像素），画面中心附近
        self.cy = cy              # 光心 y（像素）
        self.dist = dist          # 畸变系数 (k1, k2, p1, p2, k3)

        # 下面两个是从上面几个数算出来的，建对象时算一次就存住。。
        self.matrix = np.array([[fx, 0.0, cx],
                                [0.0, fy, cy],
                                [0.0, 0.0, 1.0]], dtype=np.float32)
        self.dist_coeffs = np.array([dist], dtype=np.float32)

    def scaled_to(self, width, height):
        """同一台相机换到另一个分辨率时，把内参按比例换算过去。
        """
        sx = width / self.width
        sy = height / self.height
        return Intrinsics(width=width, height=height,
                          fx=self.fx * sx, fy=self.fy * sy,
                          cx=self.cx * sx, cy=self.cy * sy,
                          dist=self.dist)

    def problems(self):
        """自检：内参和分辨率对不上就返回问题描述，全对返回空列表。

        不抛异常、不打印 —— 只把矛盾摆出来，由 main 决定怎么提示。
        写成"返回列表"而不是"直接 print"，是为了它能被单独测试：
            import config; config.CAMERA.problems()
        """
        out = []

        if self.fx <= 0 or self.fy <= 0:
            out.append(f"fx={self.fx} / fy={self.fy} 必须为正数")

        # 光心理论上就在画面正中间。偏太多说明内参不是这个分辨率下标的
        if abs(self.cx - self.width / 2) > self.width * 0.05:
            out.append(
                f"cx={self.cx:.1f} 偏离 {self.width} 宽的画面中心 "
                f"{self.width / 2:.0f} 约 {abs(self.cx - self.width / 2):.0f} 像素，"
                f"这组内参可能是在别的分辨率下标定的 -> dx/dy 会整体偏移")

        if abs(self.cy - self.height / 2) > self.height * 0.05:
            out.append(
                f"cy={self.cy:.1f} 偏离 {self.height} 高的画面中心 "
                f"{self.height / 2:.0f} 约 {abs(self.cy - self.height / 2):.0f} 像素")

        return out


# 当前正在用的一组。width/height 的语义是"这组数属于哪个分辨率"：
# 填 640 就是声称它属于 640，所以启动自检会拿 320 去比 cx —— 警告由此而来。
CAMERA = Intrinsics(width=WIDTH, height=HEIGHT,
                    fx=_FX, fy=_FY, cx=_CX, cy=_CY, dist=_DIST)


# ── 3. 目标物 ──────────────────────────────────────────────────
TARGET_REAL_H = 0.05    # 框中"高度"对应的真实尺寸（米）；魔方边长 5cm
MIN_PIXEL_H = 10        # 框高下限 = 允许的最大相对误差（1/10 → 10%）


# ── 4. 串口 ────────────────────────────────────────────────────
SERIAL_PORT = 'COM3'
SERIAL_BAUD = 115200


# ── 5. 通信协议 ────────────────────────────────────────────────
FRAME_HEAD = b'\xAA'
FRAME_TAIL = b'\x55'
