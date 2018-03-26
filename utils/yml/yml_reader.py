import yaml
from easydict import EasyDict as edict


with open('faster_rcnn_end2end.yml', 'r') as f:
    yaml_cfg = edict(yaml.load(f))
print(yaml_cfg)