from PIL import Image
import os
def show_image(image_path):
    """
    Load and display an image from the specified path.
    """
    try:
        # Load the image
        images = os.listdir(image_path)
        img = Image.open(image_path)
        
        # Display the image
        img.show()
        
        print(f"Image loaded and displayed from {image_path}")
    except Exception as e:
        print(f"Error loading image: {e}")

# Example usage
image_path = "tests/expected_results/bricks.jpg"
show_image(image_path)