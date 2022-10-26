import cv2
import pytesseract

path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = path
font = cv2.FONT_HERSHEY_PLAIN
cap = cv2.VideoCapture(0)
cntr = 0
while True:
    ret, frame = cap.read()
    cntr = cntr + 1
    if ((cntr % 20) == 0):
        imgH, imgW, _ = frame.shape
        x1, y1, w1, h1 = 0, 0, imgH, imgW
        imgchar = pytesseract.image_to_string(frame)
        imgboxes = pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes = boxes.split(' ')
            x, y, w, h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
            cv2.rectangle(frame, (x, imgH - y), (w, imgH - h), (0, 0, 255), 3)
            cv2.putText(frame, imgchar, (x1 + int(w1 / 50), y1 + int(h1 / 50)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.imshow('text detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
cap.release()
cv2.destroyAllWindows()