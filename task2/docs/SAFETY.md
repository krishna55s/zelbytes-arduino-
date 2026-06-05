# SAFETY

The relay module is used to control external loads safely.

Safety Rules:
- Never connect a solenoid valve directly to an Arduino GPIO pin.
- Relay is OFF during startup.
- Emergency stop command (e) immediately disables the relay.
