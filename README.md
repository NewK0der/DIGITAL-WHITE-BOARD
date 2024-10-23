# 🖌️ Scrollable Digital Whiteboard

This project is a **digital whiteboard** application built using Python's `Tkinter` library. It offers a variety of features to simulate a real whiteboard for drawing, writing, and manipulating images. The whiteboard supports pencil drawing, color selection, image addition, erasing, and image movement within a scrollable interface, allowing for an extended canvas space.

## Features

### 1. Pencil Tool
- Draw anywhere on the canvas with customizable color and pencil size.
- If an image is inserted, you can draw directly on the image as well as on the canvas.
- The pencil tool is disabled when moving an image, ensuring clean drawing without accidental image shifts.

### 2. Eraser Tool
- Erase content from the canvas with a brush size adjustable from the toolbar.
- If an image is inserted, the eraser tool can:
  - **Move the image** when the cursor is over the image (image movement mode).
  - **Erase the canvas** when the cursor is not over the image.
- This distinction ensures smooth interaction with both the image and canvas.

### 3. Image Insertion and Manipulation
- You can insert images from your local system and place them anywhere on the canvas.
- When the eraser tool is selected, the image can be moved around by dragging it.
- Images are automatically resized to fit within the canvas area.

### 4. Color and Size Customization
- Change the pencil's color using a color picker.
- Adjust the size of the pencil or eraser dynamically using the slider.

### 5. Scrollable Canvas
- The canvas is scrollable both horizontally and vertically, allowing you to navigate and draw on different parts of a larger canvas.
- Drawing coordinates are adjusted to allow drawing on any part of the canvas, even after scrolling.

### 6. Clear All
- Quickly clear all drawings and images from the canvas, resetting the workspace.

## Download the `.exe` Version
For users who prefer to run the application without setting up Python or dependencies, you can download the executable version:

- [Download Digital Whiteboard `.exe`](https://github.com/NewK0der/DIGITAL-WHITE-BOARD/releases/tag/v1.0.0)

*Note: The `.exe` file is available for Windows systems.*

## Usage

1. **Pencil Tool**: Click on the pencil icon to select the pencil tool, choose a color, and adjust the pencil size using the slider. You can now draw on the canvas or any inserted image.
   
2. **Eraser Tool**: Click on the eraser icon to select the eraser tool. You can erase canvas content by clicking on the empty canvas. If an image is inserted, the eraser will switch to image-movement mode when the cursor is over the image.

3. **Add Image**: Click on the image icon to select an image from your local file system. Once the image is added, you can move it with the eraser tool or draw on it with the pencil tool.

4. **Scroll and Navigate**: Use the scrollbars or your mouse’s scroll wheel to move across the canvas and navigate different areas.

## Installation

1. **Clone the Repository**:
    ```bash
    (https://github.com/NewK0der/DIGITAL-WHITE-BOARD.git)
    ```

2. **Install Dependencies**:
    The project requires Python's `Pillow` library for image handling:
    ```bash
    pip install pillow
    ```

3. **Run the Application**:
    Navigate to the project directory and run the application:
    ```bash
    python whiteboard.py
    ```

## Future Enhancements

- **Save Canvas**: Implement the ability to save the entire canvas as an image file (e.g., PNG or JPEG).
- **Undo/Redo**: Add undo/redo functionality to revert or restore drawing actions.
- **Multiple Pages**: Support multiple whiteboard pages for easier switching between different drawing sessions.
- **Shape Drawing**: Add the ability to draw basic shapes (rectangles, circles, etc.) on the canvas.

## Contributing

Feel free to contribute by submitting pull requests, reporting issues, or suggesting features. Any contributions to improve the project are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
