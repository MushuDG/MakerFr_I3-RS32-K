
# 💾 CB1 OS Installation Guide

When using CB1, you can only download and install the OS image provided by BIGTREETECH. Please visit the following link to download the latest minimal version of Debian for CB1: [Download OS Image](https://github.com/bigtreetech/CB1/releases).

## Write OS 📝

Follow these steps to write the OS image to a MicroSD card:

1. Insert a MicroSD card into your computer via a card reader.
2. Choose OS.

   ![1_Raspberry_Pi_Imager.png](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/2_CB1_OS_Installation/1_Raspberry_Pi_Imager.png)
3. Select "Use custom", then select the image that you downloaded.

   ![2_Use_Custom_Image.png](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/2_CB1_OS_Installation/2_Use_Custom_Image.png)
4. Select the MicroSD card and click "WRITE". ⚠️ **Warning:** Writing the image will format the MicroSD card. Be careful not to select the wrong storage device, as this will result in data loss.

   ![3_Write_Image.png](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/2_CB1_OS_Installation/3_Write_Image.png)

## WiFi Setting 📶

Note: This step can be skipped if you are using a network cable connection.

CB1 cannot directly use the Raspberry Pi Imager to set the WiFi name and password like CM4. After the OS image writing is completed, the MicroSD card will have a FAT32 partition recognized by the computer. Locate the "system.cfg" file. Open it with your preferred text editor and set your WiFi credentials.

![4_WiFi_Settings.png](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/2_CB1_OS_Installation/4_WiFi_Settings.png)

## Final Steps ✅

Insert the MicroSD card into the SoC SD port of the Manta M5P. Power on the main supply and wait for one to two minutes, then try to connect via SSH.

### Default SSH Credentials

- **Login as:** `biqu`
- **Password:** `biqu`

## Additional Settings 🔐

### Change Default Password

It's highly recommended to change the default password. Use the following command to do so:

```bash
biqu@BTT-CB1:~$ passwd
```

### Install ZSH for a Better Shell Experience 🐚

You can enhance your shell interface by installing ZSH using my [Bash-To-ZSH-Initialization](https://github.com/MushuDG/Bash-To-ZSH-Initialization) script. Run the following commands:

```bash
git clone https://github.com/MushuDG/Bash-To-ZSH-Initialization.git
chmod -R 740 ./Bash-To-ZSH-Initialization/
cd ./Bash-To-ZSH-Initialization
./install.sh
```

To proceed with the Klipper installation, please follow the instructions in the [Klipper Installation Guide](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Documentation/3_Klipper_Installation_Guide.md).

## References 📚

1. [BigTreeTech Manta M5P Documentation](https://github.com/bigtreetech/Manta-M5P)
