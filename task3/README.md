Task 3 - Manual Irrigation Toggle (Phase 1 Capstone)

Objective

Develop a manual irrigation controller using Arduino, a push button, relay module, and status LED.

Features

- Debounced push button input
- Relay valve control
- Status LED indication
- Configurable irrigation duration (5 seconds)
- Automatic irrigation shutdown
- Serial event logging with timestamps
- Release version: v0.1-manual

Hardware Used

- Arduino Uno
- Push Button
- Relay Module
- LED
- Jumper Wires

Pin Configuration

Component| Pin
Button| D2
Relay Valve| D8
Status LED| D13

Working Principle

1. User presses the push button.
2. Relay valve activates.
3. Status LED turns ON.
4. Irrigation start event is logged in the Serial Monitor.
5. Irrigation runs for 5 seconds.
6. Relay valve turns OFF automatically.
7. Irrigation end event is logged with timestamp.

Sample Serial Output

[EVENT] Irrigation Started | Timestamp=14 sec since boot

[EVENT] Irrigation Ended | Timestamp=19 sec since boot

Repository Structure

Task-3-Manual-Irrigation-Toggle/

├── src/
│   └── Manual_irrigation_toggle.ino

├── include/
│   └── config.h

├── docs/
│   ├── project_report.md
│   ├── test_log.md
│   ├── wiring.md
│   └── bench_card.md

├── media/
│   ├── serial_monitor.jpeg
│   ├── circuit_setup.jpeg
│   └── demovideo.mp4

└── README.md

Documentation

- project_report.md – Project description and methodology
- test_log.md – Test results and validation
- wiring.md – Hardware wiring details
- bench_card.md – Operating and safety instructions

Results

The system successfully:

- Detected button presses using software debouncing
- Activated relay-controlled irrigation
- Indicated system status using LED
- Logged irrigation events with timestamps
- Automatically stopped irrigation after the configured duration

Release

Tag: v0.1-manual

Mentor Sign-Off

Mentor Name: _______________________

Review Date: _______________________

Remarks:

---

---

Status: ☐ Approved   ☐ Needs Revision
