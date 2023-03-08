# Info
*Note:* Updated to work with **Cura 5.0**

*Note:* Turns out **MKS TFT** uses the same format, so the plugin should work for the boards using MKS TFT as well

Cura plugin generating and embedding snapshot image of a model in a gcode.

This fork has been made generic, not specific to a single model, by making code more Pythonic and without any printer name reference. It works with MKS motherboards. I used it on a Two trees Bluer Plus.

Procedure is the same as orignial repository, as following

This plugin can be configured to work only with given printers, to avoid adding unnecessary snapshot images to the G-code for printers which do not support them.
 
![LCD with a snapshot image](images/lcd.jpg "LCD with a snapshot image")

# Installation
- Download files of this project
- Unzip them if you downloaded a zip archive
- Open Cura
- Choose `Help` -> `Show Configuration Folder`    
![Configuration Folder](images/cura_1.jpg "Configuration Folder")
- Enter `plugins` folder
- Place the plugin folder inside of the `plugins` folder  
![Plugin Folder](images/file_explorer_1.jpg "Plugin Folder")
- Open printer selection menu and choose `Manage Printers`  
![Manage printers](images/cura_2.jpg "Manage printers")
- Choose your Lotmaxx printer  and then `Machine Settings`  
![Machine Settings](images/cura_3.jpg "Machine Settings")
- At the top of `Start G-code` add `;simage` and/or `;gimage` depending on your needs. If you're unsure which one you need - add both.  
![G-code](images/cura_4.jpg "G-code")

# Use
- Configure your print
- Move the STL preview as you want. What you see on screen will be what you'll see on your printer. Plugin just make a screenshot
- Save your gcode.
- Optionally, you can check the gcode. It must start by a simage and gimage sections.

# THANKS TO

Thanks to initial developer: Daniel Kukiela
