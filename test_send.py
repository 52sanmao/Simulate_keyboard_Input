import ctypes, time
from ctypes import wintypes

user32 = ctypes.windll.user32
user32.SendInput.argtypes = [ctypes.c_uint, ctypes.c_void_p, ctypes.c_int]
user32.SendInput.restype = ctypes.c_uint

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [('wVk', ctypes.c_ushort), ('wScan', ctypes.c_ushort),
                ('dwFlags', ctypes.c_ulong), ('time', ctypes.c_ulong),
                ('dwExtraInfo', ctypes.c_void_p)]

class INPUT(ctypes.Structure):
    _fields_ = [('type', ctypes.c_ulong), ('ki', KEYBDINPUT)]

print('Test 1: VK code approach (like pynput) for "a"')
inp = INPUT(1, KEYBDINPUT(0x41, 0, 0, 0, None))
r1 = user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(inp))
time.sleep(0.05)
inp2 = INPUT(1, KEYBDINPUT(0x41, 0, 0x0002, 0, None))
r2 = user32.SendInput(1, ctypes.byref(inp2), ctypes.sizeof(inp2))
print(f'  SendInput VK ret: {r1},{r2}')

print('Test 2: scancode approach for Enter')
sc = user32.MapVirtualKeyW(0x0D, 0)
print(f'  Enter scancode=0x{sc:02X}')
inp3 = INPUT(1, KEYBDINPUT(0, sc, 0x0008, 0, None))
r3 = user32.SendInput(1, ctypes.byref(inp3), ctypes.sizeof(inp3))
time.sleep(0.05)
inp4 = INPUT(1, KEYBDINPUT(0, sc, 0x0008|0x0002, 0, None))
r4 = user32.SendInput(1, ctypes.byref(inp4), ctypes.sizeof(inp4))
print(f'  SendInput scancode ret: {r3},{r4}')

print('Test 3: scancode for "a" (letter a scancode)')
sc_a = user32.MapVirtualKeyW(0x41, 0)  # VK_A
print(f'  A scancode=0x{sc_a:02X}')
inp5 = INPUT(1, KEYBDINPUT(0, sc_a, 0x0008, 0, None))
r5 = user32.SendInput(1, ctypes.byref(inp5), ctypes.sizeof(inp5))
time.sleep(0.05)
inp6 = INPUT(1, KEYBDINPUT(0, sc_a, 0x0008|0x0002, 0, None))
r6 = user32.SendInput(1, ctypes.byref(inp6), ctypes.sizeof(inp6))
print(f'  SendInput scancode ret: {r5},{r6}')
