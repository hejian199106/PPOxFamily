# Please install latest DI-engine's main branch first
# And we will release DI-engine v0.4.6 version with stable and tuned configuration of these demos.
from ding.bonus import PPOF  # 导入 PPOF 类

# 月球着陆器离散动作空间
def lunarlander_discrete():
    # Please install lunarlander env first, `pip3 install box2d`
    agent = PPOF(env='lunarlander_discrete', exp_name='./lunarlander_discrete_demo') # 创建 PPOF 对象
    agent.train(step=int(1e5))  # 训练
    # Classic RL interaction loop and save replay video
    agent.deploy(enable_save_replay=True)  # 部署

# 月球着陆器连续动作空间
def lunarlander_continuous():
    # Please install lunarlander env first, `pip3 install box2d`
    # 设置随机种子
    agent = PPOF(env='lunarlander_continuous', exp_name='./lunarlander_continuous_demo', seed=314)
    # 训练
    agent.train(step=int(1e5))
    # 批量评估
    agent.batch_evaluate(env_num=4, n_evaluator_episode=8)

# 火箭回收
def rocket_landing():
    # Please install rocket env first, `pip3 install git+https://github.com/nighood/rocket-recycling@master#egg=rocket_recycling`
    # 创建 PPOF 对象
    agent = PPOF(env='rocket_landing', exp_name='./rocket_landing_demo')
    # 训练
    agent.train(step=int(5e6), context='spawn')

# 无人机飞行
def drone_fly():
    # Please install gym_pybullet_drones env first, `pip3 install git+https://github.com/zjowowen/gym-pybullet-drones@master`
    # 创建 PPOF 对象
    agent = PPOF(env='drone_fly', exp_name='./drone_fly_demo')
    # 训练
    agent.train(step=int(5e6))

# 混合移动
def hybrid_moving():
    # Please install gym_hybrid env first, refer to the doc `https://di-engine-docs.readthedocs.io/zh_CN/latest/13_envs/gym_hybrid_zh.html`
    # 创建 PPOF 对象
    agent = PPOF(env='hybrid_moving', exp_name='./hybrid_moving_demo')
    # 训练
    agent.train(step=int(5e6))

# 运行测试
if __name__ == "__main__":
    # You can select and run your favorite demo  
    # 选择并运行你喜欢的 demo
    lunarlander_discrete()  # 月球着陆器离散动作空间    
    # lunarlander_continuous()  # 月球着陆器连续动作空间
    # rocket_landing()  # 火箭回收
    # drone_fly()  # 无人机飞行
    # hybrid_moving()  # 混合移动
