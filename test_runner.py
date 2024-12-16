# test_runner.py
import json
from encoder import encode
from decoder import decode


def run_tests():
    # Load the JSON test vectors from the file
    with open('test_vectors.json', 'r') as f:
        test_vectors = json.load(f)["test_vectors"]

    for test in test_vectors:
        name = test["name"]
        input_data = test["input"]

        print(f"Running test: {name}")

        # Encode the input data
        encoded_data = encode(input_data)
        print(f"Encoded: {encoded_data}")

        # Decode the encoded data
        decoded_data, _ = decode(encoded_data)
        print(f"Decoded: {decoded_data}")

        # You can add custom checks here or leave it for manual inspection
        print(f"Test {name} finished.\n")


if __name__ == "__main__":
    run_tests()
