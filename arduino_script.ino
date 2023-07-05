

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9 
#define SS_PIN 10 
MFRC522 mfrc522(SS_PIN, RST_PIN);

int inByte = 0;
unsigned long start;

void setup() {
  Serial.begin(9600);  //inicjujemy komunikację szeregową
  SPI.begin();         //inicjacja magistrali SPI
  mfrc522.PCD_Init();  // inicjacja RC522
}

void loop() {
  // Sprawdzamy, otrzymaliśmy jakąś wiadomość w serialu
  if (Serial.available() > 0) {
    inByte = Serial.read();
    if (inByte == 82) {  // 82 == 'R'
      start = millis();
      while (millis() - start < 10000){  // na pojawienie się karty czekamy 10s
        if (mfrc522.PICC_IsNewCardPresent()) {
        //odczyt karty
        if (mfrc522.PICC_ReadCardSerial()) {
          // wyswietlenie ID twojej karty RFID
          for (byte i = 0; i < mfrc522.uid.size; i++) {
            Serial.print(mfrc522.uid.uidByte[i]); // przez Serial wysyłamy ID karty
          }
          Serial.println();
          mfrc522.PICC_HaltA();
        }
        break;
      }
      }
    }
  }
}