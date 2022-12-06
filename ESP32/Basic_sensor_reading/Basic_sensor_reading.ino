//header file declarations 
#include "DHT.h"
#include "BH1750.h"

//on board pin assignment 
#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22   // DHT 22 (AM2302)
const int soilSensorPin = 33; //defining soil senosr pin 
const int mq135Pin = 34;

DHT dht(DHTPIN, DHTTYPE);
BH1750 lightMeter;


void setup() {
  Serial.begin(9600);
  dht.begin();
  lightMeter.begin();
}

void loop() {
Dht22();
soilsens();
mq135();
bh175();
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

void Dht22()
{
    // Read temperature as Celsius (the default)
  float temp = dht.readTemperature();

  // Read temperature as Fahrenheit (isFahrenheit = true)
  float tempF = dht.readTemperature(true);

  // Read humidity
  float h = dht.readHumidity();

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(temp) || isnan(tempF)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
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

void mq135()
{
    // Read the value from the MQ135 sensor
  int airQualityValue = analogRead(mq135Pin);
  // Compute the air quality in ppm (parts per million)
  float airQualityPpm = (float)airQualityValue / 1024 * 5.0;
  Serial.print("Air quality: ");
  Serial.print(airQualityPpm);
  Serial.println(" ppm");
  delay(1000);  // Wait 1 second before reading the sensor again
}

void bh175()
{
    // Read the light intensity in lux
  uint16_t lux = lightMeter.readLightLevel();
  Serial.print("Light intensity: ");
  Serial.print(lux);
  Serial.println(" lux");
  delay(1000);  // Wait 1 second before reading the sensor again
}
