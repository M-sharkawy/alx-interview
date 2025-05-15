#!/usr/bin/python3
"""model for detecting validUTF8"""


def validUTF8(data):
    """validUTF8"""
    num_bytes = 0

    for byte in data:
        # Only use the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's
            mask = 0b10000000
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1-byte character
            if num_bytes == 0:
                continue

            # Invalid scenarios
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Continuation bytes must start with 10xxxxxx
            if not (byte & 0b10000000 and not (byte & 0b01000000)):
                return False

        num_bytes -= 1

    return num_bytes == 0
