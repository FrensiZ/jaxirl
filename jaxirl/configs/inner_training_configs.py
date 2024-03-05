SPACE_INV_MINATAR_CONFIG = {
    "LR": 5e-3,
    "NUM_ENVS": 64,
    "NUM_STEPS": 128,
    "TOTAL_TIMESTEPS": 1e7,
    "NUM_UPDATES": 1e7 // 64 // 128,
    "ORIG_NUM_UPDATES": 1e7 // 64 // 128,
    "UPDATE_EPOCHS": 4,
    "NUM_MINIBATCHES": 8,
    "GAMMA": 0.99,
    "GAE_LAMBDA": 0.95,
    "CLIP_EPS": 0.2,
    "ENT_COEF": 0.01,
    "VF_COEF": 0.5,
    "MAX_GRAD_NORM": 0.5,
    "ACTIVATION": "relu",
    "ENV_NAME": "SpaceInvaders-MinAtar",
    "ANNEAL_LR": False,
}


REACHER_CONFIG = {
    "LR": 3e-4,
    "NUM_ENVS": 128,
    "NUM_STEPS": 100,
    "NUM_UPDATES": 100,
    "ORIG_NUM_UPDATES": 100,
    "UPDATE_EPOCHS": 10,
    "NUM_MINIBATCHES": 10,
    "GAMMA": 0.99,
    "GAE_LAMBDA": 0.95,
    "CLIP_EPS": 0.2,
    "ENT_COEF": 0.01,
    "VF_COEF": 0.5,
    "MAX_GRAD_NORM": 0.5,
    "ACTIVATION": "relu",
    "ENV_NAME": "Reacher-misc",
    "ANNEAL_LR": False,
    "DEBUG": False,
    "NORMALIZE_ENV": False,
    "DISCRETE": False,
}

GRIDWORLD_CONFIG = {
    "LR": 0.001,
    "NUM_ENVS": 256,
    "NUM_STEPS": 30,
    "NUM_UPDATES": 100,
    "ORIG_NUM_UPDATES": 100,
    "UPDATE_EPOCHS": 10,
    "NUM_MINIBATCHES": 10,
    "GAMMA": 0.99,
    "GAE_LAMBDA": 0.95,
    "CLIP_EPS": 0.2,
    "ENT_COEF": 0.01,
    "VF_COEF": 0.5,
    "MAX_GRAD_NORM": 0.5,
    "ACTIVATION": "tanh",
    "ENV_NAME": "gridworld",
    "ANNEAL_LR": False,
    "DEBUG": False,
    "NORMALIZE_ENV": False,
    "DISCRETE": True,
}

CARTPOLE_CONFIG = {
    "LR": 2.5e-4,
    "NUM_ENVS": 4,
    "NUM_STEPS": 128,
    "TOTAL_TIMESTEPS": 5e5,
    "NUM_UPDATES": 5e5 // 4 // 128,
    "ORIG_NUM_UPDATES": 5e5 // 4 // 128,
    "UPDATE_EPOCHS": 4,
    "NUM_MINIBATCHES": 4,
    "GAMMA": 0.99,
    "GAE_LAMBDA": 0.95,
    "CLIP_EPS": 0.2,
    "ENT_COEF": 0.01,
    "VF_COEF": 0.5,
    "MAX_GRAD_NORM": 0.5,
    "ACTIVATION": "tanh",
    "ENV_NAME": "CartPole-v1",
    "ANNEAL_LR": False,
    "DEBUG": False,
    "NORMALIZE_ENV": False,
    "DISCRETE": True,
}

BRAX_CONFIG = {
    "LR": 3e-4,
    "NUM_ENVS": 2048,
    "NUM_STEPS": 10,
    "NUM_UPDATES": 5e7 // 2048 // 10,
    "ORIG_NUM_UPDATES": 5e7 // 2048 // 10,
    "TOTAL_TIMESTEPS": 5e7,
    "UPDATE_EPOCHS": 4,
    "NUM_MINIBATCHES": 32,
    "GAMMA": 0.99,
    "GAE_LAMBDA": 0.95,
    "CLIP_EPS": 0.2,
    "ENT_COEF": 0.0,
    "VF_COEF": 0.5,
    "MAX_GRAD_NORM": 0.5,
    "ACTIVATION": "tanh",
    "ENV_NAME": "brax",
    "ANNEAL_LR": False,
    "NORMALIZE_OBS": True,
    "DEBUG": False,
    "DISCRETE": False,
}

PENDULUM_CONFIG = {
    "LR": 1e-3,
    "NUM_ENVS": 64,
    "NUM_STEPS": 16,
    "TOTAL_TIMESTEPS": 2e6,
    "NUM_UPDATES": 2e6 // 64 // 16,
    "ORIG_NUM_UPDATES": 2e6 // 64 // 16,
    "UPDATE_EPOCHS": 4,
    "NUM_MINIBATCHES": 8,
    "GAMMA": 0.99,
    "GAE_LAMBDA": 0.95,
    "CLIP_EPS": 0.2,
    "ENT_COEF": 0.01,
    "VF_COEF": 0.5,
    "MAX_GRAD_NORM": 1.0,
    "ACTIVATION": "tanh",
    "ENV_NAME": "Pendulum-v1",
    "ANNEAL_LR": False,
    "DEBUG": False,
    "NORMALIZE_ENV": False,
    "DISCRETE": False,
}
