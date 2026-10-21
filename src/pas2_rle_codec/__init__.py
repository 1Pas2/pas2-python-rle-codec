def encode(data: bytes) -> bytes:
    out = bytearray()
    for value in data:
        if out and out[-1] == value and out[-2] < 255:
            out[-2] += 1
        else:
            out.extend((1, value))
    return bytes(out)


def decode(data: bytes, max_output: int = 1_000_000) -> bytes:
    if type(max_output) is not int or max_output < 0 or len(data) % 2:
        raise ValueError("Invalid encoded length or output limit")
    size = sum(data[::2])
    if 0 in data[::2] or size > max_output:
        raise ValueError("Invalid run or output limit exceeded")
    return b"".join(bytes([data[i + 1]]) * data[i] for i in range(0, len(data), 2))
