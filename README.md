# Ch4ni's kmk config

This repo contains the basic files required to replicate @Chani's keyboard
layout and boot configuration via the KMK firmware.

[!NOTE]
This is a Work In Progress and should be considered incomplete. Use at your own
risk. This code comes without express or implied warranty.

## Installation

Begin by ensuring a known location and setting a few environment variables

```shell
export __KMK_WORKSPACE=${HOME}/Code/local/kmk_workspace      # define where we want the code to live
[[ ! -d ${__KMK_WORKSPACE} ]] && mkdir -p ${__KMK_WORKSPACE} # ensure the location exists
cd ${__KMK_WORKSPACE}                                        # go to the location
```

### Check out the KMK repository

- Using [Github CLI](https://cli.github.com/)

```shell
gh repo clone KMKfw/kmk_firmware
```

- Using git

```shell
git clone https://github.com/KMKfw/kmk_firmware.git
```

### Check out this repository

```shell
export __KMK_USER_KEYMAPS=${__KMK_WORKSPACE}/kmk_firmware/user_keymaps
```

- Using [Github CLI](https://cli.github.com/)

```shell
gh repo clone Ch4ni/kmk_config ${__KMK_USER_KEYMAPS}/ch4ni
```

- Using git

```shell
git clone https://github.com/Ch4ni/kmk_config.git ${__KMK_USER_KEYMAPS}/ch4ni
```

### Ensure your board is up-to-date

[!Note]
This section is a Work in Progress. There are some intuitive leaps assumed
within the following text

If you're using a Boardsource Blok, then start by
[reading the official board-update documentation](https://peg.software/docs/board-update).
I prefer to use the
[latest stoble CircuitPython forBlok](https://circuitpython.org/board/boardsource_blok/)
when updating the board firmware.

Once the board has been updated, reboot the board and ensure it's mounted. Once
mounted, set an environment variable that points to your board's mount point:

```shell
export __KMK_TARGET_MOUNTPOINT=/path/to/your/mounted/microcontroller
```

### Install KMK to your board

```shell
cd ${__KMK_WORKSPACE}/kmk_firmware
make MOUNTPOINT=${__KMK_TARGET_MOUNTPOINT} USER_KEYMAP=user_keymaps/ch4ni/crkbd.py BOARD=boards/crkbd

# __blocksize is 2x the number of bytes in the boot.py ... just to write the whole file in one go
# this will prevent CircuitPython from reloading while the boot.py is being written before
# that option is turned off via boot.py code
__blockSize=$((2* $(du -b -s boot.py | sed 's/[ \tboot.py]\{1,\}//'))) \
dd if=user_keymaps/ch4ni/boot.py of=${__KMK_TARGET_MOUNTPOINT}/boot.py bs=${__blockSize}
```

### Install any supplemental libraries

[!Note]
This is incomplete

Install the `circup` [tool](https://github.com/adafruit/circup) to manage
libraries installed on the board.

### Reboot your board!

That's it. Reboot your board and enjoy the layouts/configs!
