import tkinter as tk
from tkinter import filedialog, messagebox
from csv_handler import batch_generate_from_csv
from a4_layout import batch_layout_to_a4

def start_gui():
    root = tk.Tk()
    root.title('批量标签生成器')
    root.geometry('400x300')

    def select_and_run():
        csv_file = filedialog.askopenfilename(
            title='请选择 CSV 文件',
            filetypes=[('CSV 文件', '*.csv')]
        )
        if not csv_file:
            return
        try:
            batch_generate_from_csv(csv_file)
            batch_layout_to_a4()
            messagebox.showinfo("完成", "✅ 标签图片和 PDF 已生成！")
        except Exception as e:
            messagebox.showerror("错误", f"❌ 生成失败：{e}")

    label = tk.Label(root, text="欢迎使用标签生成器", font=("微软雅黑", 16))
    label.pack(pady=30)

    button = tk.Button(root, text="选择 CSV 文件并生成标签", command=select_and_run, width=30, height=2)
    button.pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    start_gui()
