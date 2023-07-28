import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def thresh(image):
    limit = 45
    _, thresh = cv2.threshold(image,np.amax(image)-limit, 255, cv2.THRESH_BINARY_INV)

    #otsu, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return thresh

def erode(image):
    kernel = np.ones((4,4), np.uint8)
    erosion = cv2.erode(image, kernel, iterations=1)
    return erosion

def max_objects(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    areas =[]
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        areas.append(area)

    mask = np.zeros_like(opening)
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > np.amax(areas)/2:
            cv2.drawContours(mask, [contour], -1, 255, -1)

    result = cv2.bitwise_and(image, image, mask=mask)
    return result

def fill_empty(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30,30))
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return closing

def borderfilter(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    y,x = gray.shape
    new_image = gray[40:y-40, 40:x-40]
    return new_image

def apply_mask(image,final_mask):
    new_shape = (image.shape[1], image.shape[0])
    final_mask = cv2.resize(final_mask, new_shape, interpolation = cv2.INTER_LINEAR)
    apply = cv2.bitwise_and(image, image, mask=final_mask)
    return apply

def img_show(img, mask, final_mask, apply_mask,name):
    fig = plt.figure()
    fig.suptitle(name)

    fig.add_subplot(1,4,1)
    plt.imshow(img,cmap='gray')
    plt.title('original')

    fig.add_subplot(1,4,2)
    plt.imshow(mask, cmap='gray')
    plt.title('threshold')

    fig.add_subplot(1,4,3)
    plt.imshow(final_mask, cmap='gray')
    plt.title('final_mask')

    fig.add_subplot(1,4,4)
    plt.imshow(apply_mask, cmap='gray')
    plt.title('apply_mask')

    #plt.show()

    #fig.savefig('img_save/comparative/'+name[:-4]+'.png')
    plt.pause(5)
    plt.close(fig)

def names(cont):
    folder = "C:/Users/josei/OneDrive/UAZ/2_Tesis/skin_cancer_detection/dataset/image_separate/mel/"
    files_names = os.listdir(folder)
    name = folder + files_names[cont]
    short_name = files_names[cont]
    return name, short_name
    
#=================================INIT PROGRAM=================================
#init database 7
def main():
    cont=0
    while True:
        name, short_name = names(cont)
        print(short_name)
        
        image = cv2.imread(name)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        filter = borderfilter(image)
        blur = cv2.medianBlur(filter,3)
        mask = thresh(blur)
        erosion = erode(mask)
        result = max_objects(erosion)
        final_mask = fill_empty(result)
        apply = apply_mask(img,final_mask)
        
        img_show(img, mask, final_mask, apply, short_name)
        #cv2.imwrite("img_save/segmented/"+short_name[:-4]+".png", apply)
        #cv2.waitKey(0)
        cont=cont+1



if __name__ == '__main__':
  main()