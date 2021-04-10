float factor = 0.75;        // Coeficente de filtro para bajas.
float maxValue = 0.0;       // Almacena valor máximo.
int minGapHR = 300;         // Distancia entre pulsos.
float bfrVal = 500;         // Almacenar valores previos.
int pulse = 0;              // Heart pulses counter.

void setup() {
  pinMode(13, OUTPUT);          // PIN 13 Salida.
  Serial.begin(9600);           // Serial empieza a 9600 bps.
  Serial.println("Midiendo");   // Texto de inicio.
}

void loop() {
  static unsigned long timePM = millis();     // Latidos por minuto [Tiempo Actual].
  static unsigned long btwBeat = millis();    // Tiempo entre latidos [Tiempo Actual].

  int readValue = analogRead(A0);

  float valFilter = factor * bfrVal + (1 - factor) * readValue;   // Filtro para bajas.
  float change = valFilter - readValue;
  bfrVal = valFilter;

  if ((change >= maxValue) && (millis() > btwBeat + minGapHR)){
    maxValue = change;
    digitalWrite(13, HIGH);
    btwBeat = millis();
    pulse++;
    }
  else{
    digitalWrite(13, LOW);
    }

  maxValue = maxValue * 0.97;

  if(millis() >= timePM + 15000){
    Serial.print("Latidos: ");
    Serial.println(pulse * 4);
    pulse = 0;
    timePM = millis();
    }
  delay(50);
}
