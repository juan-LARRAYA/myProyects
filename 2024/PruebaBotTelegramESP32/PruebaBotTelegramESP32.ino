#include <WiFi.h>              // Librería para conectarse a WiFi
#include <WiFiClientSecure.h>   // Librería para conexiones seguras HTTPS
#include <UniversalTelegramBot.h>  // Librería para manejar el bot de Telegram
#include <ArduinoJson.h>        // Librería para manejar JSON

const char* ssid = WIFI_SSID;
const char* password = WIFI_PASSWORD;
const char* telegramToken = TELEGRAM_TOKEN;
const char* telegramChatId = TELEGRAM_CHAT_ID;

WiFiClientSecure client;                // Cliente seguro para HTTPS
UniversalTelegramBot bot(telegramToken, client);

void setup() {
  Serial.begin(115200);
  
  // Conectar a la red WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando a WiFi...");
  }
  Serial.println("Conectado a WiFi");
  
  // Configurar el cliente seguro (opcional: desactivar verificación de certificado)
  client.setInsecure();  // No verificar certificados (útil para desarrollo, no recomendado en producción)
}

void loop() {
  // Enviar un mensaje al chat de Telegram
  //lo comente para que no me espame
  /*
  bool sent = bot.sendMessage(String(telegramChatId), "Hola desde ESP32!");

  // Comprobar si se ha enviado el mensaje
  if (sent) {
  Serial.println("Mensaje enviado correctamente");
  } else {
  Serial.println("Error al enviar el mensaje");
  }
  // Esperar 10 segundos antes de enviar otro mensaje
  delay(8000);
  */
}