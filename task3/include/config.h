#ifndef CONFIG_H
#define CONFIG_H

// Irrigation duration
#define IRRIGATION_SECONDS 5

// Pin assignments
const uint8_t LED_STATUS = 13;
const uint8_t BTN_MANUAL = 2;
const uint8_t RELAY_VALVE = 8;

// Debounce timing
const unsigned long DEBOUNCE_MS = 50;

#endif
