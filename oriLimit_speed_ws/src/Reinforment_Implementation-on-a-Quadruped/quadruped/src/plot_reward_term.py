import matplotlib.pyplot as plt
import numpy as np

x = np.load('reward_x.npy')
ori = np.load('reward_ori.npy')
z = np.load('reward_z.npy')

plt.title('Reward Term')

plt.plot(x,label='forward')
plt.plot(ori, label='orientation')
plt.plot(z, label='fall down')
plt.legend()
plt.show()
