from Block import Block
from BlockchainUtils import BlockChainUtils
from AccountModel import AccountModel


class Blockchain():

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()

    def addBlock(self, block):
        self.executeTransactions(block.transactions)
        self.blocks.append(block)
    
    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data['blocks'] = jsonBlocks
        return data
    
    def blockCountValid(self, block):
        if self.blocks[-1].blockCount == block.blockCount - 1:
            return True
        else:
            return False

    def lastBlockHashValid(self, block):
        lastBlockchainBlockHash = BlockChainUtils.hash(
            self.blocks[-1].payload()).hexdigest()
        if lastBlockchainBlockHash == block.lastHash:
            return True
        else:
            return False

    def getCoveredTransactionSet(self, transactions):
        CoveredTransactions = []
        for transaction in transactions:
            if self.transactionCovered(transaction):
                CoveredTransactions.append(transaction)
            else:
                print("Transaction is not covered by sender")
        return CoveredTransactions
    
    def transactionCovered(self, transaction):
        if transaction.type == 'EXCHANGE':
            return True
        senderBalance = self.accountModel.getBalance(
            transaction.senderpublickey)
        if senderBalance >= transaction.amount:
            return True
        else:
            return False

    def executeTransactions(self, transactions):
        for transaction in transactions:
            self.executeTransaction(transaction)
    
    def executeTransaction(self, transaction):
        sender = transaction.senderpublickey
        receiver = transaction.recieverpublickey
        amount = transaction.amount
        self.accountModel.updateBalance(sender, -amount)
        self.accountModel.updateBalance(receiver, amount)