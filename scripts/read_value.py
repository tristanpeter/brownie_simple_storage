from brownie import SimpleStorage, accounts, network, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    print(f"The contract is {simple_storage}")
    retrieved_value = simple_storage.retrieve()
    print(f"The retrieved value is: {retrieved_value}")


def main():
    read_contract()
