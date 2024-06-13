import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max size

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def extract_colors(image_path, num_colors=5):
    try:
        image = Image.open(image_path)
        image = image.convert('RGB')  # Ensure image is in RGB mode
        image = image.resize((100, 100))  # Resize for faster processing
        image_np = np.array(image)
        image_np = image_np.reshape((image_np.shape[0] * image_np.shape[1], 3))

        kmeans = KMeans(n_clusters=num_colors, n_init=10)
        kmeans.fit(image_np)
        colors = kmeans.cluster_centers_.astype(int)
        labels = kmeans.labels_

        # Calculate the percentage of each color
        label_counts = np.bincount(labels)
        total_count = len(labels)
        color_percentages = label_counts / total_count * 100

        return list(zip(colors, color_percentages))
    except Exception as e:
        print(f"Error during color extraction: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                print("No file part in the request")
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                print("No selected file")
                return redirect(request.url)
            if file and file.filename:  # Check if a file is selected and has a filename
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                colors = extract_colors(filepath)
                if colors is None or not isinstance(colors, list) or len(colors) == 0:
                    print("Failed to extract colors or colors array is empty")
                    return redirect(request.url)

                os.remove(filepath)  # Clean up the uploaded file

                return render_template('index.html', colors=colors)

        return render_template('index.html')
    except Exception as e:
        print(f"Error in the main route: {e}")
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
