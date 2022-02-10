from torch.utils.data import Dataset 
import pandas as pd 

class ImageDataset(Dataset):
    def __init__(self, path, chunk_size):
        self.chunk_size = chunk_size
        self.reader = pd.read_csv(path)

    def __len__(self):
        return self.len
    
    def __getitem__(self):
        pass 