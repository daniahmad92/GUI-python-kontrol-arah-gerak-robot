// ROBOT KONTROL KOMPUTER
// Definisi awal
int kiriA = 9;
int kiriB = 6;
int kananA = 5;
int kananB = 3;
void setup()
{
  Serial.begin(9600);
  pinMode(kiriA,OUTPUT);
  pinMode(kiriB,OUTPUT);
  pinMode(kananA,OUTPUT);
  pinMode(kananB,OUTPUT);
}
void loop()
{
  if(Serial.available()>0)
  {
    byte dataku=Serial.read();
    if (dataku=='M')
    {
      digitalWrite(kiriA,HIGH);
      digitalWrite(kiriB,LOW);
      digitalWrite(kananA,HIGH);
      digitalWrite(kananB,LOW);
      Serial.println("ROBOT MUNDUR");
    }
    else if (dataku=='K')
    {
      digitalWrite(kiriA,LOW);
      digitalWrite(kiriB,HIGH);
      digitalWrite(kananA,LOW);
      digitalWrite(kananB,HIGH);
      Serial.println("ROBOT MAJU");
    }
    else if (dataku=='Z')
    {
      digitalWrite(kiriA,LOW);
      digitalWrite(kiriB,HIGH);
      digitalWrite(kananA,HIGH);
      digitalWrite(kananB,LOW);
      Serial.println("ROBOT BELOK KIRI");
    }
    else if (dataku=='A')
    {
      digitalWrite(kiriA,HIGH);
      digitalWrite(kiriB,LOW);
      digitalWrite(kananA,LOW);
      digitalWrite(kananB,HIGH);
      Serial.println("ROBOT BELOK KANAN");
    }
    else
    {
      digitalWrite(kiriA,LOW);
      digitalWrite(kiriB,LOW);
      digitalWrite(kananA,LOW);
      digitalWrite(kananB,LOW);
      Serial.println("ROBOT DIAM");
    }
  }
}

