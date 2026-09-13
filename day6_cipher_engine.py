import numpy as np

class LearnableCipherEngine:
    def __init__(self, block_size, r=3.999):
        self.B=block_size
        self.r=r

    def _generate_chaotic_key(self, x0,size):
        key=np.zeros(size)
        x=x0
        for i in range(size):
            x=self.r*x*(1-x)
            key[i]=x
        return key

    def encrypt_frame(self, frame):
        # Resize for block alignment
        h=(frame.shape[0] // self.B) * self.B
        w=(frame.shape[1] // self.B) * self.B
        frame = frame[:h, :w]
        num_blocks = (h // self.B) * (w // self.B)

        # Extract blocks
        blocks = [frame[i*self.B:(i+1)*self.B, j*self.B:(j+1)*self.B] 
                  for i in range(h // self.B) for j in range(w // self.B)]

        # Shuffle using chaotic map
        key_shuffle = self._generate_chaotic_key(0.1234, num_blocks)
        perm_order = np.argsort(key_shuffle)
        shuffled_blocks = np.array(blocks)[perm_order]

        encrypted_frame = np.zeros_like(frame)
        idx = 0
        for i in range(h // self.B):
            for j in range(w // self.B):
                encrypted_frame[i*self.B:(i+1)*self.B, j*self.B:(j+1)*self.B] = shuffled_blocks[idx]
                idx += 1
                
        return encrypted_frame

    