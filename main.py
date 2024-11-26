from flask import Flask, request, jsonify
import telegram
import os

# Inisialisasi Flask app
app = Flask(__name__)

# Ambil TOKEN dari environment variables
BOT_TOKEN = "7704143483:AAGCBYdYmehyegfCrfR0iIzq2tYXDGUSn64"
bot = telegram.Bot(token=BOT_TOKEN)


# Endpoint untuk menangani webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        # Ambil pesan dari user
        chat_id = update.message.chat.id
        text = update.message.text

        # Balas pesan user
        bot.sendMessage(chat_id=chat_id, text=f"Kamu mengirim pesan: {text}")

        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error'})


# Endpoint untuk mengatur webhook
@app.route('/set_webhook', methods=['GET'])
def set_webhook():
    # Ganti YOUR_VERCEL_APP_URL dengan URL Vercel app kamu
    webhook_url = 'https://YOUR_VERCEL_APP_URL/webhook'
    s = bot.setWebhook(webhook_url)
    if s:
        return jsonify({'status': 'webhook setup ok'})
    else:
        return jsonify({'status': 'webhook setup failed'})


if __name__ == '__main__':
    app.run(debug=True)
