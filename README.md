# 🚀 Upgrading the MakerFr I3-RS32: From SKR v1.4 to BTT Manta M5P + Klipper 🚀

![Marlin_To_Klipper](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Pictures/Readme/Marlin_To_Klipper.png)

## 🌟 A Personal Note 🌟

Hey there, fellow 3D printing enthusiasts! 👋

After years of tinkering and printing with my trusty MakerFr I3-RS32 (an incredible Prusa like designed by RoMaker - [I3-RS32](https://www.makerfr.com/en/imprimante-3d/i3-rs32/presentation-de-la-i3rs32/)). I started to feel it was time for an upgrade. I’ve always loved tweaking my 3D printer, pushing its limits, and learning everything I can about the tech behind it. But lately, the SKR v1.4, while solid, just wasn’t cutting it anymore, and managing an external Raspberry Pi was getting... well, a bit cumbersome.

So, I decided it was time to dive into something new and exciting. I wanted a cleaner, more integrated setup, better performance, and—of course—a chance to dive deeper into the software side of things. That’s how this project was born: migrating from the SKR v1.4 to the **BTT Manta M5P** and switching from Marlin to **Klipper**. This isn’t just an upgrade; it’s a personal challenge to expand my skills and knowledge—and I’m excited to share this journey with you! 🎉

~ MushuDG

## Why Make the Switch? 🤔

1. **No More External Raspberry Pi! 🥳**

   - With the BTT Manta M5P, you get the power of a Raspberry Pi *built right in*. No more external boards cluttering up your setup—everything is clean and streamlined.
2. **Supercharge Your Firmware with Klipper 🚀**

   - Klipper isn’t just firmware—it’s a game-changer! Enjoy faster print speeds, higher precision, and advanced features that Marlin just can’t match. Discover what 3D printing can really do with Klipper’s real-time processing power.
3. **Simplified Setup & Greater Control 🎛️**

   - By upgrading to the Manta M5P, you’re moving to a modern, versatile board that simplifies your setup. And with Klipper, you’ll have unmatched control over your machine’s performance with a more intuitive configuration process.
4. **Future-Proof Your Printer 🔮**

   - The BTT Manta M5P is designed to support the latest innovations in 3D printing. This upgrade ensures that your MakerFr I3-RS32 stays ahead of the curve for years to come.
5. **A Learning Journey 🧠**

   - If you’re like me, you love to tinker and learn. This migration isn’t just about better prints—it’s about deepening your understanding of the software that drives your machine. Embrace the challenge and grow your skills!

## Parts and 3D Printed Parts 🛒

### Parts to Purchase

| Item                                             | Price (USD) | Link                                                                                                                   |
|--------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------|
| **BIGTREETECH Manta M5P**                        | ~$53.00     | [BIGTREETECH Manta M5P](https://biqu.equipment/products/manta-m4p-m8p?variant=40215552852066)                          |
| **BIGTREETECH CB1**                              | ~$30.00     | [BIGTREETECH CB1](https://biqu.equipment/products/manta-m4p-m8p?variant=39847241384034)                                |
| **BIGTREETECH CB1 Heatsink**                     | ~$5.50      | [BIGTREETECH CB1 Heatsink](https://biqu.equipment/products/manta-m4p-m8p?variant=39847241416802)                       |
| **Optional:**                                    |             |                                                                                                                        |
| **BIGTREETECH TFT35 SPI V2.1 Touch Screen**      | ~$24.00     | [BIGTREETECH TFT35 SPI V2.1 Touch Screen](https://biqu.equipment/collections/lcd-screen/products/bigtreetech-tft35-spi-v2-1-touchscreen-io2can-module) |
| **Stylus for Touch Screen**                      | ~$1.10      | [Aliexpress Stylus](https://fr.aliexpress.com/item/1005006539716369.html?gatewayAdapt=glo2fra)                                                            |
| **Neopixel LEDs (1m 74 IP30 or 1m 144 IP30)**                   | ~$5.00| [Aliexpress Neopixel LEDs](https://fr.aliexpress.com/item/1005006224130239.html?gatewayAdapt=glo2fra)                                                     |


### 3D Printed Parts

| Item                      | Link                                                                                              |
|---------------------------|---------------------------------------------------------------------------------------------------|
| **Manta_M5P_Box.stl**      | [Manta_M5P_Box.stl](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/STL)                   |
| **Manta_M5P_Cover.stl**    | [Manta_M5P_Cover.stl](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/STL)                 |
| **Optional:**             |                                                                                                   |
| **TFT35-SPI.stl**          | [TFT35-SPI.stl](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/STL)                       |
| **TFTholder.stl**          | [TFTholder.stl](https://github.com/MushuDG/MakerFr_I3-RS32-K/tree/main/STL)                       |


## Ready to Dive In? 💻

In this documentation, I’ll guide you through the entire process—from hardware setup to firmware configuration. Whether you’re a seasoned maker or just curious, this guide has something for everyone. So, let’s get started and transform your 3D printing experience! 🔧✨

**Go to [Wiring](https://github.com/MushuDG/MakerFr_I3-RS32-K/blob/main/Documentation/1_Wiring.md)**

---

**References:**

1. RoMaker. "[I3RS32 presentation](https://www.makerfr.com/en/imprimante-3d/i3-rs32/presentation-de-la-i3rs32/)." *MakerFr*.
