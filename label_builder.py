import os
import sys
from PIL import Image, ImageDraw, ImageFont

os.makedirs("label", exist_ok=True)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# 设置图像尺寸（厘米转像素：1cm ≈ 28.35 px @ 72dpi）
WIDTH_CM, HEIGHT_CM = 4.5, 18.5
DPI = 300
WIDTH = int(WIDTH_CM * DPI / 2.54)
HEIGHT = int(HEIGHT_CM * DPI / 2.54)

# 示例内容
prefix = "广东省高新技术产业开发区鹤山工业城基础设施建设工程项目"
title = "安全设施提升项目"
index = "①"


# 加载字体（可替换为中文字体路径）
font_path = resource_path("data/font/msyh.ttf")  # 替换为你自己的中文字体路径
font_prefix = ImageFont.truetype(font_path, 48)  # 新增：用于 prefix 的字体大小
font_title = ImageFont.truetype(font_path, 64)   # 新增：用于 title 的字体大小
font_index = ImageFont.truetype(font_path, 64)   # 新增：用于 index 的字体大小

def init_draw(img):
    draw = ImageDraw.Draw(img)
    # 添加边框（距离边缘 10px）
    border_width = 1
    draw.rectangle(
        [(0, 0), (img.width - 1, img.height - 1)],
        outline="black",
        width=border_width
    )
    return draw

# 将内容竖排绘制（一个字一行）
def draw_vertical_text(draw, text, start_x, line_height, font_obj):
    # 计算字符高度（使用一个常见汉字估算）
    char_bbox = font_obj.getbbox("一")
    char_height = char_bbox[3] - char_bbox[1]

    # 计算总高度和起始 y 坐标
    total_height = len(text) * char_height + (len(text) - 1) * (line_height - char_height)
    start_y = (HEIGHT - total_height) // 2

    for i, char in enumerate(text):
        draw.text((start_x, start_y + i * line_height), char, fill="black", font=font_obj)

# 绘制前缀 + 主标题 + 底部编号
def generate_prefix_oneline_title(prefix, title, index="①", year="2025"):
    # 创建空白画布
    img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
    draw = init_draw(img)
    draw_vertical_text(draw, prefix, 130, 54, font_prefix)  # 使用新的字体大小
    draw_vertical_text(draw, title,WIDTH - 230, 96,font_title)   # 使用新的字体大小
    draw.text((WIDTH//2 - 32, HEIGHT - 230), index, font=font_index, fill="black")
    draw.text((WIDTH//2 - 80, HEIGHT - 120), year, font=font_index, fill="black")
    # 保存
    filename = f"label_{title}_{index}.png"
    img.save(f"label/{filename}")

# 绘制前缀 + 双列主标题 + 底部编号
def generate_prefix_twoline_title(prefix, title1, title2, index="①", year="2025"):
    # 创建空白画布
    img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
    draw = init_draw(img)
    draw_vertical_text(draw, prefix, 99, 54, font_prefix)  # 使用新的字体大小
    draw_vertical_text(draw, title1, 231, 80,font_title)   # 使用新的字体大小
    draw_vertical_text(draw, title2, 364, 80,font_title)   # 使用新的字体大小
    draw.text((WIDTH//2 - 32, HEIGHT - 230), index, font=font_index, fill="black")
    draw.text((WIDTH//2 - 80, HEIGHT - 120), year, font=font_index, fill="black")
    # 保存
    filename = f"label_{title1+title2}_{index}.png"
    img.save(f"label/{filename}")

# 绘制主标题 + 底部编号
def generate_oneline_title(title, index="①", year="2025"):
    # 创建空白画布
    img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
    draw = init_draw(img)
    draw_vertical_text(draw, title, WIDTH//2 - 32, 96,font_title)   # 使用新的字体大小
    draw.text((WIDTH//2 - 32, HEIGHT - 230), index, font=font_index, fill="black")
    draw.text((WIDTH//2 - 80, HEIGHT - 120), year, font=font_index, fill="black")
    # 保存
    filename = f"label_{title}_{index}.png"
    img.save(f"label/{filename}")

# 绘制双列主标题 + 底部编号
def generate_twoline_title(title1, title2, index="①", year="2025"):
    # 创建空白画布
    img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
    draw = init_draw(img)
    draw_vertical_text(draw, title1, 140, 96,font_title)
    draw_vertical_text(draw, title2, WIDTH - 140 - 64, 96,font_title)
    draw.text((WIDTH//2 - 32, HEIGHT - 230), index, font=font_index, fill="black")
    draw.text((WIDTH//2 - 80, HEIGHT - 120), year, font=font_index, fill="black")
    # 保存
    filename = f"label_{title1 + title2}_{index}.png"
    img.save(f"label/{filename}")



if __name__ == "__main__":
    # generate_prefix_oneline_title()
    generate_oneline_title(title)
