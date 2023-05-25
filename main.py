import argparse
import gymnasium as gym
import numpy as np
import matplotlib.image as mpimg
from gymnasium import Wrapper


class RenderWrapper(Wrapper):
    def __init__(self, env, mapping):
        super().__init__(env)
        self.env = env
        self.mapping = mapping

        # define map of agent direction to word
        self.DIR_TO_WORD = {
            0: "right",
            1: "down",
            2: "left",
            3: "up"
        }

    def pad_boundary(self, image, pad_width=10):
        """
        pad image boundary by first removing image boundary (gray color) and then
        pad with black color boundary

        :param numpy.ndarray image: image to apply padding
        :param int pad_width: size of padding to apply
        :return: padded image
        :rtype: numpy.ndarray
        """
        # remove image boundary (gray color)
        image = image[5:-5, 5:-5, :]

        # pad with black boundary
        pad_width = [(pad_width, pad_width), (pad_width, pad_width), (0, 0)]
        padded_image = np.pad(image, pad_width=pad_width, mode='constant')

        return padded_image

    def render(self):
        """
        render minigrid environment to craft environment
        this function assumes that minigrid setup is similar to craft environment
        setup, where walls are placed only around the grid

        :return: rendered craft image
        :rtype: numpy.ndarray
        """
        # get minigrid map which has object indices, where each object index
        # corresponds to self.IDX_TO_OBJECT
        minigrid = self.env.grid.encode()

        # initialize rendered_image
        rendered_image = []

        # loop through minigrid and construct rendered_image
        for row in range(minigrid.shape[0]):
            image_row = []
            for col in range(minigrid.shape[1]):
                if row == self.env.agent_pos[0] and col == self.env.agent_pos[1]:
                    # render agent
                    direction = self.DIR_TO_WORD[self.env.agent_dir]
                    cell_image = mpimg.imread("asset/agent_" + direction + ".png")[:, :, :3]
                    image_row.append(cell_image)
                else:
                    # render objects
                    key = (minigrid[row, col][0], minigrid[row, col][-1])
                    cell = self.mapping[key]
                    if cell == "wall":
                        continue
                    else:
                        cell_image = mpimg.imread("asset/" + cell + ".png")[:, :, :3]
                        image_row.append(cell_image)

            if len(image_row) > 0:
                image_row = np.concatenate(image_row, axis=1)
                rendered_image.append(image_row)

        # concatenate and then pad rendered_image
        rendered_image = np.concatenate(rendered_image, axis=0)
        rendered_image = self.pad_boundary(rendered_image)
        return rendered_image


def main(args):
    # initialize env
    # env = gym.make("MiniGrid-Fetch-5x5-N2-v0")
    env = gym.make("SGMG-Crafting-Bonus-v0")

    # define map of minigrid object index to craft object
    # minigrid object index ref: https://github.com/Farama-Foundation/Minigrid/blob/
    # 34bfa2a6b3a963d7557ef43efa5e556fc8a6ca83/minigrid/core/constants.py#L24
    IDX_TO_OBJECT = {
        (1, 0): "empty",
        (2, 0): "wall",
        (13, 0): "wood",
        (13, 1): "grass",
        (13, 2): "iron",
        (14, 3): "toolshed",
        (14, 4): "workbench",
        (14, 5): "factory"
    }

    # apply render wrapper with custom mapping
    env = RenderWrapper(env, mapping=IDX_TO_OBJECT)

    # visualize env
    env.reset()
    image = env.render()
    mpimg.imsave("craft.png", image)


if __name__ == "__main__":
    # set argparse
    parser = argparse.ArgumentParser(description="rendering craft env")
    args = parser.parse_args()

    # run main
    main(args=args)
