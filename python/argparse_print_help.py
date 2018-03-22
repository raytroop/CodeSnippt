import argparse
import sys


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Train a Fast R-CNN network')
    # parser.add_argument('--gpu', dest='gpu_id',
    #                     help='GPU device id to use [0]',
    #                     default=0, type=int)
    parser.add_argument('--solver', dest='solver',
                        help='solver prototxt',
                        default=None, type=str)
    parser.add_argument('--iters', dest='max_iters',
                        help='number of iterations to train',
                        default=40000, type=int)
    parser.add_argument('--weights', dest='pretrained_model',
                        help='initialize with pretrained model weights',
                        default=None, type=str)
    parser.add_argument('--cfg', dest='cfg_file',
                        help='optional config file',
                        default=None, type=str)
    parser.add_argument('--imdb', dest='imdb_name',
                        help='dataset to train on',
                        default='voc_2007_trainval', type=str)
    parser.add_argument('--rand', dest='randomize',
                        help='randomize (do not use a fixed seed)',
                        action='store_true')
    parser.add_argument('--set', dest='set_cfgs',
                        help='set config keys', default=None,
                        nargs=argparse.REMAINDER)
    # for arg in sys.argv:
    #     print(arg)      # parser.py

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()

# rtp@ubuntu:~/test$ python parser.py 
# usage: parser.py [-h] [--solver SOLVER] [--iters MAX_ITERS]
#                  [--weights PRETRAINED_MODEL] [--cfg CFG_FILE]
#                  [--imdb IMDB_NAME] [--rand] [--set ...]

# Train a Fast R-CNN network

# optional arguments:
#   -h, --help            show this help message and exit
#   --solver SOLVER       solver prototxt
#   --iters MAX_ITERS     number of iterations to train
#   --weights PRETRAINED_MODEL
#                         initialize with pretrained model weights
#   --cfg CFG_FILE        optional config file
#   --imdb IMDB_NAME      dataset to train on
#   --rand                randomize (do not use a fixed seed)
#   --set ...             set config keys