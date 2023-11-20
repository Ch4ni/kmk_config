# Ada's boot.py for CRKBD, Left Hand Side on KMK w/ BoardSource Blok
# Just getting started:
# If key(0,0) is pressed, use the default boot mode. Otherwise
# boot without serial console or storage device.

import board
import storage

from kmk.bootcfg import bootcfg

# Allow writing to storage from CircuitPython
storage.remount("/", readonly=False)

# Set the volume name for our CRKBD left side
m = storage.getmount("/")
m.label = "CRKBDL"

# remount readonly in CircuitPython so that the computer
# can write to the drive (if enabled)
storage.remount("/", readonly=True)

# set "normal" boot to disable SerialUSB and Block Storage
if not bootcfg(
    sense=board.GP29,
    source=board.GP04,
    storage=False,
    cdc=False,
    usb_id=("@foostan", "crkbd"),
):
    import supervisor

    supervisor.runtime.autoreload = False
    supervisor.set_usb_identification("@foostan", "crkbd-rw")

    print(
        " Ch4ni - keypress detected! using default boot mode (storage=enabled, cdc=enabled)\n"
    )
