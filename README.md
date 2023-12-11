# CAPTCHA Generator 🤖

This Python script generates a customizable `CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart)` image with randomly colored characters and different fonts >ᴗ< .

## Prerequisites 🛠️

- Python (3.x recommended) 🐍
- Python Imaging Library (PIL) or Pillow 🖼️

## Installation ⚙️

1. Clone the repository or download the `captcha.py` file.

2. Install the required Python libraries using pip:

    ```bash
    pip install Pillow
    ```

3. Ensure you have TTF font files in the specified paths (e.g., `arial.ttf`, `times.ttf`, `calibri.ttf`). You can replace these paths with your own font files.

## Usage 🚀

1. Modify the `generate_captcha()` function in `captcha.py` to suit your preferences, such as text length, image dimensions, and font paths.

2. Run the script using the command:

    ```bash
    python captcha.py
    ```

3. The script will generate a CAPTCHA image (`captcha.png`) with random characters, colors, and fonts. The generated text will be printed in the terminal.

## Customization 🎨

- Adjust the `text_length`, `image_width`, and `image_height` parameters in `generate_captcha()` to change the length and size of the CAPTCHA.
  
- Add or remove font paths in the `font_paths` list to use different fonts for the CAPTCHA characters.

- Modify the color generation logic or font sizes to suit your preferences by updating the code within the `generate_captcha()` function.

## Notes ℹ️

- Ensure the font files exist in the specified paths. Update the font paths in the code to reflect the actual locations of your font files.

- This code provides a basic personal example of CAPTCHA generation.
