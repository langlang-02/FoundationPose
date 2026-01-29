import cv2
import os

def images_to_video(image_folder, video_name, fps=24):
    """
    将指定文件夹中的图片合成为视频。
    
    参数:
    image_folder: 包含图片的文件夹路径（支持相对路径）
    video_name: 输出视频的文件名 (例如 'output.mp4')
    fps: 帧率，即每秒播放多少张图片
    """
    # 确保路径是绝对路径（基于传入的相对路径转出，增加兼容性）
    abs_image_folder = os.path.abspath(image_folder)
    
    # 获取文件夹中所有的图片文件名
    if not os.path.exists(abs_image_folder):
        print(f"错误：路径不存在 -> {abs_image_folder}")
        return

    images = [img for img in os.listdir(abs_image_folder) 
              if img.lower().endswith((".png", ".jpg", ".jpeg"))]
    
    # 按照文件名排序
    images.sort()

    if not images:
        print("错误：在文件夹中未找到图片。")
        return

    # 读取第一张图片以获取视频的宽高
    first_image_path = os.path.join(abs_image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # 定义视频编码器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    print(f"开始转换... 正在处理文件夹: {image_folder}")
    print(f"预计处理 {len(images)} 张图片")

    for image in images:
        image_path = os.path.join(abs_image_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    video.release()
    cv2.destroyAllWindows()
    
    print(f"转换成功！视频已保存至相对路径: {video_name}")

if __name__ == "__main__":
    # 获取当前脚本所在的目录
    current_dir = os.path.dirname(__file__)

    # --- 相对路径配置 ---
    # 假设图片存放在脚本同级目录下的 'input_images' 文件夹中
    my_folder = os.path.join(current_dir, 'debug/track_vis') 
    
    # 输出视频也保存在脚本同级目录下
    output_video = os.path.join(current_dir, 'output_video.mp4')
    
    # 设置帧率
    frames_per_second = 30

    # 如果文件夹存在则运行
    if os.path.exists(my_folder):
        images_to_video(my_folder, output_video, frames_per_second)
    else:
        print(f"提示：请在脚本同级目录下创建名为 'input_images' 的文件夹并放入图片。")
        print(f"当前脚本目录为: {current_dir}")