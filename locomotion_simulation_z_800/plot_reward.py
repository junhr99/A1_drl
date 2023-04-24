import matplotlib.pyplot as plt
import numpy as np

z = np.load('reward_z.npy')

plt.title('Reward Term')

plt.plot(z, label='z reward')
plt.legend()
plt.show()

