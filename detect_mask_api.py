from flask import Flask
from detect_mask_video import capture_img_and_detect_masks

app = Flask(__name__)

@app.route("/")
def detect_mask():
    result = capture_img_and_detect_masks()
    count_people_with_mask = result[0]
    count_people_without_mask = result[1]
    return "Bitte beachten Sie unsere Maskenpflicht im gesamten Gebaeude." if capture_img_and_detect_masks()[1] > 0 else "Vielen Dank für das Tragen einer Maske. Bitte lassen Sie diese die gesamte Zeit über im Gebaeude auf."

if __name__ == "__main__":
    app.run(host="0.0.0.0")
