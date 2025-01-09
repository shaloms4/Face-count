# Face-count
Face-Count App

Face-Count is a simple app that uses the MTCNN model for face detection and counting. The backend is built with Flask, and the frontend is developed using Flutter. Since the backend doesn't run continuously, it will be hosted locally. This README provides step-by-step instructions for setting up and running the project on your local machine.

Prerequisites

Before getting started, ensure you have the following installed on your system:

Python 3.x

Pip (Python package manager)

Flutter SDK

Visual Studio Code (or any preferred IDE)

Git

How to Set Up and Run the App

Follow these steps to clone, set up, and run the Face-Count app:

1. Clone the Repository

Open a terminal (Command Prompt, PowerShell, or any preferred terminal) and run the following command:

git clone https://github.com/shaloms4/Face-count

2. Navigate to the Project Directory

Change your directory to the cloned repository:

cd Face-count

3. Open the Project in an IDE

To open the project in Visual Studio Code, run:

code .

Alternatively, open the project using your preferred IDE.

4. Set Up the Backend

Navigate to the backend directory:

cd backend

Install the required Python packages:

pip install -r requirements.txt

Run the Flask backend:

python app.py

Note: Keep this terminal open, as the backend server needs to run continuously.

5. Set Up the Frontend

Open a new terminal and navigate to the frontend directory:

cd frontend

Install the Flutter dependencies:

flutter pub get

6. Update the Backend Link in the Frontend

In the frontend/lib/screens/main_screen.dart file, locate line 54 and replace the existing link with your local machine's wireless adapter IPv4 address. You can find this address by running the following command in a terminal:

ipconfig

The link should look like:

http://192.x.x.x:5000/count_faces

7. Run the Frontend

Run the Flutter app on your connected phone or emulator:

flutter run

Using the App

Once the app is running on your device:

Tap "Get Started."

Choose an option to either upload an image from your gallery or take a new photo.

The app will detect and display the number of faces in the image.

Troubleshooting

Ensure the backend is running before starting the frontend.

Verify the IPv4 address is correct and matches your local machine.

Make sure your phone and computer are connected to the same network.

Ensure your phone is connected to the same Wi-Fi as your PC.
