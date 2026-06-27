import hashlib
import time
import json

class Block:
    def __init__(self, index, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        # NEW: The 'nonce' is the random number we guess to solve the math puzzle
        self.nonce = nonce 
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # We now include the nonce in the string we are mathematically scrambling
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        # We want our hash to start with a specific number of zeros (e.g., "0000")
        target_zeros = "0" * difficulty
        
        # Keep guessing a new nonce until our hash successfully starts with those zeros
        while self.hash[:difficulty] != target_zeros:
            self.nonce += 1
            self.hash = self.calculate_hash()
            
        print(f"✅ Block Mined! Nonce found: {self.nonce} | Hash: {self.hash}")
