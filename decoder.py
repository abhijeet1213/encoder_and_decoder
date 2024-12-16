# decoder.py

def decode(data):
    if not data:
        raise ValueError("Empty data encountered during decoding")

    data_type = data[0]

    if data_type == 0x01:  # Integer
        return decode_integer(data)
    elif data_type == 0x04:  # String
        return decode_string(data)
    elif data_type == 0x03:  # List
        return decode_list(data)

    raise ValueError(f"Unsupported data type for decoding: {data_type}")


def decode_integer(data):
    """Decodes an integer from little-endian byte sequence."""
    length = data[1]
    return int.from_bytes(data[2:2 + length], byteorder='little', signed=False), data[2 + length:]


def decode_string(data):
    """Decodes a string with length prefix."""
    length = data[1]
    return data[2:2 + length].decode('utf-8'), data[2 + length:]


def decode_list(data):
    """Decodes a list with length prefix."""
    length = data[1]
    list_data = []
    remaining_data = data[2:]

    for _ in range(length):
        item, remaining_data = decode(remaining_data)
        list_data.append(item)

    return list_data, remaining_data
