import requests
import csv
import time

csv_file = 'testing.csv'

# Replace this with your WaliChat API token
# Get your API token here: https://app.wali.chat/apikeys
api_token = ''

# Optionally specify the target WhatsApp device ID connected to WaliChat
# you want to use for messages delivery (24 characters hexadecimal value)
device = '' # or use None

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'{api_token}',
}

url = 'https://api.wali.chat/v1/messages'
url_to_update_image = 'https://api.wali.chat/v1/files'

photo_list = ["https://i.ibb.co/892T964/Feria-de-Salud-1.jpg", "https://i.ibb.co/Rh1QFSS/Feria-de-Salud-2.jpg","https://i.ibb.co/BVFgN0R/Feria-de-Salud-3.jpg", "https://i.ibb.co/br7cxwb/Feria-de-Salud-4.jpg", "https://i.ibb.co/y6RPHLQ/Feria-d-Salud-5.jpg", "https://i.ibb.co/ZgknmY7/Feria-de-la-salud-6.jpg"]
# https://es.imgbb.com/
url_img = "https://i.ibb.co/HBt4Xgt/cc-imagen.jpg"

def upload_file(image_url):
    url = "https://api.wali.chat/v1/files"

    payload = {
        "url": url_img,
        "expiration": "1d",
        "filename": "custom-filename.jpg",
        "reference": "Optional reference ID"
    }
    headers = {
        "Content-Type": "application/json",
        "Token": "835ac4f7ad92f19861c62080e5ba5ca55bd25ab587282ad13d0340963812928b13eee3960ef12ceb"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)

# for index, photo in enumerate(photo_list):
#     upload_file(photo)


# Subiendo Image -> example id 65a0b0881947b006c6c302aa

# Descomentar línea 45 para subir imagen

# upload_file(url_img)

message_testing = """¡Querida comunidad del Centro Médico Callao!💙 estamos emocionados de anunciar nuestro primer sorteo exclusivo para ustedes! 🏥🎉✨ No pierdan la oportunidad de ganar regalos que cuidarán de su bienestar y les harán sentir aún mejor. 💖👩‍⚕¡Vamos juntos hacia la buena salud y la suerte! 🍀

¿𝐂𝐎́𝐌𝐎 𝐏𝐀𝐑𝐓𝐈𝐂𝐈𝐏𝐀𝐑❓
1️⃣ Sigue nuestra cuentas @𝐜𝐦𝐜𝐚𝐥𝐥𝐚𝐨.𝐩𝐞 en Facebook /Instagram y/o Tiktok.
2️⃣ 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐚 𝐞𝐥 𝐟𝐨𝐫𝐦𝐮𝐥𝐚𝐫𝐢𝐨 𝐝𝐞𝐥 𝐬𝐨𝐫𝐭𝐞𝐨👉 https://forms.gle/KuRmAuUpmEdAk6Vw6 👈 o desde nuestro perfil de Instagram si tienes problemas comunícate al 908803905.
3️⃣ Dale like a la publicación.
4️⃣ Duplica tus posibilidades de ganar etiquetando a 2 personas en este post.
• 𝐁𝐨𝐧𝐮𝐬👀: Comparte en tu historia este post y nos etiquetas @cmcallao.pe
Y listo! ya estas participando🎉

𝐁𝐚𝐬𝐞𝐬 𝐝𝐞𝐥 𝐬𝐨𝐫𝐭𝐞𝐨:
1. Sigue nuestra cuentas @cmcallao.pe en Facebook /Instagram y/o Tiktok.
2. Completa el formulario del sorteo que está en nuestro perfil, si tienes problemas comunica te al 908803905.
3. Dale like a la publicación."""

# #ENVIA MENSAJE

image_id_list = ["65bb0cf7205fb845bfc4e58e", "65bb0edba727fa7bf35a47cc", "65bb0f35205fb8238ec53d96", "65bb0f56a727fa517f5a5cbb", "65bb0f7aa727fa29945a627c", "65bb0f9c205fb875d4c54e28"]

def send_message_with_media(phone, message, image_id):
    json = {
      'phone': phone,
      # 'message': message,
      'device': device,
      'media': {
        'file': image_id
      }
    }

    if(image_id):
        json['media'] = {'file': image_id}

    try:
        response = requests.post(url, json=json, headers=headers)
        response.raise_for_status()
        print(f'=> Image created: {phone}')
    except e:
        print(f'Failed to create message to {phone}: {e}')


def send_only_message(phone, message):
    json = {
      'phone': phone,
      'message': message,
      'device': device,
    }

    try:
        response = requests.post(url, json=json, headers=headers)
        response.raise_for_status()
        print(f'=> Message created: {phone}')
    except Exception as e:
        print(f'Failed to create message to {phone}: {e}')


with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        phone, message = row        
        for index, image in enumerate(image_id_list):
            print(index)
            send_message_with_media(phone, '', image)
        
            if index == 5:
                send_only_message(phone, message_testing)    




