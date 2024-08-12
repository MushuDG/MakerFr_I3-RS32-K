
# 🚀 Klipper Installation Guide via OctoPrint using KIAUH

This guide will walk you through installing Klipper on your BTT CB1 with a BTT Manta M5P using KIAUH (Klipper Installation And Update Helper). Let's get started!

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

## 🌕 Step 6: Install Moonraker

1. Select `Install Moonraker` from the menu using `1` and `2` in the `[ Installation Menu ]`.
2. Enter `Y` to install Moonraker.

## 🎛️ Step 7: Install OctoPrint

1. From the `Installation Menu`, type `6` to start OctoPrint installation.
2. Enter `Y` to install OctoPrint (this step may take a while. Don't quit during the installation).

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

## 🌐 Step 9: Access OctoPrint

After everything is set up, you can access OctoPrint from your web browser:

```http
http://<IP_of_your_BTT_CB1>:5000
```

Replace `<IP_of_your_BTT_CB1>` with the actual IP address of your BTT CB1.

## ⚙️ Step 10: Configure OctoPrint for Klipper

1. In OctoPrint, navigate to **Settings**.
2. Under **"Serial Connection"**, configure the serial connection to communicate with Klipper using `/home/biqu/printer_data/comms/klippy.serial`.
3. In **"Plugin Manager"**, ensure OctoKlipper is installed.
4. In **"OctoKlipper -> Basic's settings"** set:

   - Serial Port: `/home/biqu/printer_data/comms/klippy.serial`
   - Klipper Config Directory: `/home/biqu/printer_data/config`
   - Klipper Base Config Filename: `printer.cfg`
   - Klipper Log File: `~/klippy.log`

5. Copy the [printer.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Klipper_Config/printer.cfg) content into the `/home/biqu/printer_data/config/printer.cfg` file.

   **Important:** Adapt the `printer.cfg` to your requirements, and change the `[mcu]` section with your serial ID.

   To find your serial ID, enter the following command in your SSH connection:

   ```bash
   ls /dev/serial/by-id
   ```

## 🔄 Step 11: Reboot and Test

Finally, reboot your BTT CB1 to ensure everything is set up correctly. After rebooting, test your setup by sending a command to your 3D printer via OctoPrint.

You can test with the following commands:

### Home Axes + Bed Mesh Calibration:
```gcode
G28
BED_MESH_CALIBRATE
SAVE_CONFIG
```

### Z-Tilt:
```gcode
Z_TILT_ADJUST
```

### PID Calibration for Hotend:
```gcode
PID_CALIBRATE HEATER=extruder TARGET=200
```

### PID Calibration for Bed:
```gcode
PID_CALIBRATE HEATER=heater_bed TARGET=60
```

---

🎉 Congratulations! You've successfully installed Klipper on your BTT CB1 with a BTT Manta M5P using KIAUH. Enjoy the enhanced performance and capabilities Klipper brings to your 3D printing experience!
