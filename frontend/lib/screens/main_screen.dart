import 'package:flutter/material.dart';
import 'package:front_end/screens/result.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';


class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  _MainScreenState createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  final ImagePicker _picker = ImagePicker();
  XFile? _image;

  Future<void> _pickImageFromGallery() async {
    final XFile? pickedImage = await _picker.pickImage(source: ImageSource.gallery);
    setState(() {
      _image = pickedImage;
    });
    if (_image != null) {
      _uploadImageAndGetFaceCount();
    }
  }

  Future<void> _takePhoto() async {
    final XFile? takenImage = await _picker.pickImage(source: ImageSource.camera);
    setState(() {
      _image = takenImage;
    });
    if (_image != null) {
      _uploadImageAndGetFaceCount();
    }
  }

  Future<void> _uploadImageAndGetFaceCount() async {
    if (_image == null) return;

    final uri = Uri.parse('http:// :5000/count_faces');
    final request = http.MultipartRequest('POST', uri)
      ..files.add(await http.MultipartFile.fromPath('image', _image!.path));

    final response = await request.send();

    if (response.statusCode == 200) {
      final result = await response.stream.bytesToString();
      final jsonResponse = json.decode(result);
      final faceCount = jsonResponse['face_count'];

      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => ResultPage(faceCount: faceCount),
        ),
      );
    } else {
      print("Failed to upload image");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          "Count It",
          style: TextStyle(                      fontFamily: 'ClickerScript',
color: Colors.black, fontWeight: FontWeight.bold, fontSize: 25),
        ),

        backgroundColor: Colors.white,
        elevation: 0,
        actions: [
          IconButton(
            icon: const Icon(Icons.info_outline, color: Colors.black),
            onPressed: () {
              showAboutDialog(
                context: context,
                applicationName: "How to use Count It",
                children: [
                  const Text("This app detects and counts faces in images. You can either upload an image from your gallery or take a photo using the camera. Click on the 'Upload Image' button to select an image from your gallery, or click on the 'Take Now' button to take a photo. Once the image is selected or taken, the app will count the faces in the image and display the result."),
                ],
              );
            },
          ),
        ],
      ),

      backgroundColor: Colors.white,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              width: 200,
              height: 200,
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(10),
                border: Border.all(
                  color: Colors.black,
                  width: 2,
                ),
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: const [
                  Icon(
                    Icons.cloud_upload_outlined,
                    color: Colors.black,
                    size: 50,
                  ),
                  SizedBox(height: 10),
                  Text(
                    "No image selected",
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 16,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),
            SizedBox(
              width: 200,
              child: ElevatedButton(
                onPressed: _pickImageFromGallery,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.black,
                ),
                child: const Text(
                  'Upload Image',
                  style: TextStyle(color: Colors.white),
                ),
              ),
            ),
            const SizedBox(height: 10),
            SizedBox(
              width: 200,
              child: ElevatedButton(
                onPressed: _takePhoto,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.black,
                ),
                child: const Text(
                  'Take Now',
                  style: TextStyle(color: Colors.white),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
