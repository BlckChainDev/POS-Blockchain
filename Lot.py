from BlockchainUtils import BlockChainUtils


class Lot():

    def __init__(self, publicKey, iteraction, lastBlockHash):
        self.publicKey = str(publicKey)
        self.iteraction = iteraction
        self.lastBlockHash = lastBlockHash
    
    def lotHash(self):
        hashData = self.publicKey + self.lastBlockHash
        for _ in range(self.iteraction):
            hashData = BlockChainUtils.hash(hashData).hexdigest()
        return hashData
