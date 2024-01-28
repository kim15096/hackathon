'''
Command Line Interface Help

Example: python3 yolo_img_detector.py -f imgs/beach.jpg -w yolo_files/yolov3.weights -c yolo_files/yolov3.cfg -l yolo_files/coco.names -i -ca

-f: file(s) path
--folder: folder path (can't specify both -f and --folder)
-w: weights path
-c: config path
-l: labels/names path
-i: show inference
-ca: show total classes

'''

import os
import cv2
import numpy as np

# TODO: Phase 1
import sys

probability_minimum = 0.5
threshold = 0.3

class Object_Detection():
    def __init__(self):
        self.weights = "./yolo_files/yolov3.weights"
        self.config = "./yolo_files/yolov3.cfg"
        
        with open("./yolo_files/coco.names", 'r') as f:
            self.labels = [line.strip() for line in f]
        return
    
    def yolo(self, image):
        # Load YOLO model and convert loaded image to blob
        network = cv2.dnn.readNetFromDarknet(self.config, self.weights)
        if network is None:
            sys.exit('Error: Invalid Weights or Config File')
        yolo_layers = ['yolo_82', 'yolo_94', 'yolo_106']
        input_blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        
        # Define variables for drawing on image
        bounding_boxes = []
        confidences = []
        classes = []
        h, w = image.shape[:2]

        # Pass image through network
        network.setInput(input_blob)
        output = network.forward(yolo_layers)

        # Get bounding boxes, confidences, and classes
        for result in output:
            for detection in result:
                scores = detection[5:]
                class_current = np.argmax(scores)
                confidence_current = scores[class_current]
                if confidence_current > probability_minimum:
                    box_current = detection[0:4] * np.array([w, h, w, h])
                    x_center, y_center, box_width, box_height = box_current.astype('int')
                    x_min = int(x_center - (box_width / 2))
                    y_min = int(y_center - (box_height / 2))
                    bounding_boxes.append([x_min, y_min, int(box_width), int(box_height)])
                    confidences.append(float(confidence_current))
                    classes.append(class_current)
            
        return bounding_boxes, confidences, classes

    # Function to draw bounding boxes and save annotated images
    def save_annotated_image(self, image, bounding_boxes, confidences, classes, image_path, labels):
        annotated_image = image.copy()
        results = cv2.dnn.NMSBoxes(bounding_boxes, confidences, probability_minimum, threshold)
        
        # Get final classes and bounding boxes and confidences after NMS
        final_boxes = []
        final_confidences = []
        final_classes = []

        for i in results:
            final_boxes.append(bounding_boxes[i])
            final_confidences.append(confidences[i])
            final_classes.append(classes[i])
        
        coco_labels = 80
        np.random.seed(42)
        colours = np.random.randint(0, 255, size=(coco_labels, 3), dtype='uint8')
        if len(results) > 0:
            for i in results.flatten():
                x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
                box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]
                colour_box = [int(j) for j in colours[classes[i]]]
                label = labels[classes[i]]
                cv2.rectangle(annotated_image, (x_min, y_min), (x_min + box_width, y_min + box_height), colour_box, 5)
                cv2.putText(annotated_image, f'{label}: {confidences[i]:.4f}', (x_min, y_min - 7), cv2.FONT_HERSHEY_SIMPLEX, 1.5, colour_box, 2)
        # Save annotated image with '_out' suffix
        annotated_image_path = os.path.join('out_imgs', os.path.basename(image_path).replace('.jpg', '_out.jpg'))
        cv2.imwrite(annotated_image_path, annotated_image)
        print(f"Annotated image saved as {annotated_image_path}")

        return final_classes

    def process_images(self, image_path):
        # Initialize variables
        total_classes_detected = 0
        class_hash = {}
        total_counts = {}
        
        class_hash[image_path] = {}
        # Do not print if either of the inference or classes_all flag is True
    
        image = cv2.imread(image_path)
        # Check if image_path is valid
        if image is None:
            sys.exit(f'Error: The file at {image_path} does not exist or is not a valid image.')

        # Start the YOLO network
        bounding_boxes, confidences, classes = self.yolo(image)
        # Annotate image and save file
        final_classes = self.save_annotated_image(image, bounding_boxes, confidences, classes, image_path, self.labels)
        # Count for each class
        for cls in final_classes:
            class_hash[image_path][self.labels[cls]] = class_hash[image_path].get(self.labels[cls], 0) + 1
        # Get total number of classes
        total_classes_detected += len(final_classes)

        # If classes_all flag is True
        print(f"Total Number of Classes Detected: {total_classes_detected}")

        for img, objects in class_hash.items():
            # Iterate through each object in the image
            for object_name, count in objects.items():
                # If the object is already in the total_counts dict, add the count
                if object_name in total_counts:
                    total_counts[object_name] += count
                # If not, add the object to the dict with its count
                else:
                    total_counts[object_name] = count
        
        print("\nTotal Detection Breakdown:")
        for obj_name, count in total_counts.items():
            print(f"{obj_name}: {count}")

        print("\nImage Breakdown:")        
        return f"{image_path} => {' | '.join([f'{cls}: {class_hash[image_path][cls]}' for cls in class_hash[image_path]])}"


# if __name__ == '__main__':
#     objectDetection = Object_Detection()
#     objectDetection.process_images("./sample_photos/img_mouse.jpeg")