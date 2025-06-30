import json
import argparse

def rescale_intrinsics(data, new_width=200, new_height=150):
    original_width = data["w"]
    original_height = data["h"]

    scale_x = new_width / original_width
    scale_y = new_height / original_height

    # Scale focal lengths and principal point
    data["fl_x"] *= scale_x
    data["fl_y"] *= scale_y
    data["cx"] *= scale_x
    data["cy"] *= scale_y

    # Update resolution
    data["w"] = new_width
    data["h"] = new_height

    # Recalculate FOV angles
    if "camera_angle_x" in data:
        data["camera_angle_x"] = 2 * (data["fl_x"] / new_width)
    if "camera_angle_y" in data:
        data["camera_angle_y"] = 2 * (data["fl_y"] / new_height)

    return data

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    updated_data = rescale_intrinsics(data, new_width=200, new_height=150)

    with open(output_file, 'w') as f:
        json.dump(updated_data, f, indent=4)

    print(f"✅ Scaled transforms.json saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rescale camera intrinsics in transforms.json to 200x150 resolution.")
    parser.add_argument("--input", required=True, help="Path to input transforms.json")
    parser.add_argument("--output", required=True, help="Path to output transforms.json")
    args = parser.parse_args()

    main(args.input, args.output)

