from shibainu.user import User
import torch
import numpy as np
import toml


dummy = """
[[users]]
name = "Taro"
age = 1

[[users]]
name = "Jiro"
age = 2
"""


if __name__ == '__main__':
    data = toml.loads(dummy)
    for user_setting in data['users']:
        user = User(**user_setting)
        user.message()

    print(np.arange(3))
    print(torch.cuda.is_available())
