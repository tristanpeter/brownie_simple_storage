// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0; // any version of 0.6 up to 0.7

contract SimpleStorage {
    // declare a variable called favouriteNumber
    uint256 favouriteNumber;

    // create a struct called People with two parameters
    struct People {
        uint256 favouriteNumber;
        string name;
    }

    // create a dynamic array of People objects called people
    People[] public people;

    // create a public mapping called nameToFavouriteNumber.
    mapping(string => uint256) public nameToFavouriteNumber;

    // create a public function called addPerson, which takes two arguments _name and _favouriteNumber
    function addPerson(string memory _name, uint256 _favouriteNumber) public {
        // use the push method to add the persons to te people array created above
        people.push(People(_favouriteNumber, _name));
        // Use the mapping function created above to map the key (string: _name) to the uint: _favouriteNumber
        nameToFavouriteNumber[_name] = _favouriteNumber;
    }

    // create a store function which defines the memory type, and assigns _favouriteNumber to favouriteNumber
    function store(uint256 _favouriteNumber) public returns (uint256) {
        favouriteNumber = _favouriteNumber;
        return favouriteNumber;
    }

    // create a function to retrieve the favouriteNumber value. Pure and view functions are non-transaction functions (don't change state).
    function retrieve() public view returns (uint256) {
        return favouriteNumber;
    }
}
