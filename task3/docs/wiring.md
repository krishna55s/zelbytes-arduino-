Wiring Guide

Components Used

- Arduino Uno
- Push Button
- Relay Module
- LED
- 220Ω Resistor
- Jumper Wires

Connections

Push Button

Arduino Pin| Connection
D2| Push Button
GND| Push Button

The button uses the internal pull-up resistor ("INPUT_PULLUP").

Relay Module

Arduino Pin| Connection
D8| Relay IN
5V| Relay VCC
GND| Relay GND

The relay controls the irrigation valve or pump.

Status LED

Arduino Pin| Connection
D13| LED Anode (+)
GND| LED Cathode (-) through 220Ω resistor

The LED indicates irrigation status:

- ON = Irrigation Active
- OFF = Irrigation Inactive

Pin Summary

Function| Pin
Manual Button| D2
Relay Valve| D8
Status LED| D13

Notes

- Ensure all grounds are connected together.
- Verify relay logic (active-high or active-low) before testing.
- Perform a dry run before connecting an actual water pump or valve.
