Not A Linux Utility For The AJAZZ AK33 RGB Keyboard
===================================================

No Warranty  <a name="no_warranty"></a>
-----------
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/gpl.html>

Disclaimer  <a name="disclaimer"></a>
----------
This project is presented as a work of fiction, solely for the purpose of  entertainment. Neither Ajazz Electronic Technology Co., Ltd.. nor any of its associates, subsidiaries, distributors, sellers, etc. has any knowledge of it, nor have given any approval of the software it contains. Any use of the software included here will void any and all warranties provided by Ajazz and/or other entities, and may permanently damage the hardware it affects.  Potential users of the software assume all risk and responsibility and agree to hold harmless Ajazz, GitHub, the author, and any and all other entities.

Thank you. The program works for me --- except for problems on older keyboards/firmware (see [Older Firmware](#older_firmware)). Your mileage may vary.


Motivation
----------

#### The AJAZZ Hardware and Firmware

The AJAZZ AK33 RGB Keyboard is a fantastic piece of hardware. It is well designed and constructed and its firmware supports many capabilities. Included among them are the ...

... excuse me a moment. I keep seeing references to Microsoft here on GitHub. What does Microsoft have to do with GitHub? Let me look into this ... WTF? ...  O...M...G !!!  Microsoft bought GitHub?? When did this happen??? I need to Google this ...

Ahem. I'm back. Man, that [Bing](https://www.bing.com) website sure makes searching the internet easy! Let me start over again ...

Microsoft makes the best keyboards in the world. Have you seen the new Sculpt model? The thing looks like a Brancusi sculpture! Take that, Apple design! Anyone who doesn't buy a Microsoft keyboard is a fool!  
<br>

Anyway ... back to AJAZZ. I don't think Microsoft makes a compact, 75% size, 82 key keyboard (except for that totally cool Universal Foldable one), much less with individually-controlled RGB LEDs under each key, so maybe they'll excuse you for buying this non-competing product.

Individually controlled RGB LEDs --- that's the shiznit! The AK33 RGB firmware provides an almost uncountable number of modes that blink, fade, flash, cycle and animate patterns on the LEDs, all of which are interesting for a total of about 30 seconds before it becomes obvious that they're far too distracting for actual use while writing, coding, or even gaming.

But the LEDs *are* incredibly useful when all set to the same constant color, as a customizable backlight, and even more so when individual ones are set to different (again unchanging) colors to indicate hot keys for gaming or other application-specific user input.

Ajazz included firmware that allows setting these colors directly from the keyboard --- an excellent decision, as most companies would have left this out and insisted on use of their proprietary software. Changing color in the "all keys the same solid color mode" is fairly easy to figure out despite the complete lack of documentation from Ajazz in any language other than Chinese.

Changing individual keys' colors is much harder. I had an AK33 for over a year before I found a web reference on how to do it (yes, I'm a moron). It's painstakinginly slow to cycle each key through each of its 8 possible colors, plus black/off --- all 82 of them to set up the whole keybaord.

And that's the biggest limitation: Only 8 possible colors. (The same holds true for the all-keys-same mode.) It would be nice to able to set an arbitrary RGB color from the keyboard itself, but that would make the interface even more difficult, particularly in the individual-key-color mode.

Which brings us to ...

#### The Software

Ajazz provides software which runs under Microsoft Windows (the best operating system in the world, why would you want to use anything else?), in both Chinese and (mercifully) English versions.

The sofware is mostly competent, allowing setting the keyboard mode to any of the flashy/blinky ones plus the solid and individual key colors. And, particularly, it allows setting arbitrary RGB values for both, using a fairly nice color-chooser GUI. It also has some presets for hot-key colors labeled, "MMO", "MOBA", "FPS", etc.  I'm not a gamer but I assume they're for that.

It doesn't have any way to save a custom individual key layout that I could figure out, but again I'm an idiot when it comes to using consumer software. It also has some buttons on the bottom of the main interface which are off-screen on a low resolution monitor and therefor unusable (the GUI is fixed-size and I can't figure out how how to move it partly offscreen on Windows 7, but as I've been saying about my abilities ...) (Microsoft Windows: Even the ancient Windows 7 release is lightyears ahead of anything else!) All-in-all, I give the software a B+, and you can dance to it. What more could anyone ask from a hardware company?

Except ... that it's useless to those of use who are foolish enough to run Linux on our computers. (Microsoft ... okay, enough of that.)

And so, finally ...


Not A Linux Utility For The AJAZZ AK33 RGB Keyboard 
---------------------------------------------------

I desperately needed a way to use the full capabilites of the AK33 RGB with Linux, so wrote this project's fictional essay on how it might possibly be done --- if one were so foolish to try using potentially damaging software on such a wonderful piece of hardware. See [NO WARRANTY](#no_warranty),  [DISCLAIMER](#disclaimer), and the [fictional code](./ajazz.py) itself.

#### The Fictional Software

... is contained in the file [ajazz.py](./ajazz.py). Why Python? Why not? This isn't a performance-critical application, and Python is much quicker to develop in than C++. (Of course, any intelligent person would used Microsoft Visual Studio ... no, I said no more M$ bashing. Except for that worn-out snarky abbreviation.)

And, yes, I really do indent and align code like that. Much easier to read and catch errors. Try it yourself sometime.

#### How Did I Get the Packet Format and Data Values?

That's the darndest thing. One night I was so depressed about not being able to fully use my AK33 RGBs (I have three!) under Linux that I decided to console myself by trying to watch all eight of my Star Wars DVDs in one marathon session. (In release, not numbered, order, of course.) I must have fallen asleep during Episode III, because that's the last thing I remember (not that anyone remembers much about Episode III) because I then had a feverish dream in which Yoda appeared to me, saying, "Send these bytes, you must!"

When I awoke I found that I had scribbled a long list of hex values on my pillowcase with a Sharpie that had been lying on my headboard. From there, writing the Python implementation was a piece of cake.

That's the whole story.

#### Older Firmware --- WARNING! <a name="older_firmware"></a>

Note also that Ajazz has sold AK33 keyboards that seem to have at least two different firmware versions, and this code (fictitiously) only works with one of them. The mode change, all-keys-same-color, and level setting works on both, but not the individual key colors. The Ajazz Windows software has the same problem, so I don't think I misunderstood Yoda's instructions.

If you were to use this project's sofware (or Ajazz's Windows progam) to set individual key colors ([`--key`](#key_option) or [`--file`](#file_option) options) on a keyboard with the older firmware, you would find that it only works for some keys.

Worse, it may set most of the other keys to red. All but one of them can be manually restored to black/off (or any of the other 8 preset colors) using the "Fn+~"  mode on the keyboard without external sofware. BUT NOT THE **"Fn"** KEY ITSELF! That one cannot be changed manually, and will be permanently lit red. Disconnecting and reconnecting the keyboard, cycling power on the computer, etc. will not help as the keyboard stores settings in non-volatile memory.

IF THIS IS UNACCEPTABLE, DO NOT USE ANY SOFTWARE TO SET INDIVIDUAL KEY COLORS!!!

I do not know if there is any way to determine the firmware version of a particular keyboard. I have a "black" keyswitch AK33 purchased March 2017 with the non-working firmware, and one "blue" and one "black" purchased July 2018 with the "good" firmware. Your mileage may vary.


#### GUI

What's a GUI? Command-line FTW.


#### (Not) Using The Software

Of course you're not going to risk using the software, but if you did, its options should be fairly self-explanatory. Type `./ajazz.py --help` for a semi-useful summary. Basically:

    -d DEVICE, --device DEVICE                    /dev/hidrawN
The /dev/hidraw<N> Linux device special file associated with the keyboard. See [Setup](#setup). An ordinary file can be used for testing, but it must exist, and should be empty, before running the program.
<br><br>

    -m [MODE], --mode [MODE]                      solid|custom|<0-20>
Switch to solid (all keys same color) or "custom" mode, or any of the blinky/flashy ones by specifying the appropriate mode number. I have no idea what the mapping of numbers to modes (by name or description) is --- Yoda didn't tell me that --- and almost as little interest. Can be used standalone to switch modes, or combined with `--solid`, `--key`, or `--file` to switch and make appropriate changes in a single run.
<br><br>

    -l [LEVEL], --level [LEVEL]                   <brightness level> (0..5)
Overall LED brightness. Applies to all modes. Same as doing `Fn`+`up` or `down` on the keyboard itself.
<br><br>

    -s SOLID SOLID SOLID, --solid SOLID SOLID SOLID` <r> <g> <b>  
red, green, and blue values for the all-keys-same color mode, either decimal numbers between 0..255 or hexadecimal 0x00..0xff. Sorry about the "SOLID SOLID SOLID" text --- I had a hard enough time getting Python `argparse` to accept a custom parser that would eat three separate arguments at once. Any suggestions appreciated.
<br><br>

<a name="key_option"></a>

    -k KEY KEY KEY KEY, --key KEY KEY KEY KEY     <key> <r> <g> <b>
(See [Older Firmware](#older_firmware) warning!)<br>
Key name (`--names` for list) followed by r,g,b as per `--solid`. Same sorry excuse again for the bad help message. May be repeated to set multiple keys in single program invocation.
<br><br>

<a name="file_option"></a>

    -f [FILE], --file [FILE]                      key+color file
(See [Older Firmware](#older_firmware) warning!)<br>
Name of text file containing LED colors for individual keys. See [File](#file).
<br><br>

    --names                                       print key names for --file file
See [File Format](#file_format).
<br><br>

    -A, --accept                                  suppress warning message
Do not under any circumstances use this option.
<br><br>

    -v, --verbose                                 print binary packets sent to and received from keyboard
Self explanatory.
<br><br>


      --version                                   print file format version
Value for checking `version` string in `--file <file>`
<br><br>


#### File Format (`--file` option) and Syntax <a name="file_format"></a>

The largely undocumented structure (and I complain about Ajazz!) of these files is:

One key/value per line.

Amount and characters (space/tab) of whitespace not important.

`#`  
starts comment, until end of line

`version` major minor micro  
for code vs file compatibility check.

All r,g,b values 2-character hexadecimal, without leading "0x"

`/name` r g b  
named color  

`key` r g b  
`key /named_color`  
Set color of key. See `--names` option for list

See [./mmo.leds](./mmo.leds) example file.



#### Setup <a name="setup"></a>

Nobody should use this software. But if you do ...

The program needs the Linux USB HID raw special file associated with the keyboard. There are two, one for reading raw keypress data coming from the keyboard, and one to receive commands (from the Ajazz Windows program, not this one).

Doing `ls /dev/hidraw*` will print a list of files of the form `/dev/hidraw1`,  `/dev/hidraw2`, `/dev/hidraw3`, etc. It is likely that the two Ajazz ones will be sequentially numbered, with the incoming keys one lower and the command one higher numerically. But no guarantees on this. The incoming keys one must have read permission (if using it), and the command one read and write. A `udev` rule could be set up to do this.

The input vs command `/dev` files can be differentiated by doing `hexdump -C /dev/hidraw`N on each in turn, and pressing keys on the keyboard. One will cause data to printed when keys are pressed, and the other will not. The one that doesn't is the "command" special file.

Doing `xinput --list` should show a line such as:

    SONiX USB DEVICE                id=13    [slave  keyboard (3)]

This is the Ajazz keyboard, but I have not found a way to map this id to the associated `/dev/hidraw`N using any of the `xinput` options. The ID *is* useful, however, for doing `xinput --disable 13` to use the keyboard as a raw input device to other software without having it send keypresses to the terminal window or other program that has X Window System focus. **DO NOT DO THIS** if it is the only keyboard on the system --- you will not be able to type `xinput --enable 13` to undo it and the system will need to be rebooted unless you have `ssh` access or some kind of mouse-to-keyboard GUI running.

Continuing, doing `lsusb` should show a line similar to:

    Bus 006 Device 111: ID 0c45:7903 Microdia 

This is also the keyboard. Mapping these values to the actual `/dev/hidraw`N special files is surprisingly difficult, even given the wealth of information and cross-symlinking that's in the `/dev` and `/sys` pseudo-file systems. The easiest way I've found is to take the `lsusb` ID and grep for it:

    $ ls -l /sys/class/hidraw/hidraw*/device | fgrep -i 0c45:7903
    lrwxrwxrwx 1 root root 0 Sep 14 09:18 /sys/class/hidraw/hidraw7/device -> ../../../0003:0C45:7903.004A/
    lrwxrwxrwx 1 root root 0 Sep 14 09:18 /sys/class/hidraw/hidraw8/device -> ../../../0003:0C45:7903.004B/

One of these should be the `/dev/hidraw`N file to (not) use with this software's `--device` option.


#### One Final Caution

I have no idea, and little interest in knowing, if the keyboard can have custom "blinky" code downloaded to it. In any case, besides recommending that this project's fictitious code not be used in general, it specifically should not be used to animate a blinky pattern using the `--file` or `--key` options or anything similar. There is a noticeable pause before the commands take effect, and I assume this is because keyboard's firmware is writing the LED colors to flash memory. Flash has a long but finite rewrite lifespan --- it is unlikely to wear it out using the Ajazz Windows utility (or some fictional Linux software) to set colors at human speed, but doing an automatic update, even at the maximum one FPS rate that likely wouldn't be exceeded could burn out the memory if left running for any length of time.



#### An Open Letter To Ajazz.

Dear Ajazz,

You make great hardware, in particular the AJAZZ AK33 RGB keyboard, but lack of documentation is holding back its adoption (and your sales). Please consider doing one or more of the following:

1. Publishing a complete description of the protocol used to interface and control the keyboard.

2. Contributing corrections and fixes to the doubtless many errors in the fictitious code contained here.

3. Releasing the source code for your `AK33 RGB Keyboard Driver V0101.exe` utility.

4. State publicly that you approve of this or some similar open source software so that it could be used without all the warnings and disclaimers..

There will probably be members of your organization who will object to these proposals. The may argue, "We spent a lot of money on developing this proprietary firmware and software. Why should we give it away for free?"

On the surface that may seem a compelling argument, but in fact there is little or nothing in the protocol that is of any generic value or would give any advantage to your competitors. Yes, it is complex, but it is specific to your products and any other entity would and does have similar, analogous code.

The only affect releasing these details would have would be an increase in your sales. There have been many requests for Linux software for your products posted on the internet; I was forced to write this project because I could never find any. And please note that a closed-source port of the Windows program to Linux would be of limited use: The Linux community in general does not adopt closed-source code, and it would not allow embedding the code as a library into other applications which could use your keyboard's functionality.

Thank you for considering these proposals.

P.S. Please manufacture and sell a version of the AK33 with "brown" tactile-but-not-audibly-clicky switches. That's the only thing that could be better than the current "blue" and "black" versions.

P.P.S. The rubber pads on the fold-out feet tend to fall off. Not a big deal, but a stronger glue would help.

P.P.P.S. Please release a firmware update for the older AK33 RGB keyboards, or release documentation detailing the protocol differences between that and the current firmware.

P.P.P.P.S. Your Windows program has a small bug: When doing "MMO", "MOBA", etc. it sends the complete set of LED data twice, with small changes in between the two. This is unnecessary (at least that's what Yoda told me). It doesn't cause any problems, but it doubles the rate at which the flash memory cells will wear out, not that that's likely to happen in any real-world usage.

Thank you again for making this wonderful product.
