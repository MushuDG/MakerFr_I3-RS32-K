
# 🚀 Klipper Installation Guide via KIAUH

This guide will walk you through installing Klipper on your BTT CB1 with a BTT Manta M5P using KIAUH (Klipper Installation And Update Helper). Let's get started!

## Table of Contents
- [🚀 Klipper Installation Guide via KIAUH](#-klipper-installation-guide-via-kiauh)
  - [Table of Contents](#table-of-contents)
  - [🎯 Prerequisites](#-prerequisites)
  - [🛠️ Step 1: SSH into Your Machine](#️-step-1-ssh-into-your-machine)
  - [🧰 Step 2: Install Git](#-step-2-install-git)
  - [📥 Step 3: Clone the KIAUH Repository](#-step-3-clone-the-kiauh-repository)
  - [🚀 Step 4: Launch KIAUH](#-step-4-launch-kiauh)
  - [🔧 Step 5: Install Klipper](#-step-5-install-klipper)
  - [🌑 Step 6: Install Moonraker](#-step-6-install-moonraker)
  - [💧 Step 7: Install Fluidd](#-step-7-install-fluidd)
  - [🔧 Step 8: Configure Klipper](#-step-8-configure-klipper)
  - [🌐 Step 9: Access Fluidd](#-step-9-access-fluidd)
  - [⚙️ Step 10: Configure Fluidd for Klipper](#️-step-10-configure-fluidd-for-klipper)
  - [🔄 Step 11: Reboot and Test](#-step-11-reboot-and-test)
    - [Home Axes + Bed Mesh Calibration:](#home-axes--bed-mesh-calibration)
    - [Z-Tilt:](#z-tilt)
    - [PID Calibration for Hotend:](#pid-calibration-for-hotend)
    - [PID Calibration for Bed:](#pid-calibration-for-bed)
  - [🛠️ Step 12: Adjust the Z-Offset Using `PROBE_CALIBRATE`](#️-step-12-adjust-the-z-offset-using-probe_calibrate)
    - [Step 12.1: Open the Fluidd Interface](#step-121-open-the-fluidd-interface)
    - [Step 12.2: Start the Probe Calibration](#step-122-start-the-probe-calibration)
    - [Step 12.3: Adjust the Z-Offset](#step-123-adjust-the-z-offset)
    - [Step 12.4: Save the Calibration](#step-124-save-the-calibration)
    - [Step 12.5: Test the New Z-Offset](#step-125-test-the-new-z-offset)
  - [🛠️ Step 13: Calibrating Extruder Rotation Distance](#️-step-13-calibrating-extruder-rotation-distance)
    - [Initial Setup](#initial-setup)
    - [Step-by-Step Calibration](#step-by-step-calibration)
    - [Important Note](#important-note)
  - [🛠️ Step 14: Configuring Slicer](#️-step-14-configuring-slicer)
  - [References 📚](#references-)

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

To configure Klipper with Fluidd, follow these steps:

1. Download the base configuration files:
   - [printer.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config/base/printer.cfg)
   - [bed_mesh.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config/base/bed_mesh.cfg)
   - [input_shaping.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config/base/input_shaping.cfg)
   - [macros.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config/base/macros.cfg)
   - [sensors.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config/base/sensors.cfg)
   - [steppers.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config/base/steppers.cfg)

2. Choose and download the configuration files for your specific components from the **components_config** folder:
   - [leds.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config/components_config/leds.cfg) (if using Neopixel LEDs)
   - [tft35-v3.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config/components_config/tft35-v3.cfg) (if using the BTT TFT35-V3.0 screen)
   - [tmc2208.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config/components_config/tmc2208.cfg) (if using TMC2208 drivers)
   - [tmc2209.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config/components_config/tmc2209.cfg) (if using TMC2209 drivers)

3. Upload the **printer.cfg** and all relevant included configuration files (including your chosen component files) to the following directory on your BTT CB1:
   ```bash
   /home/biqu/printer_data/config/
   ```

4. Make sure to adapt the `printer.cfg` file to your setup:
   - Adjust the `[mcu]` section with the correct serial ID of your MCU.
   - Include or comment out the relevant `include` statements based on your chosen hardware from the **components_config** directory.

   Example from `printer.cfg`:

   ```ini
   [include bed_mesh.cfg]
   [include input_shaping.cfg]
   [include macros.cfg]
   [include sensors.cfg]
   [include steppers.cfg]
   #[include leds.cfg]        # Uncomment if using Neopixel LEDs
   #[include tft35-v3.cfg]    # Uncomment if using BTT TFT35-V3.0 screen
   #[include tmc2208.cfg]     # Uncomment if using TMC2208 drivers
   [include tmc2209.cfg]      # Comment out if using TMC2208 drivers
   ```

5. To find your MCU serial ID, use this command via SSH:

   ```bash
   ls /dev/serial/by-id
   ```

6. Install KAMP in a `ssh` environment with the following command:
   ```bash
    cd
   
    git clone https://github.com/kyleisah/Klipper-Adaptive-Meshing-Purging.git
   
    ln -s ~/Klipper-Adaptive-Meshing-Purging/Configuration printer_data/config/KAMP

    cp ~/Klipper-Adaptive-Meshing-Purging/Configuration/KAMP_Settings.cfg ~/printer_data/config/KAMP_Settings.cfg
   ```
7. Open your `moonraker.conf` file and add this configuration:
   ```ini
   [update_manager Klipper-Adaptive-Meshing-Purging]
   type: git_repo
   channel: dev
   path: ~/Klipper-Adaptive-Meshing-Purging
   origin: https://github.com/kyleisah/Klipper-Adaptive-Meshing-Purging.git
   managed_services: klipper
   primary_branch: main
   ```

8. Open `KAMP_Settings.cfg` file delete and paste following content:
   ```ini
   [include ./KAMP/Adaptive_Meshing.cfg]       # Include to enable adaptive meshing configuration.
   #[include ./KAMP/Line_Purge.cfg]             # Include to enable adaptive line purging configuration.
   #[include ./KAMP/Voron_Purge.cfg]            # Include to enable adaptive Voron logo purging configuration.
   #[include ./KAMP/Smart_Park.cfg]             # Include to enable the Smart Park function, which parks the printhead near the print  area for final heating.

   [gcode_macro _KAMP_Settings]
   description: This macro contains all adjustable settings for KAMP 

   # The following variables are settings for KAMP as a whole.
   variable_verbose_enable: True               # Set to True to enable KAMP information output when running. This is useful for  debugging.

   # The following variables are for adjusting adaptive mesh settings for KAMP.
   variable_mesh_margin: 10                     # Expands the mesh size in millimeters if desired. Leave at 0 to disable.
   variable_fuzz_amount: 0                     # Slightly randomizes mesh points to spread out wear from nozzle-based probes. Leave at    0 to disable.

   # The following variables are for those with a dockable probe like Klicky, Euclid, etc.                 # ----------------  Attach  Macro | Detach Macro
   variable_probe_dock_enable: False           # Set to True to enable the usage of a dockable probe.      #   ---------------------------------------------
   variable_attach_macro: 'Attach_Probe'       # The macro that is used to attach the probe.               # Klicky Probe:    'Attach_Probe' | 'Dock_Probe'
   variable_detach_macro: 'Dock_Probe'         # The macro that is used to store the probe.                # Euclid Probe:    'Deploy_Probe' | 'Stow_Probe'
                                                                                                           # Legacy Gcode:    'M401'         | 'M402'

   # The following variables are for adjusting adaptive purge settings for KAMP.
   variable_purge_height: 0.8                  # Z position of nozzle during purge, default is 0.8.
   variable_tip_distance: 20                    # Distance between tip of filament and nozzle before purge. Should be similar to    PRINT_END final retract amount.
   variable_purge_margin: 60                   # Distance the purge will be in front of the print area, default is 10.
   variable_purge_amount: 30                   # Amount of filament to be purged prior to printing.
   variable_flow_rate: 12                      # Flow rate of purge in mm3/s. Default is 12.

   # The following variables are for adjusting the Smart Park feature for KAMP, which will park the printhead near the print area at a    specified height.
   variable_smart_park_height: 10              # Z position for Smart Park, default is 10.

   gcode: # Gcode section left intentionally blank. Do not disturb.

       {action_respond_info(" Running the KAMP_Settings macro does nothing, it is only used for storing KAMP settings. ")}

   ```

9. Once all files are uploaded and configured, restart Klipper and Fluidd from the web interface.


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
  - Round the new `rotation_distance` to three decimal places.

5. **Repeat if Necessary:**
   - If the `actual_extrusion_distance` differs from the `requested_extrusion_distance` by more than 2 mm, repeat the steps above to refine your calibration.

### Important Note

Avoid using the "measure and adjust" method for calibrating X, Y, or Z axes. This method isn’t precise enough for those axes and may lead to a suboptimal setup. For those, measure your belts, pulleys, and lead screws instead.

## 🛠️ Step 14: Configuring Slicer
1. Download and install the prusaslicer [I3-RS32 preset](https://www.makerfr.com/wp-content/uploads/2020/06/preset-I3RS32.zip).
2. Modify the printer personalized Startup G-code with this:
```gcode
; ================================================
;                  STARTING G-CODE
; ================================================
; Description: This section prepares the printer for
;              the start of the print. It handles
;              preheating, bed leveling, and extrusion
;              preparation.
; ================================================

; Start of Starting G-code
M104 S170                                                                           ; Set extruder temperature
M140 S[first_layer_bed_temperature]                                                 ; Set bed temperature
M190 S[first_layer_bed_temperature]                                                 ; Wait for bed to reach target temperature
M109 S170                                                                           ; Wait for extruder to reach target temperature

Z_TILT                                                                              ; Home all axes + Z_tilt
G92 E0                                                                              ; Reset extruder position

BED_MESH_CALIBRATE
;CUSTOM_BED_MESH_CALIBRATE X={first_layer_print_min[0]} Y={first_layer_print_min[1]} W={(first_layer_print_max[0]) - (first_layer_print_min[0])} H={(first_layer_print_max[1]) - (first_layer_print_min[1])}                                                         ; Calibrate the mesh using automatic method with adaptive mesh and 2mm margin

G1 X0 Y-3 F3000                                                                     ; Move the nozzle to a safe area near the bed for priming

M104 S[first_layer_temperature]                                                     ; Set extruder temperature to the first layer temperature
M109 S[first_layer_temperature]                                                     ; Wait for extruder to reach the first layer temperature

G1 E0 F2400                                                                         ; Undo the retraction
G1 E10 F2400                                                                        ; Purge a small amount of filament
G92 E0                                                                              ; Reset extruder position again

G1 X30 Y-3 Z0.2 F3000                                                               ; Move to start position for the purge line
G1 X110.0 E9.0 F1000.0                                                              ; Draw the first line of the purge
G1 X50.0 Y-2.0 E12.5 F1000.0                                                        ; Draw the second line of the purge

G92 E0                                                                              ; Reset extruder position again
G1 Z5 F5000                                                                         ; Lift nozzle after purge to avoid dragging
; Ready for printing
```
3. Modify the printer personalized End G-code with this:
```gcode
; ================================================
;                   END G-CODE
; ================================================
; Description: This section finalizes the print by
;              retracting the filament, turning off
;              heaters, and moving the print head and
;              bed to safe positions.
; ================================================

; Start of End G-code


G91                                      ; Relative positioning
G1 E-10 F2400                             ; Retract the filament by 2mm (slower for controlled retraction)
G1 Z1                                    ; Lift the nozzle 10mm to avoid collision with the print
G90                                      ; Absolute positioning
G1 X0 Y200 F3000                         ; Move the bed forward for easy part removal and home X axis
M104 S0                                  ; Turn off the extruder heater
M140 S0                                  ; Turn off the bed heater
M107                                     ; Turn off the fan
M84                                      ; Disable motors
```
---

🎉 Congratulations! You've successfully installed Klipper on your BTT CB1 with a BTT Manta M5P using KIAUH. Enjoy the enhanced performance and capabilities Klipper brings to your 3D printing experience!

## References 📚
1. [BigTreeTech Manta M5P Documentation](https://github.com/bigtreetech/Manta-M5P)
2. [Klipper3D Documentation](https://www.klipper3d.org)
3. RoMaker. "[I3RS32 settings](https://www.makerfr.com/imprimante-3d/i3-rs32/reglages-i3-rs32/)." *MakerFr*.