class Block(object):
    def __init__(self, dictionary):
        '''
            we`re looking for index, timestamp, data, prev_hash, nonce
        '''
        for k, v in dictionary.items():
    setattr(self, k, v)
  if not hasattr(self, 'hash'): #in creating the first block, needs to be removed in future
    self.hash = self.create_self_hash()
                

            def __dict__(self):
                info = {}
                info['index'] = str(self.index)
                info['timestamp'] = str(self.timestamp)
                info['prev_hash'] = str(self.prev_hash)
                info['hash'] = str(self.hash)
                info['data'] = str(self.data)
                return info

            def __str__(self):
                return "Block<prev_hash: %s,hash: %s>" % (self.prev_hash, self.hash)

def create_first_block():
    block_data = {}
    block_data['index'] = 0
    block_data['timestamp'] = data.datetime.now()
    block_data['data'] = 'First block data'
    block_data['prev_hash'] = None
    block = Block(block_data)
    return block
