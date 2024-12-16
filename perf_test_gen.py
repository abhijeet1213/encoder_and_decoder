import json
import random
import string
import argparse

def generate_data(size, seed):
    random.seed(seed)
    data = {}
    data['title'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    data['members'] = [
        {'name': ''.join(random.choices(string.ascii_uppercase, k=5)), 'role': 'Developer'}
        for _ in range(size)
    ]
    data['completed'] = random.choice([True, False])
    data['budget'] = random.uniform(10000, 50000)
    data['deadline'] = None
    return data

def save_to_file(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f)

def main():
    parser = argparse.ArgumentParser(description='Generate test data')
    parser.add_argument('--size', type=int, required=True, help='Number of members in the generated data')
    parser.add_argument('--seed', type=int, required=True, help='Seed for random number generation')
    parser.add_argument('--output', type=str, required=True, help='Output file name')
    args = parser.parse_args()

    data = generate_data(args.size, args.seed)
    save_to_file(data, args.output)

if __name__ == '__main__':
    main()
