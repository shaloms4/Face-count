# Face-Count App

Face-Count is a simple app that uses the **MTCNN** (Multi-task Cascaded Convolutional Networks) model for face detection and counting. The backend is built with Flask, and the frontend is developed using Flutter. Since the backend doesn't run continuously, it will be hosted locally. This README provides step-by-step instructions for setting up and running the project on your local machine.

## Course Information

This app was created as part of the "Programming for AI" course.

### Group Members:
- Eyob Derese ------------------------------------------------------ UGR/6771/14
- Elizabet Yonas ---------------------------------------------------- UGR/6912/14
- Ruhama Yohannes ------------------------------------------------ UGR/7382/14
- Ruth Alemfanta -------------------------------------------------- UGR/7679/14
- Shalom Habtamu ------------------------------------------------- UGR/6901/14
- Yordanos Melaku ------------------------------------------------ UGR/8211/14

### Special Thanks:
- Estifanos Taye Tamirat ------------------------------------------ UGR/7285/14 

---

## Prerequisites

Before getting started, ensure you have the following installed on your system:

- Python 3.x
- Pip (Python package manager)
- Flutter SDK
- Visual Studio Code (or any preferred IDE)
- Git

## How to Set Up and Run the App

Follow these steps to clone, set up, and run the Face-Count app:

### 1. Clone the Repository

Open a terminal (Command Prompt, PowerShell, or any preferred terminal) and run the following command:

```bash
git clone https://github.com/shaloms4/Face-count
```

### 2. Navigate to the Project Directory

Change your directory to the cloned repository:

```bash
cd Face-count
```

### 3. Open the Project in an IDE

To open the project in Visual Studio Code, run:

```bash
code .
```

### 4. Set Up the Backend

Navigate to the backend directory:

```bash
cd backend
```
```bash
pip install -r requirements.txt
python app.py
```

### 5. Set Up the Frontend

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
```
```bash
flutter pub get
```

### 6. Update the Backend Link in the Frontend

In the `frontend/lib/screens/main_screen.dart` file, locate line 54 and replace the existing link with your local machine's wireless adapter IPv4 address. You can find this address by running the following command in a terminal:

```bash
ipconfig
```
The link should look like:
http://192.x.x.x:5000/count_faces

### 7. Run the Frontend

Run the Flutter app on your connected phone or emulator:

```bash
flutter run
```

## Using the App

Once the app is running on your device:

1. Tap "Get Started."
2. Choose an option to either upload an image from your gallery or take a new photo.
3. The app will detect and display the number of faces in the image.

## Troubleshooting

- Ensure the backend is running before starting the frontend.
- Verify the IPv4 address is correct and matches your local machine.
- Make sure your phone and computer are connected to the same network.
- Ensure your phone is connected to the same Wi-Fi as your PC.


