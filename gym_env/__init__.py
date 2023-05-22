from gym.envs.registration import register


register(
    id='craftenv-v0',
    entry_point='gym_env.craft.craft_env:CraftEnv'
)
