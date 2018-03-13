
import logging
import os

import torch


def check_environ():
    if 'PROJECT_NAME' not in os.environ:
        raise EnvironmentError('Must source bin/setenv.sh from the root prior to running')


def get_cuda_info():
    """The purpose of this function is to check whether CUDA is available and whether
       we should run on single or multi gpu mode.
    """
    use_cuda = False
    multi_gpu = False

    if torch.cuda.is_available() and os.environ['CUDA_VISIBLE_DEVICES'] != "":
        gpu_ids = os.environ['CUDA_VISIBLE_DEVICES'].split()
        use_cuda = True
        logging.info('CUDA support is active')

        if len(gpu_ids) > 1:
            logging.info('MultiGPU support is active')
            multi_gpu = True

    return use_cuda, multi_gpu


def save_checkpoint(experiment_dir, epoch, state, is_best=False):
    """Saves the current model state for later use.
    """
    if is_best:
        filename = os.path.join(experiment_dir, 'model_best.pth.tar')
    else:
        filename = os.path.join(experiment_dir, 'model_{:04d}.pth.tar'.format(epoch))

    torch.save(state, filename)


def create_experiment_dir(experiment_id):
    """Create the experiment directory where results will be saved
    """
    output_dir = os.environ[os.environ['PROJECT_NAME'] + '_OUTPUT_DIR']
    experiment_dir = os.path.join(output_dir, experiment_id)
    checkpoints_dir = os.path.join(experiment_dir, 'checkpoints')
    results_dir = os.path.join(experiment_dir, 'results')

    if not os.path.isdir(experiment_dir):
        os.mkdir(experiment_dir)
        os.mkdir(checkpoints_dir)
        os.mkdir(results_dir)

    return experiment_dir, checkpoints_dir, results_dir


class AverageMeter(object):
    """Used to keep the average of values such as Loss and Precision
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum = val * n
        self.count += n
        self.avg = self.sum / self.count
