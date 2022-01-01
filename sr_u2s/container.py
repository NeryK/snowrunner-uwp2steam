"""Parse UWP container file"""
import argparse
import struct

def decode_hash(hash_bytes):
    new_hash_bytes = bytearray()
    new_hash_bytes.append(hash_bytes[3])
    new_hash_bytes.append(hash_bytes[2])
    new_hash_bytes.append(hash_bytes[1])
    new_hash_bytes.append(hash_bytes[0])
    new_hash_bytes.append(hash_bytes[5])
    new_hash_bytes.append(hash_bytes[4])
    new_hash_bytes.append(hash_bytes[7])
    new_hash_bytes.append(hash_bytes[6])
    return new_hash_bytes.hex().upper() + hash_bytes[8:].hex().upper()

def parse_file_bytes(bytes):
    filepath = bytes[:-32].decode("utf-16").strip("\x00")
    hash1 = decode_hash(bytes[-32:-16])
    hash2 = decode_hash(bytes[-16:])
    if hash1 != hash2:
        raise ValueError(f"Inconsistent hash for {filepath}")
    return filepath, hash1

def load_container(container_path):
    save_files = []
    with open(container_path, "rb") as containerfile:
        _header = struct.unpack("I", containerfile.read(4))[0]
        numfiles = struct.unpack("I", containerfile.read(4))[0]
        for i in range(numfiles):
            save_files.append(parse_file_bytes(containerfile.read(160)))
    return save_files

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-container", help="UWP container.xyz file", required=True)
    args = parser.parse_args()

    save_list = load_container(args.input_container)
    print(save_list)
