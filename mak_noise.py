from PIL import Image, ImageDraw, ImageFilter
import random

# 設置新的圖像寬度和高度
new_width, new_height =2500, 2500

# 創建一個空白的圖像
image = Image.new('RGB', (new_width, new_height), color='white')

# 創建一個畫布對象
draw = ImageDraw.Draw(image)

# 添加背景雜訊 - 隨機圓形
for _ in range(6000):
    x = random.randint(0, new_width)
    y = random.randint(0, new_height)
    radius = random.randint(1,60)  # 調整圓形的半徑範圍
    draw.ellipse([x, y, x + radius, y + radius], fill='black')

# 添加文字或其他元素到圖像（這裡僅示範如何添加背景雜訊）
# 你可以在這個步驟中添加文字、圖案或其他CAPTCHA內容

# 模糊整個圖像以增加難度
image = image.filter(ImageFilter.BLUR)

# 保存圖像
image.save('circular_noise_captcha.png')
