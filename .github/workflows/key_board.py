import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# def drawAll(img, buttonList):
#     imgNew = np.zeros_like(img, np.uint8)
#     for button in buttonList:
#         x, y = button.pos
#         cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
#                           20, rt=0)
#         cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
#                       (255, 0, 255), cv2.FILLED)
#         cv2.putText(imgNew, button.text, (x + 40, y + 60),
#                     cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
#
#     out = img.copy()
#     alpha = 0.5
#     mask = imgNew.astype(bool)
#     print(mask.shape)
#     out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
#     return out
 
detector = HandDetector(detectionCon=0.8, maxHands=1)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "<"]]

finalText = ""
keyboard = Controller()


class Button:
    def __init__(self, pos, text, size=[70, 70]):
        self.pos = pos
        self.size = size
        self.text = text


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))


def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (x, y, w, h), 15, rt=0, colorC=(100, 100, 250))
        cv2.rectangle(img, (x, y), (x + w, y + h), (100, 100, 250), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 50),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
    return img



while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) 

    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)

    if hands:
        lmList = hands[0]["lmList"]  

        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 50),
                            cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

                l, _, _ = detector.findDistance(
                    (lmList[8][0], lmList[8][1]),
                    (lmList[12][0], lmList[12][1]),
                    img
                )

                if l < 40: 
                    keyboard.press(button.text)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 50),
                                cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

                    if button.text == "<":
                        finalText = finalText[:-1]
                    else:
                        finalText += button.text

                    sleep(0.3)

    # hien thi 
    cv2.rectangle(img, (50, 400), (1000, 500), (50, 50, 50), cv2.FILLED)
    cv2.putText(img, finalText, (60, 470),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
