import cv2

# 01 일반 이미지
# img = cv2.imread('./Day07/img/nice.jpg')

# 02 흑백 이미지
#img = cv2.imread('./Day07/img/nice.jpg', cv2.IMREAD_GRAYSCALE)

# 03 이미지 사이즈 조절
#img_small = cv2.resize(img,(200,90))
#cv2.imshow('small', img_small)

# 04 원본을 두고 흑백처리
img = cv2.imread('./Day07/img/nice.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 05 이미지 자르기
height, width, channel = img.shape
print(height, width, channel)

img_crop = img[:, :int(width / 2)]  # height, width
gray_crop = gray[:, int(width / 2):]  # height, width

# 06 이미지 블러
img_blur = cv2.blur(img_crop, (30,30))

cv2.imshow('Orignal half', img_blur)
cv2.imshow('Gray half', gray_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()