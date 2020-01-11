# Appimage File Associator

[AppImage](https://github.com/AppImage) as we know, is a next gen Linux software packaging 📦 tool. It is distro independent 😃 which means it can run on most of the thousands of Linux 🐧 distributions available online. Besides you can run it with single click 🖱 that's intersting isn't it...? Gone are the days when PC 🖥 users hit out at Linux distros' UX saying it difficult to even install ⚙️ a simple application.

Embracing the change LibreOffice 💼 the best Office 365 alternative recently launced it own version of AppImage. This version is amazing light and fast. It integrates everything 🤩 a normal office user will expect. You can try it out from [here](https://www.libreoffice.org/download/appimage/).

---

### About this repo...
Ususally an AppImage does not come included with file type association. In simple terms you may not be able to open a file direclty from a folder. For example if you have _only_ LibreOffice AppImage in your system a `.docx` or `.odp` file cannot be opened from a directory.

Now to overcome this I've written a simple python script which will make life easier if you just run. It will automatically associate file types with the respective AppImage. Currently this supports LibreOffice and I will add more as and when time permits.

 - If you find this cool 😎 and can't wait you can open up pull requests [here](https://github.com/joe247/appimage_file_associator/pulls).
  - If you find any imporvements / issues bugguing 🐞 you ping me [here](https://github.com/joe247/appimage_file_associator/issues).
  
  ### How to... (in 3 SiMpLe Steps )
  1. Just download the zip file and extract it.
  2. Open the terminal in the extracted folder namely `LibreOffice`
  3. Run the command `python3 app_asc.py`
  
  Bingo! 🎉 you've just made you're life a lot easier. Now a click on any office files will allow you to open with LibreOffice AppImage!
