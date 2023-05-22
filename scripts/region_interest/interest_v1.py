import cv2
import numpy as np
import matplotlib.pyplot as plt


def thresh(image):
    """
    print(np.amax(image))
    if np.amax(image) >220:
        limit =80
    elif np.amax(image) > 180 and np.amax(image) < 220:
        limit = 45
    else:
        limit = 40
    print(limit)
    _, thresh = cv2.threshold(image,np.amax(image)-limit, 255, cv2.THRESH_BINARY_INV)
    if np.amax(image)>195 and np.amax(image)<205:    
        otsu, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    """
    otsu, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
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
        if area > np.amax(areas)-100:
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

    fig.savefig('img_save/comparative/'+name[:-4]+'.png')
    #plt.pause(3)
    #plt.close(fig)

def names(cont):
    if cont < 10:
        name = 'D:/dataset/HAM10000_images_part_1/ISIC_002430'+str(cont)+'.jpg'
    if cont > 9 and cont < 100:
        name = 'D:/dataset/HAM10000_images_part_1/ISIC_00243'+str(cont)+'.jpg'
    if cont > 99 and cont < 1000:
        cont = cont + 300
        name = 'D:/dataset/HAM10000_images_part_1/ISIC_0024'+str(cont)+'.jpg'
    split_name = name.split('/')
    short_name = split_name[-1]
    return name, short_name


#=================================INIT PROGRAM=================================
#init database 7
def main():
    cont=7
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
        apply = apply_mask(image,final_mask)
        
        img_show(img, mask, final_mask, apply, short_name)
        cv2.imwrite("img_save/segmented/"+short_name[:-4]+".png", apply)
        
        cont=cont+1

if __name__ == '__main__':
  main()