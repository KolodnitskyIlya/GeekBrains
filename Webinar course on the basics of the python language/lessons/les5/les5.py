import os
import requests
#import some_lib.my_funks

def get_htm():
    url = 'https://gb.ru/'
    response = requests.get(url)
    return response.text

def get_image(url):
    response = requests.get(url)
    return response.content

def save_html_to_file(file_path, htm_text):
    with open(file_path, 'w', encoding='UTF-8') as file:
        file.write(htm_text)

def save_image(file_path, image_bytes):
    with open(file_path, 'wb') as file:
        file.write(image_bytes)

if __name__ == "__main__":
    img_url = 'https://gbcdn.mrgcdn.ru/uploads/geekbrains/public/ckeditor_assets/pictures/11834/retina-cee30e16e413f965c04398db0a85575e.png'
    file_name = 'temp_gb_main.html'
    file_folder = os.path.dirname(__file__)
    file_path = os.path.join(file_folder, file_name)
    image_path = os.path.join(file_folder, 'retina-cee30e16e413f965c04398db0a85575e.png')
    # html_text = get_htm()
    # save_html_to_file(file_path, html_text)
    img_bytes = get_image(img_url)
    save_image(image_path, img_bytes)



# #print(response)
# #print(response.text)
#
# # print(os.name)
# # print(os.environ)
# # os.mkdir('test_mkdir')
# # os.removedirs('test_mkdir')
#
# print(os.listdir())
# print(os.path.isdir('.DS_Store'))
# print(os.path.isfile('.DS_Store'))

