# Git安装和配置详细指导

当您遇到"'git' 不是内部或外部命令"错误时，说明您的系统中尚未安装Git工具。本指南将详细介绍如何在Windows系统上安装和配置Git。

## 第一步：下载Git

1. 打开浏览器，访问Git官网下载页面：
   https://git-scm.com/downloads

2. 在页面中找到"Windows"，点击"Download X.X.X for Windows"（X.X.X代表版本号）

3. 下载完成后，您会得到一个名为类似 `Git-X.X.X-64-bit.exe` 的安装文件

## 第二步：安装Git

1. 双击下载的安装文件（如 `Git-2.39.0-64-bit.exe`）

2. 在安装向导中：
   - 点击"Next"接受许可协议
   - 选择安装路径（建议使用默认路径）
   - 点击"Next"继续

3. 选择组件：
   - 建议保持默认选项
   - 确保以下选项被选中：
     * Windows Explorer integration
     * Git Bash Here
     * Git GUI Here
   - 点击"Next"

4. 选择默认编辑器：
   - 推荐选择"Vim"（默认选项）
   - 或者选择您熟悉的编辑器如"Nano"或"Visual Studio Code"
   - 点击"Next"

5. 调整PATH环境变量：
   - 选择"Git from the command line and also from 3rd-party software"（推荐选项）
   - 这样可以在Windows命令提示符中使用Git
   - 点击"Next"

6. 选择SSH可执行文件：
   - 选择"Use bundled OpenSSH"（推荐选项）
   - 点击"Next"

7. 选择HTTPS传输后端：
   - 选择"Use the OpenSSL library"（推荐选项）
   - 点击"Next"

8. 配置行结束符：
   - 选择"Checkout Windows-style, commit Unix-style line endings"（推荐选项）
   - 点击"Next"

9. 选择终端模拟器：
   - 选择"Use Windows' default console window"（推荐选项）
   - 点击"Next"

10. 其他选项：
    - 保持默认设置
    - 点击"Next"

11. 实验性选项：
    - 保持默认设置（不选择任何实验性选项）
    - 点击"Install"

12. 等待安装完成，完成后点击"Finish"

## 第三步：验证安装

1. 重新打开命令提示符（重要！必须重新打开以加载新的环境变量）

2. 输入以下命令验证Git是否安装成功：
   ```cmd
   git --version
   ```

3. 如果显示类似 `git version 2.39.0.windows.1` 的信息，说明安装成功

## 第四步：基本Git配置

首次使用Git前，需要配置用户信息：

1. 打开命令提示符

2. 设置用户名（替换为您的GitHub用户名）：
   ```cmd
   git config --global user.name "您的用户名"
   ```

3. 设置邮箱（替换为您的GitHub注册邮箱）：
   ```cmd
   git config --global user.email "您的邮箱@example.com"
   ```

4. 验证配置：
   ```cmd
   git config --global --list
   ```

## 第五步：解决可能的问题

### 问题1：重新打开命令提示符
安装Git后，必须重新打开命令提示符才能使用Git命令。

### 问题2：权限问题
如果遇到权限问题，尝试以管理员身份运行命令提示符：
1. 按 `Win + X`
2. 选择"Windows PowerShell (管理员)" 或 "命令提示符 (管理员)"
3. 点击"是"确认权限

### 问题3：PATH环境变量未更新
如果仍然无法使用Git命令：

1. 手动添加Git到PATH环境变量：
   - 右键"此电脑" > "属性"
   - 点击"高级系统设置"
   - 点击"环境变量"
   - 在"系统变量"中找到"Path"，点击"编辑"
   - 点击"新建"，添加Git的bin目录路径（通常是 `C:\Program Files\Git\bin`）
   - 点击"确定"保存所有更改
   - 重新打开命令提示符

## 第六步：继续执行项目命令

成功安装Git后，您就可以继续执行项目所需的Git命令了：

```cmd
# 确保您在项目目录中
cd /d D:\Visual Studio Code\project1

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

## 其他有用的Git命令

### 查看Git状态
```cmd
git status
```

### 查看提交历史
```cmd
git log --oneline
```

### 查看配置信息
```cmd
git config --global --list
```

## 使用Git Bash（可选）

除了Windows命令提示符，Git还提供了Git Bash，它提供了更类似Linux的命令行环境：

1. 在开始菜单中搜索"Git Bash"
2. 打开Git Bash
3. 导航到项目目录：
   ```bash
   cd /d/Visual\ Studio\ Code/project1
   ```
4. 执行Git命令

Git Bash在处理路径和文件名中的空格时更加友好。

通过以上步骤，您应该能够成功安装Git并继续完成项目推送到GitHub的操作。