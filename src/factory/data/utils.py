import torch


def is_torch_tensor(x):
    return type(x) == torch.tensor or type(x) == torch.Tensor


def _cudaify(x):
    
    if type(x) == dict:
        return {k:v.cuda() if is_torch_tensor(v) else v for k,v in x.items()}

    if type(x) in [tuple, list]:
        return type(x)([_.cuda() if is_torch_tensor(_) else _cudaify(_) for _ in x])

    return x.cuda()


def cudaify(batch, labels): return _cudaify(batch), _cudaify(labels)


def _mpsify(x):

    if type(x) == dict:
        return {k:v.to("mps") if is_torch_tensor(v) else v for k,v in x.items()}

    if type(x) in [tuple, list]:
        return type(x)([_.to("mps") if is_torch_tensor(_) else _mpsify(_) for _ in x])

    return x.to("mps")


def mpsify(batch, labels): return _mpsify(batch), _mpsify(labels)


def _isnone(x): return isinstance(x, type(None))
