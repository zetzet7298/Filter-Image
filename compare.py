import cv2
import os.path
import numpy as np

def center_crop(img, dim):
	"""Returns center cropped image
	Args:
	img: image to be center cropped
	dim: dimensions (width, height) to be cropped
	"""
	width, height = img.shape[1], img.shape[0]

	# process crop width and height for max available dimension
	crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
	crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0]
	mid_x, mid_y = int(width/2), int(height/2)
	cw2, ch2 = int(crop_width/2), int(crop_height/2)
	crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
	return crop_img

def getPercent(des1, kp1, des2, kp2, img1, img2):
    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    good_points = []
    for m,n in matches:
        if (m.distance < 0.6*n.distance):
            good_points.append(m)
    number_keypoints = 0
    if(len(kp1) <= len(kp2)):
        number_keypoints= len(kp1)
    else:
        number_keypoints= len(kp2)
    if(number_keypoints > 0):
        return len(good_points) / number_keypoints * 100
    else:
        return 0

def compare(filename1, filename2):
    imgPdfPath = directoryPdfImg + '/' + filename1
    imgPath = directoryImg + '/' + filename2

    img1 = cv2.imread(imgPdfPath)          # queryImage
    img2 = cv2.imread(imgPath)          # trainImage
    original = img2
    pdf_image = img1
    # Initiate SIFT detector
    sift = cv2.SIFT_create()

    w1, h1, c1 = img1.shape
    w2, h2, c2 = img2.shape

    w = h = 0
    if(w1 <= w2):
        w = w1
    else:
        w = w2

    if(h1 <= h2):
        h = h1
    else:
        h = h2
    #print(w, h)
    shape = tuple(img1.shape[1::-1])
    #print(shape)
    img2 = cv2.resize(img2,(h, w))

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    img1 = center_crop(img1, (500,500))
    img2 = center_crop(img2, (500,500))

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    percentImg1 = getPercent(des1, kp1, des2, kp2, img1, img2)
    print(len(kp1), len(kp2))
    print(percentImg1)
    #img3 = cv2.drawMatches(img1, kp1, img2, kp2, good_points, None)
    if(percentImg1 >= 7):
        #cv2.imwrite("result2/" + filename2, img3)
        print("ok")
        cv2.imwrite("result/" + filename2, original)
        return 1
    else:
        print("not same")
        #cv2.imwrite("result2/" + filename1, pdf_image)
    #exit()

directoryPdfImg = 'album-pdf'
#directoryPdfImg = 'pdf-test'
directoryImg = 'album'

for filename1 in os.listdir(directoryPdfImg):
    for filename2 in os.listdir(directoryImg):
        print("So sánh ảnh:" + filename1 + " với ảnh: " + filename2)
        if(compare(filename1, filename2) == 1): break
