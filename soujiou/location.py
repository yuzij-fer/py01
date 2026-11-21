


# ════════════════════════════════默认参数══════════════ ══════════════════

REAL_H = 0.05        # 框中"高度"对应的真实尺寸（米）——魔方边长 5cm
FY = 786.09          # Y 轴焦距（像素），配"用高度算距离"
FX = 945.15          # X 轴焦距（像素），配"用宽度算距离"

# 框高下限。含义是「允许的最大相对误差」：1/min_pixel_h = 误差上限
#   10  → 接受 10% 误差 → 有效量程约 3.9 米（= REAL_H*FY/10）
#   20  → 接受  5% 误差 → 有效量程约 2.0 米

MIN_PIXEL_H = 10



class Get_distance:

    def __init__(self, real_h=REAL_H, fx=FX, fy=FY, min_pixel_h=MIN_PIXEL_H):
        self.real_h = real_h
        self.fx = fx
        self.fy = fy
        self.min_pixel_h = min_pixel_h

    # ── 单步：框高 → 距离（米） ──────────────────────────
    def distance(self, pixel_h):

        if pixel_h <= 0:                 #除零会崩，永远不能放宽
            return None
        if pixel_h < self.min_pixel_h:   #误差超过容忍度，数据没意义
            return None
        return self.real_h * self.fy / pixel_h

    # ── 单步：像素中心 → 相对正下方的偏移（米） ─────────────
    def offset(self, center_x, center_y, z, img_w, img_h):

        dx = (center_x - img_w / 2.0) * z / self.fx
        dy = (center_y - img_h / 2.0) * z / self.fy
        return dx, dy

    # ── 组合：一个框 → 完整位置 ─────────────────────────
    def locate(self, box, img_w, img_h):

        x1, y1, x2, y2 = box
        pixel_h = y2 - y1

        z = self.distance(pixel_h)
        if z is None:
            return None

        center_x = (x1 + x2) / 2.0
        center_y = (y1 + y2) / 2.0
        dx, dy = self.offset(center_x, center_y, z, img_w, img_h)

        return {
            "z": z,
            "dx": dx,
            "dy": dy,
            "center_x": center_x,
            "center_y": center_y,
            "pixel_h": pixel_h,
        }


