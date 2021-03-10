class HashTable:  
    def __init__(self):
        self.size = 10
        self.table = [[] for i in range(self.size)]
    
    def _get_hash(self,key):
        return hash(key) % self.size

    def __getitem__(self, key):
        index = self._get_hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]
            
    def __setitem__(self, key, val):
        table_index = self._get_hash(key)
        found = False
        for i, entry in enumerate(self.table[table_index]):
            if len(entry)==2 and entry[0] == key:
                self.table[table_index][i] = (key,val)
                found = True
        if not found:
            self.table[table_index].append((key,val))
        
    def __delitem__(self, key):
        table_index = self._get_hash(key)
        for idx, entry in enumerate(self.table[table_index]):
            if entry[0] == key:
                print("del",idx)
                del self.table[table_index][idx]
