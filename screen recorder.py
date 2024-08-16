import cv2
import pyautogui as p
import numpy as np

r = p.size()
fw="\\output.avi"

fn = input("Enter the path:")
g=fn+fw
fourcc = cv2.VideoWriter_fourcc(*"XVID")
o = cv2.VideoWriter(g, fourcc, 20, r)  # isColor=False for grayscale

while True:
    img = p.screenshot()
    fg = np.array(img)
    fg = cv2.cvtColor(fg, cv2.COLOR_BGR2RGB)  # Convert to grayscale
    cv2.imshow("live", fg)
    o.write(fg)  # Write the grayscale frame to the video file

    k = cv2.waitKey(1)  # Small delay to capture keypresses
    if k == ord("q"):
        break

o.release()
cv2.destroyAllWindows()
