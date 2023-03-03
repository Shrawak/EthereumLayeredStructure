from web3 import Web3

# define the sender and receiver addresses
sender_address = '0x16Ce18876E2feCFFa33274F77AbE311f5b448b97'
receiver_address = '0xEcff2eb6fC0f7fCBEe5a5B534C774A3eb01EB090'

# connect to the Ethereum network
# Get
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))


# set the sender's private key
private_key = '0c41fe451dda139680418e3cd32e9e4a92fa430d079f8d906f9c9f22d92e1038'

# create the transaction object
transaction = {
    'to': receiver_address,
    'value': w3.toWei(2, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei'),
    'nonce': w3.eth.getTransactionCount(sender_address)
}

# sign the transaction
signed_transaction = w3.eth.account.signTransaction(transaction, private_key)

# send the transaction
tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

# get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# print the transaction receipt
print(tx_receipt)

#
# See blockID and also explore the transaction details from the ganache block explorer application
#