import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

# Инициализация дисплея
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)

disp.begin()
disp.clear()
disp.display()

# Создание изображения для вывода
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Добавление текста
font = ImageFont.load_default()
draw.text((0, 0), "Hello, Orange Pi!", font=font, fill=255)

# Отображение на экране
disp.image(image)
disp.display()
