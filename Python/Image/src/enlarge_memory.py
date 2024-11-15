"""
扩大图片内存
待升级
无法确定升级到具体的大小
只能多次增大
pip install Pillow
"""
from PIL import Image
import os


def increase_image_size(input_path, output_path,target_size_mb,num=1):
    # 打开原始图片
    image = Image.open(input_path)

    # 获取当前图片的大小
    current_size = os.path.getsize(input_path) / (1024 * 1024)  # 以MB为单位
    print(f"Current size: {current_size:.2f} MB")

    # 计算所需的放大倍数
    factor = (5*num / current_size) ** 0.5
    new_size = (int(image.width * factor), int(image.height * factor))

    # 调整图片大小
    new_image = image.resize(new_size, Image.Resampling.LANCZOS)

    # 保存新的图片
    new_image.save(output_path, quality=100)  # quality参数调节图片质量
    new_size_mb = os.path.getsize(output_path) / (1024 * 1024)  # 以MB为单位
    print(new_size_mb,target_size_mb)
    if new_size_mb < target_size_mb:
        increase_image_size(input_path,output_path,target_size_mb,num+1)
        return
    print(f"New size: {new_size_mb:.2f} MB")


if __name__ == "__main__":
    # 输入图片路径和输出图片路径
    input_path_folder = "../image/"
    output_path_folder = "../image_res/"
    # 目标图片大小（MB）
    target_size_mb = 5
    # 扩大文件内的每一张图片
    filenames = os.listdir(input_path_folder)
    for i in filenames:
        input_path = input_path_folder+i
        output_path = output_path_folder+i
        increase_image_size(input_path, output_path, target_size_mb)

