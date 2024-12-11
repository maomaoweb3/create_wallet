import web3

w3 = web3.Web3()
# 要创建多少个钱包就把下面的10修改成对应的数值
wallet_num = 10
for i in range(wallet_num):
    account = w3.eth.account.create()
    print(account.address, w3.to_hex(account.key))
