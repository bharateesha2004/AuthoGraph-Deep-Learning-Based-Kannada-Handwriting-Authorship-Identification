# AuthoGraph - Deep Learning-Based Kannada Handwriting Author Detection

A machine learning-based web application that identifies the author of Kannada handwriting samples using TensorFlow and Flask.

---

## Project Description

This project uses a deep learning model to analyze and identify the author of Kannada handwritten text. The system is built using TensorFlow for the machine learning component and Flask for the web interface, making it easily accessible through a browser.

---

## Features

- Upload images of Kannada handwriting  
- Real-time author prediction  
- Confidence-based multiple author suggestions  
- User-friendly web interface  
- Support for various image formats  

---

## Prerequisites

- Python 3.7+  
- TensorFlow 2.x  
- Flask  
- NumPy  
- Pillow (PIL)  

---

## Installation

1. Clone the repository:
```bash
  git clone [your-repository-url]
  cd kannada-author-detection
```

2. Create a virtual environment (recommended):
```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required packages:
```bash
  pip install -r requirements.txt
```

---

## Usage

1. Start the Flask server:
```bash
  python app.py
```

2. Open your web browser and navigate to:
```
  http://localhost:5000
```

3. Upload an image of Kannada handwriting through the web interface  
4. View the prediction results  

---

## Workflow

![Workflow Diagram](https://github.com/user-attachments/assets/671d7377-c5a0-482f-b87b-aeb42bc6538a)

---

## Model Information

The system uses a pre-trained deep learning model (`model_file.h5`) that:  
- Accepts images of size 150x150 pixels  
- Processes them through a neural network  
- Outputs author predictions with confidence scores  
- Provides alternative suggestions when confidence is below 99.5%  

---

## Project Structure

```
kannada-author-detection/
├── Code_files/                    # Main code directory
│   ├── app.py                    # Main Flask application
│   ├── templates/                # HTML templates
│   └── uploads/                  # Folder for uploaded images
├── Final_ppt                     # Project presentation (5,361 KB)
├── IEEE-paper                    # Research paper documentation (38 KB)
├── model_file.h5                 # Trained model (18,342 KB)
├── Result_pic                    # Result demonstration (54 KB)
├── Workflow                      # Workflow diagram (68 KB)
└── README.md                     # Project documentation
```

---

## Contributing

1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contact

Project Link: [https://github.com/yourusername/kannada-author-detection]

---

## Acknowledgments

- Special thanks to contributors and dataset providers.



