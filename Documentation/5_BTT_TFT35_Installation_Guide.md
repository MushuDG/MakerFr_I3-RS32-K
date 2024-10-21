
# 🖥️ Integration of BTT TFT35 SPI V2.1 with BTT Manta M5P

This guide will help you successfully connect and configure your **BTT TFT35 SPI V2.1** touch screen with the **BTT Manta M5P**. We’ll go over the hardware setup, cabling, and software configuration, including calibration tips to avoid ghost touches.

## Table of Contents
- [🖥️ Integration of BTT TFT35 SPI V2.1 with BTT Manta M5P](#-integration-of-btt-tft35-spi-v21-with-btt-manta-m5p)
  - [🔧 Materials Needed](#-materials-needed)
  - [🛠️ Step 1: Hardware Installation](#-step-1-hardware-installation)
  - [🔌 Step 2: Cable Length and Ghost Touch Issues](#-step-2-cable-length-and-ghost-touch-issues)
  - [📁 Step 3: Installing KlipperScreen](#-step-3-installing-klipperscreen)
  - [⚙️ Step 4: Screen Calibration](#-step-4-screen-calibration)
  - [📚 References](#-references)

## 🔧 Materials Needed

1. **BTT TFT35 SPI V2.1 Touch Screen** – *This is the touch screen we will be using.*
2. **BTT Manta M5P Board** – *Your mainboard.*
3. **600mm SPI Cable** – *I recommend using a 600mm cable to avoid ghost touch issues due to interference.*
4. **Screwdriver, Wires, and Connectors** – *Standard tools for wiring and connection.*

## 🛠️ Step 1: Hardware Installation

1. **Mount the TFT35 Screen**: Securely mount the **TFT35 SPI V2.1** screen to your printer’s frame.
2. **Wiring**: Connect the screen to the **BTT Manta M5P** using the **SPI Screen** ports on both the screen and the board.
   - Use a **600mm SPI cable** to reduce the risk of interference (see the note below for more details on cable length).

## 🔌 Step 2: Cable Length and Ghost Touch Issues

When using a longer SPI cable (over 600mm), some users have reported **ghost touch issues**, which are caused by signal interference. To avoid this problem, it's best to stick to a **600mm cable**. If you need one, here is a recommended source:
- **600mm SPI Cable**: [eBay Link](https://www.ebay.fr/itm/253935636526?var=553252486969)

This should fix most interference issues.

## 📁 Step 3: Installing KlipperScreen

Once the hardware is set up and the screen is calibrated, we need to configure it in **Klipper**. **KIAUH** (Klipper Installation and Update Helper) makes it easy to install and configure KlipperScreen.

1. **SSH into your CB1**: Open a terminal and connect to your CB1 using SSH.
2. **Install KlipperScreen**:
    - Run the following command to start **KIAUH**:
    ```bash
    ./kiauh/kiauh.sh
    ```
    - In the main menu, type `1` to open the **Install Menu**, and type `5` to install KlipperScreen.
    - The tool will automate the process. Once completed, you'll see a success message.
3. **Restart Klipper**: After installation, restart Klipper, and you should see the TFT35 screen interface.

## ⚙️ Step 4: Screen Calibration

To improve the touch accuracy and avoid any ghost touches, it's important to **calibrate your screen**. Follow this official tutorial from **BTT** for calibrating your TFT35 SPI screen:

1. login into your CB1 via SSH
2. Install `xinput_calibrator`
```bash 
sudo apt update
sudo apt install xinput-calibrator
```
3. Query the ID of the touchscreen, The name of TFT35_SPI is ns2009 or TSC2007, as shown in the figure bellow the id is 6
```bash
DISPLAY=:0 xinput_calibrator --list
```
![tft35_spi_id](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/5_BTT_TFT35_Installation_Guide/tft35_spi_id.png)

4. Start calibration, Click on the center of the cross that appears one by one on the screen. Replace the id with the actual id found in the previous step. Record the parameters of `click 0 X`, `click 0 Y`, `click 3 X`, and `click 3 Y`, which are required for conversion.
```bash
DISPLAY=:0 xinput_calibrator -v --device <id>
```
![tft35_spi_id](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/5_BTT_TFT35_Installation_Guide/tft35_spi_calibration.png)

5. **!!! WARNING:** The parameter of `xinput_calibrator` cannot be directly used for `libinput` and needs to be converted. Please refer to here for details:
6. Create conversion script:
```bash
sudo nano libinput_calibrator.sh
```
7. Copy and paste the following content:

```bash
#!/bin/bash

#according to https://wiki.archlinux.org/title/Talk:Calibrating_Touchscreen#Libinput%5Fbreaks%5Fxinput%5Fcalibrator

screen_width=$1
screen_height=$2
click_0_X=$3
click_0_Y=$4
click_3_X=$5
click_3_Y=$6

re='^[0-9]+$'
if ! [[ $screen_width =~ $re ]] ; then
  echo "error: screen_width=\"$screen_width\" Not a number" >&2; exit 1
fi
if ! [[ $screen_height =~ $re ]] ; then
  echo "error: screen_height=\"$screen_height\" Not a number" >&2; exit 1
fi
if ! [[ $click_0_X =~ $re ]] ; then
  echo "error: click_0_X=\"$click_0_X\" Not a number" >&2; exit 1
fi
if ! [[ $click_0_Y =~ $re ]] ; then
  echo "error: click_0_Y=\"$click_0_Y\" Not a number" >&2; exit 1
fi
if ! [[ $click_3_X =~ $re ]] ; then
  echo "error: click_3_X=\"$click_3_X\" Not a number" >&2; exit 1
fi
if ! [[ $click_3_Y =~ $re ]] ; then
  echo "error: click_3_Y=\"$click_3_Y\" Not a number" >&2; exit 1
fi

#a = (screen_width * 6 / 8) / (click_3_X - click_0_X)
#c = ((screen_width / 8) - (a * click_0_X)) / screen_width
#e = (screen_height * 6 / 8) / (click_3_Y - click_0_Y)
#f = ((screen_height / 8) - (e * click_0_Y)) / screen_height

a=$(awk "BEGIN { printf(\"%.6f\", ($screen_width * 6 / 8) / ($click_3_X - $click_0_X))}")
c=$(awk "BEGIN { printf(\"%.6f\", (($screen_width / 8) - ($a * $click_0_X)) / $screen_width)}")
e=$(awk "BEGIN { printf(\"%.6f\", ($screen_height * 6 / 8) / ($click_3_Y - $click_0_Y))}")
f=$(awk "BEGIN { printf(\"%.6f\", (($screen_height / 8) - ($e * $click_0_Y)) / $screen_height)}")

CONFIG_OPTION="Option \"CalibrationMatrix\" "
CONFIG_LINE="\"$a 0.000000 $c 0.000000 $e $f 0.000000 0.000000 1.000000\""

echo "${CONFIG_OPTION}${CONFIG_LINE}"
echo ""

CONFIG_OPTION="Option \"CalibrationMatrix\" "
CONFIG="/usr/share/X11/xorg.conf.d/40-libinput.conf"
INPUT_CLASS="Identifier \"libinput touchscreen catchall\""
if [ -e "${CONFIG}" ]; then
    ks_restart=0
    grep -e "^\        ${CONFIG_OPTION}${CONFIG_LINE}" ${CONFIG} > /dev/null
    STATUS=$?
    if [ $STATUS -eq 1 ]; then
        sudo sed -i "/${CONFIG_OPTION}/d" ${CONFIG}
        sudo sed -i "/${INPUT_CLASS}/a\        ${CONFIG_OPTION}${CONFIG_LINE}" ${CONFIG}
        echo "Written to file:"
        echo "    ${CONFIG}"
        echo ""
        ks_restart=1
    fi

    # restart KlipperScreen
    if [ ${ks_restart} -eq 1 ];then
        sudo service KlipperScreen restart
    fi

    echo "run:"
    echo "    DISPLAY=:0 xinput list-props <device>"
    echo "to check if the calibration parameters are effective"
    echo ""
fi

```

8. Add executable permissions
```bash
sudo chmod +x libinput_calibrator.sh
```

9. Run the script with previous values in argument (got on point 4):

```bash
sudo ./libinput_calibrator.sh <screen width> <screen height> <click_0 X> <click_0 Y> <click_3 X> <click_3 Y>

```
Replace <arguments> with following values:
`<screen width>`: Screen horizontal resolution, TFT35 SPI is `480`
`<screen height>`: Screen vertical resolution, TFT35 SPI is `320`
`<click_0 X>`: The `X` position of `click 0` during the previous step calibration
`<click_0 Y>`: The `Y` position of `click 0` during the previous step calibration
`<click_3 X>`: The `X` position of `click 3` during the previous step calibration
`<click_3 Y>`: The `Y` position of `click 3` during the previous step calibration

for example:
```bash
sudo ./libinput_calibrator.sh 480 320 61 35 417 281
```

## 📚 References

1. [BTT TFT35 SPI V2.1 Documentation](https://bttwiki.com/tft35_spi_v2.1.html)
2. [BTT Manta M5P Documentation](https://github.com/bigtreetech/Manta-M5P)
3. [600mm SPI Cable on eBay](https://www.ebay.fr/itm/253935636526?var=553252486969)
4. [BTT Screen Calibration Guide](https://bttwiki.com/libinput_calibration.html)
5. [KlipperScreen Installation Guide](https://www.obico.io/blog/klipper-screen/)

Feel free to ask any questions or report issues in the [MakerFR forum](https://www.makerfr.com/forum/viewtopic.php?t=14710). Happy printing with your new touchscreen setup! 😊
