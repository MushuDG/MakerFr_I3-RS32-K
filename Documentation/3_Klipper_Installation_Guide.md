
# 🚀 Klipper Installation Guide via KIAUH

This guide will walk you through installing Klipper on your BTT CB1 with a BTT Manta M5P using KIAUH (Klipper Installation And Update Helper). Let's get started!

## Table of Contents
1. [🎯 Prerequisites](#-prerequisites)
2. [🛠️ Step 1: SSH into Your Machine](#️-step-1-ssh-into-your-machine)
3. [🧰 Step 2: Install Git](#-step-2-install-git)
4. [📥 Step 3: Clone the KIAUH Repository](#-step-3-clone-the-kiauh-repository)
5. [🚀 Step 4: Launch KIAUH](#-step-4-launch-kiauh)
6. [🔧 Step 5: Install Klipper](#-step-5-install-klipper)
7. [🌑 Step 6: Install Moonraker](#-step-6-install-moonraker)
8. [💧 Step 7: Install Fluidd](#-step-7-install-fluidd)
9. [🔧 Step 8: Configure Klipper](#-step-8-configure-klipper)
10. [🌐 Step 9: Access Fluidd](#-step-9-access-fluidd)
11. [⚙️ Step 10: Configure Fluidd for Klipper](#️-step-10-configure-fluidd-for-klipper)
12. [🔄 Step 11: Reboot and Test](#-step-11-reboot-and-test)
    - [Home Axes + Bed Mesh Calibration](#home-axes--bed-mesh-calibration)
    - [Z-Tilt](#z-tilt)
    - [PID Calibration for Hotend](#pid-calibration-for-hotend)
    - [PID Calibration for Bed](#pid-calibration-for-bed)
13. [🛠️ Step 12: Adjust the Z-Offset Using `PROBE_CALIBRATE`](#%EF%B8%8F-step-12-adjust-the-z-offset-using-probe_calibrate)
    - [Step 12.1: Open the Fluidd Interface](#step-121-open-the-fluidd-interface)
    - [Step 12.2: Start the Probe Calibration](#step-122-start-the-probe-calibration)
    - [Step 12.3: Adjust the Z-Offset](#step-123-adjust-the-z-offset)
    - [Step 12.4: Save the Calibration](#step-124-save-the-calibration)
    - [Step 12.5: Test the New Z-Offset](#step-125-test-the-new-z-offset)
14. [🛠️ Step 13: Calibrating Extruder Rotation Distance](#%EF%B8%8F-step-13-calibrating-extruder-rotation-distance)
    - [Initial Setup](#initial-setup)
    - [Step-by-Step Calibration](#step-by-step-calibration)

## 🎯 Prerequisites

Before we begin, ensure you have the following:

- **BTT CB1 + BTT Manta M5P**: Your hardware should be set up and running a compatible Linux-based OS.
- **SSH Access**: Make sure SSH is enabled and you can connect to your system.

## 🛠️ Step 1: SSH into Your Machine

First, connect to your BTT CB1 via SSH:

```bash
ssh <username>@<IP_of_your_BTT_CB1>
```

Replace `<username>` with your actual username and `<IP_of_your_BTT_CB1>` with the IP address of your BTT CB1.

## 🧰 Step 2: Install Git

Ensure Git is installed on your machine:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git -y
```

## 📥 Step 3: Clone the KIAUH Repository

Next, clone the KIAUH repository:

```bash
git clone https://github.com/th33xitus/kiauh.git
cd kiauh
```

## 🚀 Step 4: Launch KIAUH

Run KIAUH to open the installation menu:

```bash
./kiauh.sh
```

## 🔧 Step 5: Install Klipper

1. Select `Install Klipper` from the menu using `1` and `1` in the `[ Installation Menu ]`.
2. Select your preferred Python version. Use `1` for the recommended setting.
3. Select the number of Klipper instances to set up. The number of Klipper instances will determine the amount of printers you can run from the host. Select `1` to install 1 instance.

## 🌑 Step 6: Install Moonraker

1. From the `Installation Menu`, type `1` to start the installation process.
2. Select `2 [Moonraker]` to install Moonraker.
3. Enter `Y` to confirm the installation.

## 💧 Step 7: Install Fluidd

1. From the `Installation Menu`, type `1` to start the installation process.
2. Select `4 [Fluidd]` to install Fluidd.
3. Enter `Y` to confirm the installation.
4. Enter `Y` again when prompted to install the recommended macros.

## 🔧 Step 8: Configure Klipper

1. From the main menu, use `4` to enter the `Advanced Menu`.
2. Type `2` to enter the Klipper firmware building setup.
3. Enter these parameters:

```bash
[*] Enable extra low-level configuration options
    Micro-controller Architecture (STMicroelectronics STM32) --->
    Processor model (STM32G0B1) --->
    Bootloader offset (8KiB bootloader) --->
    Clock Reference (8 MHz crystal) --->
    Communication interface (USB (on PA11/PA12)) --->
```

4. Type `q` to quit and save the config. The building step will automatically be launched.
5. Type `3` in the `Advanced Menu`.
6. Type `1` to use the regular flashing method.
7. Type `1` to use `make flash`.
8. Type `1` to install in USB mode.
9. Enter your available MCU number and enter `Y` to continue.

   **Note:** After the writing is completed, there will be an error message: `dfu-util: Error during download get_status`, just ignore it.

## 🌐 Step 9: Access Fluidd

After everything is set up, you can access Fluidd from your web browser:

```http
http://<IP_of_your_BTT_CB1>
```

Replace `<IP_of_your_BTT_CB1>` with the actual IP address of your BTT CB1.

## ⚙️ Step 10: Configure Fluidd for Klipper

Copy the [printer.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config) (select and adapt it to your requirements) content into the `/home/biqu/printer_data/config/printer.cfg` file.

   **Important:** Adapt the `printer.cfg` to your requirements, and change the `[mcu]` section with your serial ID.

   To find your serial ID, enter the following command in your SSH connection:

   ```bash
   ls /dev/serial/by-id
   ```

## 🔄 Step 11: Reboot and Test

Finally, reboot your BTT CB1 to ensure everything is set up correctly. After rebooting, test your setup by sending a command to your 3D printer via Fluidd.

You can test with the following commands:

### Home Axes + Bed Mesh Calibration:
```gcode
G28
BED_MESH_CALIBRATE
SAVE_CONFIG
```

### Z-Tilt:
```gcode
G28
Z_TILT_ADJUST
```

### PID Calibration for Hotend:
```gcode
PID_CALIBRATE HEATER=extruder TARGET=205
```

### PID Calibration for Bed:
```gcode
PID_CALIBRATE HEATER=heater_bed TARGET=65
```

## 🛠️ Step 12: Adjust the Z-Offset Using `PROBE_CALIBRATE`

Setting the correct Z-offset is crucial for achieving a perfect first layer. Here’s how to do it using the `PROBE_CALIBRATE` command directly from the Fluidd interface.

### Step 12.1: Open the Fluidd Interface

1. Access your Fluidd interface via your web browser.
2. Navigate to the **Console** tab.

### Step 12.2: Start the Probe Calibration

In the console, initiate the probe calibration process by entering:

```gcode
PROBE_CALIBRATE
```

This command will begin the process by homing the printer and then moving the probe to the center of the bed.

### Step 12.3: Adjust the Z-Offset

Once the probe is positioned, the nozzle will move down toward the bed. You need to manually adjust the Z-offset using the following command:

```gcode
TESTZ Z=-0.1
```

Keep sending the `TESTZ` command with small negative increments (e.g., `Z=-0.1`) until the nozzle is at the perfect distance from the bed. Use a piece of paper as a feeler gauge—when you feel slight resistance while moving the paper, you've found the correct offset.

### Step 12.4: Save the Calibration

After finding the right Z-offset, save the configuration with:

```gcode
ACCEPT
SAVE_CONFIG
```

The `ACCEPT` command will finalize the Z-offset setting, and `SAVE_CONFIG` will write this setting to your `printer.cfg` file.

### Step 12.5: Test the New Z-Offset

Finally, test your new Z-offset by printing a small test print to ensure the first layer adheres correctly. If further adjustments are needed, repeat the above steps.

## 🛠️ Step 13: Calibrating Extruder Rotation Distance

The `rotation_distance` of an extruder is the distance that the filament travels during one complete rotation of the stepper motor. To get this setting just right, it’s best to use a "measure and adjust" method. Here’s how:

### Initial Setup

1. **Estimate the Rotation Distance:** Start with an initial estimate of the `rotation_distance`. You can derive this from `steps_per_mm` or by inspecting your hardware.
   
2. **Prepare Your Printer:**
   - Make sure the extruder is loaded with filament.
   - Heat the hotend to the appropriate temperature.
   - Ensure your printer is ready to extrude.

### Step-by-Step Calibration

1. **Mark the Filament:**
   - Use a marker to place a mark on the filament approximately 70 mm from where it enters the extruder.
   - Use digital calipers to measure the exact distance from the mark to the extruder entrance. Record this as `initial_mark_distance`.

2. **Extrude Filament:**
   - In your printer’s console, run the following commands to extrude 50 mm of filament:
     ```
     G91
     G1 E50 F60
     ```
   - Record 50 mm as `requested_extrusion_distance`.
   - Wait for the extruder to complete the movement (about 50 seconds). Using a slow speed is crucial for accuracy, as faster speeds may cause high pressure, distorting your results. (Avoid using graphical interface extrude buttons for this test—they extrude too quickly.)

3. **Measure the Result:**
   - Use the calipers again to measure the new distance from the extruder entrance to the mark on the filament. Record this as `final_mark_distance`.
   - Calculate the actual amount extruded:  
     `actual_extrusion_distance = initial_mark_distance - final_mark_distance`

4. **Update the Rotation Distance:**
   - Calculate the new `rotation_distance` using:  
     `new_rotation_distance = previous_rotation_distance * actual_extrusion_distance / requested_extrusion_distance`

