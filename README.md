Terminator OtpAuth Plugin
----------------------
Terminator plugin to generate a QR Code corresponding to an `otpauth://` URI that you can scan with your phone.
The QR Code is generated via the Google Chart API.

### Installing the Plugin ###
* Create the plugins folder if it doesn't exist. On linux: `mkdir -p ~/.config/terminator/plugins`
* Copy the plugin file to the plugins folder.
* In Terminator go to Preferences >> Plugins and enable EditorPlugin.
* Restart Terminator.


### Using the Plugin ###
- When your shell is showing an `otpauth://` URI
  or
  If you can copy an `otpauth://` URI and paste it in the terminal
- Use &lt;ctrl&gt;+click to display the corresponding QR Code.
- Right click to copy the link.
