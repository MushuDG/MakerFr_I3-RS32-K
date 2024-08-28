# 🛠️ MakerFr I3-RS32-K Wiring Guide

This guide will help you correctly connect all components to ensure your 3D printer functions optimally. Remember to double-check every connection before powering up, particularly the polarities, to avoid any potential damage. ⚠️

## Table of Contents
1. [Wiring Overview](#wiring-overview)
   - [Connection Table](#connection-table)
2. [Important Note 📌](#important-note-)
3. [Display Wiring](#display-wiring)
4. [Jumpers Configuration 🔧](#jumpers-configuration-)
   - [UART Mode of TMC Driver](#uart-mode-of-tmc-driver)
   - [Driver Voltage Selection](#driver-voltage-selection)
   - [CNC Fan Voltage Selection](#cnc-fan-voltage-selection)
5. [Additional Steps ✅](#additional-steps-)
6. [References 📚](#references-)

## Wiring Overview

Refer to the following diagram for the overall wiring layout:

![Manta_M5P_Wiring](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/1_Wiring/Wiring.png)

### Connection Table

The table below provides detailed information on each connection point, including the pin or port, the connected component, its function, and the corresponding pinout.


| Pin/Port   | Connected Component     | Description                                | Pinout                                        |
| ------------ | ------------------------- | -------------------------------------------- | ----------------------------------------------- |
| **M1**     | Motor 1 (X-Axis)        | Stepper motor for X-Axis movement          | PA15 (EN), PB9 (STEP), PC6 (DIR), PD9 (CS)    |
| **M2**     | Motor 2 (Y-Axis)        | Stepper motor for Y-Axis movement          | PA13 (EN), PA10 (STEP), PA14 (DIR), PB9 (CS)  |
| **M3A**    | Motor 3A (Z-Axis)       | Stepper motor for Z-Axis (Left)            | PA9 (EN), PC7 (STEP), PC8 (DIR), PD8 (CS)     |
| **M4**     | Motor 4 (Z-Axis)        | Stepper motor for Z-Axis (Right)           | PA8 (EN), PB12 (STEP), PB11 (DIR), PB2 (CS)   |
| **M5**     | Motor 4 (Extruder)      | Stepper motor for the extruder             | PC4 (EN), PB0 (STEP), PB1 (DIR), PA6 (CS)     |
| **MIN1**   | X switch                | Endstop switch for X-Axis                  | PD3 (GND), PA3 (5V), PA2 (Signal)             |
| **MIN2**   | Y switch                | Endstop switch for Y-Axis                  | PD5 (GND), PA4 (5V), PA1 (Signal)             |
| **HE0**    | Hotend Heater           | Heats the filament for extrusion           | PA5 (VBB), PA7 (GND)                          |
| **TH0**    | Hotend Thermistor       | Measures the temperature of the hotend     | PA0 (Signal), GND                             |
| **TH1**    | Bed Thermistor          | Measures the temperature of the heated bed | PA0 (Signal), GND                             |
| **HV-IN**  | Power Input             | 24V Power supply connection                | HV+, HV-                                      |
| **FAN0**   | Part Cooling Fan        | Fan for cooling the printed part           | VBB (Power), PF3 (GND)                        |
| **FAN1**   | Hotend Cooling Fan      | Fan for cooling the hotend                 | VBB (Power), PF4 (GND)                        |
| **+FAN-**  | Electronics Cooling Fan | Fan for cooling the mainboard electronics  | VBB (Power), PF5 (GND)                        |
| **PI-FAN** | CB1 Cooling Fan         | Fan for cooling the CB1                    | VBB (Power), PF6 (GND)                        |
| **Probe**  | BLTouch                 | Used for automatic bed leveling            | PA11 (Signal), PC15 (GND), PA6 (5V)           |
| **HB**     | Bed Heater              | Power for the heated bed                   | PA5 (VBB), PA7 (GND)                          |

### Important Note 📌

The colors of the cables in the diagram can generally be trusted. However, the color order of stepper motor cables may vary depending on the manufacturer. Please ensure that the color sequence of your stepper motors matches the diagram or the pinout provided.

### Display Wiring

Connect the two EXP ports (EXP1, EXP2) to the TFT35 as shown in the diagram below:

![Screen](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/1_Wiring/Screen.png)

## Jumpers Configuration 🔧

### UART Mode of TMC Driver

If you're using TMC2208, TMC2209, TMC2225, or similar drivers, ensure the jumpers are placed as shown in the diagram below. The microsteps and current settings can be configured within the firmware.

![UART_TMC_Mode](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/1_Wiring/TMC_Drivers_Jumpers.png)

### Driver Voltage Selection

Select the appropriate driver voltage according to your configuration needs. Use the following diagram as a guide:

![Drivers_Voltage_Selection](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/1_Wiring/Drivers_Voltage.png)

### CNC Fan Voltage Selection

You can set the output voltage for the CNC fan to 24V, 12V, or 5V by adjusting the jumper cap accordingly.

![CNC_Fan_Voltage](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/1_Wiring/CNC_Fan_Voltage.png)

## Additional Steps ✅

Once everything is wired and set up, the power supply should start up, and the 40mm fan in the case should begin to spin, indicating that the system is powered on correctly.

To proceed with the installation of the CB1 OS, please follow the instructions in the [CB1 OS Installation Guide](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Documentation/2_CB1_OS_Installation.md).

## References 📚

1. RoMaker. "[I3RS32 wiring](https://www.makerfr.com/en/imprimante-3d/i3-rs32/cablage-i3rs32/)." *MakerFr*.
2. [BigTreeTech Manta M5P Documentation](https://github.com/bigtreetech/Manta-M5P)
