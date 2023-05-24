# gym-craftenv-render
code for rendering the craft environment in ["Modular Multitask Reinforcement Learning with Policy Sketches"](https://arxiv.org/pdf/1611.01796.pdf) (Andreas, Klein, Levine. ICML 2017) by using ["minigrid environment"](https://minigrid.farama.org/)

## Dependency
Known dependencies are (please refer to `requirements.txt`):
```
gym==0.26.2
matplotlib==3.7.1
minigrid
gymnasium==0.28.1
```

## Setup
To avoid any conflict, please install virtual environment with [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/):
```
pip3.11 install --upgrade virtualenv
```
Please note that all the required dependencies will be automatically installed in the virtual environment by running the script (`run.sh`).

## Run
Please run code by running the script `run.sh`.

The code should reproduce the following image:
![alt text](https://github.com/dkkim93/gym-craftenv-render/blob/main/craft.png)
