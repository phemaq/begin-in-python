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
 #создание блока 
def create_first_block():
    block_data = {}
    block_data['index'] = 0
    block_data['timestamp'] = data.datetime.now()
    block_data['data'] = 'First block data'
    block_data['prev_hash'] = None
    block = Block(block_data)
    return block

    chaindata_dir = 'chaindata'
    if not os.path.exists(chaindata_dir):
        os.mkdir(chaindata_dir)
    if os.listdir(chaindata_dir) == []:
        first_block = create_first_block()
        first_block.self_save()



 #синхронизация блокчейна - локально
        def sync():
            node_blocks = []
            chaindata_dir = 'chaindata'
            if os.path.exists(chaindata_dir):
                for filename in os.listdir(chaindata_dir):
                    if filename.endswith('.json'):
                        filepath = '%s/%s' % (chaindata_dir, filename)
                        with open(filepath, 'r') as block_file:
                            block_info = json.load(block_file)
                            block_object = Block(block_info)

                            node_blocks.append(block_object)
                        return node_blocks
                        
