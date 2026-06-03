"""สร้าง icon (128px) + store screenshots (1280x800) สำหรับ extension ใน Roadmap 6 ตัว
Price Compare, Facebook Toolkit, YouTube Toolkit, Instagram Toolkit, Stock Alert, Social Analytics
ใส่ลงในโฟลเดอร์ images/ โดยตรง — python3 make_roadmap_assets.py"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 800
WHITE = (255, 255, 255)
DARK  = (17, 24, 39)
GRAY  = (107, 114, 128)
SOFT  = (249, 250, 251)
BORDER= (229, 231, 235)
HERE  = os.path.dirname(os.path.abspath(__file__))
OUT   = os.path.join(HERE, "images")
os.makedirs(OUT, exist_ok=True)

FONT_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]
def font(size, bold=False):
    for p in FONT_PATHS:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: continue
    return ImageFont.load_default()

def rr(d, xy, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

def shadow(d, x, y, w, h, r=14):
    for i in range(7):
        a = max(0, 9 - i)
        rr(d, [x-i, y-i, x+w+i, y+h+i], r, fill=(0, 0, 0, a))

def lighten(c, f=0.35):
    return tuple(int(v + (255 - v) * f) for v in c)

# ── promo frame (left text, brand chip) ──────────────────────────────────────
def frame(bg, brand, accent, title, subtitle, bullets):
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    chip_w = 60 + d.textlength(brand, font=font(14, True))
    rr(d, [32, 28, 32 + chip_w, 60], 16, fill=accent)
    d.ellipse([46, 36, 62, 52], fill=WHITE)
    d.text((72, 35), brand, fill=WHITE, font=font(14, True))
    ty = 120
    for line in title.split("\n"):
        d.text((60, ty), line, fill=DARK, font=font(50, True))
        ty += 62
    d.text((60, ty + 8), subtitle, fill=GRAY, font=font(19))
    ty += 52
    for b in bullets:
        by = ty + 16
        d.ellipse([60, by, 82, by + 22], fill=accent)
        d.line([66, by + 11, 71, by + 16], fill=WHITE, width=3)
        d.line([71, by + 16, 78, by + 6], fill=WHITE, width=3)
        d.text((94, ty + 4), b, fill=DARK, font=font(18))
        ty += 38
    return img, d

# ── popup shell ──────────────────────────────────────────────────────────────
def popup_shell(d, title, sub, accent, tabs, active):
    pw, ph = 360, 490
    px = W - pw - 60
    py = (H - ph) // 2
    shadow(d, px, py, pw, ph)
    rr(d, [px, py, px + pw, py + ph], 14, fill=WHITE)
    rr(d, [px, py, px + pw, py + 58], 14, fill=DARK)
    d.rectangle([px, py + 44, px + pw, py + 58], fill=DARK)
    d.ellipse([px + 16, py + 18, px + 40, py + 42], fill=accent)
    d.text((px + 50, py + 14), title, fill=WHITE, font=font(14, True))
    d.text((px + 50, py + 33), sub, fill=(170, 175, 185), font=font(10))
    tw = pw // len(tabs)
    for i, t in enumerate(tabs):
        tx = px + i * tw
        d.rectangle([tx, py + 58, tx + tw, py + 88], fill=(accent if i == active else (38, 41, 51)))
        d.text((tx + tw // 2, py + 73), t, fill=WHITE, font=font(11, True), anchor="mm")
    return px, py, pw, ph

def label(d, x, y, text):
    d.text((x, y), text, fill=GRAY, font=font(10)); return y + 16
def inp(d, x, y, w, value):
    rr(d, [x, y, x + w, y + 28], 7, fill=SOFT, outline=BORDER)
    d.text((x + 10, y + 7), value, fill=DARK, font=font(12)); return y + 36
def btn(d, x, y, w, text, fill):
    rr(d, [x, y, x + w, y + 34], 8, fill=fill)
    d.text((x + w // 2, y + 17), text, fill=WHITE, font=font(12, True), anchor="mm"); return y + 42

# ── generic content drawers ──────────────────────────────────────────────────
def draw_form(d, p, fields, btn_text, accent):
    px, py, pw, ph = p
    x, w = px + 14, pw - 28; y = py + 102
    for lbl, val in fields:
        y = label(d, x, y, lbl); y = inp(d, x, y, w, val); y += 4
    y += 6
    btn(d, x, y, w, btn_text, accent)

def draw_two_col_form(d, p, header, pairs, btn_text, accent):
    px, py, pw, ph = p
    x, w = px + 14, pw - 28; y = py + 100
    label(d, x, y, header); y += 22
    half = (w - 10) // 2
    for i in range(0, len(pairs), 2):
        l1, v1 = pairs[i]
        label(d, x, y, l1); inp(d, x, y + 16, half, v1)
        if i + 1 < len(pairs):
            l2, v2 = pairs[i + 1]
            label(d, x + half + 10, y, l2); inp(d, x + half + 10, y + 16, half, v2)
        y += 56
    y += 6
    btn(d, x, y, w, btn_text, accent)

def row_card(d, x, y, w, title, sub, badge, bcol):
    h = 62
    rr(d, [x, y, x + w, y + h], 9, fill=SOFT, outline=BORDER)
    d.text((x + 12, y + 11), title, fill=DARK, font=font(12, True))
    d.text((x + 12, y + 32), sub, fill=GRAY, font=font(11))
    if badge:
        bw = max(36, d.textlength(badge, font=font(11, True)) + 16)
        rr(d, [x + w - bw - 12, y + 19, x + w - 12, y + 43], 7, fill=bcol)
        d.text((x + w - bw / 2 - 12, y + 31), badge, fill=WHITE, font=font(11, True), anchor="mm")
    return y + h + 10

def draw_list(d, p, header, rows, accent):
    px, py, pw, ph = p
    x, w = px + 14, pw - 28; y = py + 100
    label(d, x, y, header); y += 22
    for title, sub, badge, bcol in rows:
        y = row_card(d, x, y, w, title, sub, badge, bcol)

def toggle(d, x, y, w, lbl, on, accent):
    rr(d, [x, y, x + w, y + 40], 9, fill=SOFT, outline=BORDER)
    d.text((x + 12, y + 14), lbl, fill=DARK, font=font(12))
    sw_w, sw_h = 38, 22
    sx, sy = x + w - sw_w - 12, y + 9
    rr(d, [sx, sy, sx + sw_w, sy + sw_h], 11, fill=(accent if on else (203, 213, 225)))
    knob = sx + sw_w - 19 if on else sx + 3
    d.ellipse([knob, sy + 3, knob + 16, sy + 19], fill=WHITE)
    return y + 48

def draw_toggles(d, p, header, items, btn_text, accent):
    px, py, pw, ph = p
    x, w = px + 14, pw - 28; y = py + 100
    label(d, x, y, header); y += 22
    for lbl, on in items:
        y = toggle(d, x, y, w, lbl, on, accent)
    y += 6
    btn(d, x, y, w, btn_text, accent)

def draw_stats(d, p, header, bars, accent):
    px, py, pw, ph = p
    x, w = px + 14, pw - 28; y = py + 100
    label(d, x, y, header); y += 22
    for lbl, pct, val in bars:
        d.text((x, y), lbl, fill=DARK, font=font(12, True))
        d.text((x + w, y), val, fill=accent, font=font(12, True), anchor="ra"); y += 20
        rr(d, [x, y, x + w, y + 14], 7, fill=SOFT, outline=BORDER)
        rr(d, [x, y, x + int(w * pct), y + 14], 7, fill=accent); y += 30

# ── ICON generator (128px gradient rounded square + simple white glyph) ───────
def gradient_square(size, c1, c2):
    base = Image.new("RGB", (size, size), c1)
    top = Image.new("RGB", (size, size), c2)
    mask = Image.new("L", (size, size))
    md = ImageDraw.Draw(mask)
    for yy in range(size):
        for xx in range(0, size, 4):
            md.rectangle([xx, yy, xx + 4, yy], fill=int(255 * ((xx + yy) / (2 * size))))
    base = Image.composite(top, base, mask)
    return base

def make_icon(slug, c1, c2, glyph_fn):
    S = 128
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    grad = gradient_square(S, c1, c2).convert("RGBA")
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).rounded_rectangle([4, 4, S - 4, S - 4], radius=28, fill=255)
    img.paste(grad, (0, 0), mask)
    d = ImageDraw.Draw(img)
    glyph_fn(d, S)
    img.save(os.path.join(OUT, f"{slug}.png"))
    print(f"OK {slug}.png (icon)")

def g_baht(d, S):
    d.text((S/2, S/2), "฿", fill=WHITE, font=font(74, True), anchor="mm")
def g_f(d, S):
    d.text((S/2, S/2 + 2), "f", fill=WHITE, font=font(82, True), anchor="mm")
def g_play(d, S):
    rr(d, [30, 40, 98, 88], 14, fill=WHITE)
    d.polygon([(56, 52), (56, 76), (76, 64)], fill=c_red[0] if False else (220, 0, 0))
def g_camera(d, S):
    rr(d, [30, 34, 98, 94], 18, outline=WHITE, width=7)
    d.ellipse([48, 50, 80, 82], outline=WHITE, width=7)
    d.ellipse([82, 42, 92, 52], fill=WHITE)
def g_bell(d, S):
    d.pieslice([40, 34, 88, 94], 180, 360, fill=WHITE)
    d.rectangle([40, 64, 88, 84], fill=WHITE)
    d.ellipse([56, 84, 72, 100], fill=WHITE)
    d.ellipse([58, 26, 70, 38], fill=WHITE)
def g_chart(d, S):
    for i, h in enumerate([28, 48, 36, 60]):
        bx = 28 + i * 20
        rr(d, [bx, 96 - h, bx + 13, 96], 3, fill=WHITE)

# ============================================================================
# EXTENSION DEFINITIONS
# ============================================================================
GREEN = (5, 150, 105); RED = (239, 68, 68); BLUE = (37, 99, 235); AMBER = (217, 119, 6)
c_red = [(220, 0, 0)]

EXTS = [
    {
        "slug": "price-compare", "brand": "Price Compare",
        "accent": (22, 163, 74), "ico": ((34, 197, 94), (5, 122, 85)), "glyph": g_baht,
        "tabs": ["เทียบราคา", "ประวัติ", "ตั้งค่า"],
        "sub": "เทียบราคา · ข้ามแพลตฟอร์ม",
        "shots": [
            ((240, 253, 244), "เทียบราคาสินค้า\nข้ามแพลตฟอร์ม", "Lazada · Shopee · JD Central คลิกเดียวรู้ที่ถูกสุด",
             ["ดึงราคาเรียลไทม์ 3 แพลตฟอร์ม", "ไฮไลต์ร้านที่ถูกที่สุดให้อัตโนมัติ", "รวมส่วนลด/คูปองในการคำนวณ"],
             ("list", "ราคาถูกสุดตอนนี้", [
                 ("Shopee · ของแท้ Official", "ส่งฟรี · มีโค้ดลด ฿40", "฿359", GREEN),
                 ("Lazada · LazMall", "ส่งใน 2 วัน", "฿389", BLUE),
                 ("JD Central", "—", "฿420", GRAY),
             ])),
            ((236, 253, 245), "ไฮไลต์ที่ถูกสุด\nให้อัตโนมัติ", "ไม่ต้องเปิดหลายแท็บเทียบเอง ระบบจัดอันดับให้",
             ["จัดอันดับราคาจากถูกไปแพง", "คำนวณราคาสุทธิหลังหักโค้ด", "เห็นค่าส่งของแต่ละร้าน"],
             ("list", "เรียงจากถูกสุด · 3 ร้าน", [
                 ("Shopee", "สุทธิหลังโค้ด", "฿319", GREEN),
                 ("Lazada", "สุทธิหลังโค้ด", "฿389", BLUE),
                 ("JD Central", "ไม่มีโค้ด", "฿420", GRAY),
             ])),
            ((240, 250, 244), "กราฟราคาย้อนหลัง\nรู้ว่าควรซื้อหรือรอ", "เก็บประวัติราคาในเครื่อง เทียบว่าตอนนี้ถูกจริงไหม",
             ["กราฟราคา 30 วันย้อนหลัง", "บอกว่าราคาต่ำสุด/สูงสุดเท่าไร", "เตือนเมื่อราคาต่ำกว่าค่าเฉลี่ย"],
             ("stats", "ราคาย้อนหลัง 30 วัน", [
                 ("ต่ำสุด", 0.35, "฿349"), ("เฉลี่ย", 0.62, "฿402"), ("ตอนนี้", 0.40, "฿359"),
             ])),
            ((243, 251, 246), "ตั้งค่าแพลตฟอร์ม\nที่อยากเทียบ", "เลือกเปิด-ปิดร้านที่ต้องการเปรียบเทียบได้เอง",
             ["เปิด-ปิดแต่ละแพลตฟอร์ม", "รวมค่าส่งในการเทียบ", "สกุลเงินบาทเสมอ"],
             ("toggles", "แพลตฟอร์มที่เปิดเทียบ", [
                 ("Shopee", True), ("Lazada", True), ("JD Central", True), ("รวมค่าส่งในราคา", True),
             ], "บันทึกการตั้งค่า")),
            ((244, 252, 247), "เร็ว · แม่นยำ\n· ปลอดภัย", "อ่านเฉพาะหน้าสินค้าที่คุณเปิด ไม่ส่งข้อมูลออกนอกเครื่อง",
             ["ทำงานบนหน้าสินค้าเท่านั้น", "ไม่เก็บข้อมูลส่วนตัว", "ฟรี ใช้ได้ไม่จำกัด"],
             ("list", "ราคาถูกสุดตอนนี้", [
                 ("Shopee · ของแท้", "ถูกที่สุด", "฿359", GREEN),
                 ("Lazada · LazMall", "—", "฿389", BLUE),
             ])),
        ],
    },
    {
        "slug": "facebook-toolkit", "brand": "Facebook Toolkit",
        "accent": (24, 119, 242), "ico": ((59, 137, 247), (10, 88, 202)), "glyph": g_f,
        "tabs": ["Follow", "Like", "ตั้งค่า"],
        "sub": "follow · like · คุมลิมิต",
        "shots": [
            ((237, 244, 253), "จัดการ Facebook\nอัตโนมัติ", "follow/unfollow เพจและคน ไลก์/คอมเมนต์ตามเงื่อนไข",
             ["กดติดตามเพจ/คนอัตโนมัติ", "ไลก์โพสต์ในฟีดตามเกณฑ์", "คุมลิมิตต่อชั่วโมง/ต่อวัน"],
             ("form", [("กลุ่มเป้าหมาย", "ผู้ติดตามเพจคู่แข่ง"), ("จำนวนสูงสุด/รอบ", "30"),
                       ("หน่วงเวลา (วินาที)", "8 – 20")], "Start Follow")),
            ((240, 246, 254), "Follow ตามเงื่อนไข\nพร้อม Whitelist", "เลือกกลุ่มเป้าหมาย ตั้งลิมิต แล้วกด Start",
             ["follow จากผู้ติดตามเพจอื่น", "Whitelist กันบัญชีที่ไม่ต้องการ", "หน่วงเวลาแบบสุ่มเหมือนคนจริง"],
             ("form", [("เป้าหมาย", "facebook.com/.../followers"), ("จำนวนสูงสุด", "30"),
                       ("Whitelist", "เพื่อน, แบรนด์เรา")], "Start Follow")),
            ((237, 245, 253), "ไลก์โพสต์ในฟีด\nตามเกณฑ์", "ไลก์เฉพาะโพสต์ที่ผ่านเงื่อนไข เลื่อนฟีดให้อัตโนมัติ",
             ["ไลก์ตามคำค้นในโพสต์", "ข้ามโพสต์โฆษณา", "เลื่อนฟีดต่อให้เอง"],
             ("toggles", "เกณฑ์การไลก์", [
                 ("เฉพาะโพสต์ที่มีคำค้น", True), ("ข้ามโพสต์ที่เป็นโฆษณา", True),
                 ("ไลก์เฉพาะเพจที่ติดตาม", False), ("เลื่อนฟีดอัตโนมัติ", True),
             ], "Start Like")),
            ((240, 247, 254), "ลิมิตต่อชั่วโมง\n/ ต่อวัน", "กำหนดเพดาน action กันเสี่ยง พร้อมตัวนับเรียลไทม์",
             ["ตั้งเพดานต่อชั่วโมง/ต่อวัน", "ตัวนับ usage เรียลไทม์", "หยุดอัตโนมัติเมื่อถึงลิมิต"],
             ("two", "ลิมิตความปลอดภัย", [
                 ("Follow/ชั่วโมง", "20"), ("Follow/วัน", "120"),
                 ("Like/ชั่วโมง", "60"), ("Like/วัน", "400"),
             ], "บันทึกการตั้งค่า")),
            ((242, 248, 254), "ทำงานต่อ\nแม้ปิด popup", "เครื่องยนต์รันเบื้องหลัง ปิดหน้าต่างได้ งานเดินต่อ",
             ["รันด้วย service worker", "ไม่เก็บข้อมูลส่วนตัว", "ใช้ด้วยความระมัดระวัง"],
             ("form", [("สถานะ", "กำลังทำงาน · 12/30"), ("เหลือโควตาชั่วโมงนี้", "8 ครั้ง"),
                       ("ถัดไปใน", "14 วินาที")], "Stop")),
        ],
    },
    {
        "slug": "youtube-toolkit", "brand": "YouTube Toolkit",
        "accent": (255, 0, 0), "ico": ((255, 64, 64), (200, 0, 0)), "glyph": g_play,
        "tabs": ["Subscribe", "Like", "ตั้งค่า"],
        "sub": "subscribe · like · กรอง",
        "shots": [
            ((255, 240, 240), "จัดการ YouTube\nอัตโนมัติ", "subscribe/unsubscribe และไลก์วิดีโอตามเกณฑ์",
             ["กด subscribe ช่องตามเงื่อนไข", "ไลก์วิดีโอที่ผ่านเกณฑ์ยอดวิว", "กรองตาม keyword ในชื่อวิดีโอ"],
             ("form", [("คำค้นช่อง/วิดีโอ", "สอนทำอาหาร"), ("ยอดผู้ติดตามขั้นต่ำ", "10,000"),
                       ("จำนวนสูงสุด/รอบ", "25")], "Start Subscribe")),
            ((255, 243, 243), "Subscribe ช่อง\nตามเงื่อนไข", "เปิดหน้าค้นหาช่อง ตั้งเกณฑ์ แล้วกด Start",
             ["subscribe จากผลค้นหา", "กรองตามผู้ติดตามขั้นต่ำ", "Whitelist ช่องที่ไม่ต้องการ"],
             ("list", "ช่องที่ตรงเกณฑ์ · 3 ช่อง", [
                 ("Cooking Channel TH", "ผู้ติดตาม 240K", "Subscribe", RED),
                 ("ครัวบ้านๆ", "ผู้ติดตาม 88K", "Subscribe", RED),
                 ("Street Food", "ผู้ติดตาม 15K", "Subscribe", RED),
             ])),
            ((255, 241, 241), "ไลก์วิดีโอ\nตามเกณฑ์", "ไลก์เฉพาะวิดีโอที่ผ่านยอดวิว/คำค้นที่ตั้งไว้",
             ["ยอดวิวขั้นต่ำที่จะไลก์", "คำค้นในชื่อวิดีโอ", "ข้ามวิดีโอที่ไลก์แล้ว"],
             ("two", "เกณฑ์การไลก์วิดีโอ", [
                 ("ยอดวิวขั้นต่ำ", "50,000"), ("ความยาว ≥", "3 นาที"),
                 ("คำค้นในชื่อ", "รีวิว"), ("จำนวน/รอบ", "20"),
             ], "Start Like")),
            ((255, 244, 244), "กรองตามยอดวิว\nผู้ติดตาม · keyword", "ตั้งเงื่อนไขละเอียด เจาะเฉพาะที่ต้องการ",
             ["กรองตามยอดผู้ติดตามขั้นต่ำ", "กรองตามยอดวิวขั้นต่ำ", "กรองด้วย keyword ในชื่อวิดีโอ"],
             ("toggles", "ตัวกรอง", [
                 ("กรองตามยอดผู้ติดตาม", True), ("กรองตามยอดวิว", True),
                 ("กรองตาม keyword", True), ("ข้ามช่องที่ subscribe แล้ว", True),
             ], "บันทึกการตั้งค่า")),
            ((255, 245, 245), "ปลอดภัย\nควบคุมได้", "ลิมิตต่อชั่วโมง/ต่อวัน ทำงานต่อแม้ปิด popup",
             ["ลิมิตกันโดนตรวจจับบอท", "ไม่เก็บข้อมูลส่วนตัว", "ฟรี ใช้ได้ไม่จำกัด"],
             ("two", "ลิมิตความปลอดภัย", [
                 ("Sub/ชั่วโมง", "15"), ("Sub/วัน", "80"),
                 ("Like/ชั่วโมง", "50"), ("Like/วัน", "300"),
             ], "บันทึกการตั้งค่า")),
        ],
    },
    {
        "slug": "instagram-toolkit", "brand": "Instagram Toolkit",
        "accent": (225, 48, 108), "ico": ((247, 119, 55), (193, 53, 132)), "glyph": g_camera,
        "tabs": ["Follow", "Unfollow", "ตั้งค่า"],
        "sub": "follow · unfollow · กรอง",
        "shots": [
            ((253, 240, 245), "จัดการ Instagram\nอัตโนมัติ", "follow/unfollow ตามเงื่อนไข พร้อม Whitelist",
             ["follow จากผู้ติดตามบัญชีอื่น", "กรองเฉพาะ verified / keyword ใน bio", "unfollow คนที่ไม่ตามกลับ"],
             ("form", [("เป้าหมาย", "ผู้ติดตามของ @competitor"), ("ผู้ติดตามขั้นต่ำ", "1,000"),
                       ("จำนวนสูงสุด/รอบ", "20")], "Start Follow")),
            ((253, 242, 247), "Follow ตามเงื่อนไข\nที่ละเอียด", "เลือกเฉพาะบัญชีที่ตรงกลุ่มเป้าหมายจริง ๆ",
             ["เลือกเฉพาะบัญชี verified ได้", "มี keyword ใน bio", "ผู้ติดตามขั้นต่ำที่กำหนด"],
             ("toggles", "ตัวกรองบัญชี", [
                 ("เฉพาะบัญชี verified", False), ("มี keyword ใน bio", True),
                 ("ผู้ติดตามขั้นต่ำ 1,000", True), ("ข้ามบัญชีส่วนตัว (private)", True),
             ], "Start Follow")),
            ((253, 241, 246), "Unfollow คนที่\nไม่ Follow กลับ", "เก็บกวาด Following ให้สะอาด เลือก Non-mutual",
             ["เลือกเฉพาะคนที่ไม่ตามกลับ", "Whitelist รายชื่อที่ห้าม unfollow", "หน่วงเวลาแบบสุ่ม"],
             ("list", "Following ที่ไม่ตามกลับ", [
                 ("@user_one", "ไม่ตามกลับ · 2 เดือน", "Unfollow", (225, 48, 108)),
                 ("@brand_x", "ไม่ตามกลับ", "Unfollow", (225, 48, 108)),
                 ("@bestie", "อยู่ใน Whitelist", "ข้าม", GRAY),
             ])),
            ((253, 243, 248), "Whitelist\nกันลบผิดคน", "ใส่รายชื่อที่ห้าม unfollow ไม่ว่ากรณีใด",
             ["ใส่รายชื่อห้าม unfollow", "หน่วงเวลาแบบสุ่มเหมือนคนจริง", "ตั้งจำนวนต่อรอบได้"],
             ("form", [("Whitelist", "@bestie, @family, @work"), ("หน่วงเวลา (วินาที)", "10 – 25"),
                       ("จำนวน/รอบ", "20")], "บันทึกการตั้งค่า")),
            ((253, 244, 248), "ปลอดภัย\nควบคุมได้", "ลิมิตต่อชั่วโมง/ต่อวัน ทำงานต่อแม้ปิด popup",
             ["ลิมิตกันโดนตรวจจับบอท", "ไม่เก็บข้อมูลส่วนตัว", "ฟรี ใช้ได้ไม่จำกัด"],
             ("two", "ลิมิตความปลอดภัย", [
                 ("Follow/ชั่วโมง", "12"), ("Follow/วัน", "80"),
                 ("Unfollow/ชั่วโมง", "12"), ("Unfollow/วัน", "80"),
             ], "บันทึกการตั้งค่า")),
        ],
    },
    {
        "slug": "stock-alert", "brand": "Stock Alert",
        "accent": (217, 119, 6), "ico": ((251, 191, 36), (217, 119, 6)), "glyph": g_bell,
        "tabs": ["รายการ", "แจ้งเตือน", "ตั้งค่า"],
        "sub": "ติดตามราคา · สต็อก",
        "shots": [
            ((255, 248, 235), "แจ้งเตือนเมื่อ\nราคาลด · ของกลับมา", "ติดตามสินค้า Lazada/Shopee ไม่พลาดดีล",
             ["ตั้งราคาเป้าหมายต่อสินค้า", "เตือนเมื่อราคาถึงเกณฑ์", "เตือนเมื่อสินค้ากลับมามีสต็อก"],
             ("list", "สินค้าที่ติดตาม · 3 รายการ", [
                 ("หูฟัง TWS กันน้ำ", "เป้า ฿350 · ตอนนี้ ฿359", "ใกล้ถึง", AMBER),
                 ("เคสมือถือ", "เป้า ฿120 · ตอนนี้ ฿99", "ถึงแล้ว!", GREEN),
                 ("พาวเวอร์แบงค์", "หมดสต็อก", "รอของ", GRAY),
             ])),
            ((255, 249, 237), "ตั้งราคาเป้าหมาย\nต่อสินค้า", "กดเพิ่มจากหน้าสินค้า ตั้งราคาที่อยากให้เตือน",
             ["เพิ่มสินค้าได้ในคลิกเดียว", "ตั้งราคาเป้าหมายเอง", "ติดตามได้ไม่จำกัดรายการ"],
             ("form", [("สินค้า", "หูฟัง TWS กันน้ำ"), ("ราคาปัจจุบัน", "฿359"),
                       ("ราคาเป้าหมาย", "฿350")], "เพิ่มเข้ารายการติดตาม")),
            ((255, 247, 233), "เตือนทันที\nผ่าน Chrome", "ได้รับ notification ทันทีที่ถึงเกณฑ์ที่ตั้งไว้",
             ["แจ้งเตือนผ่าน Chrome ทันที", "เลือกประเภทการเตือนได้", "เตือนทั้งราคาและสต็อก"],
             ("toggles", "ประเภทการแจ้งเตือน", [
                 ("เตือนเมื่อราคาลดถึงเป้า", True), ("เตือนเมื่อมีโค้ดส่วนลด", True),
                 ("เตือนเมื่อกลับมามีสต็อก", True), ("เตือนเมื่อราคาขึ้น", False),
             ], "บันทึกการตั้งค่า")),
            ((255, 248, 236), "เช็คราคา\nอัตโนมัติเบื้องหลัง", "ตั้งความถี่การตรวจสอบ ทำงานเองแม้ไม่เปิดเว็บ",
             ["ตั้งความถี่การตรวจสอบเอง", "ทำงานเองเบื้องหลัง", "เก็บประวัติราคา 30 วัน"],
             ("two", "ความถี่การตรวจสอบ", [
                 ("ตรวจทุก", "30 นาที"), ("ช่วงเวลา", "08:00–23:00"),
                 ("จำนวนสินค้า", "ไม่จำกัด"), ("เก็บประวัติ", "30 วัน"),
             ], "บันทึกการตั้งค่า")),
            ((255, 250, 240), "ส่วนตัว\nและปลอดภัย", "เก็บรายการในเครื่อง ไม่ส่งข้อมูลออกนอก",
             ["ข้อมูลอยู่ในเครื่องคุณ", "ลบรายการได้ตลอดเวลา", "ฟรี ใช้ได้ไม่จำกัด"],
             ("list", "สินค้าที่ติดตาม", [
                 ("เคสมือถือ", "ถึงราคาเป้าแล้ว", "ถึงแล้ว!", GREEN),
                 ("หูฟัง TWS", "เป้า ฿350", "ใกล้ถึง", AMBER),
             ])),
        ],
    },
    {
        "slug": "social-analytics", "brand": "Social Analytics",
        "accent": (124, 58, 237), "ico": ((139, 92, 246), (109, 40, 217)), "glyph": g_chart,
        "tabs": ["ภาพรวม", "เทียบ", "ตั้งค่า"],
        "sub": "สถิติ · เทียบคู่แข่ง",
        "shots": [
            ((244, 240, 253), "ดูสถิติบัญชี\nแบบเรียลไทม์", "engagement rate · growth rate ในที่เดียว",
             ["ดูสถิติบัญชีตัวเองเรียลไทม์", "คำนวณ engagement rate ให้", "ติดตาม growth rate รายวัน"],
             ("stats", "ภาพรวม 7 วันล่าสุด", [
                 ("Engagement Rate", 0.72, "5.8%"), ("Growth Rate", 0.45, "+2.1%"),
                 ("Reach", 0.66, "48.2K"),
             ])),
            ((245, 242, 253), "Engagement Rate\nคำนวณให้อัตโนมัติ", "ไม่ต้องนั่งคิดเอง ระบบดึงตัวเลขมาคำนวณ",
             ["ER จาก like + comment + share", "เทียบกับค่าเฉลี่ยอุตสาหกรรม", "ดูโพสต์ที่ปังที่สุด"],
             ("stats", "Engagement แยกตามโพสต์", [
                 ("โพสต์รีวิวสินค้า", 0.88, "8.4%"), ("คลิปสั้น", 0.64, "6.1%"),
                 ("ภาพนิ่ง", 0.38, "3.6%"),
             ])),
            ((243, 240, 252), "เปรียบเทียบ\nกับคู่แข่ง", "ใส่บัญชีคู่แข่ง ดูว่าใครโตเร็วกว่ากัน",
             ["เทียบ follower / ER / ความถี่โพสต์", "เห็นช่องว่างที่ต้องไล่ตาม", "อัปเดตอัตโนมัติ"],
             ("list", "เทียบกับคู่แข่ง", [
                 ("บัญชีของคุณ", "ER 5.8% · โต +2.1%", "คุณ", (124, 58, 237)),
                 ("@competitor_a", "ER 4.2% · โต +1.4%", "ตามหลัง", GRAY),
                 ("@competitor_b", "ER 6.9% · โต +3.0%", "นำหน้า", RED),
             ])),
            ((245, 243, 253), "เลือกแพลตฟอร์ม\nที่อยากติดตาม", "รองรับหลายแพลตฟอร์ม เปิด-ปิดได้เอง",
             ["รองรับหลายแพลตฟอร์ม", "เปิด-ปิดได้เอง", "อัปเดตข้อมูลอัตโนมัติ"],
             ("toggles", "แพลตฟอร์มที่ติดตาม", [
                 ("Instagram", True), ("Facebook Page", True),
                 ("TikTok", True), ("X (Twitter)", False),
             ], "บันทึกการตั้งค่า")),
            ((246, 244, 253), "ส่วนตัว\nและปลอดภัย", "อ่านเฉพาะข้อมูลสาธารณะ ไม่ส่งออกนอกเครื่อง",
             ["อ่านข้อมูลสาธารณะเท่านั้น", "ไม่เก็บข้อมูลส่วนตัว", "ฟรี ใช้ได้ไม่จำกัด"],
             ("stats", "ภาพรวม 7 วันล่าสุด", [
                 ("Engagement Rate", 0.72, "5.8%"), ("Growth Rate", 0.45, "+2.1%"),
             ])),
        ],
    },
]

def render_content(d, p, kind_data, accent):
    kind = kind_data[0]
    if kind == "form":
        draw_form(d, p, kind_data[1], kind_data[2], accent)
    elif kind == "two":
        draw_two_col_form(d, p, kind_data[1], kind_data[2], kind_data[3], accent)
    elif kind == "list":
        draw_list(d, p, kind_data[1], kind_data[2], accent)
    elif kind == "toggles":
        draw_toggles(d, p, kind_data[1], kind_data[2], kind_data[3], accent)
    elif kind == "stats":
        draw_stats(d, p, kind_data[1], kind_data[2], accent)

for ext in EXTS:
    make_icon(ext["slug"], ext["ico"][0], ext["ico"][1], ext["glyph"])
    accent = ext["accent"]; tabs = ext["tabs"]
    for i, shot in enumerate(ext["shots"], 1):
        bg, title, sub, bullets, content = shot[0], shot[1], shot[2], shot[3], shot[4]
        if not isinstance(bullets, list):  # guard against accidental tuple
            bullets = ["ใช้งานง่าย", "ปลอดภัย", "ฟรี"]
        img, d = frame(bg, ext["brand"], accent, title, sub, bullets)
        active = min(i - 1, len(tabs) - 1)
        # choose active tab heuristically: shot 4 -> settings, etc.
        active = {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}.get(i, 0)
        if len(tabs) == 3 and content[0] in ("toggles", "two") and i in (4, 5):
            active = 2
        p = popup_shell(d, ext["brand"], ext["sub"], accent, tabs, active)
        render_content(d, p, content, accent)
        img.save(os.path.join(OUT, f"{ext['slug']}-ss-{i}.png"))
        print(f"OK {ext['slug']}-ss-{i}.png")

print("\nDONE -> images/")
