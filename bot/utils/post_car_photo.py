import requests


def post_photo_to_telegraph(car_image, photo):
    response = requests.post("https://telegra.ph/upload",
                             files={"file": photo})
    if response.status_code == 200:
        photo_path = response.json()[0]['src']
        photo_post_link = f"https://telegra.ph{photo_path}"
    else:
        photo_post_link = None

    car_image.telegraph = photo_post_link
    car_image.save()

    # return photo_post_link
