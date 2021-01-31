import torch
import numpy as np

from libs import tpcpath
from torchpcp.utils import pytorch_tools
# pytorch_tools.set_seed(0)
device = pytorch_tools.select_device("cuda")

from libs.dataset import SimpleSceneDataset
from torch.utils.data import DataLoader
from torchpcp.modules.functional.sampling import furthest_point_sampling
from torchpcp.modules.functional.nns import py_k_nearest_neighbors
from torchpcp.modules.functional.nns import k_nearest_neighbors as knn
from torchpcp.utils.monitor import timecheck
from torchpcp.modules.functional.other import gather, index2points

# PointRCNN impl. from https://github.com/sshaoshuai/PointRCNN
import pointnet2_cuda as pointnet2
from typing import Tuple

dataset = SimpleSceneDataset()
loader = DataLoader(
    dataset,
    batch_size=2,
    num_workers=8,
    pin_memory=True,
    shuffle=False
)

for data in loader:
    point_clouds, sem_label, ins_label = data
    point_clouds = point_clouds[:, :3].to(device)
    center_idxs = furthest_point_sampling(point_clouds, 1024)
    outs = gather(point_clouds, center_idxs)
    print(outs)
    exit()


