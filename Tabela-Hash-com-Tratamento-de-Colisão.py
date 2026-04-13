class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        # Verifica se a chave já existe para atualizar
        for i, kv in enumerate(self.table[hash_key]):
            k, v = kv
            if key == k:
                self.table[hash_key][i] = (key, value)
                return
        # Se não houver colisão exata de chave, adiciona ao final (Chaining)
        self.table[hash_key].append((key, value))
