# ThinkPad Setup
#### Delete Useless Packages

```
sudo apt-get clean

sudo apt-get autoremove
```

#### Launch UnetBootin after Installation using command line  

```
sudo QT_X11_NO_MITSHM=1 /usr/bin/unetbootin
```

#### Install Power Management and Cooling Essentials [TLP]

```
sudo add-apt-repository ppa:linrunner/tlp
sudo apt-get update
sudo apt-get install tlp tlp-rdw
//thinkpad Machines :
sudo apt-get install tp-smapi-dkms acpi-call-dkms
```

#### Enable Battery percentage in top bar without installing Tweaks

```shell
gsettings set org.gnome.desktop.interface show-battery-percentage true
```



#### Install LXDE GUI on top of ubuntu  

``` sudo apt-get install lxde ```

#### Update the Conda Environment

``` 
condat update --all
```

#### Install MPV player 

```shell
sudo apt install mpv
```

#### Install Conda

```shell
# Download the Package
bash Anaconda3-2019.03-Linux-x86_64.sh

```

#### Image Viewer for handling big file size

```bash
sudo apt install eom
```

PDF viewer for heavy PDF

```shell
sudo apt-get update

sudo apt-get install mupdf mupdf-tools
```

Terminal Update 

```
link-https://itnext.io/terminal-101-the-setup-guide-that-will-boost-your-workflow-12df2570052

nano ~/.zshrc
change theme o "xiong-chiamiov"
```

