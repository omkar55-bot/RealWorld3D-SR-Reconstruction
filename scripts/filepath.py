import json
import argparse
import os

def fix_paths(data):
    for frame in data.get("frames", []):
        old_path = frame["file_path"]
        # Remove leading './' and trailing file extension
        fixed_path = os.path.splitext(old_path.lstrip("./"))[0]
        frame["file_path"] = fixed_path
    return data

def main(input_json, output_json):
    with open(input_json, 'r') as f:
        data = json.load(f)

    updated_data = fix_paths(data)

    with open(output_json, 'w') as f:
        json.dump(updated_data, f, indent=4)

    print(f"✅ Updated file paths saved to: {output_json}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fix file paths in transforms.json")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Path to output JSON file")
    args = parser.parse_args()

    main(args.input, args.output)

