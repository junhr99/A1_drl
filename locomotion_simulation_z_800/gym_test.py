import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import PPO2
from stable_baselines.common.evaluation import evaluate_policy

# multiprocess environment
env = gym.make('locomotion:A1GymEnv-v1', render=True)
'''
model = PPO2(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=250)
model.save("ppo2_cartpole")

del model # remove to demonstrate saving and loading
'''

model = PPO2.load("PPO_A1_z_40hr")

#mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

# Enjoy trained agent
obs = env.reset()
i=0
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render(mode='rgb_array')


'''
import gym
env = gym.make('locomotion:A1GymEnv-v1', render=True)

from absl import app
from absl import flags
from tqdm import tqdm

from locomotion.envs import env_builder
from locomotion.robots import a1
from locomotion.robots import laikago
from locomotion.robots import robot_config

FLAGS = flags.FLAGS
flags.DEFINE_enum('robot_type', 'A1', ['A1', 'Laikago'], 'Robot Type.')
flags.DEFINE_enum('motor_control_mode', 'Torque',
                  ['Torque', 'Position', 'Hybrid'], 'Motor Control Mode.')
flags.DEFINE_bool('on_rack', False, 'Whether to put the robot on rack.')

ROBOT_CLASS_MAP = {'A1': a1.A1, 'Laikago': laikago.Laikago}

MOTOR_CONTROL_MODE_MAP = {
    'Torque': robot_config.MotorControlMode.TORQUE,
    'Position': robot_config.MotorControlMode.POSITION,
    'Hybrid': robot_config.MotorControlMode.HYBRID
}


def main(_):
  robot = ROBOT_CLASS_MAP[FLAGS.robot_type]
  motor_control_mode = MOTOR_CONTROL_MODE_MAP[FLAGS.motor_control_mode]
  env = env_builder.build_regular_env(robot,
                                      motor_control_mode=motor_control_mode,
                                      enable_rendering=True,
                                      on_rack=FLAGS.on_rack)

  env.reset()
  for _ in tqdm(range(1000)):
    _, _, done, _ = env.step(env.action_space.sample())
    

if __name__ == "__main__":
  app.run(main)
'''
