import argparse
import cv2
import os
import progressbar


def crop_biggest(imgPath, outPath, threshold = 50):
    img = cv2.imread(imgPath, 1)
    file_name = os.path.basename(imgPath)[:-4]
    rgbimg = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    image_gray = cv2.cvtColor(rgbimg, cv2.COLOR_BGR2GRAY)
    _,threshold = cv2.threshold(image_gray, threshold, 255,0)
    
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    
    biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    x, y, w, h = cv2.boundingRect(biggest_contour)
    roi = img[y  :y + h, x : x + w ]
    export_file_name = (f"{file_name}_crop.jpg")
    cv2.imwrite(os.path.join(outPath, export_file_name), roi)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', help='Path to image directory')
    parser.add_argument('-o', '--output_path', help='Output Path')
    parser.add_argument('-t', '--threshold', help='border detection threshold')
    args = parser.parse_args()

    input_path = args.input_path
    output_path = args.output_path if args.output_path else args.input_path
    threshold = args.threshold

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    imgs = os.listdir(input_path)
    with progressbar.ProgressBar(max_value = len(imgs)) as bar:
        for i, image in enumerate(imgs):
            imgPath = os.path.join(input_path, image)
            crop_biggest(imgPath, output_path)
            bar.update(i)
        

    
    


    
