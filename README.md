# opencv-python

## 01 Image Loading
```python
img = cv2.imread('file.png', cv2.IMREAD_GRAYSCALE) # reads image in grayscale
cv2.imshow('myWindow', img) # opens window with image
cv2.waitKey(0) # waits for any key to be pressed
cv2.destroyAllWindows()
cv2.imwrite('newFile.png', img) # writes new img
```

### 02 Video Loading
```python
webcam = cv2.VideoCapture(0)

while True:
	ret, frame = webcam.read() # we only care about frame
	grayVersion = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # creates object with grayscale of webcam
	
	cv2.imshow('myColoredWebcam', frame) 
	cv2.imshow('myGrayscaleWebcam', grayVersion)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

webcam.release()
cv2.destoryAllWindows()
```

### 03 Drawing
```python
img = cv2.imread('file.png'), cv2.IMREAD_COLOR) # reads image in color

# line
cv2.line(img, tuple start point, tuple end point, tuple BGR)
# rectangle
cv2.rectangle(img, tuple start point, tuple end point, tuple BGR, int borderWidth) # -1 as border fills in shape
# circle
cv2.circle(img, tuple center, int radius, tuple BGR, int borderWidth)
# polygon
pts = np.array([ [10,10],[20,30],[40,50],[20,20] ], np.int32)
cv2.polylines(img, [pts], boolean connectEndPointToStartPoint?, tuple BGR, int borderWidth)
# text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, String text, tuple start point, font, int size, tuple BGR, cv2.LINE_AA)
```

### 04 IMG OPS
```python
img = cv2.imread(...)

onePixel = img[15,15] # returns array BGR
img [15,15] = [255,255,255]

# Region of Image: ROI
roi = img[100:200,120:220]
img[0:50,0:50] = roi # copies all color values over

# adding
sum = img1 + img2 # adds color values
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) # adds color values by weight
