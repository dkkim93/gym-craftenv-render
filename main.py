import gym
import gym_env  # noqa
import argparse


def main(args):
    # initialize env
    env = gym.make(args.env_name)

    # reset env
    env.reset()

    # render env
    state = [
        ["blank", "blank", "workbench", "blank", "blank"],
        ["iron", "blank", "blank", "blank", "blank"],
        ["blank", "blank", "blank", "blank", "blank"],
        ["agent_right", "blank", "blank", "blank", "blank"],
        ["blank", "blank", "blank", "wood", "toolshed"]
    ]
    env.render(state)


if __name__ == "__main__":
    # set argparse
    parser = argparse.ArgumentParser(description="rendering craft env")
    parser.add_argument(
        "--env-name", type=str, default="craftenv-v0",
        help="OpenAI gym environment name")
    args = parser.parse_args()

    main(args=args)
