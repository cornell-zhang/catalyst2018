/////////////////////////////////////////////////
// mobile robot - FSM
// 0 - forward; 1 - reverse; 2 - rotate; 
// 3 - target;  4 - stop;
////////////////////////////////////////////////
// global constant for pin assignments
// control circuit
int state_machine_next_state(int current_state)
{ 
  int next_state = 0;
  if (current_state == 0)
  {
    if (switch_pressed_right or switch_pressed_left)
    {
      next_state = 1;
    }
  }
  else if (current_state == 1)
  {
    next_state = 2;
  }
  else if (current_state == 2)
  {
    next_state = 0;
  }
  return next_state;
}

int state_machine_switch(int state)
{
  switch(state)
  {
    case 0: 
    {
      forward(); break;
    }
    case 1: 
    {
      reverse(); break;
    }
    case 2: 
    {
      rotate(); break;
    }
  }
  return state;
}