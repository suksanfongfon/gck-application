# GCK Chrome Extension — Project Instructions

## Overview

เว็บไซต์ศูนย์รวม Chrome Extension ภายใต้แบรนด์ **GCK Chrome Extension**
เป็น **static site** (HTML/CSS/JS ล้วน) deploy บน **GitHub Pages**

- **Live URL:** https://suksanfongfon.github.io/gck-application/
- **GitHub repo:** https://github.com/suksanfongfon/gck-application
- **Facebook Page:** https://www.facebook.com/GCKApplication
- **Contact email:** suksan.cmu@gmail.com

---

## 🔄 Standard Workflow — สร้าง Extension ใหม่ทุกตัว

ทำตามลำดับนี้ทุกครั้ง ห้ามข้ามขั้น:

### ขั้นที่ 1 — Idea & เพิ่มในเว็บ
- [ ] กำหนดชื่อ, ฟีเจอร์หลัก, กลุ่มเป้าหมาย
- [ ] เพิ่มการ์ด **"เร็ว ๆ นี้"** ใน `index.html` (section `#extensions`)
- [ ] เพิ่มการ์ด **feature** ใน Roadmap section (`index.html`)
- [ ] `git push` → เว็บอัปเดต

### ขั้นที่ 2 — สร้าง Extension
- [ ] สร้างโฟลเดอร์ใน `/Users/suksanfongfon/<ชื่อ Extension>/`
- [ ] เขียนไฟล์ครบ: `manifest.json`, `popup.html/css/js`, `background.js`, `content.js`
- [ ] ตรวจ `description` ใน manifest ≤ **132 ตัวอักษร**
- [ ] โหลดทดสอบใน Chrome (`chrome://extensions` → Load unpacked)

### ขั้นที่ 3 — Icon + ภาพตัวอย่าง 5 ภาพ
- [ ] เขียน `generate_icons.py` สร้าง icon 4 ขนาด (16/48/128/512)
- [ ] รัน `python3 generate_icons.py` ได้ `icons/` ครบ
- [ ] สร้าง store screenshots 5 ภาพ (1280×800) — แต่ละภาพมี:
  - พื้นหลังสีอ่อน + mockup popup ด้านขวา
  - หัวข้อใหญ่ภาษาไทยด้านซ้าย
  - bullet points อธิบายฟีเจอร์ 3 ข้อ
  - ใช้ Python (`make_screenshots.py`) หรือ Canva ก็ได้
- [ ] คัดลอก icon และ screenshots ไปที่ `Website chrome extension/images/`
- [ ] อัปเดตการ์ดในเว็บจาก "เร็ว ๆ นี้" → **"พร้อมใช้งาน"** + icon จริง
- [ ] สร้างหน้ารายละเอียด `ชื่อ-extension.html` ครบ (features, screenshots, วิธีติดตั้ง)
- [ ] `git push`

### ขั้นที่ 4 — รอทดสอบ ✋ (หยุดรอ owner)
> **หยุดรอ** ให้ owner ทดลองใช้งานจริง แล้วแจ้งผลหรือสิ่งที่ต้องแก้ไข
> ห้าม proceed ไปขั้น 5 โดยไม่ได้รับ OK จาก owner

- รับ feedback → แก้ code และอัปเดตเว็บตามที่แจ้ง
- ทำซ้ำจนกว่า owner จะบอกว่า "ผ่าน" หรือ "OK"

### ขั้นที่ 5 — เตรียม Deploy (Chrome Web Store)
เมื่อได้รับ "ผ่าน" จาก owner แล้วเท่านั้น:

- [ ] **ZIP:** `cd <extension folder> && zip -r -X ../ชื่อ-extension-vX.X.X.zip . -x ".claude/*" ".DS_Store" "*/.DS_Store"`
- [ ] ตรวจ description อีกครั้ง ≤ 132 ตัวอักษร
- [ ] เตรียม **Store listing** (อยู่ใน `STORE_LISTING.md` ในโฟลเดอร์ extension):
  - ชื่อ (≤ 45 chars)
  - Short description (≤ 132 chars) = manifest description
  - Long description (ภาษาไทย + ฟีเจอร์ครบ)
  - Screenshots 5 ภาพ (1280×800 หรือ 640×400)
  - Icon 128px
- [ ] เตรียม **Privacy Practices** justification ทุก permission:
  - Single purpose description
  - Justification สำหรับ `storage`, `tabs`, host permissions, remote code
  - Data use certifications (checkbox ทั้งหมด)
- [ ] Privacy Policy URL: `https://suksanfongfon.github.io/gck-application/privacy.html`
- [ ] อัปเดต `privacy.html` ให้มีตารางสิทธิ์ของ extension ตัวใหม่
- [ ] อัปเดต `CLAUDE.md` — เพิ่มชื่อ extension และโฟลเดอร์ในตาราง

---

## Folder Structure

```
/Users/suksanfongfon/
├── Website chrome extension/     ← เว็บไซต์ (repo นี้)
│   ├── index.html                  หน้าแรก — hub ส่วนขยายทั้งหมด
│   ├── x-toolkit.html              หน้ารายละเอียด X Toolkit
│   ├── lazada-product-finder.html  หน้ารายละเอียด Lazada Product Finder
│   ├── shopee-product-finder.html  หน้ารายละเอียด Shopee Product Finder
│   ├── tiktok-toolkit.html         หน้ารายละเอียด TikTok Toolkit
│   ├── twitter-video-grabber.html  หน้ารายละเอียด Twitter Video Grabber
│   ├── usage.html                  วิธีใช้งาน
│   ├── faq.html                    คำถามที่พบบ่อย
│   ├── privacy.html                นโยบายความเป็นส่วนตัว (ครบทุก extension)
│   ├── css/style.css               สไตล์ทั้งหมด (CSS variables ที่ :root)
│   ├── js/main.js                  เมนูมือถือ, FAQ accordion, ปีอัตโนมัติ
│   ├── images/                     icon + screenshots ของแต่ละ extension
│   └── downloads/                  ไฟล์ดาวน์โหลด (ตอนนี้ว่าง)
│
├── chrom extendion 2/            ← X Toolkit extension source
├── Lazada/                       ← Lazada Product Finder extension source
├── Shopee Product Finder/        ← Shopee Product Finder extension source
├── TikTok Toolkit/               ← TikTok Toolkit extension source
└── Chrome extension/             ← Twitter Video Grabber extension source
```

---

## Extensions ที่มีอยู่

| ชื่อ | Version | สถานะ | โฟลเดอร์ | หน้าเว็บ |
|------|---------|--------|----------|----------|
| X Toolkit | 1.1.0 | พร้อมใช้งาน | `chrom extendion 2/` | `x-toolkit.html` |
| Lazada Product Finder | 2.0.0 | พร้อมใช้งาน | `Lazada/` | `lazada-product-finder.html` |
| Shopee Product Finder | 1.0.0 | พร้อมใช้งาน | `Shopee Product Finder/` | `shopee-product-finder.html` |
| TikTok Toolkit | 1.0.0 | พร้อมใช้งาน | `TikTok Toolkit/` | `tiktok-toolkit.html` |
| Twitter Video Grabber | 4.0.0 | พร้อมใช้งาน | `Chrome extension/` | `twitter-video-grabber.html` |

> หมายเหตุ: "พร้อมใช้งาน" = มีการ์ด + หน้ารายละเอียดในเว็บแล้ว — ปุ่ม "เพิ่มลงใน Chrome" ยัง `href="#"` รอลิงก์ Chrome Web Store จริง

### Extension ที่อยู่ใน Roadmap (ยังไม่ได้สร้าง)
- Price Compare (Lazada + Shopee + JD Central)
- Facebook Toolkit
- YouTube Toolkit
- Instagram Toolkit
- Stock Alert
- Social Analytics

---

## Brand & Design

- **Brand colors:** `--brand: #4f46e5` (indigo), `--accent: #06b6d4` (cyan)
- **Font:** IBM Plex Sans Thai (Google Fonts)
- **Logo mark:** ตัวอักษร "G" บนพื้นสีน้ำเงิน-ฟ้า
- **Language:** ภาษาไทยทั้งหมด
- **Responsive:** รองรับมือถือ (hamburger menu ที่ < 880px)

### CSS Variables (แก้ที่ `css/style.css` → `:root`)
```css
--brand: #4f46e5;
--brand-dark: #4338ca;
--brand-light: #eef2ff;
--accent: #06b6d4;
```

---

## การเพิ่ม Extension ใหม่

### 1. เพิ่มการ์ดใน index.html

**พร้อมใช้งาน:**
```html
<div class="ext-card">
  <div class="ext-card-head">
    <div class="ext-icon has-img">
      <img src="images/ชื่อ-extension.png" alt="ชื่อ" />
    </div>
    <span class="status ready">พร้อมใช้งาน</span>
  </div>
  <h3>ชื่อ Extension</h3>
  <p>คำอธิบาย</p>
  <a href="ชื่อ-extension.html" class="btn btn-primary">ดูรายละเอียด &amp; ติดตั้ง →</a>
</div>
```

**เร็ว ๆ นี้:**
```html
<div class="ext-card is-soon">
  <div class="ext-card-head">
    <div class="ext-icon">🎯</div>
    <span class="status soon">เร็ว ๆ นี้</span>
  </div>
  <h3>ชื่อ Extension</h3>
  <p>คำอธิบาย</p>
  <span class="btn btn-disabled">เร็ว ๆ นี้</span>
</div>
```

### 2. สร้างหน้ารายละเอียด

ก็อปจาก `lazada-product-finder.html` แล้วแก้:
- ชื่อ/icon/version/คำอธิบาย
- feature cards (6 ใบ)
- screenshots (ใส่ใน `images/`)
- วิธีติดตั้ง

### 3. เพิ่ม icon และ screenshots

```bash
cp path/to/icon128.png images/ชื่อ-extension.png
cp path/to/screenshot*.png images/ชื่อ-extension-ss-*.png
```

---

## Deploy ขึ้น GitHub Pages

```bash
cd "/Users/suksanfongfon/Website chrome extension"
git add -A
git commit -m "คำอธิบาย"
git push
```

GitHub Pages จะ rebuild อัตโนมัติภายใน ~1 นาที

---

## Extension Development Conventions

### Folder structure ของแต่ละ extension
```
ExtensionName/
├── manifest.json      MV3, name ≤ 45 chars, description ≤ 132 chars
├── popup.html
├── popup.css
├── popup.js
├── background.js      service worker
├── content.js         inject บนหน้าเว็บเป้าหมาย
├── generate_icons.py  สร้าง icon ด้วย Pillow
└── icons/
    ├── icon16.png
    ├── icon48.png
    ├── icon128.png
    └── icon512.png    (สำหรับ Chrome Web Store)
```

### Chrome Web Store requirements
- `description` ใน manifest: **≤ 132 ตัวอักษร**
- Privacy Policy URL: `https://suksanfongfon.github.io/gck-application/privacy.html`
- ต้องระบุ justification สำหรับทุก permission ใน Privacy Practices tab
- ไม่ใช้ Remote Code (ทุก script เป็น local file เท่านั้น)

### บริการรับทำ Chrome Extension
- ราคาเริ่มต้น **1,000 บาท**
- ติดต่อผ่าน Facebook: https://www.facebook.com/GCKApplication

---

## Dev Server (local)

เปิดในเครื่องก่อน push:
```bash
cd "/Users/suksanfongfon/Website chrome extension"
python3 -m http.server 8000
# เปิด http://localhost:8000
```

หรือใช้ `.claude/launch.json` ผ่าน preview_start tool

---

## Notes

- อีเมลทุกหน้าต้องเป็น `suksan.cmu@gmail.com`
- Footer ทุกหน้ามี Facebook Page link
- `privacy.html` ครอบคลุมทุก extension ภายใต้ GCK — เมื่อเพิ่ม extension ใหม่ให้อัปเดตตารางสิทธิ์ในหน้านั้นด้วย
- ปุ่ม Chrome Web Store ปัจจุบันยัง `href="#"` — เมื่อได้ลิงก์จริงให้เปลี่ยนทุกจุดใน HTML ที่เกี่ยวข้อง
