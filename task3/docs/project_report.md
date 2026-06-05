# Project Report

## Title

Manual Irrigation Toggle

## Objective

Create a manual irrigation system with timed relay control and event logging.

## Methodology

A push button connected to D2 is monitored using software debouncing.

When a valid button press is detected:

- Relay activates
- LED turns ON
- Irrigation event is logged

The irrigation remains active for 5 seconds and then automatically stops.

## Components Used

- Arduino Uno
- Push Button
- Relay Module
- LED
- Jumper Wires

## Results

The system successfully activated the relay and logged irrigation events.

Example:

[EVENT] Irrigation Started | Timestamp=14 sec since boot

[EVENT] Irrigation Ended | Timestamp=19 sec since boot

## Conclusion

The manual irrigation controller worked successfully and met the Task 3 requirements.
