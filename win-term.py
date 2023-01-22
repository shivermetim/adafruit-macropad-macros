#  Under MIT License, Copyright © 2023 Timothy Gray

from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Win Term'
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x800000, 'FontV', [Keycode.LEFT_CONTROL, '-']), # reduce font size
        (0x0de05e, 'Focus^', [Keycode.LEFT_ALT, Keycode.UP_ARROW]), # move focus up
        (0x800000, 'Font^', [Keycode.LEFT_CONTROL, '+']), # increase font size
        # 2nd row ----------
        (0x0de05e, '<Focus', [Keycode.LEFT_ALT, Keycode.LEFT_ARROW]), # move focus to left 
        (0x0de05e, 'FocusV', [Keycode.LEFT_ALT, Keycode.DOWN_ARROW]), # move focus down
        (0x0de05e, 'Focus>', [Keycode.LEFT_ALT, Keycode.RIGHT_ARROW]), # move focus to right
        # 3rd row ----------
        (0x800000, 'Split-', [Keycode.LEFT_ALT, Keycode.LEFT_SHIFT, '-']), # split pane horizontally
        (0x770de0, 'Size^', [Keycode.LEFT_ALT, Keycode.LEFT_SHIFT, Keycode.UP_ARROW]), # resize pane up
        (0x800000, 'Split|', [Keycode.LEFT_ALT, Keycode.LEFT_SHIFT, '+']), # split pane vertically
        # 4th row ----------
        (0x770de0, '<Size', [Keycode.LEFT_ALT, Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW]), # resize pane left
        (0x770de0, 'SizeV', [Keycode.LEFT_ALT, Keycode.LEFT_SHIFT, Keycode.DOWN_ARROW]), # resize pane down
        (0x770de0, 'Size>', [Keycode.LEFT_ALT, Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW]), # resize pane to the right
        # Encoder button ---
        (0x000000, 'Close', [Keycode.WINDOWS, Keycode.GRAVE_ACCENT]), # drop down 'quake mode' terminal
    ]
}
