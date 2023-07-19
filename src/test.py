class Data:
    """  
    Author - Johann9616@gmail.com
    
    Build a Pythonic data model class `Data` with the following requirements:

    1. loads a dictionary and can save to dictionary: `to_dict`, `from_dict`
    2. ability to instantiate directly from the class
    3. default value: can define a default value for attributes
    4. autocomplete
    5. dynamic and general usability for the class (easily define new data structures)
    6. ability to reflect inner value on the main level
    """
    def __init__(self, data=None, default=None, **kwargs):
        """Initializes the data instance

        Args:
            data (dict, optional): current dict. Defaults to None.
            default (dict, optional): default dict. Defaults to None.
        """
        self._data = {} if data is None else data
        self._default = default or {}
        self._data.update(kwargs)

    @classmethod
    def from_dict(cls, data_dict, default=None):
        """Creates a new Data instance from a dictionary.

        Args:
            data_dict (dict): Dictionary to initialize the Data instance.
            default (dict, optional): Default dictionary. Defaults to None.

        Returns:
            Data: The instantiated Data object.
        """
        return cls(data_dict, default)

    def to_dict(self):
        """Converts the Data instance to a dictionary.

        Returns:
            dict: The dictionary representation of the Data instance.
        """
        return self._data

    def me(self):
        """Converts the Data instance to a dictionary.

        Returns:
            dict: The dictionary representation of the Data instance.
        """
        return self.metadata

    def __getattr__(self, name, value=100):
        """Get attribute, if doesn't exist, it will a new attribute with the key and deafult value

        Args:
            name (str):  Name of the attribute.
            value (int, optional): Value for new attribute added. Defaults to 100.

        Returns:
            Any: The value of the attribute.
        """    
        if name in self._data:
            value = self._data[name]
            if isinstance(value, dict):
                return Data(value, self._default)
            return value
        elif name in self._default:
            return self._default[name]
        else:
            # Add the attribute as a new attribute
            self._data[name] = value
            return f"Key not found, new Key added as {name}:{value}"


    def __setattr__(self, name, value):
        """Handles attribute assignment.

        Args:
            name (str): Name of the attribute.
            value (Any): Value to assign to the attribute.
        """
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            self._data[name] = value

    def __delattr__(self, name):
        """Handles attribute deletion.

        Args:
            name (str): Name of the attribute.
        """
        if name in self._data:
            del self._data[name]

    def __repr__(self):
        """Returns a string representation of the Data instance.

        Returns:
            str: The string representation of the Data instance.
        """
        return repr(self._data)
    

if __name__ == "__main__":
    data = {
        "id": "1",
        "name": "first",
        "metadata": {
            "system": {
                "size": 10.7
            },
            "user": {
                "batch": 10
            }
        }
    }

    # load from dict
    my_inst_1 = Data.from_dict(data)
    # load from inputs
    my_inst_2 = Data(name="my")
    # reflect inner value
    print(my_inst_1.metadata.system.size)  # should print 10.7

    # default values
    print(my_inst_1.metadata.system.height)  # should set a default value of 100 in metadata.system.height
    print(my_inst_1.to_dict()['metadata']['system']['height'])  # should print the default value

    # autocomplete - should complete to metadata
    print(my_inst_1.me())