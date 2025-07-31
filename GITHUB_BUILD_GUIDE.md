# 在GitHub上构建APK详细操作指导

本指南将详细介绍如何在GitHub上自动构建"小图弟弟"APP的APK文件，无需在本地配置复杂环境。

## 前期准备

### 1. 创建GitHub账户
如果您还没有GitHub账户，请访问 [github.com](https://github.com) 注册一个免费账户。

### 2. 准备项目文件
确保您拥有以下文件：
- [xiaotu.py](file:///d:/Visual%20Studio%20Code/project1/xiaotu.py) - 主程序文件
- [buildozer.spec](file:///d:/Visual%20Studio%20Code/project1/buildozer.spec) - Android构建配置文件
- [requirements.txt](file:///d:/Visual%20Studio%20Code/project1/requirements.txt) - 依赖文件
- [.github/workflows/build-apk.yml](file:///d:/Visual%20Studio%20Code/project1/.github/workflows/build-apk.yml) - GitHub Actions构建配置
- [README.md](file:///d:/Visual%20Studio%20Code/project1/README.md) - 项目说明文件
- [.gitignore](file:///d:/Visual%20Studio%20Code/project1/.gitignore) - Git忽略文件

## 详细操作步骤

### 步骤1：创建GitHub仓库

1. 登录您的GitHub账户
2. 点击右上角的"+"号，选择"New repository"
3. 为仓库命名，例如"xiaotu-app"
4. 选择设为公开（Public）或私有（Private）
5. 不要初始化README、.gitignore或license
6. 点击"Create repository"

### 步骤2：安装Git工具

如果您遇到"'git' 不是内部或外部命令"的错误，说明需要先安装Git工具：

👉 **[查看Git安装和配置详细指导](GIT_INSTALLATION_GUIDE.md)**

### 步骤3：推送代码到GitHub

👉 **[查看如何在本地项目目录中打开命令行工具的详细指导](LOCAL_COMMAND_GUIDE.md)**

在您的本地项目目录中打开命令行工具，执行以下命令：

```bash
# 初始化本地Git仓库
git init

# 添加所有文件到暂存区
git add .

# 提交文件
git commit -m "Initial commit - 小图弟弟APP"

# 添加远程仓库地址（将URL替换为您自己的仓库地址）
git remote add origin https://github.com/您的用户名/仓库名.git

# 设置默认分支
git branch -M main

# 推送代码到GitHub
git push -u origin main
```

### 步骤4：触发构建流程

代码推送到GitHub后，GitHub Actions会自动开始构建APK：

1. 访问您的GitHub仓库页面
2. 点击"Actions"选项卡
3. 您将看到"Build APK"工作流正在运行或已经完成

### 步骤5：下载构建的APK

构建完成后，您可以通过以下方式下载APK：

#### 方法一：从Artifacts下载（推荐）
1. 在"Actions"选项卡中，点击最近的构建记录
2. 向下滚动到"Artifacts"部分
3. 点击"xiaotu-app-apk"下载构建好的APK文件

#### 方法二：从Releases下载
1. 如果您推送到main分支，系统会自动创建Release
2. 点击仓库页面的"Releases"选项卡
3. 下载"xiaotu-app.apk"文件

## 构建状态监控

您可以在以下位置监控构建状态：

1. **Actions页面**：查看构建进度和日志
2. **邮箱通知**：如果配置了通知，会收到构建成功或失败的邮件
3. **仓库首页**：如果有构建状态徽章，会显示当前构建状态

## 常见问题及解决方案

### 1. 构建失败
如果构建失败，请检查以下几点：
- 查看Actions中的构建日志，找到错误信息
- 确保所有必需的文件都已推送
- 检查[buildozer.spec](file:///d:/Visual%20Studio%20Code/project1/buildozer.spec)配置是否正确

### 2. APK文件过大
- 这是正常的，因为包含了Python解释器和所有依赖
- 最终APK通常在10-30MB之间

### 3. 中文显示问题
- 应用会自动使用设备系统字体
- 如果仍有显示问题，请确保设备支持中文显示

## 更新应用版本

当您需要更新应用时：

1. 修改[buildozer.spec](file:///d:/Visual%20Studio%20Code/project1/buildozer.spec)中的版本号：
   ```
   version = 0.2  # 或其他新版本号
   ```

2. 提交并推送更改：
   ```bash
   git add buildozer.spec
   git commit -m "升级到版本 0.2"
   git push origin main
   ```

3. GitHub Actions会自动构建新版本APK

## 安装APK到Android设备

下载APK后，按以下步骤安装：

1. 在Android设备上，找到下载的APK文件
2. 点击APK文件开始安装
3. 如果提示"不允许安装未知应用"，请前往设置>应用和通知>特殊应用访问>安装未知应用，允许文件管理器安装应用
4. 点击"安装"按钮完成安装
5. 安装完成后，即可在应用列表中找到"小图弟弟"APP

## 注意事项

1. **首次运行**：应用可能需要存储权限来访问和保存图片
2. **构建时间**：首次构建可能需要10-20分钟，因为需要下载Android SDK等工具
3. **后续构建**：之后的构建会更快，因为缓存了大部分工具
4. **存储空间**：确保GitHub仓库有足够的存储空间（免费账户有配额限制）

## 技术支持

如果遇到任何问题，您可以：
1. 查看GitHub Actions构建日志
2. 检查README.md中的说明
3. 在相关技术论坛寻求帮助