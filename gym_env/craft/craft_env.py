import gym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from gym import spaces


class CraftEnv(gym.Env):
    def __init__(self):
        super(CraftEnv, self).__init__()

        self.observation_space = spaces.Box(low=-1., high=1., shape=(1,), dtype=np.float32)
        self.action_space = spaces.Discrete(1)
        self.asset_path = "gym_env/craft/asset/"
        self.border_size = 5  # unit in pixel

    def step(self, action):
        raise NotImplementedError()

    def reset(self):
        return None

    def render(self, state):
        concatenate_images = []
        for row in state:
            images = [
                mpimg.imread(self.asset_path + item + ".png")[:, :, :3]
                for item in row]
            concatenate_image = np.concatenate(images, axis=1)
            concatenate_images.append(concatenate_image)
        rendered_image = np.concatenate(concatenate_images, axis=0)
        rendered_image = rendered_image[self.border_size:-self.border_size, self.border_size:-self.border_size, :]
        rendered_image = np.pad(rendered_image, pad_width=[(10, 10), (10, 10), (0, 0)], mode='constant')
        plt.imshow(rendered_image)
        plt.axis('off')
        plt.show()
