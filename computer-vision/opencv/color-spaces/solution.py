"""
OpenCV Color Space Conversions & HSV Masking
Reference: https://mlhive.com/playground/computer-vision/opencv/color-spaces
"""

# RUN CONFIGURATION & PARAMETERS
TARGET_COLOR = "red"  # "red", "green", "blue"
IMAGE_URL = "https://mlhive.com/playground/opencv/color-spaces/peppers.webp"

# HSV Ranges (OpenCV scale: H in [0..179], S in [0..255], V in [0..255])
HSV_PRESETS = {
    "red": {"h_min": 170, "h_max": 10, "s_min": 100, "s_max": 255, "v_min": 60, "v_max": 255, "wrap": True},
    "green": {"h_min": 35, "h_max": 85, "s_min": 70, "s_max": 255, "v_min": 50, "v_max": 255, "wrap": False},
    "blue": {"h_min": 100, "h_max": 135, "s_min": 80, "s_max": 255, "v_min": 50, "v_max": 255, "wrap": False},
}

def rgb_to_hsv(r: int, g: int, b: int) -> tuple[float, float, float]:
    r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
    c_max = max(r_norm, g_norm, b_norm)
    c_min = min(r_norm, g_norm, b_norm)
    diff = c_max - c_min

    # Hue in degrees
    if diff == 0:
        h = 0.0
    elif c_max == r_norm:
        h = (60.0 * ((g_norm - b_norm) / diff) + 360.0) % 360.0
    elif c_max == g_norm:
        h = (60.0 * ((b_norm - r_norm) / diff) + 120.0) % 360.0
    else:
        h = (60.0 * ((r_norm - g_norm) / diff) + 240.0) % 360.0

    s = 0.0 if c_max == 0 else (diff / c_max)
    v = c_max
    return h / 2.0, s * 255.0, v * 255.0  # Scale H to 0-180 for OpenCV convention

def is_in_range(h: float, s: float, v: float, p: dict) -> bool:
    if p["wrap"]:
        h_ok = (h >= p["h_min"] or h <= p["h_max"])
    else:
        h_ok = (p["h_min"] <= h <= p["h_max"])
    s_ok = (p["s_min"] <= s <= p["s_max"])
    v_ok = (p["v_min"] <= v <= p["v_max"])
    return h_ok and s_ok and v_ok

def main():
    preset = HSV_PRESETS[TARGET_COLOR]
    print(f"--- Color Space & HSV Masking Visualizer ---")
    print(f"Target Color Preset: {TARGET_COLOR.upper()}")
    print(f"HSV Thresholds: H=[{preset['h_min']}..{preset['h_max']}], S=[{preset['s_min']}..{preset['s_max']}], V=[{preset['v_min']}..{preset['v_max']}]")
    print(f"Sample asset link: {IMAGE_URL}\n")

    sample_colors = [
        ("Pure Red", (255, 0, 0)),
        ("Dark Red", (160, 20, 20)),
        ("Forest Green", (20, 140, 30)),
        ("Sky Blue", (40, 120, 230)),
        ("White", (255, 255, 255)),
        ("Gray", (128, 128, 128)),
    ]

    print(f"{'Color Name':14s} | {'RGB':14s} | {'HSV (H, S, V)':18s} | Mask Active")
    print("-" * 62)
    for name, (r, g, b) in sample_colors:
        h, s, v = rgb_to_hsv(r, g, b)
        active = is_in_range(h, s, v, preset)
        rgb_str = f"({r:3d}, {g:3d}, {b:3d})"
        hsv_str = f"({h:5.1f}, {s:5.1f}, {v:5.1f})"
        print(f"{name:14s} | {rgb_str:14s} | {hsv_str:18s} | {'[YES]' if active else ' No '}")

if __name__ == "__main__":
    main()
