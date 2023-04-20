import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import skimage.morphology, skimage.data

def DrawContour(LSF):
    final_img = np.zeros(img.shape);
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if LSF[i,j] < 0:
                final_img[i,j] = img[i,j];
    return final_img;

def mat_math (intput,str):
    output=intput;
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if str=="atan":
                output[i,j] = math.atan(intput[i,j]);
            if str=="sqrt":
                output[i,j] = math.sqrt(intput[i,j]);
    return output;

def RSF (LSF, img, mu, nu, epison,step,lambda1,lambda2,kernel):

    Drc = (epison / math.pi) / (epison*epison+ LSF*LSF);
    Hea = 0.5*(1 + (2 / math.pi)*mat_math(LSF/epison,"atan"));
    Iy, Ix = np.gradient(LSF);
    s = mat_math(Ix*Ix+Iy*Iy,"sqrt");
    Nx = Ix / (s+0.000001);
    Ny = Iy / (s+0.000001);
    Mxx,Nxx =np.gradient(Nx);
    Nyy,Myy =np.gradient(Ny);
    cur = Nxx + Nyy;
    Length = nu*Drc*cur;

    Lap = cv2.Laplacian(LSF,-1);
    Penalty = mu*(Lap - cur);

    KIH = cv2.filter2D(Hea*img,-1,kernel);
    KH = cv2.filter2D(Hea,-1,kernel);
    f1 = KIH / KH; 
    KIH1 = cv2.filter2D((1-Hea)*img,-1,kernel);
    KH1 = cv2.filter2D(1-Hea,-1,kernel);
    f2 = KIH1 / KH1; 
    R1 = (lambda1- lambda2)*img*img;
    R2 = cv2.filter2D(lambda1*f1 - lambda2*f2,-1,kernel);
    R3 = cv2.filter2D(lambda1*f1*f1 - lambda2*f2*f2,-1,kernel);
    RSFterm = -Drc*(R1-2*R2*img+R3);

    LSF = LSF + step*(Length + Penalty + RSFterm);
    return LSF;

original_img = cv2.imread('D:/dataset/HAM10000_images_part_1/ISIC_0024307.jpg')
original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

img = original_img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray,5)   #filtro para reduccion de ruido
otsu, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#rellenar huecos
#kernel = np.ones((3,3), np.uint8)
#img_dilation = cv2.dilate(thresh, kernel, iterations=3)


img = np.float64(thresh)
draw = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)
#Kernel
sig = 3;
kernel = np.ones((sig*4+1,sig*4+1),np.float64)/(sig*4+1)**2;

IniLSF = np.ones((img.shape[0],img.shape[1]),img.dtype);
IniLSF[30:80,30:80] = -1;
IniLSF = -IniLSF;

mu = 1;
nu = 0.003 * 255 * 255;
num = 10;
epison = 1;
step = 0.1;
lambda1 = lambda2 = 1;
LSF = IniLSF;

for i in range(1,num):
    LSF = RSF(LSF, img, mu, nu, epison,step,lambda1,lambda2,kernel);


final_mask = DrawContour(LSF)

#rellenar huecos
#kernel = np.ones((3,3), np.uint8)
#final_mask = cv2.dilate(final_mask, kernel, iterations=3)

apply_mask = original_img.copy()

b,g,r = cv2.split(apply_mask)


for i in range(0,thresh.shape[0]):
        for j in range(0,thresh.shape[1]):
            if final_mask[i,j] != 255:
                r[i,j] = 0
                g[i,j] = 0
                b[i,j] = 0
apply_mask = cv2.merge((b,g,r))

cv2.imwrite('mask.png',thresh)
fig = plt.figure()

fig.add_subplot(1,4,1)
plt.imshow(original_img, cmap='gray')
plt.title("Original Image")

fig.add_subplot(1,4,2)
plt.imshow(thresh, cmap='gray')
plt.title("Mask")

fig.add_subplot(1,4,3)
plt.imshow(final_mask, cmap='gray')
plt.title("Final mask")

fig.add_subplot(1,4,4)
plt.imshow(apply_mask, cmap='gray')
plt.title("Apply mask")

plt.show()
