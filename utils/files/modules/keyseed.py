#!/usr/bin/python

# Formats payload to HID Keyboard sequences. Real rough poc for testing basic payloads.

def findinlist(byte):

# Symbols 
	if   byte=="\x20": print '''echo -ne "\\x00\\x00\\x00\\x2c\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x21": print '''echo -ne "\\x20\\x00\\x00\\x1e\\x00\\x00\\x00\\x00" > /dev/hidg0'''
        elif byte=="\x22": print '''echo -ne "\\x20\\x00\\x00\\x34\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x23": print '''echo -ne "\\x20\\x00\\x00\\x20\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x24": print '''echo -ne "\\x20\\x00\\x00\\x21\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x25": print '''echo -ne "\\x20\\x00\\x00\\x22\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x26": print '''echo -ne "\\x20\\x00\\x00\\x24\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x27": print '''echo -ne "\\x00\\x00\\x00\\x34\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x28": print '''echo -ne "\\x20\\x00\\x00\\x26\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x29": print '''echo -ne "\\x20\\x00\\x00\\x27\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x2a": print '''echo -ne "\\x20\\x00\\x00\\x25\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x2b": print '''echo -ne "\\x20\\x00\\x00\\x2e\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x2c": print '''echo -ne "\\x00\\x00\\x00\\x36\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x2d": print '''echo -ne "\\x00\\x00\\x00\\x2d\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x2e": print '''echo -ne "\\x00\\x00\\x00\\x37\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x2f": print '''echo -ne "\\x00\\x00\\x00\\x38\\x00\\x00\\x00\\x00" > /dev/hidg0'''
# Numbers
	elif byte=="\x30": print '''echo -ne "\\x00\\x00\\x00\\x27\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x31": print '''echo -ne "\\x00\\x00\\x00\\x1e\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x32": print '''echo -ne "\\x00\\x00\\x00\\x1f\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x33": print '''echo -ne "\\x00\\x00\\x00\\x20\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x34": print '''echo -ne "\\x00\\x00\\x00\\x21\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x35": print '''echo -ne "\\x00\\x00\\x00\\x22\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x36": print '''echo -ne "\\x00\\x00\\x00\\x23\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x37": print '''echo -ne "\\x00\\x00\\x00\\x24\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x38": print '''echo -ne "\\x00\\x00\\x00\\x25\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x39": print '''echo -ne "\\x00\\x00\\x00\\x26\\x00\\x00\\x00\\x00" > /dev/hidg0'''
# Symbols
	elif byte=="\x3a": print '''echo -ne "\\x20\\x00\\x00\\x33\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x3b": print '''echo -ne "\\x00\\x00\\x00\\x33\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x3c": print '''echo -ne "\\x20\\x00\\x00\\x36\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x3d": print '''echo -ne "\\x00\\x00\\x00\\x2e\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x3e": print '''echo -ne "\\x20\\x00\\x00\\x37\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x3f": print '''echo -ne "\\x20\\x00\\x00\\x38\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x40": print '''echo -ne "\\x20\\x00\\x00\\x1f\\x00\\x00\\x00\\x00" > /dev/hidg0'''
# Uppercase
	elif byte=="\x41": print '''echo -ne "\\x20\\x00\\x00\\x04\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x42": print '''echo -ne "\\x20\\x00\\x00\\x05\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x43": print '''echo -ne "\\x20\\x00\\x00\\x06\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x44": print '''echo -ne "\\x20\\x00\\x00\\x07\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x45": print '''echo -ne "\\x20\\x00\\x00\\x08\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x46": print '''echo -ne "\\x20\\x00\\x00\\x09\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x47": print '''echo -ne "\\x20\\x00\\x00\\x0a\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x48": print '''echo -ne "\\x20\\x00\\x00\\x0b\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x49": print '''echo -ne "\\x20\\x00\\x00\\x0c\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x4a": print '''echo -ne "\\x20\\x00\\x00\\x0d\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x4b": print '''echo -ne "\\x20\\x00\\x00\\x0e\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x4c": print '''echo -ne "\\x20\\x00\\x00\\x0f\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x4d": print '''echo -ne "\\x20\\x00\\x00\\x10\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x4e": print '''echo -ne "\\x20\\x00\\x00\\x11\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x4f": print '''echo -ne "\\x20\\x00\\x00\\x12\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x50": print '''echo -ne "\\x20\\x00\\x00\\x13\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x51": print '''echo -ne "\\x20\\x00\\x00\\x14\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x52": print '''echo -ne "\\x20\\x00\\x00\\x15\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x53": print '''echo -ne "\\x20\\x00\\x00\\x16\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x54": print '''echo -ne "\\x20\\x00\\x00\\x17\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x55": print '''echo -ne "\\x20\\x00\\x00\\x18\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x56": print '''echo -ne "\\x20\\x00\\x00\\x19\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x57": print '''echo -ne "\\x20\\x00\\x00\\x1a\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x58": print '''echo -ne "\\x20\\x00\\x00\\x1b\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x59": print '''echo -ne "\\x20\\x00\\x00\\x1c\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x5a": print '''echo -ne "\\x20\\x00\\x00\\x1d\\x00\\x00\\x00\\x00" > /dev/hidg0'''
# Symbols
	elif byte=="\x5b": print '''echo -ne "\\x00\\x00\\x00\\x2f\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x5c": print '''echo -ne "\\x00\\x00\\x00\\x31\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x5d": print '''echo -ne "\\x00\\x00\\x00\\x30\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x5e": print '''echo -ne "\\x20\\x00\\x00\\x23\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x5f": print '''echo -ne "\\x00\\x00\\x00\\x2d\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x60": print '''echo -ne "\\x00\\x00\\x00\\x35\\x00\\x00\\x00\\x00" > /dev/hidg0'''
# Lowercase
	elif byte=="\x61": print '''echo -ne "\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x62": print '''echo -ne "\\x00\\x00\\x00\\x05\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x63": print '''echo -ne "\\x00\\x00\\x00\\x06\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x64": print '''echo -ne "\\x00\\x00\\x00\\x07\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x65": print '''echo -ne "\\x00\\x00\\x00\\x08\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x66": print '''echo -ne "\\x00\\x00\\x00\\x09\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x67": print '''echo -ne "\\x00\\x00\\x00\\x0a\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x68": print '''echo -ne "\\x00\\x00\\x00\\x0b\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x69": print '''echo -ne "\\x00\\x00\\x00\\x0c\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x6a": print '''echo -ne "\\x00\\x00\\x00\\x0d\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x6b": print '''echo -ne "\\x00\\x00\\x00\\x0e\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x6c": print '''echo -ne "\\x00\\x00\\x00\\x0f\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x6d": print '''echo -ne "\\x00\\x00\\x00\\x10\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x6e": print '''echo -ne "\\x00\\x00\\x00\\x11\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x6f": print '''echo -ne "\\x00\\x00\\x00\\x12\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x70": print '''echo -ne "\\x00\\x00\\x00\\x13\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x71": print '''echo -ne "\\x00\\x00\\x00\\x14\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x72": print '''echo -ne "\\x00\\x00\\x00\\x15\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x73": print '''echo -ne "\\x00\\x00\\x00\\x16\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x74": print '''echo -ne "\\x00\\x00\\x00\\x17\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x75": print '''echo -ne "\\x00\\x00\\x00\\x18\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x76": print '''echo -ne "\\x00\\x00\\x00\\x19\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x77": print '''echo -ne "\\x00\\x00\\x00\\x1a\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x78": print '''echo -ne "\\x00\\x00\\x00\\x1b\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x79": print '''echo -ne "\\x00\\x00\\x00\\x1c\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x7a": print '''echo -ne "\\x00\\x00\\x00\\x1d\\x00\\x00\\x00\\x00" > /dev/hidg0'''
#Shift chars
	elif byte=="\x7b": print '''echo -ne "\\x20\\x00\\x00\\x2f\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x7c": print '''echo -ne "\\x20\\x00\\x00\\x31\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x7d": print '''echo -ne "\\x20\\x00\\x00\\x30\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x7e": print '''echo -ne "\\x00\\x00\\x00\\x40\\x00\\x00\\x00\\x00" > /dev/hidg0'''
#SDLK_RETURN,0x28
	elif byte=="\x0a": print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	elif byte=="\x0d": print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
#SDLK_ESCAPE,0x29
#SDLK_BACKSPACE,0x2a
#SDLK_TAB,0x2b
	else: print "#crap, couldn't find ["+byte +"]. Perhaps try adding it to the list."
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''	

def wincmd():
	print '''sleep 1'''
	print '''echo -ne "\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x00\\x00\\x00\\x06\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x00\\x00\\x00\\x10\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x00\\x00\\x00\\x07\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x10\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x20\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 3'''

def win8cmd_elevated():
	print '''sleep 1'''
	print '''echo -ne "\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x00\\x00\\x00\\x06\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x00\\x00\\x00\\x10\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x00\\x00\\x00\\x07\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x10\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x02\\x00\\x00\\x43\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 2'''
	print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 2'''
	print '''echo -ne "\\x04\\x00\\x00\\x1c\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 3'''

def enterb():
	print '''sleep 2'''
	print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''


