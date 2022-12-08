//header file declarations 
#include "DHT.h"
#include "BH1750.h"
#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <ArduinoJson.h>
#include <FreeRTOS.h>
//on board pin assignment 
#define DHTPIN 4     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22   // DHT 22 (AM2302)
const int soilSensorPin = 33; //defining soil senosr pin 
const int mq135Pin = 34;
#define ONBOARD_LED  2
int temp;
int h;
int airQualityPpm;
DHT dht(DHTPIN, DHTTYPE);
BH1750 lightMeter;

const char *SSID = "SAI";
const char *PWD = "123sai456";
WebServer server(80);
// JSON data buffer
StaticJsonDocument<250> jsonDocument;
char buffer[250];
 
// env variable
float temperature;
float humidity;
float pressure;
 
void connectToWiFi() {
  Serial.print("Connecting to ");
  Serial.println(SSID);
  
  WiFi.begin(SSID, PWD);
  
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
    // we can even make the ESP32 to sleep
  }
  digitalWrite(ONBOARD_LED,HIGH);
  Serial.print("Connected. IP: ");
  Serial.println(WiFi.localIP());
}
void create_json(char *tag, float value, char *unit) { 
  jsonDocument.clear(); 
  jsonDocument["type"] = tag;
  jsonDocument["value"] = value;
  jsonDocument["unit"] = unit;
  serializeJson(jsonDocument, buffer);
  Serial.println("Buffer:");
  Serial.println(buffer);  
}
 
void add_json_object(char *tag, float value, char *unit) {
  JsonObject obj = jsonDocument.createNestedObject();
  obj["type"] = tag;
  obj["value"] = value;
  obj["unit"] = unit; 
}

void read_sensor_data(void * parameter) {
   for (;;) {
Dht22();
soilsens();
mq135();
bh175();
     temperature = temp;
     humidity = h;
     pressure = airQualityPpm;
     Serial.println("Read sensor data");
     
     // delay the task
     vTaskDelay(60000 / portTICK_PERIOD_MS);
   }
}

void getTemperature() {
  Serial.println("Get temperature");
  create_json("temperature", temperature, "°C");
  server.send(200, "application/json", buffer);
}
 
void getHumidity() {
  Serial.println("Get humidity");
  create_json("humidity", humidity, "%");
  server.send(200, "application/json", buffer);
}
 
void getPressure() {
  Serial.println("Get pressure");
  create_json("pressure", pressure, "mBar");
  server.send(200, "application/json", buffer);
}
void getEnv() {
  Serial.println("Get env");
  jsonDocument.clear();
  add_json_object("temperature", temperature, "°C");
  add_json_object("humidity", humidity, "%");
  add_json_object("pressure", pressure, "mBar");
  serializeJson(jsonDocument, buffer);
  server.send(200, "application/json", buffer);
}

void handlePost() {
  if (server.hasArg("plain") == false) {
    //handle error here
  }

  String body = server.arg("plain");
  Serial.println(body);
  deserializeJson(jsonDocument, body);
  // Respond to the client
  server.send(200, "application/json", "{}");
}


// setup API resources
void setup_routing() {
  server.on("/temperature", getTemperature);
  server.on("/pressure", getPressure);
  server.on("/humidity", getHumidity);
  server.on("/env", getEnv);
  server.on("/led", HTTP_POST, handlePost);
 
  // start server
  server.begin();
}


void setup_task() {
  xTaskCreate(
    read_sensor_data,    
    "Read sensor data",   // Name of the task (for debugging)
    1000,            // Stack size (bytes)
    NULL,            // Parameter to pass
    1,               // Task priority
    NULL             // Task handle
  );
}
int soilsens()
{
      // Read the value from the soil sensor
  int soilMoistureValue = analogRead(soilSensorPin);

  // Convert the value to a percentage
  int soilMoisturePercentage = map(soilMoistureValue, 0, 1023, 0, 100);
 
  Serial.print("Soil moisture: ");
  Serial.print(soilMoisturePercentage);
  Serial.println("%");

  delay(1000);  // Wait 1 second before reading the sensor again



}

int Dht22()
{
    // Read temperature as Celsius (the default)
  temp = dht.readTemperature();

  // Read humidity
  h = dht.readHumidity();

  // Check if any reads failed and exit early (to try again).
  //if (isnan(h) || isnan(temp) || isnan(tempF)) 
    //Serial.println("Failed to read from DHT sensor!");
    //return;
  {
  }
  //heat index calculation 
  float hic = dht.computeHeatIndex(temp, h, false);

  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.print("°C ");
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print("% ");
}


int mq135()
{
    // Read the value from the MQ135 sensor
  int airQualityValue = analogRead(mq135Pin);
  // Compute the air quality in ppm (parts per million)
  airQualityPpm = (float)airQualityValue / 1024 * 5.0;
  Serial.print("Air quality: ");
  Serial.print(airQualityPpm);
  Serial.println(" ppm");
  delay(1000);  // Wait 1 second before reading the sensor again
}

int bh175()
{
    // Read the light intensity in lux
  uint16_t lux = lightMeter.readLightLevel();
  Serial.print("Light intensity: ");
  Serial.print(lux);
  Serial.println(" lux");
  delay(1000);  // Wait 1 second before reading the sensor again
}


void setup() {
  Serial.begin(9600);
  connectToWiFi();
  setup_task();
  setup_routing(); 
  dht.begin();
  lightMeter.begin();
}

void loop() {
Dht22();
soilsens();
mq135();
bh175();
server.handleClient();
}
