
# 🌈 Neopixel LED Installation with Klipper on BTT Manta M5P

This guide will walk you through installing and configuring Neopixel LEDs on your BTT Manta M5P with Klipper. We’ll cover the physical installation, wiring, and configuring the Klipper firmware for dynamic LED control.

## Table of Contents
  1. [🔧 Materials Needed](#-materials-needed)
  2. [🛠️ Step 1: Physical Installation of LEDs](#️-step-1-physical-installation-of-leds)
  3. [🖥️ Step 2: Klipper Configuration for LEDs](#️-step-2-klipper-configuration-for-leds)
  4. [🚀 Step 3: Installing Klipper-LED\_Effect Plugin](#-step-3-installing-klipper-led_effect-plugin)
  5. [✅ Step 4: Testing and Verifying LED Installation](#-step-4-testing-and-verifying-led-installation)
  6. [📚 References](#-references)

## 🔧 Materials Needed

- **Neopixel LEDs** – *We used Black PCB, 1m 74 IP30, but feel free to choose your desired density (e.g., 144 LEDs/m).*
- **Wires** – *Three wires for power, ground, and signal.*
- **Soldering Kit** – *Ensure to solder correctly, following the directional arrow on the PCB!*
- **Connector JST** – *For connecting to the Manta board.*
- **BTT Manta M5P** – *Your baseboard where the LEDs will be connected.*

## 🛠️ Step 1: Physical Installation of LEDs

1. **Unboxing and Preparing LEDs**: Start by preparing your Neopixel LEDs. You can use 74 LEDs/m or opt for 144 LEDs/m for a more consistent lighting effect.
2. **Wiring and Soldering**: Solder the three wires to the LED strip, ensuring to follow the directional arrow on the PCB that indicates signal direction. 
    - **Common mistake**: Don’t solder on the wrong side (the direction of the arrow is crucial). 
3. **Connecting to the Manta Board**: 
    - Use a **JST connector** to hook up the LEDs directly to the **RGB1 port** of the Manta board:
![Manta_M5P_LEDS_Wiring](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/4_Neopixel_LED_Installation_Guide/LEDS.png)
  

## 🖥️ Step 2: Klipper Configuration for LEDs

1. **Download the Configuration File**: Download the `leds.cfg` from this [GitHub link](https://raw.githubusercontent.com/MushuDG/MakerFr_I3-RS32-K/refs/heads/main/Klipper_Config/components_config/leds.cfg) and place it in the `~/printer_data/config/` directory.
2. **Edit printer.cfg**: 
    - In your `printer.cfg`, include the line `[include leds.cfg]` to load the LED configuration file. Uncomment this line by removing the `#`.
3. **Configure the LED settings**: In the `leds.cfg` file, adjust the following parameters:
    - **Pin**: Specify the pin depending on where the LEDs are connected. Use `PC11` for **RGB1** and `PC14` for **RGB2**.
    - **Chain Count**: Specify the number of LEDs in your chain. For example, `chain_count: 22`.

    ```ini
    pin: PC11  # Pin connected to the Neopixel LEDs.
    chain_count: 22  # Number of Neopixels in the chain.
    ```

## 🚀 Step 3: Installing Klipper-LED_Effect Plugin

1. **SSH into Your CB1**: Open a terminal and SSH into your CB1 board.
2. **Run the following commands** to clone and install the Klipper-LED_Effect plugin:

    ```bash
    cd ~
    git clone https://github.com/julianschill/klipper-led_effect.git
    cd klipper-led_effect
    ./install-led_effect.sh
    ```

3. **Configure LED Effects**: Follow the instructions in the Klipper-LED_Effect repository to set up and customize various LED effects.

## ✅ Step 4: Testing and Verifying LED Installation

1. **Restart Klipper**: Once everything is installed, restart Klipper for the changes to take effect.
2. **Test LED Operation**: Use commands in the Klipper console to check if the LEDs are functioning correctly. Adjust the effects or configurations as needed.
3. **Troubleshooting**: If the LEDs don’t light up or behave unexpectedly, double-check the wiring and ensure that the `leds.cfg` file is correctly configured.

## 📚 References
1. [Klipper LED Effects Plugin Documentation](https://github.com/julianschill/klipper-led_effect)
2. [BTT Manta M5P Documentation](https://github.com/bigtreetech/Manta-M5P)

Happy printing with your glowing setup! 🌟
