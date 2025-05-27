@echo off
echo ========================================
echo PPOxFamily Windows 安装脚本
echo ========================================
echo.

:: 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.7+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo 检测到Python版本:
python --version

:: 升级pip
echo.
echo 正在升级pip...
python -m pip install --upgrade pip

:: 创建虚拟环境
echo.
echo 正在创建虚拟环境...
python -m venv ppoxfamily_env

:: 激活虚拟环境
echo.
echo 正在激活虚拟环境...
call ppoxfamily_env\Scripts\activate.bat

:: 安装基础依赖
echo.
echo 正在安装基础依赖...
pip install torch numpy gym DI-engine DI-treetensor transformers

:: 尝试安装OpenCV
echo.
echo 正在尝试安装OpenCV...
pip install opencv-python
if errorlevel 1 (
    echo 警告: OpenCV安装失败，将跳过
    echo 如需使用第三章功能，请手动安装: pip install opencv-python
)

:: 尝试安装游戏环境
echo.
echo 正在尝试安装游戏环境依赖...
echo 注意: 如果失败，请先安装Visual Studio Build Tools
pip install gym-super-mario-bros nes-py
if errorlevel 1 (
    echo.
    echo ========================================
    echo 游戏环境安装失败！
    echo ========================================
    echo 这通常是因为缺少Microsoft Visual C++ Build Tools
    echo.
    echo 解决方案:
    echo 1. 下载并安装 Microsoft C++ Build Tools:
    echo    https://visualstudio.microsoft.com/visual-cpp-build-tools/
    echo 2. 安装时选择 "C++ build tools" 工作负载
    echo 3. 重新运行此脚本或手动安装:
    echo    pip install gym-super-mario-bros nes-py
    echo.
    echo 或者，如果不需要游戏环境，可以跳过此步骤
    echo ========================================
)

:: 安装可选依赖
echo.
echo 正在安装可选依赖...
pip install pandas matplotlib seaborn tqdm tensorboard

echo.
echo ========================================
echo 安装完成！
echo ========================================
echo.
echo 使用方法:
echo 1. 激活虚拟环境: ppoxfamily_env\Scripts\activate.bat
echo 2. 运行示例代码: cd chapter1_overview && python ppo_zh.py
echo.
echo 如果遇到问题，请查看 INSTALL.md 获取详细说明
echo.
pause 