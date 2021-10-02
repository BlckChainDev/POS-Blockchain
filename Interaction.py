from Wallet import Wallet
from BlockchainUtils import BlockChainUtils
import requests

if __name__ == '__main__':
    bob = Wallet()
    alice = Wallet()
    exchange = Wallet()

    transaction = exchange.createTransaction(
        alice.publicKeyString(), 10, 'EXCHANGE')

    url = 'http://localhost:5000/transaction'
    package = {'transaction': BlockChainUtils.encode(transaction)}
    request = requests.post(url, json=package)
    print(request.text)
