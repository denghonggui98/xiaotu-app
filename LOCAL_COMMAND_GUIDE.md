# 在本地项目目录中打开命令行工具详细指导

本指南将详细介绍如何在Windows系统上打开命令行工具并导航到项目目录，以便执行Git命令将项目推送到GitHub。

## 方法一：使用文件资源管理器（推荐）

### 步骤1：打开项目文件夹
1. 打开文件资源管理器（Windows Explorer）
2. 导航到您的项目目录：`d:\Visual Studio Code\project1`

### 步骤2：打开命令行工具
在文件资源管理器中：
1. 点击地址栏（确保地址栏处于可编辑状态）
2. 输入 `cmd` 并按回车键
   或者
3. 按住 `Shift` 键，同时右键点击文件夹空白处
4. 在弹出菜单中选择"在此处打开命令窗口"或"在此处打开 PowerShell 窗口"

### 步骤3：确认当前目录
您应该看到类似以下的命令行提示：
```
D:\Visual Studio Code\project1>
```

这表示您已在正确的项目目录中。

## 方法二：使用开始菜单

### 步骤1：打开命令提示符
1. 点击Windows开始按钮
2. 输入 `cmd` 或 "命令提示符"
3. 点击"命令提示符"应用

### 步骤2：导航到项目目录
在命令行中输入以下命令并按回车：
```cmd
cd /d D:\Visual Studio Code\project1
```

### 步骤3：确认当前目录
输入以下命令确认您已在正确目录：
```cmd
dir
```

您应该能看到项目文件，如 [xiaotu.py](file:///d:/Visual%20Studio%20Code/project1/xiaotu.py)、[buildozer.spec](file:///d:/Visual%20Studio%20Code/project1/buildozer.spec) 等。

## 方法三：使用VS Code内置终端（推荐）

如果您使用Visual Studio Code：

### 步骤1：打开项目
1. 打开Visual Studio Code
2. 选择"文件" > "打开文件夹"
3. 选择 `D:\Visual Studio Code\project1` 文件夹

### 步骤2：打开终端
1. 按下 `Ctrl + `` （反引号）快捷键
   或
2. 选择"视图" > "终端"

### 步骤3：确认当前目录
终端底部应该显示：
```
PS D:\Visual Studio Code\project1>
```

## 安装Git工具

如果您遇到"'git' 不是内部或外部命令"的错误，说明需要先安装Git工具：

👉 **[查看Git安装和配置详细指导](GIT_INSTALLATION_GUIDE.md)**

## 执行Git命令

无论使用哪种方法打开命令行工具，一旦进入项目目录，就可以执行以下Git命令：

```cmd
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

## 常见问题及解决方案

### 1. 'git' 不是内部或外部命令
**问题**：执行git命令时提示"'git' 不是内部或外部命令"
**解决方案**：
- 需要先安装Git工具
- 访问 https://git-scm.com/downloads 下载并安装Git for Windows
- 安装完成后重启命令行工具

### 2. 权限被拒绝
**问题**：执行某些命令时提示权限不足
**解决方案**：
- 右键点击命令提示符，选择"以管理员身份运行"
- 或者确保您对项目目录有读写权限

### 3. 路径包含空格
**问题**：路径中包含空格导致命令执行失败
**解决方案**：
- 使用双引号包围路径，例如：
  ```cmd
  cd "D:\Visual Studio Code\project1"
  ```

### 4. 中文显示乱码
**问题**：命令行中显示中文乱码
**解决方案**：
- 在命令行中执行：
  ```cmd
  chcp 65001
  ```
- 或者在命令行属性中设置字体为支持中文的字体

## 验证操作成功

执行完Git命令后，可以通过以下方式验证：

1. 检查Git状态：
   ```cmd
   git status
   ```

2. 查看提交历史：
   ```cmd
   git log --oneline
   ```

3. 查看远程仓库配置：
   ```cmd
   git remote -v
   ```

## 其他有用的命令行技巧

### 查看当前目录
```cmd
cd
```

### 列出目录内容
```cmd
dir
```

### 清屏
```cmd
cls
```

### 查看Git状态
```cmd
git status
```

通过以上方法，您就能顺利在本地项目目录中打开命令行工具并执行所需的Git命令了。