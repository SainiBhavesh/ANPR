# ANPR - Automatic Number Plate Recognition
<img width="520px" height="340px" src="https://github.com/SainiBhavesh/ANPR/blob/master/a.png"/>

<img width="520px" height="340px" src="https://github.com/SainiBhavesh/ANPR/blob/master/b.png"/>

## Introduction

This project implements an Automatic Number Plate Recognition (ANPR) system that utilizes Optical Character Recognition (OCR) to extract and read characters from license plates in an input image. The system is designed to be accurate, efficient, and capable of processing images containing one or multiple vehicles.

## Features

- License plate detection: The system utilizes image processing and computer vision techniques to detect license plates within an input image.
- Character segmentation: Once the license plate is detected, the characters on the plate are segmented to prepare them for OCR.
- Optical Character Recognition (OCR): The segmented characters are passed through an OCR engine to recognize and extract the alphanumeric information from the license plate.
- Support for multiple countries: The system is designed to handle license plates from various countries, supporting different character formats and sizes.
- Easy-to-use interface: The project provides a user-friendly interface to input images and receive the recognized license plate information as output.

 ## Requirements

- Python
- OpenCV
- OCR
- NumPy
- Other dependencies as listed in requirements.txt
