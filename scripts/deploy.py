from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    print(f"Ganache account is: {account}")

    # deploy the contract to a chain, and it returns a contract object because this is a state-changing function call
    simple_storage = SimpleStorage.deploy({"from": account})
    print(f"SimpleStorage returned object: {simple_storage}")
    stored_value = simple_storage.retrieve()
    print(f"The current stored value is: {stored_value}")
    update_stored_value = simple_storage.store(15, {"from": account})
    update_stored_value.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(f"The updated stored value is: {updated_stored_value}")


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
