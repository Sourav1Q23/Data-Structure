class Pair(object):
    """
        holds key, value pairs
    """
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.is_deleted = False

class Hashtable(object):
    """
        A Simple implementation of a Hash Table
    """
    def __init__(self):

        self.table = [None] * 10
        self.load_factor = .75
        self.current_size = 0

    def __setitem__(self, key, item):
        """
            Stores the (key, value) pair in the table
            implements open addressing collision resolution
            using linear probing
        """
        t_length = len(self.table)
        entry = Pair(key, item)
        hashValue = hash(key)        
        for i in range(t_length):
            probeValue = self._probing_function(i)    
            index= (probeValue + hashValue) % t_length
            
            if self.table[index] is None or self.table[index].is_deleted:
                self.table[index] = entry 
                self.current_size += 1
                if float(self.current_size) / len(self.table) >= self.load_factor:
                    self.__resize_table()           
                break
            elif self.table[index].key==key:
                self.table[index].value = item
                break
        if i> t_length:
            raise Exception("Cycle detected. Chane Your Probing function")
    

    def __getitem__(self, key):
        """
            gets the value associated with the key
        """
        hashValue = hash(key)

        for i in range(len(self.table)):
            probeValue = self._probing_function(i)    
            index= (probeValue + hashValue) % t_length
            if self.table[index] is not None:
                if self.table[index].key == key:
                    if self.table[index].is_deleted:
                        raise KeyError('Key is not in the table')
                    else:
                        return self.table[index].value

            elif self.table[index] is None:
                raise KeyError('Key is not in the table')

        raise KeyError('Key is not in the table')
 
    
    def _probing_function(self,x):
        """
        For linear probing, function ax+b, here a is 3 and b is 0  
        """
        return 3*x

    def __resize_table(self):
        new_table = [None] * (len(self.table) * 2)
        for i, entry in enumerate(self.table):
            if entry is None or entry.is_deleted==False:
                continue
            for i in range(len(new_table)):
                index = (hash(entry.key)+self. _probing_function(i))% len(new_table)
                if self.table[index] is None:
                    self.table[index] = entry 
                    break

        self.table = new_table

    def delete(self, key):
        """
            deletes a value from the hash table
        """
        hashValue = self.hash(key)
        
        for i in range(len(self.table)):
            index = (hashValue + self._probing_function(i))% len(self.table)

            if self.table[index] is not None:
                if self.table[index].key == key:
                    if self.table[index].is_deleted:
                        raise KeyError('Key is not in the table')
                    else:
                        self.table[index].is_deleted = True
                        self.current_size -= 1
                        break
    
        raise KeyError('Key is not in the table')
        
    def getkeys(self):
        keys =[]
        for i , entry  in enumerate(self.table):
            if entry ==None:
                continue
            keys.append(entry.key)
        return keys

    def entries(self):
        entries = []
        for i, entry in enumarate(self.table):
            if entry == None:
                continue
            entries.append(tuple([entry.key , entry.value]))
        return entries        