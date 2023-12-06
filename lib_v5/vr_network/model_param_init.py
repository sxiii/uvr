import json

default_param = {
    'bins': -1,
    'unstable_bins': -1,
    'stable_bins': -1,
    'sr': 44100,
    'pre_filter_start': -1,
    'pre_filter_stop': -1,
    'band': {},
}
N_BINS = 'n_bins'

def int_keys(d):
    r = {}
    for k, v in d:
        if k.isdigit():
            k = int(k)
        r[k] = v
    return r
    
class ModelParameters(object):
    def __init__(self, config_path=''):
        with open(config_path, 'r') as f:
                self.param = json.loads(f.read(), object_pairs_hook=int_keys)

        for k in ['mid_side', 'mid_side_b', 'mid_side_b2', 'stereo_w', 'stereo_n', 'reverse']:
            if k not in self.param:
                self.param[k] = False

        if N_BINS in self.param:
            self.param['bins'] = self.param[N_BINS]