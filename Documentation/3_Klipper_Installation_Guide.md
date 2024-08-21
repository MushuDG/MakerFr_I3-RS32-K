
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

5. Copy the [printer.cfg](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/Klipper_Config) (select and adapt it to your requirements) content into the `/home/biqu/printer_data/config/printer.cfg` file.

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

Setting the correct Z-offset is crucial for achieving a perfect first layer. Here’s how to do it using the `PROBE_CALIBRATE` command directly from the OctoPrint terminal.

### Step 12.1: Open the OctoPrint Terminal

1. Access your OctoPrint interface via your web browser.
2. Navigate to the **Terminal** tab.

### Step 12.2: Start the Probe Calibration

In the terminal, initiate the probe calibration process by entering:

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
   - In your printer’s terminal, run the following commands to extrude 50 mm of filament:
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
G28                                                                                 ; Home all axes
G92 E0                                                                              ; Reset extruder position
;G1 E-2 F2400                                                                        ; Retract filament to avoid oozing during heating

G1 X0 Y0 Z10 F3000                                                                  ; Move the nozzle to the corner of the bed
M104 S170                                                                           ; Set extruder temperature
M140 S[first_layer_bed_temperature]                                                 ; Set bed temperature
M190 S[first_layer_bed_temperature]                                                 ; Wait for bed to reach target temperature
M109 S170                                                                           ; Wait for extruder to reach target temperature

CUSTOM_BED_MESH_CALIBRATE X={first_layer_print_min[0]} Y={first_layer_print_min[1]} W={(first_layer_print_max[0]) - (first_layer_print_min[0])} H={(first_layer_print_max[1]) - (first_layer_print_min[1])}                                                         ; Calibrate the mesh using automatic method with adaptive mesh and 2mm margin

G1 X10 Y-3 F3000                                                                    ; Move the nozzle to a safe area near the bed for priming

M104 S[first_layer_temperature]                                                     ; Set extruder temperature to the first layer temperature
M109 S[first_layer_temperature]                                                     ; Wait for extruder to reach the first layer temperature

G1 E0 F2400                                                                         ; Undo the retraction
G1 E4 F2400                                                                         ; Purge a small amount of filament
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
G1 E-5 F2400                             ; Retract the filament by 2mm (slower for controlled retraction)
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