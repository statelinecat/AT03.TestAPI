
import requests

def get_random_cat_image():

    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]['url']
    else:
        return None



if __name__ == "__main__":

    image_url = get_random_cat_image()

    if image_url:

        print(f"Случайное изображение кошки: {image_url}")

