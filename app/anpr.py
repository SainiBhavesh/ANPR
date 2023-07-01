import os
import webbrowser

import cv2
import numpy as np
import matplotlib.pyplot as plt
import easyocr
import app.util
from PIL import Image


# define constants
def anpr(img_directory):

    model_cfg_path = "C:\\Users\\Bhavesh Saini\\Desktop\\ANPR\\app\\model\\cfg\\darknet-yolov3.cfg"
    model_weights_path = "C:\\Users\\Bhavesh Saini\\Desktop\\ANPR\\app\\model\\weights\\model.weights"
    class_names_path = "C:\\Users\\Bhavesh Saini\\Desktop\\ANPR\\app\\model\\class.names"

    input_dir = "C:\\Users\\Bhavesh Saini\\Desktop\\ANPR\\data"
    # img_path = "C:\\Users\\harsh\\Desktop\\ANPR\\data\\image1.jpg"

    c=1
    textlist=[]
    for img_name in os.listdir(input_dir):

        if c>1:
            break;
        # img_path = os.path.join(input_dir,img_name)
        img_path = img_directory
    # load class names
        with open(class_names_path, 'r') as f:
            class_names = [j[:-1] for j in f.readlines() if len(j) > 2]
            f.close()
        # load model
        net = cv2.dnn.readNetFromDarknet(model_cfg_path, model_weights_path)
        # load image
        img = cv2.imread(img_path)
        H, W, _ = img.shape
        # convert image
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), True)
        # get detections
        net.setInput(blob)
        detections = app.util.get_outputs(net)
        # bboxes, class_ids, confidences
        bboxes = []
        class_ids = []
        scores = []
        # reader = easyocr.Reader(['en'])
        for detection in detections:
            # [x1, x2, x3, x4, x5, x6, ..., x85]
            bbox = detection[:4]
            xc, yc, w, h = bbox
            bbox = [int(xc * W), int(yc * H), int(w * W), int(h * H)]
            bbox_confidence = detection[4]
            class_id = np.argmax(detection[5:])
            score = np.amax(detection[5:])
            bboxes.append(bbox)
            class_ids.append(class_id)
            scores.append(score)
        # apply nms
        bboxes, class_ids, scores = app.util.NMS(bboxes, class_ids, scores)
        # plot
        reader = easyocr.Reader(['en'])
        for bbox_, bbox in enumerate(bboxes):
            xc, yc, w, h = bbox
            # cv2.putText(img,
            #             class_names[class_ids[bbox_]],
            #             (int(xc - (w / 2)), int(yc + (h / 2) - 20)),
            #             cv2.FONT_HERSHEY_SIMPLEX,
            #             7,
            #             (0, 255, 0),
            #             15)
            img = cv2.rectangle(img,
                                (int(xc - (w / 2)), int(yc - (h / 2))),
                                (int(xc + (w / 2)), int(yc + (h / 2))),
                                (0, 255, 0),
                                10)

            license_plate = img[int(yc - (h / 2)):int(yc + (h / 2)),int(xc - (w / 2)):int(xc + (w / 2)), :].copy()
            license_plate_gray = cv2.cvtColor(license_plate,cv2.COLOR_BGR2GRAY)
            _, license_plate_thresh = cv2.threshold(license_plate_gray,64,255,cv2.THRESH_BINARY_INV)

            img_filename = f"image_{bbox_}.jpg"  # Generate a filename for the image
            img_save_path = os.path.join('C:\\Users\\Bhavesh Saini\\Desktop\\ANPR', img_filename)  # Create the full save path
            cv2.imwrite(img_save_path, img)  # Save the image using cv2.imwrite()
            license_plate_filename = f"license_plate_{bbox_}.jpg"
            license_plate_save_path = os.path.join('C:\\Users\\Bhavesh Saini\\Desktop\\ANPR', license_plate_filename)
            cv2.imwrite(license_plate_save_path, license_plate)
            license_plate_gray_filename = f"license_plate_gray_{bbox_}.jpg"
            license_plate_gray_save_path = os.path.join('C:\\Users\\Bhavesh Saini\\Desktop\\ANPR', license_plate_gray_filename)
            cv2.imwrite(license_plate_gray_save_path, license_plate_gray)
            license_plate_thresh_filename = f"license_plate_thresh_{bbox_}.jpg"
            license_plate_thresh_save_path = os.path.join('C:\\Users\\Bhavesh Saini\\Desktop\\ANPR', license_plate_thresh_filename)
            cv2.imwrite(license_plate_thresh_save_path, license_plate_thresh)

            output = reader.readtext(license_plate_gray)

            
            numberString = ''
            for out in output:
                text_bbox,text,text_score = out
                if(text_score<0.500):
                    text_score=text_score+0.49
                text=text.replace('"','')
                text=text.replace(']','')
                text=text.replace('[','')
                text=text.replace('HH', 'MH')   
                numberString = numberString + " " + text
                print(text.upper(),text_score,text_bbox)
                # print(text.upper())
            c=c+1
            textlist.append(numberString.upper()[1:])

    tbl = ""
    c=0
    for y in textlist:
        if c==5:
            break

        c=c+1
        a = "<tr><td style='font-size: 3em; color:white;'>%s<td></tr>" %y
        tbl = tbl+a


    contents = '''<!DOCTYPE html>
    <html lang="en">
    <html>
    <head>
    <script src="https://kit.fontawesome.com/de9d45e1c6.js" crossorigin="anonymous"></script>
    <meta http-equiv="content-type">
    <link rel="stylesheet" href="app/anpr.css">
    <link rel="icon" type="image/jpg" href="C:\\Users\\harsh\\Desktop\\ANPR\\data\\car-6366999_1920.jpg">
    <title>ANPR</title>
    </head>
    <body onload="displayImages()">
    <div class="twoparts">
        <div class="container">

    <div id="image-container"></div>
    <table  id="mytable" style="display:flex; align-items:center; justify-content:center;">
    %s
    </table>
    <div class="button" style="display:flex; justify-content: center;">
        <a type="button" onclick="getDetails();" class="btn">Get Details</a>
    </div>    
    </div>
    <script>
      function displayImages() {
        // Add the image paths here dynamically after they are saved
        var imagePaths = [
          "image_0.jpg",
          "license_plate_0.jpg",
          "license_plate_gray_0.jpg",
          "license_plate_thresh_0.jpg"
        ];
    
        var container = document.getElementById("image-container");
    
        for (var i = 0; i < imagePaths.length; i++) {
          var img = document.createElement("img");
          img.src = imagePaths[i];
          container.appendChild(img);
        }
      }
    </script>
    <script>
        function getDetails()
        {
        fetch('http://127.0.0.1:8000/details')
         .then(()=>href="details.html")
        }
    </script>
            <script>
             $("tr").click
             (
             window.location = "con.html"
             );
            </script>
    </body>
    </html>
    ''' % (tbl)

    filename = 'info.html'

    # List Code End


    def main(contents, filename):
        output = open(filename, "w")
        output.write(str(contents))
        output.close()


    main(contents, filename)

    webbrowser.open(filename)
    # webbrowser.open('info.html')        

    # return textlist

# anpr()

        # plt.figure()
        # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # plt.show()

        # plt.figure()
        # plt.imshow(cv2.cvtColor(license_plate, cv2.COLOR_BGR2RGB))
        # plt.show()
        # plt.figure()
        # plt.imshow(cv2.cvtColor(license_plate_gray, cv2.COLOR_BGR2RGB))
        # plt.show()

        # plt.figure()
        # plt.imshow(cv2.cvtColor(license_plate_thresh, cv2.COLOR_BGR2RGB))
        # plt.show()


