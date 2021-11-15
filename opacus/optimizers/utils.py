from typing import List

import torch.nn as nn
from torch.optim import Optimizer


def params(optimizer: Optimizer) -> List[nn.Parameter]:
    ret = []
    for param_group in optimizer.param_groups:
        ret += [p for p in param_group["params"] if p.requires_grad]
    return ret
