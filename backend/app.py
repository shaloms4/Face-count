from flask import Flask, request, jsonify
from face_detection import FaceDetection
import os
import cv2
from flask_cors import CORS, cross_origin
from PIL import Image, ExifTags


app = Flask(__name__)
CORS(app)
face_detector = FaceDetection()

# Endpoint to detect faces and return bounding boxes and probabilities


@app.route('/detect_faces', methods=['POST'])
def detect_faces():
    try:
        # Check if image file is provided
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400

        # Save the uploaded file temporarily
        image_file = request.files['image']
        image_path = os.path.join('temp', image_file.filename)
        os.makedirs('temp', exist_ok=True)
        image_file.save(image_path)

        # Detect faces
        image, boxes, probs = face_detector.detect_faces(image_path)

        # Annotate the image
        annotated_image = face_detector.annotate_image(
            image.copy(), boxes, probs)

        # Save the annotated image for response
        annotated_image_path = os.path.join(
            'temp', 'annotated_' + image_file.filename)
        cv2.imwrite(annotated_image_path, annotated_image)

        # Clean up uploaded file
        os.remove(image_path)

        # Return the response with the bounding boxes
        response = {
            'boxes': boxes.tolist() if boxes is not None else [],
            'probs': probs.tolist() if probs is not None else []
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Additional endpoint to return the number of faces detected


def rotate_image_left(image_path):
    try:
        with Image.open(image_path) as img:
            # Rotate image 90° to the left (counterclockwise)
            rotated_img = img.transpose(Image.ROTATE_90)
            img.save(image_path)
            print("image is roteted")  # Save the rotated image back
    except Exception as e:
        print(f"Error rotating image: {e}")
        raise e


@app.route('/count_faces', methods=['POST'])
def count_faces():
    try:
        # Check if image file is provided

        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400

        # Parse confidence threshold from request (default to 0.5)

        # Save the uploaded file temporarily
        image_file = request.files['image']
        image_path = os.path.join('temp', image_file.filename)
        os.makedirs('temp', exist_ok=True)
        image_file.save(image_path)

        rotate_image_left(image_path)
        # Count the number of faces
        face_count = face_detector.count_faces(image_path)

        # Clean up uploaded file
        # os.remove(image_path)

        # Return the response with the face count
        return jsonify({'face_count': face_count}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

