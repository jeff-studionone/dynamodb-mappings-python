def build_from_model(data):
    """ Mapping all data and building the data structure that is required for DynamoDB
        There are some special validations such as int should be type N but in string format
        Parameters
        ----------
        data : dict | list | tuple | set
            List of all attributes to insert into the db
        Returns
        -------
        response : dict {'M': data}
    """
    mappings = {
        dict: 'M',
        int: 'N',
        float: 'N',
        str: 'S',
        list: 'L',
        tuple: 'L',
        set: 'L',
        bool: 'BOOL',
        bytes: 'S',
    }

    # check data type
    value_type = type(data)

    # map any of this types to string format S
    if value_type in [str, int, float]:
        return {mappings[value_type]: str(data)}

    # map any of these types to a dynamodb List format L
    if value_type in [tuple, list, set]:
        return {mappings[value_type]: [build_from_model(value) for value in data]}

    # map any of these types to a dynamodb dictionary format M
    if value_type is dict:
        return {mappings[value_type]: {str(key): build_from_model(value) for key, value in data.items()}}

    # map any of this type to a dynamodb string format S
    if value_type is bytes:
        return {mappings[value_type]: data.decode('utf-8')}

    # map any of this type to a dynamodb bool format BOOL
    if value_type is bool:
        return {mappings[value_type]: data}

    raise TypeError('[ERROR] build_from_model This {} Data type is not supported.'.format(value_type))

def get_from_model(data):
    """ Normalizing the data back from DynamoDB to a readable and friendly data
        The problem here is that we loss the tuples format and set format and they become
        into a list.
        Parameters
        ----------
        data : dict
            List of all attributes to insert into the db
        Returns
        -------
        response : dict
    """
    mappings = ['M', 'N', 'S', 'L', 'BOOL']
    value_type = list(data.keys())[0]

    if value_type in mappings:
        data = data[value_type]

        if value_type == 'N':
            for type_cast in [int, float]:
                try:
                    return type_cast(data)
                except ValueError:
                    pass

        if value_type == 'S':
            return str(data)

        if value_type == 'BOOL':
            return bool(data)

        if value_type == 'L':
            return [get_from_model(value) for value in data]

        if value_type == 'M':
            return {key: get_from_model(value) for key, value in data.items()}

    raise TypeError('[ERROR] get_from_model This ({}) Data type is not supported. {}'.format(value_type, data))
