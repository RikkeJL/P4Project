//const means that these values will not change during runtime
const int frequency_Effect_Indicator = 13, echo_Effect_Indicator = 12,
          vibrato_Effect_Indicator = 11, chorus_Effect_Indicator = 10,
          change_State_Button = 2, FSR_Pin = A5;

int buttonState = 0, buttonLastState = 0, state = 0;
int FSR_Value = 0;

unsigned long previousMillis = 0;
const long interval = 300;

void setup() {
  //Opens up the Serial connection, and sets the datarate to be 9600
  Serial.begin(9600);
  
  //specify the task that each pin will do.
  pinMode(frequency_Effect_Indicator, OUTPUT);
  pinMode(echo_Effect_Indicator, OUTPUT);
  pinMode(vibrato_Effect_Indicator, OUTPUT);
  pinMode(chorus_Effect_Indicator, OUTPUT);
  pinMode(change_State_Button, INPUT);
  pinMode(FSR_Pin, INPUT);
}

void loop() {
  
  //read the current state of the button
  buttonState = digitalRead(change_State_Button);
  
  //if the last state is different from the current, then:
  if (buttonState != buttonLastState && buttonState == HIGH) {
    //if state is below four, add one and print the value. else set it to 0.
    if (state < 4) {
      state++;
      Serial.print("S");
      Serial.println(state);
    } else {
      state = 0;
      Serial.print("S");
      Serial.println(state);
    }
    changedState(state);
  }

  //load in the state of the button, to compare with future button states.
  buttonLastState = buttonState;

  unsigned long currentMillis = millis();
  
  if (currentMillis - previousMillis >= interval) {
    //Read FSR value and print it.
    FSR_Value = analogRead(FSR_Pin);
    Serial.print("F");
    Serial.println(FSR_Value);
    previousMillis = currentMillis;
  }
}

//changes which LED is on, depending on the value of the state verible.
void changedState(int state) {
  switch (state) {
    case 1:
      digitalWrite(frequency_Effect_Indicator, HIGH);
      digitalWrite(echo_Effect_Indicator, LOW);
      digitalWrite(vibrato_Effect_Indicator, LOW);
      digitalWrite(chorus_Effect_Indicator, LOW);
      break;
    case 2:
      digitalWrite(frequency_Effect_Indicator, LOW);
      digitalWrite(echo_Effect_Indicator, HIGH);
      digitalWrite(vibrato_Effect_Indicator, LOW);
      digitalWrite(chorus_Effect_Indicator, LOW);
      break;
    case 3:
      digitalWrite(frequency_Effect_Indicator, LOW);
      digitalWrite(echo_Effect_Indicator, LOW);
      digitalWrite(vibrato_Effect_Indicator, HIGH);
      digitalWrite(chorus_Effect_Indicator, LOW);
      break;
    case 4:
      digitalWrite(frequency_Effect_Indicator, LOW);
      digitalWrite(echo_Effect_Indicator, LOW);
      digitalWrite(vibrato_Effect_Indicator, LOW);
      digitalWrite(chorus_Effect_Indicator, HIGH);
      break;
    default:
      digitalWrite(frequency_Effect_Indicator, LOW);
      digitalWrite(echo_Effect_Indicator, LOW);
      digitalWrite(vibrato_Effect_Indicator, LOW);
      digitalWrite(chorus_Effect_Indicator, LOW);
      break;
  }
}
