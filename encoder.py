# encoder.py

def encode(data):
    if data is None:
        return b''  # Encode None as empty byte sequence

    if isinstance(data, int):
        return encode_integer(data)

    if isinstance(data, str):
        return encode_string(data)

    if isinstance(data, list):
        return encode_list(data)

    raise ValueError(f"Unsupported data type for encoding: {type(data)}")

def encode_integer(value):
    """Encodes an integer into little-endian format."""
    return value.to_bytes((value.bit_length() + 7) // 8, byteorder='little', signed=False)

def encode_string(value):
    """Encodes a string as length-prefixed UTF-8."""
    encoded_string = value.encode('utf-8')
    return bytes([len(encoded_string)]) + encoded_string

def encode_list(values):
    """Encodes a list as length-prefixed sequence of encoded elements."""
    encoded_list = b''.join([encode(value) for value in values])
    return bytes([len(values)]) + encoded_list
