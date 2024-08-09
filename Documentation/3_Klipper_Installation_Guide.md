
# 🚀 Klipper Installation Guide via OctoPrint using KIAUH

Welcome! This guide will walk you through installing Klipper on your BTT CB1 with a BTT Manta M5P using KIAUH (Klipper Installation And Update Helper). Let's get started!

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

1. **Select `Install Klipper` from the menu**.
2. Follow the on-screen prompts to install Klipper on your BTT CB1.
3. Choose the appropriate firmware options for your BTT Manta M5P during the installation process.

## 🌕 Step 6: Install Moonraker

1. **From the KIAUH menu, choose `Install Moonraker`**.
2. Follow the instructions to set up Moonraker, the API that allows Klipper to communicate with OctoPrint.

## 🎛️ Step 7: Install OctoPrint

1. **Go back to the KIAUH menu and select `Install OctoPrint`**.
2. Follow the steps to install and integrate OctoPrint with Klipper.

## 🔧 Step 8: Configure Klipper

1. **Flash the compiled firmware onto your BTT Manta M5P** using the SD card.
2. **Update the `printer.cfg` file** with settings specific to your 3D printer. You can start with a template or customize it as needed.

## 🌐 Step 9: Access OctoPrint

After everything is set up, you can access OctoPrint from your web browser:

```http
http://<IP_of_your_BTT_CB1>:5000
```

Replace `<IP_of_your_BTT_CB1>` with the actual IP address of your BTT CB1.

## ⚙️ Step 10: Configure OctoPrint for Klipper

1. In OctoPrint, navigate to **Settings**.
2. Under **"Serial Connection"**, configure the serial connection to communicate with Klipper.
3. In **"Plugin Manager"**, ensure all necessary plugins are installed, including those required for Klipper.

## 🔄 Step 11: Reboot and Test

Finally, reboot your BTT CB1 to ensure everything is set up correctly. After rebooting, test your setup by sending a command to your 3D printer via OctoPrint.

---

🎉 Congratulations! You've successfully installed Klipper on your BTT CB1 with a BTT Manta M5P using KIAUH. Enjoy the enhanced performance and capabilities Klipper brings to your 3D printing experience!
