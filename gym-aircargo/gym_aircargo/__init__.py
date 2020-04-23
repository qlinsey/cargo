import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Cargo-v0',
    entry_point='gym_aircargo.envs:CargoEnv',
    timestep_limit=1000,
    reward_threshold=100000.0,
    nondeterministic = True,
)

