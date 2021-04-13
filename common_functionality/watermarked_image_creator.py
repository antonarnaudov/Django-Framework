import cv2

'''
    This code takes a watermark png file,
    which needs to be white text on black background,
    and the photo that's going to be watermarked and
    then puts them on top of one another.
'''


def create_watermarked_image(image):
    # This part of the code takes the watermark png file and its dimensions.
    watermark = cv2.imread('static/images/watermark/watermark.png')
    watermark_h, watermark_w, _ = watermark.shape

    # This part of the code takes the image dimensions.
    img_h, img_w, _ = image.shape

    center_img_h = int(img_h / 2)
    center_img_w = int(img_w / 2)

    top_y = center_img_h - int(watermark_h / 2)
    left_x = center_img_w - int(watermark_w / 2)

    bottom_y = top_y + watermark_h
    right_x = left_x + watermark_w

    roi = image[top_y: bottom_y, left_x: right_x]

    result = cv2.addWeighted(roi, 1, watermark, 0.3, 0)

    image[top_y: bottom_y, left_x: right_x] = result

    return image
