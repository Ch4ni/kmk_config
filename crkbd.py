
from kb import KMKKeyboard
from kmk.hid import HIDModes
from kmk.keys import KC

from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.modules.holdtap import HoldTap, HoldTapRepeat


# TODO-Ch4ni: replace this with *something else*
# since we're not using Peg, we can get a little more creative with the OLED
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
oled_data = OledData(
    corner_one={0:OledReactionType.STATIC,1:["  1 2 3 4","","","","","","",""]},
    corner_two={0:OledReactionType.STATIC,1:["  5 6 7 8","","","","","","",""]},
    corner_three={0:OledReactionType.LAYER,1:["  ^","    ^","      ^","        ^","","","","   LAYER"]},
    corner_four={0:OledReactionType.LAYER,1:["","","","","  ^","    ^","      ^","  SELECT"]})

# TODO-Ch4ni: replace this with "something else"
# since we're not using Peg, we're not bound to Peg's RGB/UI limitations.
#from kmk.extensions.peg_rgb_matrix import Rgb_matrix

keyboard = KMKKeyboard()
keyboard.tap_time = 50         # determined by experimentation
keyboard.debug_enabled = False

keyboard.modules = [
        Split(split_type=SplitType.UART, use_pio=True, uart_interval=20),
        Layers(),
        HoldTap(),
        Oled(oled_data, toDisplay=OledDisplayMode.TXT, flip=False)
    ]

def customHT(*args, **kwargs):
    defaultRepeat = HoldTapRepeat.TAP
    # mod HoldTap -> custom defalts for simplicity:
    # https://kmkfw.io/docs/holdtap/#custom-holdtap-behavior
    # prefer_hold = False       # setting to false means that when typing quickly, the next keypress is interpreted as a tap.
    #                           # When intending a hold, this is less likely to happen quickly enough to be interpreted as a tap.
    #                           # Fewer false positives than when set to true
    # tap_interrupted = False   # interrupt the "hold" after another key is released. For things like Emacs this may provide
    #                           # problems, but I'm an nvim user, so it's all good
    #                           # REMOVED - turns out that when both sides are in sync, this actually does cause issues
    # repeat = defaultRepeat    # use the value of the defaultRepeat variable for repeat behavior. This is determined by
    #                           # experimentation to see what works best for the way I type.
    return KC.HT(*args, prefer_hold=False, repeat=defaultRepeat, **kwargs)

# TODO-Ch4ni: this is the static LEDmap that I used in Peg. It kinda ... sucks.
#               Would _love_ to do something a little more dynamic here.
# ledmap
# rgb_ext = Rgb_matrix(ledDisplay=[
#         [ 93,145,242], [ 93,145,242], [255, 73,176], [255, 73,176], [250,245,245], [250,245,245],
#         [250,245,245], [250,245,245], [255, 73,176], [255, 73,176], [ 93,145,242], [ 93,145,242],
#         [ 93,145,242], [ 93,145,242], [255, 73,176], [255, 73,176], [250,245,245], [250,245,245],
#         [250,245,245], [250,245,245], [255, 73,176], [255, 73,176], [ 93,145,242], [ 93,145,242],
#         [ 93,145,242], [ 93,145,242], [255, 73,176], [255, 73,176], [250,245,245], [250,245,245],
#         [250,245,245], [250,245,245], [255, 73,176], [255, 73,176], [ 93,145,242], [ 93,145,242],
#         [ 93,145,242], [255, 73,176], [250,245,245], [250,245,245], [255, 73,176], [ 93,145,242],
#         [255, 73,176], [255, 73,176], [255, 73,176], [255, 73,176], [255, 73,176], [255, 73,176],
#         [255, 73,176], [255, 73,176], [255, 73,176], [255, 73,176], [255, 73,176], [255, 73,176]
#     ],split=True,rightSide=False,disable_auto_write=True)


# KeyCode aliases, functions, etc.
_______ = KC.TRNS
XXXXXXX = KC.NO

LT1 = KC.MO(1)
LT2 = KC.MO(2)
LT_ESC = customHT(KC.GESC, LT2)

HRM_A = customHT(KC.A, KC.LCTRL)
HRM_S = customHT(KC.S, KC.LCTRL)
HRM_U = customHT(KC.U, KC.LALT)
HRM_H = customHT(KC.H, KC.LALT)


keyboard.keymap = [
    # DVORAK
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Tab  |   '  |   ,  |   .  |   P  |   Y  |                    |   F  |   G  |   C  |   R  |   L  |   /  |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LGUI |HRM_A |   O  |   E  |HRM_U |   I  |                    |   D  |HRM_H |   T  |   N  |HRM_S |   -  |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | Shft |   ;  |   Q  |   J  |   K  |   X  |-------.    ,-------|   B  |   M  |   W  |   V  |   Z  | Shft |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          | ENT  | SPC  | / BKSP  /       \LT_ESC\  |  LT1 |      |
    #                          |      |      |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    #
    [
        # DVORAK
        KC.TAB,   KC.QUOT, KC.COMM, KC.DOT,  KC.P,    KC.Y,                      KC.F,    KC.G,    KC.C,    KC.R,    KC.L,    KC.SLSH, \
        KC.LGUI,  HRM_A,   KC.O,    KC.E,    HRM_U,   KC.I,                      KC.D,    HRM_H,   KC.T,    KC.N,    HRM_S,   KC.MINUS, \
        KC.LSFT,  KC.SCLN, KC.Q,    KC.J,    KC.K,    KC.X,                      KC.B,    KC.M,    KC.W,    KC.V,    KC.Z,    KC.RSHIFT, \
                                        KC.ENT,  KC.SPACE, KC.BSPC,   LT_ESC,  LT1,  KC.NO,
    ],
    #
    # 
    # Numbers
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # |   `  |  1   |   2  |   3  |   4  |  5   |                    |   6  |   7  |   8  |   9  |   0  |  =   |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # |      |  [   | LEFT |  UP  | RIGHT|      |                    |      | PGUP |      |      |   ]  |  \   |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # |      |      | LEFT | DOWN | RIGHT|      |-------.    ,-------|      | PGDN |      |      |      |      |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |      |      | /       /       \      \  |      |      |
    #                          |      |      |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    #
    [
        # Numbers
        KC.GRAVE,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                   KC.N6,     KC.N7,   KC.N8,   KC.N9,   KC.N0, KC.EQUAL,  \
        _______, KC.LBRC, KC.LEFT,   KC.UP, KC.RGHT, _______,                   _______, KC.PGUP, _______, _______, KC.RBRC, KC.BSLS, \
        _______, _______, KC.LEFT, KC.DOWN, KC.RGHT, _______,                   _______, KC.PGDN, _______, _______, _______, _______, \
                                            _______, _______, _______, _______, _______, _______,
    ]
] 


# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)
