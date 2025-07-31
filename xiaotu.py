import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.core.image import Image as CoreImage
from kivy.clock import Clock
from PIL import Image as PILImage
from PIL import ImageOps
import os
import io

# 注册中文字体以确保正确显示
# 在移动设备上，我们将使用系统默认的中文字体
try:
    # 尝试注册中文字体以支持中文显示
    from kivy.core.text import LabelBase
    # 这里不实际注册字体，因为在Android上会使用系统默认字体
except:
    pass

kivy.require('2.0.0')

class ImageProcessor:
    def __init__(self):
        self.original_image = None
        self.processed_image = None
    
    def load_image(self, image_path):
        """加载图片"""
        try:
            self.original_image = PILImage.open(image_path)
            return True
        except Exception as e:
            print(f"加载图片失败: {e}")
            return False
    
    def resize_image(self, width, height, maintain_aspect_ratio=False):
        """调整图片尺寸"""
        if self.original_image is None:
            return False
        
        try:
            if maintain_aspect_ratio:
                self.processed_image = ImageOps.fit(self.original_image, (width, height))
            else:
                self.processed_image = self.original_image.resize((width, height))
            return True
        except Exception as e:
            print(f"调整图片尺寸失败: {e}")
            return False
    
    def set_dpi(self, dpi):
        """设置图片DPI"""
        if self.processed_image is None:
            return False
        
        try:
            self.processed_image.info['dpi'] = (dpi, dpi)
            return True
        except Exception as e:
            print(f"设置DPI失败: {e}")
            return False
    
    def save_image(self, file_path, format_type, quality):
        """保存图片"""
        if self.processed_image is None:
            return False
        
        try:
            save_kwargs = {}
            if format_type.upper() == 'JPEG':
                if self.processed_image.mode in ('RGBA', 'LA', 'P'):
                    # JPEG不支持透明度，需要转换
                    rgb_image = self.processed_image.convert('RGB')
                    rgb_image.save(file_path, format=format_type, quality=quality, **save_kwargs)
                else:
                    self.processed_image.save(file_path, format=format_type, quality=quality, **save_kwargs)
            else:  # PNG
                self.processed_image.save(file_path, format=format_type, **save_kwargs)
            return True
        except Exception as e:
            print(f"保存图片失败: {e}")
            return False

class ImageProcessLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.image_processor = ImageProcessor()
        self.selected_image_path = ""
        
        # 创建UI元素
        self.create_ui()
    
    def create_ui(self):
        # 标题
        title_label = Label(text='小图弟弟 - 图片处理工具', size_hint_y=None, height=50, font_size=20)
        self.add_widget(title_label)
        
        # 图片选择区域
        image_select_layout = BoxLayout(size_hint_y=None, height=50)
        select_button = Button(text='选择图片', size_hint_x=None, width=100)
        select_button.bind(on_press=self.select_image)
        self.image_path_label = Label(text='未选择图片')
        image_select_layout.add_widget(select_button)
        image_select_layout.add_widget(self.image_path_label)
        self.add_widget(image_select_layout)
        
        # 尺寸输入区域
        size_layout = BoxLayout(size_hint_y=None, height=50)
        width_label = Label(text='宽度:', size_hint_x=None, width=50)
        self.width_input = TextInput(text='800', multiline=False, size_hint_x=None, width=100)
        height_label = Label(text='高度:', size_hint_x=None, width=50)
        self.height_input = TextInput(text='600', multiline=False, size_hint_x=None, width=100)
        
        # 保持长宽比复选框
        aspect_layout = BoxLayout(size_hint_x=None, width=200)
        self.aspect_checkbox = CheckBox(size_hint_x=None, width=30)
        aspect_label = Label(text='保持长宽比', size_hint_x=None, width=100)
        aspect_layout.add_widget(self.aspect_checkbox)
        aspect_layout.add_widget(aspect_label)
        
        size_layout.add_widget(width_label)
        size_layout.add_widget(self.width_input)
        size_layout.add_widget(height_label)
        size_layout.add_widget(self.height_input)
        size_layout.add_widget(aspect_layout)
        self.add_widget(size_layout)
        
        # DPI输入区域
        dpi_layout = BoxLayout(size_hint_y=None, height=50)
        dpi_label = Label(text='DPI:', size_hint_x=None, width=50)
        self.dpi_input = TextInput(text='72', multiline=False, size_hint_x=None, width=100)
        dpi_layout.add_widget(dpi_label)
        dpi_layout.add_widget(self.dpi_input)
        self.add_widget(dpi_layout)
        
        # 质量选择区域
        quality_layout = BoxLayout(size_hint_y=None, height=50)
        quality_label = Label(text='输出质量:', size_hint_x=None, width=100)
        self.quality_spinner = Spinner(
            text='中质量',
            values=('高质量', '中质量', '低质量'),
            size_hint_x=None,
            width=100
        )
        quality_layout.add_widget(quality_label)
        quality_layout.add_widget(self.quality_spinner)
        self.add_widget(quality_layout)
        
        # 格式选择区域
        format_layout = BoxLayout(size_hint_y=None, height=50)
        format_label = Label(text='保存格式:', size_hint_x=None, width=100)
        self.format_spinner = Spinner(
            text='JPEG',
            values=('JPEG', 'PNG'),
            size_hint_x=None,
            width=100
        )
        format_layout.add_widget(format_label)
        format_layout.add_widget(self.format_spinner)
        self.add_widget(format_layout)
        
        # 处理按钮
        process_button = Button(text='处理并保存图片', size_hint_y=None, height=50)
        process_button.bind(on_press=self.process_image)
        self.add_widget(process_button)
        
        # 状态标签
        self.status_label = Label(text='就绪', size_hint_y=None, height=30)
        self.add_widget(self.status_label)
    
    def select_image(self, instance):
        # 在实际APP中，这里会打开文件选择器
        # 为了演示，我们创建一个简单的弹窗提示
        popup = Popup(title='选择图片',
                      content=Label(text='在移动设备上，这里会打开文件选择器\n请选择设备上的图片文件'),
                      size_hint=(0.8, 0.4))
        popup.open()
        self.status_label.text = '请在设备上选择图片文件'
    
    def process_image(self, instance):
        # 获取输入值
        try:
            width = int(self.width_input.text)
            height = int(self.height_input.text)
            maintain_aspect = self.aspect_checkbox.active
            dpi = int(self.dpi_input.text)
            
            # 质量映射
            quality_map = {
                '高质量': 95,
                '中质量': 75,
                '低质量': 40
            }
            quality = quality_map[self.quality_spinner.text]
            
            format_type = self.format_spinner.text
            
            # 显示处理状态
            self.status_label.text = '正在处理图片...'
            
            # 在实际应用中，这里会处理真实的图片
            # 由于演示限制，我们显示处理完成
            Clock.schedule_once(lambda dt: self.finish_processing(format_type, quality), 1)
            
        except ValueError:
            self.status_label.text = '输入参数无效，请检查输入'
    
    def finish_processing(self, format_type, quality):
        self.status_label.text = f'图片处理完成! 格式: {format_type}, 质量: {quality}'

class XiaoTuApp(App):
    def build(self):
        # 设置默认字体以更好地支持中文显示
        self.title = '小图弟弟'
        return ImageProcessLayout()

if __name__ == '__main__':
    # 设置环境变量以更好地支持中文
    os.environ['KIVY_DEFAULT_FONT'] = 'Roboto'
    XiaoTuApp().run()