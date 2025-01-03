import cv2
from facenet_pytorch import MTCNN


class FaceDetection:
    def __init__(self):
        self.mtcnn = MTCNN()

    def detect_faces(self, image_path):
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Failed to load the image.")

        # Convert the image to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detect faces and probabilities
        boxes, probs = self.mtcnn.detect(image_rgb)

        return image, boxes, probs

    def annotate_image(self, image, boxes, probs, confidence_threshold=0.5):
        if boxes is not None:
            for box, prob in zip(boxes, probs):
                if prob is not None and prob > confidence_threshold:
                    x1, y1, x2, y2 = map(int, box)
                    color = (0, 255, 0)  # Green for bounding box
                    thickness = 2

                    # Draw the bounding box
                    cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)

                    # Display confidence score
                    text = f"{prob:.2f}"
                    font_scale = 0.5
                    font_thickness = 1
                    cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                font_scale, color, font_thickness, cv2.LINE_AA)
        return image
    def count_faces(self, image_path, confidence_threshold=0.5):
        """
        Returns the number of faces detected in the image with a probability
        greater than the specified confidence threshold.
        """
        _, boxes, probs = self.detect_faces(image_path)
        if boxes is not None and probs is not None:
            count = sum(1 for prob in probs if prob is not None and prob > confidence_threshold)
            return count
        return 0