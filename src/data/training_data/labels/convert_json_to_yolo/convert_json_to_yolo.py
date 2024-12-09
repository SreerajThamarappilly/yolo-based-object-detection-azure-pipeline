import json
import os

def convert_json_to_yolo(json_file, output_dir, image_width, image_height, class_mapping):
    """
    Converts PixLab Annotate JSON file to YOLO format.
    
    Args:
        json_file (str): Path to the .json file.
        output_dir (str): Directory to save the .txt files.
        image_width (int): Width of the annotated image.
        image_height (int): Height of the annotated image.
        class_mapping (dict): Mapping of label names to YOLO class IDs.
    """
    # Load JSON
    with open(json_file, "r") as f:
        data = json.load(f)

    # Get the base name for the output .txt file
    base_name = os.path.splitext(os.path.basename(json_file))[0]
    output_path = os.path.join(output_dir, f"{base_name}.txt")

    with open(output_path, "w") as yolo_file:
        for item in data:
            rect = item["rectMask"]
            label_name = item["labels"]["labelName"]

            # Convert to YOLO format
            x_min = rect["xMin"]
            y_min = rect["yMin"]
            width = rect["width"]
            height = rect["height"]

            x_center = (x_min + width / 2) / image_width
            y_center = (y_min + height / 2) / image_height
            norm_width = width / image_width
            norm_height = height / image_height

            # Get class ID
            class_id = class_mapping.get(label_name, -1)
            if class_id == -1:
                raise ValueError(f"Label {label_name} not found in class mapping!")

            # Write to YOLO file
            yolo_file.write(f"{class_id} {x_center:.6f} {y_center:.6f} {norm_width:.6f} {norm_height:.6f}\n")

    print(f"YOLO labels saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Input JSON file
    input_json = "./people3.json"
    # Output directory for YOLO .txt files
    output_dir = "./"
    os.makedirs(output_dir, exist_ok=True)

    # Image dimensions (replace with your image's actual dimensions)
    image_width = 640
    image_height = 480

    # Class mapping (e.g., "person" -> 0)
    class_mapping = {"person": 0}

    # Convert
    convert_json_to_yolo(input_json, output_dir, image_width, image_height, class_mapping)
