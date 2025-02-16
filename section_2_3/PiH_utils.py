import os
import torch

def checkpoint(best_f1, iteration, model, dir):
    """Saves the parameters of the generator G and discriminator D.
    """
    ckpt_path = os.path.join(dir, 'ckpt_{:06d}.pth.tar'.format(iteration))
    torch.save({'model': model.state_dict(),
                'best_f1': best_f1,
                'iter': iteration}, 
               ckpt_path)
    print('Saved checkpoint: {}'.format(ckpt_path))