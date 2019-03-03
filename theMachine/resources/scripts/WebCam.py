import cv2 as cv2

def get_feed(url):
    vc = cv2.VideoCapture(url)
    return vc

def show_camera(feed,title):

    #print(type(feed))

    if feed.isOpened(): # try to get the first frame
        rval, frame = feed.read()
    else:
        rval = False
    while rval:
        cv2.imshow(title, frame)
        rval, frame = feed.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

def create_window(title):
    cv2.namedWindow(title)

def destroy_window(title):
    cv2.destroyWindow(title)

def test(title,url):
    vc=get_feed(url)
    create_window(title)
    show_camera(vc,title)
    destroy_window(title)