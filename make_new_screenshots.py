"""สร้าง store screenshots 1280x800 สำหรับ Shopee Product Finder + Twitter Video Grabber
ใส่ลงในโฟลเดอร์ images/ ของเว็บโดยตรง — python3 make_new_screenshots.py"""
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

# ── promo frame ──────────────────────────────────────────────────────────────
def frame(bg, brand, accent, title, subtitle, bullets):
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    # brand chip top-left
    chip_w = 60 + d.textlength(brand, font=font(14, True))
    rr(d, [32, 28, 32 + chip_w, 60], 16, fill=accent)
    d.ellipse([46, 36, 62, 52], fill=WHITE)
    d.text((72, 35), brand, fill=WHITE, font=font(14, True))
    # title (left)
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
    px, pw, ph = W - 360 - 50, 360, 480
    py = (H - ph) // 2
    shadow(d, px, py, pw, ph)
    rr(d, [px, py, px + pw, py + ph], 14, fill=WHITE)
    # header
    rr(d, [px, py, px + pw, py + 58], 14, fill=DARK)
    d.rectangle([px, py + 44, px + pw, py + 58], fill=DARK)
    d.ellipse([px + 16, py + 18, px + 40, py + 42], fill=accent)
    d.text((px + 50, py + 14), title, fill=WHITE, font=font(14, True))
    d.text((px + 50, py + 33), sub, fill=(170, 175, 185), font=font(10))
    # tab bar
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

# ── Shopee product card ──────────────────────────────────────────────────────
def product_card(d, x, y, w, name, price, disc, rating, sold, score, tier):
    h = 76
    rr(d, [x, y, x + w, y + h], 9, fill=SOFT, outline=BORDER)
    d.text((x + 12, y + 10), name, fill=DARK, font=font(12, True))
    # score badge
    tcol = {"hot": (239, 68, 68), "mid": (245, 158, 11), "low": (107, 114, 128)}[tier]
    bw = 34
    rr(d, [x + w - bw - 12, y + 9, x + w - 12, y + 29], 6, fill=tcol)
    d.text((x + w - bw // 2 - 12, y + 19), str(score), fill=WHITE, font=font(11, True), anchor="mm")
    # chips
    cx = x + 12; cy = y + 40
    def chip(txt, col):
        nonlocal cx
        tl = d.textlength(txt, font=font(10)) + 14
        rr(d, [cx, cy, cx + tl, cy + 22], 11, fill=col)
        d.text((cx + 7, cy + 5), txt, fill=WHITE, font=font(10)); cx += tl + 6
    chip(f"B{price}", (37, 99, 235))
    if disc: chip(f"-{disc}%", (220, 38, 38))
    chip(f"* {rating}", (217, 119, 6))
    chip(f"ขาย {sold}", (5, 150, 105))
    return y + h + 10

os.makedirs(OUT, exist_ok=True)

# ============================================================================
# SHOPEE PRODUCT FINDER — 5 screenshots
# ============================================================================
SHOPEE_ACCENT = (238, 77, 45)  # shopee orange
S_TABS = ["ค้นหา", "ผลลัพธ์", "ตั้งค่า"]

def shopee_search(d):
    px, py, pw, ph = popup_shell(d, "Shopee Product Finder", "ค้นหา · กรอง · export", SHOPEE_ACCENT, S_TABS, 0)
    x, w = px + 14, pw - 28; y = py + 102
    y = label(d, x, y, "Keyword"); y = inp(d, x, y, w, "หูฟังบลูทูธ")
    y = label(d, x, y, "ความลึกการค้นหา"); y = inp(d, x, y, w, "600 สินค้า")
    y += 4
    half = (w - 10) // 2
    label(d, x, y, "รีวิวขั้นต่ำ"); inp(d, x, y + 16, half, "100")
    label(d, x + half + 10, y, "ยอดขายขั้นต่ำ"); inp(d, x + half + 10, y + 16, half, "500"); y += 52
    label(d, x, y, "เรตติ้งขั้นต่ำ"); inp(d, x, y + 16, half, "4.5")
    label(d, x + half + 10, y, "ส่วนลดขั้นต่ำ %"); inp(d, x + half + 10, y + 16, half, "20"); y += 56
    btn(d, x, y, w, "ค้นหาสินค้า", SHOPEE_ACCENT)

def shopee_results(d):
    px, py, pw, ph = popup_shell(d, "Shopee Product Finder", "ค้นหา · กรอง · export", SHOPEE_ACCENT, S_TABS, 1)
    x, w = px + 14, pw - 28; y = py + 100
    label(d, x, y, "เรียงตาม: น่าขายมากสุด  ·  142 สินค้า"); y += 22
    y = product_card(d, x, y, w, "หูฟังบลูทูธ TWS กันน้ำ", "359", 45, "4.9", "12k", 98, "hot")
    y = product_card(d, x, y, w, "หูฟังเกมมิ่ง RGB", "590", 30, "4.7", "3.4k", 81, "mid")
    y = product_card(d, x, y, w, "หูฟังครอบหู wireless", "1,290", 18, "4.6", "980", 64, "low")

def shopee_compare(d):
    px, py, pw, ph = popup_shell(d, "Shopee Product Finder", "ค้นหา · กรอง · export", SHOPEE_ACCENT, S_TABS, 1)
    x, w = px + 14, pw - 28; y = py + 100
    label(d, x, y, "เรียงตาม: ขายพุ่ง (เทียบครั้งก่อน)"); y += 22
    rr(d, [x, y, x + w, y + 86], 9, fill=(236, 253, 245), outline=(167, 243, 208))
    d.text((x + 12, y + 10), "หูฟังบลูทูธ TWS กันน้ำ", fill=DARK, font=font(12, True))
    d.text((x + 12, y + 32), "ยอดขาย  8,200  ->  12,400", fill=(5, 150, 105), font=font(12, True))
    d.text((x + 12, y + 52), "ราคา  ฿399  ->  ฿359  (ลดลง)", fill=(220, 38, 38), font=font(11))
    rr(d, [x + w - 70, y + 10, x + w - 12, y + 32], 6, fill=(5, 150, 105))
    d.text((x + w - 41, y + 21), "+51%", fill=WHITE, font=font(11, True), anchor="mm")
    y += 96
    y = product_card(d, x, y, w, "หูฟังเกมมิ่ง RGB", "590", 30, "4.7", "3.4k", 81, "mid")

def shopee_settings(d):
    px, py, pw, ph = popup_shell(d, "Shopee Product Finder", "ค้นหา · กรอง · export", SHOPEE_ACCENT, S_TABS, 2)
    x, w = px + 14, pw - 28; y = py + 102
    label(d, x, y, "คอลัมน์สำหรับ export"); y += 20
    cols = ["ชื่อสินค้า", "ราคา", "ส่วนลด %", "เรตติ้ง", "ยอดขาย", "คะแนนน่าขาย", "รายได้โดยประมาณ", "URL สินค้า"]
    for c in cols:
        rr(d, [x, y + 3, x + 16, y + 19], 4, fill=SHOPEE_ACCENT)
        d.line([x + 4, y + 11, x + 7, y + 15], fill=WHITE, width=2)
        d.line([x + 7, y + 15, x + 13, y + 6], fill=WHITE, width=2)
        d.text((x + 24, y + 2), c, fill=DARK, font=font(12)); y += 26
    y += 6
    btn(d, x, y, w, "บันทึกการตั้งค่า", SHOPEE_ACCENT)

shopee = [
    ((255, 245, 240), "ค้นหาสินค้า Shopee\nแบบมือโปร", "กรอง keyword + เงื่อนไข แล้วเจอของน่าขายใน 1 คลิก",
     ["ค้นได้ลึกถึงดึงจนสุด", "กรอง 4 เงื่อนไข: รีวิว ยอดขาย เรตติ้ง ส่วนลด", "เจาะเฉพาะของที่ขายดีจริง"], shopee_search),
    ((255, 248, 243), "รู้ทันทีว่า\nตัวไหนน่าขาย", "ระบบให้คะแนน \"น่าขาย\" และเรียงให้อัตโนมัติ",
     ["คะแนนน่าขาย 0-100", "เรียง 9 แบบ: ลดราคา รายได้ ยอดขาย", "เห็นราคา ส่วนลด เรตติ้ง ครบในใบเดียว"], shopee_results),
    ((240, 253, 247), "ติดตามคู่แข่ง\nอัตโนมัติ", "ค้น keyword เดิมซ้ำ ระบบเทียบให้ว่าอะไรขายพุ่ง",
     ["เทียบราคา/ยอดขายกับครั้งก่อน", "จับเทรนด์ \"ขายพุ่ง\" ก่อนใคร", "เก็บประวัติในเครื่อง ลบได้ตลอด"], shopee_compare),
    ((243, 249, 255), "Export ไป\nGoogle Sheets / CSV", "เลือกคอลัมน์ที่ต้องการ คัดลอกหรือดาวน์โหลดได้เลย",
     ["เลือก export ได้ 10 คอลัมน์", "คัดลอก TSV วางใน Sheets ทันที", "ดาวน์โหลด CSV เปิดใน Excel"], shopee_settings),
    ((255, 252, 240), "เร็ว · แม่นยำ\n· ปลอดภัย", "อ่านเฉพาะข้อมูลสาธารณะบน Shopee ไม่ส่งออกนอกเครื่อง",
     ["ทำงานบน shopee.co.th เท่านั้น", "ไม่เก็บข้อมูลส่วนตัว", "ฟรี ใช้ได้ไม่จำกัด"], shopee_results),
]
for i, (bg, t, s, bl, draw) in enumerate(shopee, 1):
    img, d = frame(bg, "Shopee Product Finder", SHOPEE_ACCENT, t, s, bl)
    draw(d)
    img.save(os.path.join(OUT, f"shopee-ss-{i}.png"))
    print(f"OK shopee-ss-{i}.png")

# ============================================================================
# TWITTER VIDEO GRABBER — 5 screenshots
# ============================================================================
TW_ACCENT = (29, 155, 240)  # twitter blue
TW_DARK   = (15, 20, 25)

def tw_popup(d, active, rows_fn):
    px, pw, ph = W - 340 - 50, 340, 470
    py = (H - ph) // 2
    shadow(d, px, py, pw, ph)
    rr(d, [px, py, px + pw, py + ph], 14, fill=WHITE)
    rr(d, [px, py, px + pw, py + 60], 14, fill=TW_DARK)
    d.rectangle([px, py + 46, px + pw, py + 60], fill=TW_DARK)
    d.text((px + 18, py + 16), "Video Grabber", fill=WHITE, font=font(15, True))
    # badge count
    rr(d, [px + pw - 54, py + 16, px + pw - 18, py + 40], 12, fill=TW_ACCENT)
    d.text((px + pw - 36, py + 28), "3", fill=WHITE, font=font(13, True), anchor="mm")
    rows_fn(d, px, py, pw)

def video_row(d, x, y, w, res, kind, kcol):
    rr(d, [x, y, x + w, y + 56], 9, fill=SOFT, outline=BORDER)
    rr(d, [x + 10, y + 12, x + 56, y + 44], 6, fill=(209, 213, 219))
    d.polygon([(x + 27, y + 20), (x + 27, y + 36), (x + 41, y + 28)], fill=WHITE)
    d.text((x + 68, y + 12), res, fill=DARK, font=font(13, True))
    rr(d, [x + 68, y + 32, x + 68 + d.textlength(kind, font=font(10)) + 14, y + 50], 9, fill=kcol)
    d.text((x + 75, y + 35), kind, fill=WHITE, font=font(10))
    rr(d, [x + w - 96, y + 16, x + w - 12, y + 42], 7, fill=TW_ACCENT)
    d.text((x + w - 54, y + 29), "ดาวน์โหลด", fill=WHITE, font=font(10, True), anchor="mm")

def tw_list(d, px, py, pw):
    x, w = px + 14, pw - 28; y = py + 78
    rr(d, [x, y, x + w, y + 30], 7, fill=SOFT, outline=BORDER)
    d.text((x + 10, y + 8), "วาง URL ทวีต: x.com/.../status/...", fill=GRAY, font=font(10)); y += 42
    video_row(d, x, y, w, "1280x720", "MP4", (5, 150, 105)); y += 64
    video_row(d, x, y, w, "640x360", "MP4", (5, 150, 105)); y += 64
    video_row(d, x, y, w, "playlist", "HLS m3u8", (217, 119, 6))

def tw_search(d, px, py, pw):
    x, w = px + 14, pw - 28; y = py + 78
    rr(d, [x, y, x + w, y + 32], 7, fill=WHITE, outline=TW_ACCENT, width=2)
    d.text((x + 10, y + 9), "x.com/i/status/1789...", fill=DARK, font=font(11)); y += 44
    btn(d, x, y, w, "ค้นหาวิดีโอในทวีต", TW_ACCENT); y += 50
    label(d, x, y, "พบ 3 ความละเอียด"); y += 22
    video_row(d, x, y, w, "1280x720", "MP4", (5, 150, 105))

def tw_export(d, px, py, pw):
    x, w = px + 14, pw - 28; y = py + 78
    label(d, x, y, "รายการวิดีโอที่เจอในแท็บนี้"); y += 22
    for res, kind, kc in [("1280x720", "MP4", (5,150,105)), ("640x360", "MP4", (5,150,105))]:
        video_row(d, x, y, w, res, kind, kc); y += 64
    y += 4
    btn(d, x, y, w, "Export CSV", (5, 150, 105))

def tw_progress(d, px, py, pw):
    x, w = px + 14, pw - 28; y = py + 90
    d.text((x, y), "กำลังรวมไฟล์ HLS...", fill=DARK, font=font(13, True)); y += 28
    rr(d, [x, y, x + w, y + 16], 8, fill=SOFT, outline=BORDER)
    rr(d, [x, y, x + int(w * 0.66), y + 16], 8, fill=TW_ACCENT)
    d.text((x + w - 4, y - 2), "66%", fill=TW_ACCENT, font=font(11, True), anchor="ra"); y += 34
    d.text((x, y), "อย่าปิดหน้าต่างนี้ระหว่างดาวน์โหลด", fill=GRAY, font=font(11)); y += 30
    video_row(d, x, y, w, "1280x720", "MP4", (5, 150, 105))

twitter = [
    ((237, 245, 252), "ดาวน์โหลดวิดีโอ\nจาก Twitter / X", "วาง URL ทวีต แล้วกดดาวน์โหลดได้เลย ไม่ต้องพึ่งเว็บนอก",
     ["จับวิดีโอจากทวีตอัตโนมัติ", "เลือกความละเอียดที่ต้องการ", "ดาวน์โหลด MP4 ปุ่มเดียว"], tw_list),
    ((240, 248, 255), "วาง URL\nค้นหาทันที", "เปิดทวีตที่มีวิดีโอ หรือวางลิงก์ตรง ๆ ก็เจอ",
     ["รองรับทั้ง twitter.com และ x.com", "badge บอกจำนวนวิดีโอที่เจอ", "แยกรายการตามแท็บ"], tw_search),
    ((236, 250, 245), "เลือกความละเอียด\nที่คมที่สุด", "แต่ละวิดีโอมักมีหลายขนาด เลือกตัวใหญ่สุดได้",
     ["320p / 360p / 720p ครบ", "ไฟล์ MP4 ดาวน์โหลดตรง", "HLS m3u8 คัดลอกไปใช้ ffmpeg"], tw_progress),
    ((245, 248, 252), "Export รายการ\nเป็น CSV", "เก็บลิงก์วิดีโอทั้งหมดในแท็บไว้ใช้ต่อ",
     ["ชนิด ความละเอียด ลิงก์ เวลา", "เปิดใน Excel / Google Sheets", "ล้างรายการได้ในคลิกเดียว"], tw_export),
    ((250, 250, 245), "ส่วนตัว\nและปลอดภัย", "ทำงานในเครื่องของคุณ ไม่ส่งข้อมูลออกนอก",
     ["ไม่เก็บข้อมูลส่วนตัว", "ใช้เพื่อการส่วนตัว เคารพลิขสิทธิ์", "ฟรี ใช้ได้ไม่จำกัด"], tw_list),
]
for i, (bg, t, s, bl, rows_fn) in enumerate(twitter, 1):
    img, d = frame(bg, "Twitter Video Grabber", TW_ACCENT, t, s, bl)
    tw_popup(d, 0, rows_fn)
    img.save(os.path.join(OUT, f"twitter-video-grabber-ss-{i}.png"))
    print(f"OK twitter-video-grabber-ss-{i}.png")

print("\nDONE -> images/")
