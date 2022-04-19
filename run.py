from web3 import Web3
import dotenv
import os
import sys
import time
import abi
import config

# path to working directory
dir_path = os.path.dirname(os.path.realpath(__file__))
dotenv.load_dotenv(dir_path + '/.env')
# connect to blockchain
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
# check if .env file exist and correct address
try:
    address = web3.toChecksumAddress(os.environ['ADDRESS'])
    balance = web3.eth.getBalance(os.environ['ADDRESS'])
    balance = web3.fromWei(balance, 'ether')
except:
    with open(dir_path + '/log.txt', 'a') as file:
        print('Set correct .env file witch ADDRESS and KEY')
        file.write("Set correct .env file witch ADDRESS and KEY\n")
    sys.exit()

contract_adres = web3.toChecksumAddress(
    "0xe2d26507981a4daaaa8040bae1846c14e0fb56bf")
ref = web3.toChecksumAddress("0xf81a4D3e44Daa168cdD9a0b97AA62F528e298858")
contract = web3.eth.contract(address=contract_adres, abi=abi.ABI)
miners = contract.functions.getMyMiners(address).call()


def reBake():
    nonce = web3.eth.get_transaction_count(address)

    tx = contract.functions.hatchEggs(ref).buildTransaction({
        'nonce': nonce,
        'gas': 150000,  # that's enough
        'gasPrice': web3.toWei('5', 'gwei'),
    })

    signed_tx = web3.eth.account.sign_transaction(
        tx, private_key=os.environ['KEY'])
    txn = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    with open(dir_path + '/log.txt', 'a') as file:
        file.write(
            f"{time.strftime(format('%d.%m %H:%M'))} RE-BAKE {miners}\n")


def eatBake():
    pass


def main():
    if balance < config.MIN_BALANCE:
        with open(dir_path + '/log.txt', 'a') as file:
            file.write(
                f"{time.strftime(format('%d.%m %H:%M'))} Balance too low \n")
        sys.exit()

    reBake()


if __name__ == "__main__":
    main()
