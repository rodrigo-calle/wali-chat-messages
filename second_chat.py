import requests
import csv
import time

# Configuraciones y Constantes
CSV_FILE = 'testing.csv'
API_TOKEN = '835ac4f7ad92f19861c62080e5ba5ca55bd25ab587282ad13d0340963812928b13eee3960ef12ceb'
DEVICE = '659eb3d9ef4a6d6748df9299'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': API_TOKEN,
}
URL = 'https://api.wali.chat/v1/messages'
IMAGE_ID_LIST = ["65bb0cf7205fb845bfc4e58e", "65bb0edba727fa7bf35a47cc", "65bb0f35205fb8238ec53d96", "65bb0f56a727fa517f5a5cbb", "65bb0f7aa727fa29945a627c", "65bb0f9c205fb875d4c54e28"]
MESSAGE_TESTING = "Tu mensaje aquí..."

def send_message_with_media(phone, image_id):
    json_data = {
        'phone': phone,
        'device': DEVICE,
        'media': {'file': image_id}
    }

    try:
        response = requests.post(URL, json=json_data, headers=HEADERS)
        response.raise_for_status()
        return response.status_code == 200
    except Exception as e:
        print(f'Failed to send image to {phone}: {e}')
        return False

def send_only_message(phone, message):
    json_data = {
        'phone': phone,
        'message': message,
        'device': DEVICE,
    }

    try:
        response = requests.post(URL, json=json_data, headers=HEADERS)
        response.raise_for_status()
        return response.status_code == 200
    except Exception as e:
        print(f'Failed to send message to {phone}: {e}')
        return False

def main():
    with open(CSV_FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            phone, _ = row
            for image_id in IMAGE_ID_LIST:
                if send_message_with_media(phone, image_id):
                    print(f'Image {image_id} sent successfully to {phone}')
                    time.sleep(1)  # Pequeña pausa para asegurar el orden
                else:
                    print(f'Failed to send image {image_id} to {phone}')
            
            if send_only_message(phone, MESSAGE_TESTING):
                print(f'Message sent successfully to {phone}')
            else:
                print(f'Failed to send message to {phone}')

if __name__ == "__main__":
    main()
