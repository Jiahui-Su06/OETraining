import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from sklearn.cluster import DBSCAN
# from mpl_toolkits.mplot3d import Axes3D

# --------- 参数设置 ---------
wavelength = 632.8e-9      # 波长（单位：米）
pixel_size = 5.2e-6        # 像元尺寸（单位：米）
z_start = 0.000            # z扫描起点（单位：米）
z_end = 0.160               # z扫描终点（单位：米）
z_step = 0.0002            # z步进（单位：米）
filename = 'images/test1.png'         # 全息图文件名

# --------- 读取全息图像 ---------
hologram = np.array(Image.open(filename).convert('L'), dtype=np.float32)
hologram = (hologram - hologram.min()) / (hologram.max() - hologram.min())

# --------- 显示原始全息图 ---------
plt.figure(figsize=(6, 6))
plt.title("原始全息图")
plt.imshow(hologram, cmap='gray')
plt.axis('off')
plt.show()

N, M = hologram.shape
fx = np.fft.fftfreq(M, d=pixel_size)
fy = np.fft.fftfreq(N, d=pixel_size)
FX, FY = np.meshgrid(fx, fy)

# --------- z-stack重建与圆检测 ---------
z_list = np.arange(z_start, z_end + z_step, z_step)
bubble_candidates = []

for zi in z_list:
    H = np.exp(1j * 2 * np.pi * zi / wavelength) * np.exp(-1j * np.pi * wavelength * zi * (FX**2 + FY**2))
    U1 = np.fft.ifft2(np.fft.fft2(hologram) * H)
    intensity = np.abs(U1)**2

    # --------- 降噪处理 ---------
    norm_img = cv2.normalize(intensity, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    background = cv2.medianBlur(norm_img, 51)
    norm_img2 = cv2.subtract(norm_img, background)
    blur = cv2.GaussianBlur(norm_img2, (7, 7), 0)
    kernel = np.ones((3,3), np.uint8)
    opened = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)
    edges = cv2.Canny(opened, 80, 200)

    # --------- 圆检测（气泡半径0.1-0.6mm，像素约15-92） ---------
    h, w = edges.shape
    circles = cv2.HoughCircles(
        edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20,
        param1=50, param2=15, minRadius=15, maxRadius=92
    )
    if circles is not None:
        for c in circles[0]:
            x, y, r = c
            if 0 <= int(y) < h and 0 <= int(x) < w:
                score = edges[int(y), int(x)]
            else:
                score = 0
            bubble_candidates.append({'x': x, 'y': y, 'z': zi*1e3, 'r': r, 'score': score})

# --------- 气泡三维定位（聚类+最锐利z层） ---------
bubbles_3d = []
if bubble_candidates:
    data = np.array([[b['x'], b['y'], b['r']] for b in bubble_candidates])
    clustering = DBSCAN(eps=35, min_samples=1).fit(data)
    labels = clustering.labels_
    for label in set(labels):
        if label == -1:
            continue
        group = [b for b, l in zip(bubble_candidates, labels) if l == label]
        best = max(group, key=lambda b: b['score'])
        bubbles_3d.append(best)

# --------- 控制显示气泡数量和显示形式 ---------
N_show = 20  # 只显示最大的N个气泡
sort_key = 'r'  # 可选 'r'（半径）或 'score'（得分）

# if bubbles_3d:
#     # 按半径或得分排序
#     bubbles_3d_sorted = sorted(bubbles_3d, key=lambda b: b[sort_key], reverse=True)
#     bubbles_3d_show = bubbles_3d_sorted[:N_show]

#     xs = [b['x'] * pixel_size * 1000 for b in bubbles_3d_show]
#     ys = [b['y'] * pixel_size * 1000 for b in bubbles_3d_show]
#     zs = [b['z'] for b in bubbles_3d_show]
#     rs = np.array([b['r'] * pixel_size * 1000 for b in bubbles_3d_show])  # mm

#     # 线性映射半径到像素
#     min_px, max_px = 5, 30
#     if len(rs) > 0:
#         r_min, r_max = rs.min(), rs.max()
#         if r_max > r_min:
#             sizes = min_px + (rs - r_min) / (r_max - r_min) * (max_px - min_px)
#         else:
#             sizes = np.full_like(rs, (min_px + max_px) / 2)
#     else:
#         sizes = []

#     # 可选：按半径着色
#     colors = rs
#     colorbar_title = 'Radius (mm)'

#     hover_text = [f"X: {x:.2f} mm<br>Y: {y:.2f} mm<br>Z: {z:.2f} mm<br>R: {r:.2f} mm"
#                   for x, y, z, r in zip(xs, ys, zs, rs)]

#     x_range = max(xs) - min(xs) if xs else 1
#     y_range = max(ys) - min(ys) if ys else 1
#     z_range = max(zs) - min(zs) if zs else 1
#     max_range = max(x_range, y_range, z_range)
#     aspect_x = x_range / max_range
#     aspect_y = y_range / max_range
#     aspect_z = z_range / max_range

#     fig = go.Figure(data=[go.Scatter3d(
#     x=xs, y=ys, z=zs,
#     mode='markers',
#     marker=dict(
#         size=sizes,
#         color=colors,
#         colorscale='Viridis',
#         opacity=0.8,
#         line=dict(width=1, color='black'),
#         colorbar=dict(title=colorbar_title)
#     ),
#     text=hover_text,
#     hoverinfo='text'
#     )])

#     fig.update_layout(
#         scene=dict(
#             xaxis_title='X (mm)',
#             yaxis_title='Y (mm)',
#             zaxis_title='Z (mm)',
#             aspectmode='manual',
#             aspectratio=dict(x=1, y=1, z=1)
#         ),
#         title=f'三维气泡分布（显示最大{N_show}个气泡，单位：mm）',
#         width=1200,
#         height=900
#     )

#     fig.show()
# else:
#     print("未检测到气泡，请调整检测参数或全息图质量。")

# --------- 三维气泡分布可视化（使用 matplotlib 替代 Plotly） ---------
if bubbles_3d:
    # 提取物理坐标（单位：mm）
    xs = np.array([b['x'] * pixel_size * 1e3 for b in bubbles_3d])
    ys = np.array([b['y'] * pixel_size * 1e3 for b in bubbles_3d])
    zs = np.array([b['z'] * 1e3 for b in bubbles_3d])
    rs = np.array([b['r'] * pixel_size * 1e3 for b in bubbles_3d]) # 真实的物理半径

    # 设置散点大小：在matplotlib中，s代表面积。为了让半径线性变化的视觉效果更明显，这里对半径做平方并乘以一个放大系数
    # 你可以根据实际气泡数量和稠密程度调节 5000 这个系数
    sizes = (rs ** 2) * 5000 

    # 创建三维画布
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # 绘制三维散点图
    # cmap='viridis' 对应 Plotly 的 Viridis 渐变色
    sc = ax.scatter(xs, ys, zs, s=sizes, c=rs, cmap='viridis', alpha=0.8, edgecolors='black', linewidths=0.5)

    # 添加颜色条，用以指示气泡的真实半径
    cbar = fig.colorbar(sc, ax=ax, pad=0.1)
    cbar.set_label('Radius (mm)', fontsize=10)

    # 设置坐标轴标签
    ax.set_xlabel('X (mm)', fontsize=10)
    ax.set_ylabel('Y (mm)', fontsize=10)
    ax.set_zlabel('Z (mm)', fontsize=10)
    
    # 设置坐标轴比例
    # 模拟你原代码中的 aspectratio=dict(x=1, y=1, z=4)
    # Matplotlib 3.3.0+ 支持 set_box_aspect
    try:
        ax.set_box_aspect((1, 1, 4)) 
    except AttributeError:
        # 如果 matplotlib 版本较低，可以使用较老的方法（通常默认的长宽高比也足够清晰）
        pass

    # 设置图表标题
    ax.set_title('Three-Dimensional Bubble Distribution', fontsize=12, pad=20)

    # 调整视角（可选：设置一个较好的初始观察角度，如仰角20度，方位角30度）
    ax.view_init(elev=20, azim=30)

    plt.tight_layout()
    plt.show()