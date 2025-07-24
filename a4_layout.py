from PIL import Image
import os

# A4 纸尺寸（300dpi）
A4_WIDTH, A4_HEIGHT = int(29.7 * 300 / 2.54), int(21 * 300 / 2.54) # 2480 x 3508

# 标签尺寸（与 main.py 一致）
LABEL_WIDTH, LABEL_HEIGHT = int(4.5 * 300 / 2.54), int(18.5 * 300 / 2.54)  # 536 x 2188

# 每页布局：6 张图
LABELS_PER_PAGE = 6

# 标签图片路径
LABEL_DIR = "label"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_label_images():
    return [os.path.join(LABEL_DIR, f) for f in os.listdir(LABEL_DIR) if f.endswith(".png")]

def create_a4_sheet(images):
    a4_sheet = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), (255, 255, 255))
    x, y = 0, 0
    for img_path in images:
        img = Image.open(img_path)
        img = img.resize((LABEL_WIDTH, LABEL_HEIGHT))  # 确保尺寸一致
        a4_sheet.paste(img, (x, y))
        x += LABEL_WIDTH
        if x + LABEL_WIDTH > A4_WIDTH:
            break
    return a4_sheet

def batch_layout_to_a4():
    label_files = get_label_images()
    page_count = 0

    for i in range(0, len(label_files), LABELS_PER_PAGE):
        page_count += 1
        batch = label_files[i:i + LABELS_PER_PAGE]
        a4_image = create_a4_sheet(batch)
        output_path = os.path.join(OUTPUT_DIR, f"a4_page_{page_count}.pdf")
        a4_image.save(output_path, resolution=300, save_all=True)
        print(f"已生成 A4 页面：{output_path}")

if __name__ == '__main__':
    batch_layout_to_a4()