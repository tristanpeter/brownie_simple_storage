from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange (includes deploying because this is more of the setup than the test)
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    expected = 20
    tx = simple_storage.store(expected, {"from": account})
    tx.wait(1)

    # Assert
    assert 6 == simple_storage.retrieve()
