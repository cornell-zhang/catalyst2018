// Global constants for pin assignments

int pin_bump_right = 6;
int pin_bump_left = 7;

int pin_motor_left_dir = 12;
int pin_motor_right_dir = 13;
int pin_motor_left_speed = 3;
int pin_motor_right_speed = 11;

int pin_IR_sensor=A4;


 // The setup routine runs once when you press reset
int state_looking = 0;
int state_found = 2;
int state_block = 1;
int curr_state;
int sensor_value;
int target_value;

void setup() {
  Serial.begin(9600);  // setup the serial terminal
  pinMode( pin_bump_right, INPUT );
  pinMode( pin_bump_left, INPUT );
  
  pinMode( pin_motor_left_dir, OUTPUT );
  pinMode( pin_motor_right_dir, OUTPUT );
  pinMode( pin_motor_left_speed, OUTPUT );
  pinMode( pin_motor_right_speed, OUTPUT );
  
  // Motors are initially turning forward but with zero speed
  
  digitalWrite( pin_motor_left_dir, LOW );
  digitalWrite( pin_motor_right_dir, LOW );
  analogWrite( pin_motor_left_speed, 0 );
  analogWrite( pin_motor_right_speed, 0 );
  curr_state = state_looking;
  target_value = 500;
 }

 // The loop routine runs over and over again

void loop() {

  // Insert code to check if bump switches are pressed (Hint: See Part 2.A)
  int switch_left_pressed = digitalRead(pin_bump_left);
  int switch_right_pressed = digitalRead(pin_bump_right);
  sensor_value=analogRead(pin_IR_sensor);
  if((curr_state!=state_found) or (curr_state!=state_detect)) curr_state = state_looking;
  if (switch_left_pressed or switch_right_pressed ) {curr_state = state_detect;}
  if((sensor_value-target_value<50) or (sensor_value-target_value>-50)){curr_state = state_found;} //gives us a range of values for target

  

  if(curr_state == state_detect){
    // Insert code to stop robot by setting motor speed to zero
    analogWrite( pin_motor_left_speed, 0 );
    analogWrite( pin_motor_right_speed, 0 );
    digitalWrite( pin_motor_left_dir, HIGH );
    digitalWrite( pin_motor_right_dir, LOW );
    analogWrite( pin_motor_left_speed, 100 );
    analogWrite( pin_motor_right_speed, 100 );
    digitalWrite( pin_motor_left_dir, LOW );
    digitalWrite( pin_motor_right_dir, LOW );
  }
  else if(curr_state == state_found){
    analogWrite( pin_motor_left_speed, 0 );
    analogWrite( pin_motor_right_speed, 0 );
    digitalWrite( pin_motor_left_dir, HIGH );
    digitalWrite( pin_motor_right_dir, LOW );
    analogWrite( pin_motor_left_speed, 100 );
    analogWrite( pin_motor_right_speed, 100 );
  }
  else{
    analogWrite( pin_motor_left_speed, 200 );
    analogWrite( pin_motor_right_speed, 200 );
  }
  

}
