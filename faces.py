import numpy as np
import uuid
import cv2


def draw_label(image, point, label, font=cv2.FONT_HERSHEY_SIMPLEX,
               font_scale=0.8, thickness=1):
    size = cv2.getTextSize(label, font, font_scale, thickness)[0]
    x, y = point
    cv2.rectangle(image, (x, y - size[1]), (x + size[0], y), (255, 0, 0), cv2.FILLED)
    cv2.putText(image, label, point, font, font_scale, (255, 255, 255), thickness, lineType=cv2.LINE_AA)


def detect_faces_and_predict_age_and_gender(cv2_resized_image, detector, model):
    img_size = 64
    margin = 0.4

    img_h, img_w, _ = np.shape(cv2_resized_image)

    detected = detector(cv2_resized_image, 1)
    faces = np.empty((len(detected), img_size, img_size, 3))

    if len(detected) > 0:

        for i, d in enumerate(detected):
            x1, y1, x2, y2, w, h = d.left(), d.top(), d.right() + 1, d.bottom() + 1, d.width(), d.height()
            xw1 = max(int(x1 - margin * w), 0)
            yw1 = max(int(y1 - margin * h), 0)
            xw2 = min(int(x2 + margin * w), img_w - 1)
            yw2 = min(int(y2 + margin * h), img_h - 1)
            cv2.rectangle(cv2_resized_image, (x1, y1), (x2, y2), (255, 0, 0), 2)

            faces[i, :, :, :] = cv2.resize(cv2_resized_image[yw1:yw2 + 1, xw1:xw2 + 1, :], (img_size, img_size))


        results = model.predict(faces)
        predicted_genders = results[0]
        ages = np.arange(0, 101).reshape(101, 1)
        predicted_ages = results[1].dot(ages).flatten()

        for i, d in enumerate(detected):
            label = "{}, {}".format(int(predicted_ages[i]),
                                    "M" if predicted_genders[i][0] < 0.5 else "F")
            draw_label(cv2_resized_image, (d.left(), d.top()), label)

        temp_picture = uuid.uuid4().hex
        cv2.imwrite(f'{temp_picture}.jpg', cv2_resized_image)

        return f'{temp_picture}.jpg'
    else:

        return
