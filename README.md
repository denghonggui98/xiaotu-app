# 小图弟弟 - 图片处理APP

一个基于Python和Kivy的Android图片处理应用，可以调整图片尺寸、DPI和质量，并支持导出为JPEG或PNG格式。

## 功能特点

1. 导入手机中的图片文件（支持常见格式如JPG、PNG等）
2. 自定义调整图片像素大小
3. 可选保持长宽比功能
4. 自定义DPI值
5. 三种输出质量选择（高质量、中质量、低质量）
6. 支持导出为JPEG和PNG格式

## 技术栈

- Python 3.x
- Kivy (跨平台UI框架)
- Pillow (图像处理库)

## 中文显示优化

本应用已经针对中文显示进行了优化：
- 使用系统默认中文字体支持
- 设置了正确的编码环境
- 在Android平台上能正确显示中文界面

## 在GitHub上自动构建APK

本项目使用GitHub Actions自动构建APK文件，无需在本地配置复杂环境。

👉 **[查看详细的GitHub构建APK操作指导](GITHUB_BUILD_GUIDE.md)**

### 构建步骤

1. 将代码推送到GitHub仓库
2. GitHub Actions会自动触发构建流程
3. 构建完成后，APK文件会作为artifact提供下载

### 手动构建方法（如果需要在本地构建）

如果您希望在本地构建APK，请按照以下步骤操作：

1. 安装Buildozer：
   ```bash
   pip install buildozer
   ```

2. 安装系统依赖（Ubuntu/Debian示例）：
   ```bash
   sudo apt update
   sudo apt install -y build-essential git python3 python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
   ```

3. 构建APK：
   ```bash
   buildozer android debug
   ```

APK文件将生成在`bin/`目录中。

## 质量参数设置

本应用提供三种质量选项，参数如下：
- 高质量：95（JPEG）
- 中质量：75（JPEG）
- 低质量：40（JPEG）

对于PNG格式，质量参数不适用，因为PNG是无损格式。

## 使用说明

1. 打开应用后，点击"选择图片"按钮选择设备上的图片
2. 输入目标宽度和高度
3. 如需保持长宽比，勾选"保持长宽比"选项
4. 设置DPI值
5. 选择输出质量
6. 选择保存格式（JPEG/PNG）
7. 点击"处理并保存图片"完成处理

## 注意事项

- 由于Android权限系统，首次使用时需要授予应用存储权限
- 处理大图片时可能需要一些时间，请耐心等待
- 应用会自动使用设备系统中文字体，确保中文正确显示

## 更新日志

### v1.0
- 修复GitHub Actions中已弃用的actions/upload-artifact@v3版本问题
- 更新所有GitHub Actions到最新稳定版本
- 使用更现代的release-action替代旧的create-release和upload-release-asset
- 修复buildozer.spec中的重复section问题
- 优化Android SDK安装过程，解决Aidl未找到问题
- 修复GitHub Actions配置文件中的重复run字段问题