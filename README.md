# Color Analysis Tool

This project is a web-based application that analyzes and classifies the colors present in uploaded images. It identifies the primary colors and provides details on various shades along with their percentages.

## Features

- Upload an image to the web application.
- Extract primary colors from the uploaded image.
- Display the primary colors with their respective RGB values and percentages.
- User-friendly interface with attractive design.

## Technologies Used

- Python
- Flask
- Pillow (Python Imaging Library)
- NumPy
- Scikit-learn (KMeans Clustering)
- HTML/CSS
- JavaScript (for form handling)

## Project Structure

```
color_analysis_tool/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
└── requirements.txt
```

## Setup and Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/color_analysis_tool.git
    cd color_analysis_tool
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:
    
        ```bash
        venv\Scripts\activate
        ```
        
    - On macOS/Linux:
    
        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask Application:**

    ```bash
    python app.py
    ```

6. **Open the Application in Your Browser:**

    - Navigate to `http://127.0.0.1:5000/` in your web browser.

## Usage

1. **Upload an Image:**
    - Click the "Choose File" button to select an image from your computer.
    - Click the "Upload Image" button to submit the image.

2. **View Extracted Colors:**
    - After the image is processed, the primary colors will be displayed on the page along with their RGB values and percentages.

## Example Output

The application will display the extracted colors in blocks, each showing the RGB value and the percentage of that color in the uploaded image.

![Example Output](https://i.imgur.com/Qu6uHcK.png)

## Troubleshooting

- **No Colors Displayed:**
  - Ensure the uploaded image is in a valid format (JPEG, PNG).
  - Check the console where you ran `python app.py` for error messages.

- **Port Conflict:**
  - If you encounter an `Address already in use` error, specify a different port when running Flask:
  
    ```bash
    python app.py --port=5001
    ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
