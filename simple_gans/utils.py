import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
lr = 3e-4
z_dim = 64
image_dim = 784
batch_size = 32
num_epochs = 50