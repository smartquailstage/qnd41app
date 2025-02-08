import json
import requests
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario, Mensaje

# Configuración
OPENAI_API_KEY = "TU_OPENAI_API_KEY"
ACCESS_TOKEN = "TU_ACCESS_TOKEN_WHATSAPP"
VERIFY_TOKEN = "TU_VERIFY_TOKEN"

openai.api_key = OPENAI_API_KEY

@csrf_exempt
def whatsapp_webhook(request):
    """ Webhook para recibir mensajes de WhatsApp y responder con GPT-4 """

    if request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return JsonResponse(int(challenge), safe=False)

        return JsonResponse({"error": "Verificación fallida"}, status=403)

    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        if "entry" in data:
            for entry in data["entry"]:
                for change in entry.get("changes", []):
                    message = change.get("value", {}).get("messages", [])
                    if message:
                        msg_text = message[0]["text"]["body"]
                        sender_id = message[0]["from"]

                        # Obtener o crear usuario en la BD
                        usuario, created = Usuario.objects.get_or_create(telefono=sender_id)

                        # Obtener respuesta de GPT-4 con historial del usuario
                        respuesta = obtener_respuesta_gpt(usuario, msg_text)

                        # Guardar mensaje en la BD
                        Mensaje.objects.create(usuario=usuario, mensaje=msg_text, respuesta=respuesta)

                        # Enviar respuesta a WhatsApp
                        send_whatsapp_message(sender_id, respuesta)

        return JsonResponse({"status": "ok"}, status=200)


def obtener_respuesta_gpt(usuario, mensaje):
    """ Genera una respuesta de GPT-4 basada en el historial del usuario """
    
    # Incluir historial de conversación
    historial = usuario.historial.strip()
    contexto = f"Historial del usuario:\n{historial}\n\nUsuario: {mensaje}\nBot:"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente amigable especializado en responder preguntas sobre tecnología y soporte técnico."},
                {"role": "user", "content": contexto}
            ]
        )
        
        respuesta = response["choices"][0]["message"]["content"]
        
        # Actualizar historial del usuario
        usuario.historial += f"\nUsuario: {mensaje}\nBot: {respuesta}\n"
        usuario.save()

        return respuesta

    except Exception as e:
        print(f"Error en GPT-4: {e}")
        return "Lo siento, hubo un problema al procesar tu mensaje."


def send_whatsapp_message(to, text):
    """ Envía un mensaje a WhatsApp usando la API de Meta """
    url = "https://graph.facebook.com/v18.0/TU_PHONE_NUMBER_ID/messages"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": text}
    }
    requests.post(url, json=payload, headers=headers)
