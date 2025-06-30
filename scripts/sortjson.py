import json
import argparse
import os

def sort_transforms_by_filepath(input_path, output_path):
    # Load the original JSON file
    with open(input_path, 'r') as f:
        data = json.load(f)

    # Sort the frames by 'file_path'
    data['frames'] = sorted(data['frames'], key=lambda x: x['file_path'])

    # Save to a new file
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Sorted file saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort transforms.json by file_path")
    parser.add_argument("--input", type=str, required=True, help="Path to input transforms.json")
    parser.add_argument("--output", type=str, default="transforms_sorted.json", help="Path to output sorted JSON")
    args = parser.parse_args()

    sort_transforms_by_filepath(args.input, args.output)
