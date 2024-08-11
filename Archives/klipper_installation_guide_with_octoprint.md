
# 🚀 Installing Klipper on BigTreeTech CB1 and Manta M5P

This guide will help you install and configure Klipper on your BigTreeTech CB1 board with the Manta M5P motherboard.

## 📋 Prerequisites

Before starting, ensure you have the following:

- BigTreeTech CB1 and Manta M5P properly connected and set up.
- A running instance of OctoPrint or access to the CB1 via SSH.

## 🔧 Preparing OctoPrint for Klipper

To use Klipper with OctoPrint, you will need to install the necessary plugin:

1. Open OctoPrint in your web browser.
2. Navigate to **Settings** (wrench icon) > **Plugin Manager**.
3. Click **Get More...** to install a new plugin.
4. Search for "Klipper" and click **Install** on the "OctoPrint-Klipper" plugin.
5. After installation, restart OctoPrint.

## 🔧 Preparing Your System

### 1. Update Your System

Before installing Klipper, ensure your system is up to date:

```bash
sudo apt-get update
sudo apt-get upgrade
```

### 2. Install Required Dependencies

Install the necessary packages for Klipper:

```bash
sudo apt-get install make cmake gcc g++ python3-dev libffi-dev build-essential libncurses-dev avrdude binutils-dev libusb-1.0-0-dev
sudo apt-get install gcc-arm-none-eabi libnewlib-arm-none-eabi libusb-1.0 dfu-util
```

## 🛠️ Installing Klipper

### 1. Clone Klipper Repository

To install Klipper, you'll first need to clone the repository:

```bash
cd ~
git clone https://github.com/Klipper3d/klipper.git
```

### 2. Build the Klipper Firmware for the CB1 and Manta M5P

1. Navigate to the Klipper directory:

    ```bash
    cd ~/klipper
    ```

2. Start the configuration tool:

    ```bash
    make menuconfig
    ```

3. In the menu:

Compile the firmware with the following configuration(if the options below are
not available, please update your Klipper source code to the newest version).
* [*] Enable extra low-level configuration options
* Micro-controller Architecture (STMicroelectronics STM32) --->
* Processor model (STM32G0B1) --->
* Bootloader offset (8KiB bootloader) --->
* Clock Reference (8 MHz crystal) --->
* Communication interface (USB (on PA11/PA12)) --->

4. Save and exit the configuration tool.

5. Build the firmware:

    ```bash
    make
    ```

### 3. Flash the Firmware to the Manta M5P

1. Once the firmware is built, it will be located in the `~/klipper/out/klipper.bin` file.
If ls /dev/serial/by-id/ can find the klipper device ID of the MCU, you can enter
```bash
make flash FLASH_DEVICE=/dev/serial/by-id/usb-Klipper_stm32g0b1xx_190028000D50415833323520-if00
```
directly to write the firmware. (note: replace /dev/serial/by-id/xxx with the actual ID
queried in the previous step.)
After the writing is completed, there will be an error message: dfu-util: Error
during download get_status, just ignore it.

### 4. Configure Klipper for Your Printer

1. Access your Klipper instance, either through OctoPrint or SSH.
2. Edit the Klipper configuration file:

    ```bash
    nano ~/printer.cfg
    ```

3. Set up your configuration file based on your specific printer setup, including stepper motor settings, endstops, and more. You may find pre-made configurations for your specific printer model on the Klipper GitHub repository or community forums.

4. Save the configuration and restart Klipper:

    ```bash
    sudo service klipper restart
    ```

## 🔄 Verifying the Installation

1. Use the OctoPrint terminal or SSH to connect to Klipper.
2. Type `status` to ensure Klipper is running correctly.
3. If the status is `Ready`, your setup is successful. Otherwise, review the configuration for any errors.

## 🛠️ Additional Configuration

For optimal performance, consider configuring the following:

- **PID Tuning**: Fine-tune your hotend and bed PID settings for stable temperatures.
- **Pressure Advance and Input Shaping**: These advanced features can improve print quality, especially at higher speeds.

## 🎉 Final Steps

Your BigTreeTech CB1 and Manta M5P are now set up with Klipper. Enjoy the enhanced capabilities and performance of your 3D printer!

---
If you have any issues or need further assistance, check out the [Klipper documentation](https://www.klipper3d.org/Installation.html) or join the Klipper community forums.



python3 -m venv /home/biqu/klipper-env
source /home/biqu/klipper-env/bin/activate
pip install cffi pyserial greenlet numpy pygments pillow




sudo nano /etc/systemd/system/klipper.service


[Unit]
Description=Klipper 3D printer firmware
After=network.target

[Service]
User=biqu
ExecStart=/home/biqu/klipper-env/bin/python /home/biqu/klipper/klippy/klippy.py /home/biqu/printer.cfg -l /tmp/klippy.log
Restart=always
Type=simple
TimeoutStartSec=10
TimeoutStopSec=30

[Install]
WantedBy=multi-user.target

sudo systemctl daemon-reload
sudo systemctl restart klipper
sudo systemctl status klipper

https://all3dp.com/2/install-octoprint-klipper-single-board-computer-sbc/


Clone KIAUH

Now that we have Git installed, we can copy the GitHub repository where KIAUH is stored:

    We choose the target directory with the command cd ~.
    We clone the repository with git clone https://github.com/th33xitus/kiauh.git.
    We run the script with ./kiauh/kiauh.sh.
