# 🛠️ OctoPrint Setup Guide

This guide will walk you through the process of setting up OctoPrint on your system, including installing dependencies, creating a virtual environment, and configuring OctoPrint to start automatically on boot.

## 📋 Prerequisites

Before you begin, ensure your system is up to date:

```bash
sudo apt-get update
sudo apt-get upgrade
```

### 🔧 Install Required Dependencies

OctoPrint requires Python 3 and several additional packages. Install them with the following command:

```bash
sudo apt-get install python3 python3-pip python3-dev python3-setuptools python3-venv git libyaml-dev build-essential
```

## 🛠️ Installing OctoPrint

### 📁 Create a Virtual Environment

It is recommended to run OctoPrint within a virtual environment to isolate its dependencies. Follow these steps:

1. Create a directory for OctoPrint:

   ```bash
   mkdir ~/OctoPrint
   cd ~/OctoPrint
   ```
2. Set up the virtual environment:

   ```bash
   python3 -m venv venv
   ```

### 🔌 Activate the Virtual Environment

Activate the virtual environment with the following command:

```bash
source venv/bin/activate
```

### 📦 Install OctoPrint

With the virtual environment activated, install OctoPrint using pip:

```bash
pip install pip --upgrade
pip install octoprint
```

### 🚀 Start OctoPrint

Once the installation is complete, you can start OctoPrint using the following command (ensure the virtual environment is still activated):

```bash
octoprint serve
```

OctoPrint should now be accessible from your web browser at: `http://<YOUR_PI_IP>:5000`.

## 🔄 Configure OctoPrint to Start Automatically

To have OctoPrint start automatically when your Raspberry Pi boots up, create a systemd service.

### 📝 Create a systemd Service File

1. Open the systemd service file for editing:

   ```bash
   sudo nano /etc/systemd/system/octoprint.service
   ```
2. Add the following configuration, replacing `<username>` with your actual username:

   ```ini
   [Unit]
   Description=OctoPrint
   After=network.target

   [Service]
   User=<username>
   ExecStart=/home/<username>/OctoPrint/venv/bin/octoprint serve
   Restart=on-failure
   TimeoutStopSec=300

   [Install]
   WantedBy=multi-user.target
   ```

### ⚙️ Enable the Service

Reload systemd, enable the OctoPrint service, and start it:

```bash
sudo systemctl daemon-reload
sudo systemctl enable octoprint.service
sudo systemctl start octoprint.service
```

### 🔍 Verify the Service

Check that the service is running correctly:

```bash
sudo systemctl status octoprint.service
```

If everything is configured correctly, OctoPrint should now be set to start automatically when your Raspberry Pi boots up.

---

🎉 You're all set! Enjoy using OctoPrint with your 3D printer.
