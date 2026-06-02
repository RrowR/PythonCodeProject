from PIL import Image

# 读取图像获得Image对象
image = Image.open('../026_day/psc.jpg')
# 通过Image对象的format属性获得图像的格式
print(image.format) # JPEG
# 通过Image对象的size属性获得图像的尺寸
print(image.size)   # (500, 750)
# 通过Image对象的mode属性获取图像的模式
print(image.mode)   # RGB
# 通过Image对象的show方法显示图像
# image.show()

# 剪裁图像
# image.crop((80, 20, 310, 360)).show()

# 生成缩略图
# image.thumbnail((128, 128))
# image.show()

# # 缩放和粘贴图像
# 霞沢ミユ_image = Image.open('128515905_p0.png')
# psc_image = Image.open('../026_day/psc.jpg')
# # guido_head = 霞沢ミユ_image.crop((900, 20, 1999, 3000))
# # guido_head.show()
# # 获取原图的宽度和高度
# width, height = psc_image.size
# # 计算缩放后的尺寸
# new_width = int(width / 1.5)
# new_height = int(height / 1.5)
# # 缩放并粘贴图像
# 霞沢ミユ_image.paste(psc_image.resize((new_width, new_height)), (900, 1999))
# 霞沢ミユ_image.show()

# # 图像的旋转与翻转
# image = Image.open('128515905_p0.png')
# # image.rotate(45).show()
# # Image.FLIP_LEFT_RIGHT - 水平翻转
# # Image.FLIP_TOP_BOTTOM - 垂直翻转
# image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 手动修改像素点
# image = Image.open('128515905_p0.png')
# for x in range(80, 310):
#     for y in range(20, 360):
#         # 通过Image对象的putpixel方法修改图像指定像素点
#         image.putpixel((x, y), (128, 128, 128))
# image.show()


# 滤镜效果
from PIL import ImageFilter
image = Image.open('128515905_p0.png')
# 使用Image对象的filter方法对图像进行滤镜处理
# ImageFilter模块包含了诸多预设的滤镜也可以自定义滤镜
image.filter(ImageFilter.CONTOUR).show()







