#!/usr/bin/env python

COPYRIGHT = '''
Copyright 2018 Mark R. Rubin
This is free software with ABSOLUTELY NO WARRANTY.
'''

NO_WARRANTY = '''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/gpl.html>
'''

WARNING = '''
This is experimental software. Using it will void any and all warranties
from Electronic Technologyu Co., Ltd. or any other entity. This software may
permanently damage your keyboard. By typing "accept" you assume all risk and
agree to hold harmless it's author, the copyright holder, and any and all
other entities.

Type "accept" to continue, or anything else to exit.
'''



import argparse
import operator
import sys
import types


VERSION = (0, 1, 0)


KEYCODES = {
    'esc'           : (0x00, 0x00),
    'f1'            : (0x03, 0x00),
    'f2'            : (0x06, 0x00),
    'f3'            : (0x09, 0x00),
    'f4'            : (0x0C, 0x00),
    'f5'            : (0x0F, 0x00),
    'f6'            : (0x12, 0x00),
    'f7'            : (0x15, 0x00),
    'f8'            : (0x18, 0x00),
    'f9'            : (0x1B, 0x00),
    'f10'           : (0x1E, 0x00),
    'f11'           : (0x21, 0x00),
    'f12'           : (0x24, 0x00),
  # 'fn'            : (0x2A, 0x00),     # known not to work: 27 2A 9B A2 A5
    'del'           : (0xA8, 0x00),
    '`'             : (0x3F, 0x00),
    '~'             : (0x3F, 0x00),
    'backtick'      : (0x3F, 0x00),
    'tilde'         : (0x3F, 0x00),
    '1'             : (0x42, 0x00),
    '2'             : (0x45, 0x00),
    '3'             : (0x48, 0x00),
    '4'             : (0x4B, 0x00),
    '5'             : (0x4E, 0x00),
    '6'             : (0x51, 0x00),
    '7'             : (0x54, 0x00),
    '8'             : (0x57, 0x00),
    '9'             : (0x5A, 0x00),
    '0'             : (0x5D, 0x00),
    '-'             : (0x60, 0x00),
    'hyphen'        : (0x60, 0x00),
    '='             : (0x63, 0x00),
    'equal'         : (0x63, 0x00),
    'backspace'     : (0x66, 0x00),
    'bckspc'        : (0x66, 0x00),
    'home'          : (0x6C, 0x00),
    'tab'           : (0x7E, 0x00),
    'q'             : (0x81, 0x00),
    'w'             : (0x84, 0x00),
    'e'             : (0x87, 0x00),
    'r'             : (0x8A, 0x00),
    't'             : (0x8D, 0x00),
    'y'             : (0x90, 0x00),
    'u'             : (0x93, 0x00),
    'i'             : (0x96, 0x00),
    'o'             : (0x99, 0x00),
    'p'             : (0x9C, 0x00),
    '['             : (0x9F, 0x00),
    'open_bracket'  : (0x9F, 0x00),
    ']'             : (0xA2, 0x00),
    'close_bracket' : (0xA2, 0x00),
    '|'             : (0xA5, 0x00),
    '\\'            : (0xA5, 0x00),
    'backslash'     : (0xA5, 0x00),
    'page_up'       : (0x6F, 0x00),
    'pgup'          : (0x6F, 0x00),
    'cpslck'        : (0xBD, 0x00),
    'capslock'      : (0xBD, 0x00),
    'a'             : (0xC0, 0x00),
    's'             : (0xC3, 0x00),
    'd'             : (0xC6, 0x00),
    'f'             : (0xC9, 0x00),
    'g'             : (0xCC, 0x00),
    'h'             : (0xCF, 0x00),
    'j'             : (0xD2, 0x00),
    'k'             : (0xD5, 0x00),
    'l'             : (0xD8, 0x00),
    ';'             : (0xDB, 0x00),
    'semicolon'     : (0xDB, 0x00),
    ':'             : (0xDB, 0x00),
    'colon'         : (0xDB, 0x00),
    "'"             : (0xDE, 0x00),
    'apostrophe'    : (0xDE, 0x00),
    '"'             : (0xDE, 0x00),
    'quote'         : (0xDE, 0x00),
    'enter'         : (0xE4, 0x00),
    'return'        : (0xE4, 0x00),
    'pgdwn'         : (0xAE, 0x00),
    'page_down'     : (0xAE, 0x00),
    'shftl'         : (0xFC, 0x00),
    'left_shift'    : (0xFC, 0x00),
    'z'             : (0x02, 0x01),
    'x'             : (0x05, 0x01),
    'c'             : (0x08, 0x01),
    'v'             : (0x0B, 0x01),
    'b'             : (0x0E, 0x01),
    'n'             : (0x11, 0x01),
    'm'             : (0x14, 0x01),
    ','             : (0x17, 0x01),
    'comma'         : (0x17, 0x01),
    '.'             : (0x1A, 0x01),
    'period'        : (0x1A, 0x01),
    '/'             : (0x1D, 0x01),
    'slash'         : (0x1D, 0x01),
    'shftr'         : (0x23, 0x01),
    'right_shift'   : (0x23, 0x01),
    'up'            : (0x29, 0x01),
    'end'           : (0xAB, 0x00),     # guess, all 2b,2f,32,35,38 wrong
    'ctrll'         : (0x3B, 0x01),
    'left_ctrl'     : (0x3B, 0x01),
    'wndws'         : (0x3E, 0x01),
    'windows'       : (0x3E, 0x01),
    'altl'          : (0x41, 0x01),
    'left_alt'      : (0x41, 0x01),
    ' '             : (0x44, 0x01),
    'spc'           : (0x44, 0x01),
    'space'         : (0x44, 0x01),
    'altr'          : (0x47, 0x01),
    'right_alt'     : (0x47, 0x01),
    'ctrlr'         : (0x53, 0x01),
    'right_ctrl'    : (0x53, 0x01),
    'left'          : (0x65, 0x01),
    'down'          : (0x68, 0x01),
    'right'         : (0x6B, 0x01),
}




PACKET_SIZE = 64

START_PKT =        (0x04, 0x01, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)

FINISH_PKT =       (0x04, 0x02, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)

mode_pkt =         [0x04, 0x0d, 0x00, 0x06, 0x01, 0x00, 0x00, 0x00,
                    0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

level_pkt =        [0x04, 0x00, 0x00, 0x06, 0x01, 0x01, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

SOLID_PREFIX_PKT = (0x04, 0x0b, 0x00, 0x06, 0x01, 0x04, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)

solid_color_pkt =  [0x04, 0x00, 0x00, 0x06, 0x03, 0x05, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

key_pkt =          [0x04, 0x00, 0x00, 0x11, 0x03, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

LEDS_PREFIX_PKT =  (0x04, 0x11, 0x00, 0x06, 0x03, 0x08, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)

leds_pkts =        [    [0x04, 0x00, 0x00, 0x11, 0x36] + 59 * [0]
                    for ndx in range(7)                          ]



CHECKSUM_NDX     = 1
FIRST_DATA_NDX   = 3

MAX_LEVEL        = 5
LEVEL_NDX        = 8

SOLID_MODE       = 0x06
CUSTOM_MODE      = 0x14
MAX_MODE         = CUSTOM_MODE
MODE_NAMES       = {'solid' : SOLID_MODE ,
                   'custom' : CUSTOM_MODE }
MODE_NDX         = 8

SOLID_LED_NDX    = 8

KEY_CODE_NDX     = 5
KEY_RGB_NDX      = 8

LEDS_PER_PACKET  = 0x36
LEDS_PER_PKT_NDX = 5
FIRST_LED_NDX    = 8






def lo_hi_16(lo_hi):
    return (lo_hi[1] << 8) | lo_hi[0]

def to_byte(s):
    base = 16 if s.lower().startswith('0x') else 10
    return int(s, base)

def rgb_strings_to_bytes(raw):
    bytes = [to_byte(e) for e in raw]
    assert max(bytes) <= 0xff and min(bytes) >= 0, "Bad rgb value in %s" % raw
    return bytes

def set_16_bit(packet, index, short):
    packet[index    ] =  short & 0x00ff
    packet[index + 1] = (short & 0xff00) >> 8

def set_lo_hi(packet, index, lo_hi):
    packet[index:index+2] = lo_hi

def check_rgb(rgb):
    for val in rgb:
        assert val >= 0 and val <= 255, "Bad rgb value in %s" % rgb

def set_rgb(packet, index, rgb):
    packet[index:index+3] = rgb



def init_leds_pkts():
    for (ndx, pkt) in enumerate(leds_pkts):
        set_16_bit(pkt, LEDS_PER_PKT_NDX, ndx * LEDS_PER_PACKET)



def print_packet(caption, packet):
    sys.stdout.write("%s:\n" % caption)
    for (ndx, byte) in enumerate(packet):
        sys.stdout.write("%02x" % byte)
        sys.stdout.write(" " if (ndx + 1) % 16 else "\n")



def write_read(device, packet, verbose):
    if issubclass(type(packet), types.ListType):
        checksum  = reduce(operator.add, packet[FIRST_DATA_NDX:])
        set_16_bit(packet, CHECKSUM_NDX, checksum)

    if verbose: print_packet("send", packet)

    device.write(bytearray(packet))

    response = device.read(PACKET_SIZE)

    if verbose:
        print_packet("recv", [ord(byte) for byte in response])



def do_mode_packet(device, mode, verbose):
    if mode:
        mode_pkt[MODE_NDX] = mode
        write_read(device, mode_pkt, verbose)



def check_version(fields):
    (major, minor, micro) = [int(field) for field in fields[1:4]]
    if major != VERSION[0] or minor > VERSION[1]:
        raise ValueError,   "version mismatch, file: %s  code: %s" \
                          % ((major, minor, micro), VERSION)


def rgb(hexs, filename, linenum):
    try:
        assert len(hexs) == 3
        rgb = tuple([int(hex, 16) for hex in hexs])
    except:
        raise ValueError,   "bad RGB hex triplet %s, line %d of file %s ("    \
                            "must be 3 hexidecimal numbers in range 00..ff)"  \
                          % (hexs, linenum, filename)
    return rgb



def parse_file(file):
    colors  = {}
    leds    = []
    sets    = set()
    default = None
    linenum = 0

    for line in file:
        linenum += 1
        fields   = line.split()

        if len(fields) < 2: continue

        if fields[0] in KEYCODES:
            if fields[1].startswith('/'):
                try:
                    led = colors[fields[1]]
                except:
                    raise ValueError, \
                            "Unknown color %s, line %d of file %s" \
                          % (fields[1], linenum, file.name)
            else:
                led = rgb(fields[1:4], file.name, linenum)

            leds.append((lo_hi_16(KEYCODES[fields[0]]), led))
            sets.add   (                   fields[0]        )

        elif fields[0].startswith('/') and fields[0] != '/':
            if fields[0].lower() == '/default':
                default = rgb(fields[1:4], file.name, linenum)
            else:
                colors[fields[0]] = rgb(fields[1:4], file.name, linenum)

        elif fields[0].startswith('#'):
            continue

        elif fields[0].lower() == 'version':
            check_version(fields)

        else:
            raise SyntaxError,   "Unknown key or syntax error, file %s line %d" \
                               % (file.name, linenum)

    if default:
        for key in KEYCODES.keys():
            if not key in sets:
                leds.append((lo_hi_16(KEYCODES[key]), default))

    return leds



def do_mode(device, mode, verbose):
    if mode:
        assert mode in range(MAX_MODE + 1), \
               "Mode must be in range 1..%d" % MAX_MODE
        write_read    (device, START_PKT , verbose)
        do_mode_packet(device, mode      , verbose)
        write_read    (device, FINISH_PKT, verbose)



def do_level(device, mode, level, verbose):
    assert level in range(MAX_LEVEL + 1), "Level must 0..%d" % MAX_LEVEL

    level_pkt[LEVEL_NDX] = level

    write_read    (device, START_PKT , verbose)
    do_mode_packet(device, mode      , verbose)
    write_read    (device, level_pkt , verbose)
    write_read    (device, FINISH_PKT, verbose)



def do_solid(device, mode, solid, verbose):
    check_rgb(solid)
    set_rgb  (solid_color_pkt, SOLID_LED_NDX, solid)

    write_read    (device, START_PKT       , verbose)
    do_mode_packet(device, mode            , verbose)
    write_read    (device, SOLID_PREFIX_PKT, verbose)
    write_read    (device, solid_color_pkt , verbose)
    write_read    (device, FINISH_PKT      , verbose)



def do_keys(device, mode, keys_rgbs, verbose):
    for (key, rgb) in keys_rgbs:
        if not key.lower() in KEYCODES:
            raise KeyError, "No such key '%s'" % key
        check_rgb(rgb)

    write_read    (device, START_PKT, verbose)
    do_mode_packet(device, mode     , verbose)

    for (key, rgb) in keys_rgbs:
        set_lo_hi(key_pkt, KEY_CODE_NDX, KEYCODES[key.lower()])
        set_rgb  (key_pkt, KEY_RGB_NDX ,          rgb         )

        write_read(device, key_pkt, verbose)

    write_read(device, FINISH_PKT, verbose)



def do_file(device, mode, file, verbose):
    try:
        leds = parse_file(file)
    except (SyntaxError, ValueError) as error:
        sys.stderr.write("%s\n" % error)
        sys.exit(1)

    for led in leds:
        pkt_ndx = led[0] / LEDS_PER_PACKET
        led_ndx = led[0] % LEDS_PER_PACKET + FIRST_LED_NDX

        leds_pkts[pkt_ndx][led_ndx:led_ndx+3] = led[1]

    write_read    (device, START_PKT      , verbose)
    do_mode_packet(device, mode,            verbose)
    write_read    (device, LEDS_PREFIX_PKT, verbose)

    for pkt in leds_pkts: write_read(device, pkt, verbose)

    write_read(device, FINISH_PKT, verbose)



def ajazz(device, mode, level, solid, keys, file, verbose):
    init_leds_pkts()

    if mode is not None:
        assert mode in range(1, MAX_MODE + 1), \
                        "mode must be in range 1..%d" % MAX_MODE

    if mode and not (level or solid or keys or file):
        do_mode(device, mode, verbose)
    elif level is not None:
        do_level(device, mode, level, verbose)
    elif solid:
        do_solid(device, mode, solid, verbose)
    elif keys:
        do_keys(device, mode, keys, verbose)
    elif file:
        do_file(device, mode, file, verbose)



def key_names():
    for name in KEYCODES.keys():
        sys.stdout.write(" %s" % name)
    sys.stdout.write('\n')



def parse_commandline():
    parser = argparse.ArgumentParser(prog=sys.argv[0])

    def mode(text):
        mode_name = text.lower()
        if mode_name in MODE_NAMES.keys():
            return MODE_NAMES[mode_name]
        else:
            try:
                mode = int(text)
                assert mode in range(1, MAX_MODE + 1)
            except:
                raise argparse.ArgumentTypeError(  "mode must be one of %s "
                                                   "or number from 1..%d"
                                                  % (','.join(MODE_NAMES.keys()),
                                                     MAX_MODE                  ))
            return mode

    def level(text):
        try:
            level = int(text)
            assert level in range(MAX_LEVEL + 1)
        except:
            raise argparse.ArgumentTypeError("brightness level must be "
                                              "number 0..%d" % MAX_LEVEL)
        return level

    class Rgb(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            try:
                rgb = rgb_strings_to_bytes(values)
            except:
                parser.error("bad RGB '%s'" % " ".join(values))  # not ArgTypErr
            setattr(namespace, self.dest, rgb)

    class KeyRgb(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            key = values[0  ]
            rgb = values[1:4]
            if not key in KEYCODES:
                parser.error("unknown key '%s'\n" % key)  # not ArgumentTypeError
            try:
                key_rgb = (values[0], rgb_strings_to_bytes(rgb))
            except:
                parser.error("bad RGB '%s'\n" % " ".join(rgb))  # not ArgTypErr
            if getattr(namespace, 'keys', None) is None:
                setattr(namespace, 'keys', [])
            getattr(namespace, 'keys'            ).append(key_rgb)
            setattr(namespace, self.dest, key_rgb)

    parser.add_argument('-d', '--device',
                        required=True,
                        type=argparse.FileType('r+'),
                        help="/dev/hidrawN")

    parser.add_argument('-m', '--mode',
                        nargs='?',
                        type=mode,
                        default=None,
                        help="solid|custom|<1-%d>" % MAX_MODE)

    exclsv = parser.add_mutually_exclusive_group(required=False)

    exclsv.add_argument('-l', '--level',
                        nargs='?',
                        type=level,
                        default=None,
                        help="<brightness level> (0..%d)" % MAX_LEVEL)

    exclsv.add_argument('-s', '--solid',
                        nargs=3,
                        action=Rgb,
                        help="<r> <g> <b>")

    exclsv.add_argument('-k', '--key',
                        nargs=4,
                        action=KeyRgb,
                        help="<key> <r> <g> <b>")

    parser.add_argument('--keys',
                        action='store_const',
                        const=None,
                        default=None,
                        help=argparse.SUPPRESS)

    exclsv.add_argument('-f', '--file',
                        nargs='?',
                        type=argparse.FileType('r'),
                        help="key+color file ")

    exclsv.add_argument('--names',
                        action='store_true',
                        help="print key names for --file file")

    parser.add_argument('-A', '--accept',
                        action='store_true',
                        help="suppress warning message")

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help="print binary packets sent to and received "
                             "from keyboard")

    exclsv.add_argument('--version',
                        action='version',
                        version=str(VERSION),
                        help="print file format version")

    return parser.parse_args()



if __name__ == "__main__":
    args = parse_commandline()

    # can't do this with argparse.add_mutually_exclusive_group(required=True)
    # because --mode can be standalone or added to other options
    if not (    args.mode
            or  args.level
            or (args.level == 0)
            or  args.solid
            or  args.key
            or  args.file
            or  args.names      ):
        sys.stderr.write("Specify -m and/or one of -l, -s, -k, -f (or --help)\n")
        sys.exit(1)

    if not args.accept:
        print COPYRIGHT
        print NO_WARRANTY
        print WARNING
        if sys.stdin.readline() != "accept\n":
            sys.stderr.write("\nexiting ...\n")
            sys.exit(1)
        sys.stderr.write('\n')

    if args.names:
        key_names()
        sys.exit(0)

    ajazz(args.device    ,
          args.mode      ,
          args.level     ,
          args.solid     ,
          args.keys      ,
          args.file      ,
          args.verbose    )
