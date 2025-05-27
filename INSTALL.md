# PPOxFamily 安装指南

## 环境要求

- Python 3.7+
- CUDA 10.2+ (如果使用GPU)
- **Windows用户**: Microsoft Visual C++ 14.0+ (详见下方Windows安装说明)

## 快速安装

### 1. 克隆项目
```bash
git clone https://github.com/opendilab/PPOxFamily.git
cd PPOxFamily
```

### 2. 创建虚拟环境 (推荐)
```bash
# 使用conda
conda create -n ppoxfamily python=3.8
conda activate ppoxfamily

# 或使用venv
python -m venv ppoxfamily
source ppoxfamily/bin/activate  # Linux/Mac
# ppoxfamily\Scripts\activate  # Windows
```

### 3. 安装依赖

#### Windows用户特别说明
如果你在Windows上遇到编译错误，请先按照以下步骤操作：

**方法1: 安装Visual Studio Build Tools (推荐)**
1. 下载并安装 [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. 在安装时选择 "C++ build tools" 工作负载
3. 确保包含 "Windows 10 SDK" 和 "CMake tools"

**方法2: 使用conda安装预编译包**
```bash
# 优先使用conda安装可能有编译问题的包
conda install -c conda-forge opencv
conda install -c conda-forge gym

# 然后安装其他依赖
pip install torch numpy DI-engine DI-treetensor transformers
```

**方法3: 跳过游戏环境依赖**
如果你不需要运行第三章的Mario游戏环境，可以安装不包含游戏环境的核心依赖：
```bash
pip install -r requirements-minimal.txt  # 见下方创建的最小依赖文件
```

#### 标准安装流程
```bash
# 安装所有依赖
pip install -r requirements.txt

# 或者分步安装核心依赖
pip install torch numpy gym DI-engine DI-treetensor
```

## 分章节安装

如果你只想运行特定章节的代码，可以选择性安装依赖：

### 第一章 - 基础PPO算法
```bash
pip install torch numpy
```

### 第二章 - 动作空间处理
```bash
pip install torch numpy DI-engine DI-treetensor
```

### 第三章 - 观察空间处理
```bash
pip install torch numpy opencv-python gym-super-mario-bros nes-py DI-engine
```

### 第四章 - 奖励工程
```bash
pip install torch numpy DI-treetensor
```

### 第五章 - 时序建模
```bash
pip install torch numpy DI-engine DI-treetensor
```

### 第六章 - 多智能体学习
```bash
pip install torch numpy DI-treetensor
```

### 第七章 - 优化技巧
```bash
pip install torch numpy DI-treetensor
```

### 第八章 - 大模型应用
```bash
pip install torch numpy transformers gym
```

## 可选依赖

根据你的需求，可以安装以下可选依赖：

### 数据分析和可视化
```bash
pip install pandas matplotlib seaborn plotly
```

### 实验跟踪
```bash
pip install tensorboard wandb
```

### 开发工具
```bash
pip install jupyter ipython pytest black flake8
```

### 图像处理
```bash
pip install pillow
```

## 验证安装

运行以下命令验证安装是否成功：

```bash
# 测试第一章PPO算法
cd chapter1_overview
python ppo_zh.py

# 测试第三章环境包装器 (如果安装了游戏环境)
cd chapter3_obs
python mario_wrapper_zh.py
```

## 常见问题

### 1. Windows下nes-py编译失败
**错误信息**: `Microsoft Visual C++ 14.0 or greater is required`

**解决方案**:
```bash
# 方案A: 安装Visual Studio Build Tools
# 1. 下载: https://visualstudio.microsoft.com/visual-cpp-build-tools/
# 2. 安装时选择 "C++ build tools" 工作负载
# 3. 重新运行: pip install nes-py

# 方案B: 使用conda安装
conda install -c conda-forge nes-py

# 方案C: 跳过游戏环境，使用最小依赖
pip install -r requirements-minimal.txt
```

### 2. DI-engine 安装失败
```bash
# 尝试从源码安装
pip install git+https://github.com/opendilab/DI-engine.git

# 或使用conda
conda install -c opendilab DI-engine
```

### 3. gym-super-mario-bros 安装问题
```bash
# 确保安装了必要的系统依赖
# Ubuntu/Debian:
sudo apt-get install cmake zlib1g-dev

# macOS:
brew install cmake zlib

# Windows: 确保已安装Visual Studio Build Tools
```

### 4. CUDA 相关问题
```bash
# 检查CUDA版本
nvidia-smi

# 安装对应版本的PyTorch
# 访问 https://pytorch.org/get-started/locally/ 获取安装命令
```

### 5. 权限问题
```bash
# 使用用户安装
pip install --user -r requirements.txt
```

### 6. 网络连接问题
```bash
# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 或配置永久镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
```

## 平台特定说明

### Windows
- 确保安装了Microsoft Visual C++ Build Tools
- 推荐使用Anaconda/Miniconda管理Python环境
- 某些包可能需要从conda-forge安装

### macOS
- 确保安装了Xcode Command Line Tools: `xcode-select --install`
- 推荐使用Homebrew安装系统依赖

### Linux
- 确保安装了build-essential: `sudo apt-get install build-essential`
- 某些发行版可能需要额外的开发包

## 性能优化建议

1. **使用GPU**: 如果有NVIDIA GPU，安装CUDA版本的PyTorch
2. **内存优化**: 对于大模型应用，建议至少16GB内存
3. **并行处理**: 设置合适的线程数
   ```python
   import torch
   torch.set_num_threads(4)  # 根据CPU核心数调整
   ```

## 更新依赖

定期更新依赖以获得最新功能和bug修复：

```bash
pip install --upgrade -r requirements.txt
```

## 卸载

如果需要完全卸载：

```bash
# 删除虚拟环境
conda remove -n ppoxfamily --all  # conda环境
# 或直接删除venv文件夹

# 卸载全局安装的包
pip uninstall -r requirements.txt
```

## 技术支持

如果遇到安装问题，可以通过以下方式获取帮助：

- GitHub Issues: https://github.com/opendilab/PPOxFamily/issues
- 官方文档: https://opendilab.github.io/PPOxFamily/
- 社区讨论: OpenDILab Slack频道

## 故障排除检查清单

安装遇到问题时，请按以下顺序检查：

1. ✅ Python版本是否为3.7+
2. ✅ 是否在虚拟环境中
3. ✅ pip版本是否最新: `pip install --upgrade pip`
4. ✅ 网络连接是否正常
5. ✅ Windows用户是否安装了Visual C++ Build Tools
6. ✅ 是否有足够的磁盘空间
7. ✅ 是否有管理员权限（如需要） 