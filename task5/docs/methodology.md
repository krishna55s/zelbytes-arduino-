Methodology

    Initialize sensors and outputs.

    Enter IDLE state at startup.

    Transition to MONITORING state.

    Continuously read:
        Soil moisture
        Humidity

    If soil moisture remains below 25% for three consecutive readings:
        Start irrigation.

    Open valve through relay.

    Continue irrigation until:
        Moisture reaches 40%, or
        Maximum runtime expires.

    Enter COOLDOWN state.

    Wait 5 seconds.

    Return to MONITORING state.

    If DHT22 fails three consecutive readings:

    Enter FAULT state.
    Close valve.
    Blink status LED.

