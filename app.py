from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
from dotenv import load_dotenv
import os
from datetime import datetime
from threading import Timer

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT') or 0)
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'False') == 'True'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', 'False') == 'True'
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

def schedule_email(subject, body, send_time):
    recipient = os.getenv('RECIPIENT_EMAIL')
    if not recipient:
        print('Error: No se ha configurado el correo del destinatario en RECIPIENT_EMAIL')
        return

    def send_email():
        with app.app_context():
            msg = Message(subject, recipients=[recipient])
            msg.body = body
            try:
                mail.send(msg)
                print(f'Correo enviado exitosamente a {recipient}')
            except Exception as e:
                print(f'Error al enviar correo: {e}')

    # Calcular el tiempo en segundos hasta el envío
    now = datetime.now()
    delay = (send_time - now).total_seconds()
    if delay <= 0:
        # Si la fecha es en el pasado o inmediata, enviar el correo ahora
        send_email()
    else:
        # Programar el envío del correo
        Timer(delay, send_email).start()

@app.route('/schedule_email/', methods=['POST'])
def schedule_email_route():
    # Verificar API Key
    api_key = request.headers.get('X-API-Key')
    expected_api_key = os.getenv('API_KEY')
    if expected_api_key and api_key != expected_api_key:
        return jsonify({'error': 'No autorizado'}), 401

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No se proporcionaron datos'}), 400

    subject = data.get('subject', 'Sin Asunto')
    body = data.get('body', 'Sin Contenido')
    send_time_str = data.get('send_time')

    if not send_time_str:
        return jsonify({'error': 'No se proporcionó la fecha y hora de envío'}), 400

    try:
        # Parsear la fecha y hora de envío
        send_time = datetime.strptime(send_time_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return jsonify({'error': 'Formato de fecha y hora inválido. Debe ser YYYY-MM-DD HH:MM:SS'}), 400

    # Programar el envío del correo
    schedule_email(subject, body, send_time)

    return jsonify({'message': f'Correo programado para {send_time_str}'}), 200

if __name__ == '__main__':
    app.run(debug=True)
