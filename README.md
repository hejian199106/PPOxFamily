<div align="center">
    <a href="https://github.com/opendilab/PPOxFamily"><img width="500px" height="auto" src="https://github.com/opendilab/PPOxFamily/blob/main/assets/ppof_logo.png"></a>
</div>

# PPO x Family 决策智能入门公开课
欢迎来到 **PPO x Family** 系列决策智能入门公开课。该系列将深入理解深度强化学习算法 PPO ，灵活运用**一个 PPO 算法**解决几乎**所有常见的决策智能应用** ，帮助一切对于深度强化学习技术有好奇心的人，轻便且高效地制作应用原型，了解和学习最强大最易用的 PPO Family 。


P.S. 路过记得点个 star ![stars - ppof](https://img.shields.io/github/stars/opendilab/PPOxFamily?style=social) ，2022年12月起持续更新中~

## 🚀 快速开始

### 安装依赖

我们提供了多种安装方式，请根据你的需求选择：

```bash
# 方式1: 完整安装（推荐）
pip install -r requirements.txt

# 方式2: 核心依赖安装
pip install -r requirements-core.txt

# 方式3: 最小依赖安装（避免编译问题）
pip install -r requirements-minimal.txt

# 方式4: Windows用户一键安装
# 双击运行 install_windows.bat
```

### Windows用户特别说明

如果遇到 `nes-py` 编译错误，请：
1. 安装 [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. 或使用 `requirements-minimal.txt` 跳过游戏环境依赖
3. 详细说明请查看 [INSTALL.md](INSTALL.md)

### 验证安装

```bash
# 测试基础PPO算法
cd chapter1_overview
python ppo_zh.py
```

# News
- 2025.03.13: ❗️❗️Notice: 课程作业数据集及其他相关附加材料现已更新至 [HuggingFace](https://huggingface.co/OpenDILabCommunity/PPOxFamily/tree/main)
- 2023.06.07: PPO x Family 第八章（突破智能体终极界限）及课程大作业将在十月下旬正式上线
- 2023.06.01: [bilibili] [PPO x Family 第七章（挖掘黑科技）正式上线](https://www.bilibili.com/video/BV1ou4y1o7qY)
- 2023.04.06: [bilibili] [PPO x Family 第六章（统筹多智能体）正式上线](https://www.bilibili.com/video/BV1dg4y1g7BC)
- 2023.03.09: [bilibili] [PPO x Family 第五章（探索时序建模）正式上线](https://www.bilibili.com/video/BV1Uj411u7GA)
- 2023.02.23: [bilibili] [PPO x Family 第四章（解密稀疏奖励空间）正式上线](https://www.bilibili.com/video/BV15j411F7ni)
- 2023.01.16: [bilibili] [PPO x Family 第三章（表征多模态观察空间）正式上线](https://www.bilibili.com/video/BV1rK411r7Kg)
- 2022.12.23: [bilibili] [PPO x Family 第二章（解构复杂动作空间）正式上线](https://www.bilibili.com/video/BV1wv4y167w2)
- 2022.12.23: PPO x Family "算法-代码" 注解文档网站上线 [传送门](https://opendilab.github.io/PPOxFamily/)
- 2022.12.08: [bilibili] [PPO x Family 第一章（开启决策AI探索之旅）正式上线](https://www.bilibili.com/video/BV1cG4y137dJ)
- 2022.12.06: [bilibili] [PPO x Family 第一章微课视频：4分钟带你快速入门强化学习的万能钥匙](https://www.bilibili.com/video/BV1e841157Um/)
- 2022.12.05: [PaperWeekly] [给你一个 PPO × Family 课程，撑起整个决策 AI 宇宙](https://mp.weixin.qq.com/s/KCKfH1VnQGnNWW6svVxdXw)
- 2022.12.01: [bilibili] [PPO x Family 课程品牌宣传视频](https://www.bilibili.com/video/BV1sK411R7JP/?spm_id_from=333.337.search-card.all.click)
- 2022.11.30: [机器之心] [集中一点，演化无限：PPO × Family决策智能入门公开课即日开讲](https://mp.weixin.qq.com/s/l_JB3-BgLE2pEBJ2zgRkGQ)
- 2022.11.30: [中国计算机学会CCF] [【CCF科普群星计划】决策智能入门公开课开课啦](https://mp.weixin.qq.com/s/NkHi7eeUgQkp31R5Qgsbvw)



# 课程大纲

<div align="center">
    <a href="https://github.com/opendilab/PPOxFamily"><img width="1000px" height="auto" src="https://github.com/opendilab/PPOxFamily/blob/main/assets/outline.png"></a>
</div>

# 内容导航
| 章节（视频课） |  算法理论资料 | 补充资料 | 习题 | 代码样例                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 应用样例|
|------|-----|----------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ---|
| [第一章：开启决策AI探索之旅](https://www.bilibili.com/video/BV1cG4y137dJ) | [课程PPT](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/chapter1_lecture.pdf) <br> [课程文字稿](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/chapter1_manuscript.pdf) | [微课视频](https://www.bilibili.com/video/BV1e841157Um) <br> [策略梯度](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/chapter1_supp_pg.pdf) <br> [A2C](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/chapter1_supp_a2c.pdf) <br> [TRPO](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/chapter1_supp_trpo.pdf) <br> [符号表](https://github.com/opendilab/PPOxFamily/blob/main/common/notation.pdf) <br> [QA总结](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/chapter1_qa.pdf) | [习题](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/chapter1_homework.pdf) <br> [习题题解](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/chapter1_hw_solution.pdf) | [PG算法示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/pg_zh.py) <br> [A2C算法示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/a2c_zh.py) <br> [PPO算法示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter1_overview/ppo_zh.py)                                                                                                                                                                                                                                                                                                                                                                                                                     | [应用混剪](https://www.bilibili.com/video/BV1vW4y1M7cH/?spm_id_from=333.337.search-card.all.click) |
| [第二章：解构复杂动作空间](https://www.bilibili.com/video/BV1wv4y167w2) | [课程PPT](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/chapter2_lecture.pdf) <br> [课程文字稿](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/chapter2_manuscript.pdf) | [重参数化](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/chapter2_supp_reparameterization.pdf) <br> [PPO&DDPG](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/chapter2_supp_ppovsddpg.pdf) <br> [HyAR](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/chapter2_supp_hyar.pdf) <br> [QA总结](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/chapter2_qa.pdf) | [习题](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/chapter2_homework.pdf) <br> [习题题解](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/chapter2_hw_solution.pdf) | [离散动作示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/discrete_tutorial_zh.py) <br> [连续动作示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/continuous_tutorial_zh.py) <br> [混合动作示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/hybrid_tutorial_zh.py) <br> [应用训练代码](https://github.com/opendilab/PPOxFamily/blob/main/chapter2_action/chapter2_application_demo.py)                                                                                                                                                                                                                                                                    | [火箭回收等](https://github.com/opendilab/PPOxFamily/issues/4) |
| [第三章：表征多模态动作空间](https://www.bilibili.com/video/BV1rK411r7Kg) | [课程PPT](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/chapter3_lecture.pdf) <br> [课程文字稿](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/chapter3_manuscript.pdf) | [表征学习](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/chapter3_supp_representation.pdf) <br> [PPG](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/chapter3_supp_ppg.pdf) <br> [不变性](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/chapter3_supp_invariance.pdf) <br> [QA总结](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/chapter3_qa.pdf) | [习题](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/chapter3_homework.pdf) <br> [习题题解](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/chapter3_hw_solution.pdf) | [编码方法示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/encoding.py) <br> [Wrapper示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/mario_wrapper.py) <br> [计算图示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/gradient.py) <br>[应用训练代码](https://github.com/opendilab/PPOxFamily/blob/main/chapter3_obs/chapter3_application_demo.py)                                                                                                                                                                                                                                                                                                              | [软体机器人等](https://github.com/opendilab/PPOxFamily/issues/8) |
| [第四章：解密稀疏奖励空间](https://www.bilibili.com/video/BV15j411F7ni) | [课程PPT](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/chapter4_lecture.pdf) <br> [课程文字稿](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/chapter4_manuscript.pdf) | [逆强化学习](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/chapter4_supp_irl.pdf) <br> [行为克隆BC](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/chapter4_supp_bc.pdf) <br> [QA总结](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/chapter4_qa.pdf) | [习题](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/chapter4_homework.pdf) <br> [习题题解](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/chapter4_hw_solution.pdf) | [ICM好奇心奖励](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/curiosity_icm.py) <br> [RND好奇心奖励](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/curiosity_rnd.py) <br> [Pop-Art示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/popart.py) <br> [价值缩放](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/value_rescale.py) <br> [应用训练代码](https://github.com/opendilab/PPOxFamily/blob/main/chapter4_reward/chapter4_application_demo.py)                                                                                                                                                                                         | [自动驾驶等](https://github.com/opendilab/PPOxFamily/issues/44) |
| [第五章：探索时序建模](https://www.bilibili.com/video/BV1Uj411u7GA) | [课程PPT](https://github.com/opendilab/PPOxFamily/blob/main/chapter5_time/chapter5_lecture.pdf) | [随机性策略](https://github.com/opendilab/PPOxFamily/blob/main/chapter5_time/chapter5_supp_sto_det.pdf) <br> [RWKV](https://github.com/opendilab/PPOxFamily/blob/main/chapter5_time/chapter5_supp_rwkv.pdf) <br> [Belief MDP](https://github.com/opendilab/PPOxFamily/blob/main/chapter5_time/chapter5_supp_belief.pdf) <br> [QA总结](https://github.com/opendilab/PPOxFamily/blob/main/chapter5_time/chapter5_qa.pdf) | [习题](https://github.com/opendilab/PPOxFamily/blob/main/chapter5_time/chapter5_homework.pdf) <br> [习题题解](https://github.com/opendilab/PPOxFamily/blob/main/chapter5_time/chapter5_hw_solution.pdf) | [LSTM示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter5_time/lstm.py) <br> [GTrXL示例](https://github.com/opendilab/PPOxFamily/blob/main/chapter5_time/gtrxl.py) <br> [应用训练代码](https://github.com/opendilab/PPOxFamily/blob/main/chapter5_time/chapter5_application_demo.py)                                                                                                                                                                                                                                                                                                                                                                                                                 |  [记忆型决策](https://github.com/opendilab/PPOxFamily/issues/48) |
| [第六章：统筹多智能体](https://www.bilibili.com/video/BV1dg4y1g7BC) | [课程PPT](https://github.com/opendilab/PPOxFamily/blob/main/chapter6_marl/chapter6_lecture.pdf) | [HAPPO](https://github.com/opendilab/PPOxFamily/tree/main/chapter6_marl/chapter6_supp_happo.pdf) <br> [ACE](https://github.com/opendilab/PPOxFamily/blob/main/chapter6_marl/chapter6_supp_ace.pdf) <br> [值分解](https://github.com/opendilab/PPOxFamily/tree/main/chapter6_marl/chapter6_supp_value_dec.pdf) <br> [QA总结](https://github.com/opendilab/PPOxFamily/blob/main/chapter6_marl/chapter6_qa.pdf) | [习题](https://github.com/opendilab/PPOxFamily/blob/main/chapter6_marl/chapter6_homework.pdf) <br> [习题题解](https://github.com/opendilab/PPOxFamily/blob/main/chapter6_marl/chapter6_hw_solution.pdf) | [IndependentPG](https://github.com/opendilab/PPOxFamily/tree/main/chapter6_marl/independentpg.py) <br> [MAPG](https://github.com/opendilab/PPOxFamily/tree/main/chapter6_marl/mapg.py) <br> [MAPPO](https://github.com/opendilab/PPOxFamily/tree/main/chapter6_marl/mappo.py) <br> [HAPPO] <br> [应用训练代码](https://github.com/opendilab/PPOxFamily/blob/main/chapter6_marl/chapter6_application_demo.py)                                                                                                                                                                                                                                                                                                 | [多智能体协作](https://github.com/opendilab/PPOxFamily/issues/62) | 
| [第七章：挖掘黑科技](https://www.bilibili.com/video/BV1ou4y1o7qY) | [课程PPT](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/chapter7_lecture.pdf) | [Adv 估计](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/chapter7_supp_adv.pdf) <br> [PPO off 版](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/chapter7_supp_ppo_offpolicy.pdf) <br> [Entropy](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/chapter7_supp_entropy.pdf) <br> [QA总结](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/chapter7_qa.pdf) | [习题](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/chapter7_homework.pdf) <br> [习题题解](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/chapter7_hw_solution.pdf) | [GAE](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/gae.py) <br> [Recompute](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/recompute.py) <br> [梯度裁剪](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/grad_clip_norm.py) <br> [正交初始化](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/orthogonal_init.py) <br> [Dual Clip](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/dual_clip.py) <br> [Value Clip](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/value_clip.py) <br> [应用训练代码](https://github.com/opendilab/PPOxFamily/blob/main/chapter7_tricks/chapter7_application_demo.py) | [学术基准环境](https://github.com/opendilab/PPOxFamily/issues/79) |
| 第八章：突破终极界限 | | LLM RLHF | | [语言模型 RL 环境](https://github.com/opendilab/PPOxFamily/blob/main/chapter8_large/lm_env.py) | |

# 课程特点

## 一个算法解决万千应用 [视频传送门](https://www.bilibili.com/video/BV1vW4y1M7cH/?spm_id_from=333.337.search-card.all.click)
<div align="center">
    <a href="https://github.com/opendilab/PPOxFamily"><img width="1000px" height="auto" src="https://github.com/opendilab/PPOxFamily/blob/main/assets/ppof_application.jpg"></a>
</div>


## 算法理论和代码实现一一对应 [网站传送门](https://opendilab.github.io/PPOxFamily/)
<div align="center">
    <a href="https://github.com/opendilab/PPOxFamily"><img width="1000px" height="auto" src="https://github.com/opendilab/PPOxFamily/blob/main/assets/algo2code_demo.png"></a>
</div>

# 项目结构
```text
.
├── LICENSE
├── README.md                    --> 项目说明文档
├── INSTALL.md                   --> 详细安装指南
├── requirements.txt             --> 完整依赖列表
├── requirements-core.txt        --> 核心依赖列表
├── requirements-minimal.txt     --> 最小依赖列表（避免编译问题）
├── install_windows.bat          --> Windows一键安装脚本
├── 项目调研/                     --> 项目调研报告
│   └── 项目调研.md
├── assets/                      --> 相关图片素材（转载请注明来源）
├── common/                      --> 公共资源
│   ├── notation.pdf             --> 符号表
│   └── faq.pdf                  --> 常见问题FAQ
├── chapter1_overview/           --> 课程第一章相关内容
│   ├── chapter1_manuscript.pdf  --> 课程第一章文字稿（对于PPT的补充说明）
│   ├── chapter1_lecture.pdf     --> 课程第一章PPT
│   ├── chapter1_qa.pdf          --> 课程第一章答疑文稿
│   ├── chapter1_homework.pdf    --> 课程第一章习题作业
│   ├── chapter1_hw_solution.pdf --> 课程第一章习题作业题解
│   ├── chapter1_supp_*.pdf      --> 课程第一章补充材料（算法理论推导等）
│   └── *.py                     --> 课程第一章相关代码实现
├── chapter2_action/             --> 课程第二章：动作空间处理
├── chapter3_obs/                --> 课程第三章：观察空间处理
├── chapter4_reward/             --> 课程第四章：奖励工程
├── chapter5_time/               --> 课程第五章：时序建模
├── chapter6_marl/               --> 课程第六章：多智能体学习
├── chapter7_tricks/             --> 课程第七章：优化技巧
└── chapter8_large/              --> 课程第八章：大模型应用
```

# 课程答疑和反馈
- 常见问题FAQ：[传送门](https://github.com/opendilab/PPOxFamily/tree/main/common/faq.pdf)
- 小助手微信号：ding314assist
- Slack：[OpenDILab](https://join.slack.com/t/opendilab/shared_invite/zt-v9tmv4fp-nUBAQEH1_Kuyu_q4plBssQ)
- GitHub Issue区：[链接](https://github.com/opendilab/PPOxFamily/issues)
- B站账号：[OpenDILab](https://space.bilibili.com/1112854351?spm_id_from=333.337.0.0)
- 知乎账号：[DILab决策实验室](https://www.zhihu.com/people/dilab-46)
- Youtube：[OpenDILab](https://www.youtube.com/@opendilab)
- 邮箱：opendilab@pjlab.org.cn

# License
PPOxFamily is released under the Apache 2.0 license.
