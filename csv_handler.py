import csv
from label_builder import generate_prefix_oneline_title, generate_prefix_twoline_title, generate_twoline_title, generate_oneline_title
def batch_generate_from_csv(csv_path):
    with open(csv_path, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # 预处理数据
            row = preprocess_row(row)
            prefix = row.get('前缀', '').strip()
            title1 = row.get('标题一', '').strip()
            title2 = row.get('标题二', '').strip()
            index = row.get('序号', '').strip()

            # 判断使用哪个模板
            print(f"正在生成: {title1+title2}")
            print(f"前缀: {prefix}")
            if prefix and title1 and title2:
                generate_prefix_twoline_title(prefix, title1, title2, index)
            elif prefix and title1:
                generate_prefix_oneline_title(prefix, title1, index)
            elif title1 and title2:
                generate_twoline_title(title1, title2, index)
            elif title1:
                generate_oneline_title(title1, index)
            else:
                print("无法识别的数据格式，跳过")

# 竖排专用括号替换
def replace_parentheses(text):
    return text.replace("（", "︵").replace("）", "︶").replace("(", "︵").replace(")", "︶")

# 统一文本预处理函数
def preprocess_row(row):
    new_row = {}
    for key, value in row.items():
        cleaned = replace_parentheses(value)
        new_row[key] = cleaned
    return new_row


if __name__ == '__main__':
    batch_generate_from_csv('csv/待处理标签.csv')