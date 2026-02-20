import uuid

def guid_to_ldap_filter(guid_string):
    """
    Convert a GUID string to LDAP filter format.

    Args:
        guid_string: GUID as string (e.g., '12345678-1234-1234-1234-123456789abc')

    Returns:
        LDAP filter string for objectGUID attribute
    """
    # Parse the GUID string
    guid = uuid.UUID(guid_string)

    # Convert to bytes
    guid_bytes = guid.bytes_le  # Use little-endian byte order for AD

    # Convert each byte to \XX format
    ldap_format = ''.join(f'\\{byte:02x}' for byte in guid_bytes)

    # Return as LDAP filter
    return f"(objectGUID={ldap_format})"


def guid_bytes_to_ldap_filter(guid_bytes):
    """
    Convert GUID bytes directly to LDAP filter format.

    Args:
        guid_bytes: GUID as bytes (16 bytes)

    Returns:
        LDAP filter string for objectGUID attribute
    """
    ldap_format = ''.join(f'\\{byte:02x}' for byte in guid_bytes)
    return f"(objectGUID={ldap_format})"


# Example usage
if __name__ == "__main__":
    # Example GUID
    example_guid = "a2b9312c-f112-44e0-bbb1-22e1fdb6f5c3"

    # Convert to LDAP filter
    ldap_filter = guid_to_ldap_filter(example_guid)

    print(f"Original GUID: {example_guid}")
    print(f"LDAP Filter: {ldap_filter}")

    # Example with bytes
    guid_obj = uuid.UUID(example_guid)
    ldap_filter2 = guid_bytes_to_ldap_filter(guid_obj.bytes_le)
    print(f"From bytes: {ldap_filter2}")

    # Verify they match
    print(f"\nFilters match: {ldap_filter == ldap_filter2}")