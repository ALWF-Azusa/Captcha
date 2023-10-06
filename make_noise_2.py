from PIL import Image, ImageDraw

# 圖像大小（寬度和高度）
width = 1500 # 圖像寬
height = 1500  # 圖像高

# 白色背景图像
image = Image.new('RGB', (width, height), 'white')

draw = ImageDraw.Draw(image)

# 定義圓大小
circle_diameter = width // 150  # 圓的直徑是圖寬度的四分之一

# 算圓之間的間距
spacing = circle_diameter

# 繪製黑白圓形交替排列
for x in range(0, width, spacing):
    for y in range(0, height, spacing):
        if (x // spacing + y // spacing) % 2 == 0:
            draw.ellipse([(x, y), (x + circle_diameter, y + circle_diameter)], fill='black')
        else:
            draw.ellipse([(x, y), (x + circle_diameter, y + circle_diameter)], fill='white')

# 保存圖像
image.save('checkerboard_circles.png')


image.show()
