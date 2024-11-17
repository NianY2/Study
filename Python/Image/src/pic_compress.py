"""
对图片进行保真压缩
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple Pillow
"""
from PIL import Image
import  os
def pic_compress(pic_path, out_path, quality=75):
    try:
        size = os.path.getsize(pic_path)/1024
        print(f"压缩({size})：",pic_path)
        img = Image.open(pic_path)
        width, height = img.size
        while width > 100 and height > 100:
            width,height = round(width*0.9), round(height*0.9)
            img = img.resize((width,height))
        img.save(out_path,quality=quality)
        size = os.path.getsize(out_path)/1024
        print(f"压缩完成({size})：",out_path)
    except IOError as e:
        print(e)

if __name__ == '__main__':
    # 输入图片路径和输出图片路径
    input_path_folder = "../image/"
    output_path_folder = "../image_res/"

    filenames = os.listdir(input_path_folder)
    for i in filenames:
        input_path = input_path_folder+i
        output_path = output_path_folder+i
        pic_compress(input_path,output_path)
        pic_compress(input_path,output_path)