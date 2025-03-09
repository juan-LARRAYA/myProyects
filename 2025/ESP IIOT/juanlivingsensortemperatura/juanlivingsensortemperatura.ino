#include <WiFi.h>
#include <PubSubClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include "../config.h"

// Configuración del sensor DS18B20
#define ONE_WIRE_BUS 23 // Pin donde está conectado DQ del sensor
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// Configuración de red WiFi
const char* ssid = WIFI_SSID;        // Cambia por el nombre de tu red WiFi
const char* password = WIFI_PASSWORD;   // Cambia por la contraseña de tu red WiFi

// Configuración del broker MQTT
const char* mqtt_server = "192.168.0.15"; // Dirección IP o dominio de tu broker EMQX
const int mqtt_port = 1883;            // Puerto MQTT (por defecto 1883)
const char* mqtt_user = MQQT_USR;     // Usuario MQTT (opcional)
const char* mqtt_password = MQQT_PSW;  // Contraseña MQTT (opcional)
const char* mqtt_topic = "/juan/casa/living/temperatura"; // Tema donde publicar

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.println("Conectando a WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println("\nConectado a WiFi");
}

void reconnect() {
  // Reintenta conexión con el broker MQTT
  while (!client.connected()) {
    Serial.print("Intentando conexión con MQTT...");
    if (client.connect("ESP32Client", mqtt_user, mqtt_password)) {
      Serial.println("Conectado a MQTT");
    } else {
      Serial.print("Error: ");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);

  // Inicializa WiFi y MQTT
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);

  // Inicializa el sensor de temperatura
  sensors.begin();
  Serial.println("Sensor de temperatura inicializado.");
}

void loop() {
  // Reconectar si la conexión MQTT se pierde
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Leer la temperatura del sensor
  sensors.requestTemperatures();
  float temperature = sensors.getTempCByIndex(0);

  if (temperature != DEVICE_DISCONNECTED_C) {
    Serial.print("Temperatura leída: ");
    Serial.print(temperature);
    Serial.println(" °C");

    // Publicar el valor de temperatura en el tema MQTT
    char tempStr[8];
    dtostrf(temperature, 6, 2, tempStr); // Convierte la temperatura a string
    client.publish(mqtt_topic, tempStr);
    Serial.println("Temperatura publicada en MQTT.");
  } else {
    Serial.println("Error: Sensor desconectado.");
  }

  delay(5000); // Esperar 5 segundos antes de la próxima publicación
}

