# Linux Home  
#### [<--Back to Home](../Readme.md)

* [Linux Terminal Commands](commands.md)
* [Git Commands](git.md)
* [Windows Subsystem for Linux](wsl.md)





### My Personal Essential Commands :

- Delete Useless Packages

  ```
  sudo apt-get clean
  
  sudo apt-get autoremove
  ```

- Launch UnetBootin after Installation using command line  

  ```
  sudo QT_X11_NO_MITSHM=1 /usr/bin/unetbootin
  ```

- Install Power Management and Cooling Essentials [TLP]

  ```
  sudo add-apt-repository ppa:linrunner/tlp
  sudo apt-get update
  sudo apt-get install tlp tlp-rdw
  //thinkpad Machines :
  sudo apt-get install tp-smapi-dkms acpi-call-dkms
  ```

  