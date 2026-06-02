# GCK Application — เว็บไซต์ศูนย์รวม Chrome Extension (ภาษาไทย)

เว็บไซต์ static (HTML/CSS/JS ล้วน) เป็น **ศูนย์รวม (hub) ส่วนขยาย Chrome หลายตัว** ภายใต้แบรนด์ GCK Application ออกแบบให้ deploy บน **GitHub Pages** ได้ทันที ไม่ต้อง build

## 📂 โครงสร้างไฟล์

```
.
├── index.html       # หน้าแรก (Landing)
├── usage.html       # วิธีใช้งาน
├── faq.html         # คำถามที่พบบ่อย
├── privacy.html     # นโยบายความเป็นส่วนตัว
├── css/style.css    # สไตล์ทั้งหมด (แก้สีแบรนด์ที่ :root)
├── js/main.js       # เมนูมือถือ + FAQ accordion
├── .nojekyll        # บอก GitHub Pages ไม่ต้องประมวลผลด้วย Jekyll
└── README.md
```

## ✏️ สิ่งที่ต้องแก้ก่อนใช้งานจริง

ค้นหาและแทนที่ข้อความเหล่านี้ในไฟล์ `.html`:

| ข้อความ placeholder | แทนที่ด้วย |
|---|---|
| `ส่วนขยายตัวที่ 1/2/3` | ชื่อ extension จริงแต่ละตัว (ใน `index.html`) |
| `you@example.com` | อีเมลซัพพอร์ตของคุณ |
| `href="#"` (ปุ่มเพิ่มลงใน Chrome) | ลิงก์ Chrome Web Store ของแต่ละ extension |
| `G` (โลโก้) | ใส่ไฟล์โลโก้จริง หรือ emoji อื่น |

### ➕ วิธีเพิ่ม extension ตัวใหม่

ใน `index.html` ส่วน `<section id="extensions">` ให้ก็อปบล็อก `<div class="ext-card">…</div>`
แล้วแก้ไอคอน ชื่อ คำอธิบาย และลิงก์ปุ่ม สถานะใช้ `class="status ready"` (พร้อมใช้งาน)
หรือ `class="status soon"` (เร็ว ๆ นี้) สำหรับการ์ดที่ยังไม่เปิดให้ใช้ ใส่ `class="ext-card is-soon"`

> เคล็ดลับ: หน้า `usage.html` (ฟีเจอร์ที่ 1–3) และ `privacy.html` เป็น template กลาง —
> แก้เนื้อหาให้ตรงกับส่วนขยายจริง

- **เปลี่ยนสีแบรนด์:** แก้ตัวแปรที่ `:root` ในไฟล์ [css/style.css](css/style.css) (เช่น `--brand`)
- **ใส่ภาพหน้าจอจริง:** แทนที่ `.browser-mock` ใน `index.html` ด้วย `<img>` (วางไฟล์ในโฟลเดอร์ `images/`)

## 🚀 วิธี Deploy ขึ้น GitHub Pages

1. สร้าง repository ใหม่บน GitHub แล้ว push โค้ดนี้ขึ้นไป:
   ```bash
   git init
   git add .
   git commit -m "เว็บไซต์เผยแพร่ Chrome extension"
   git branch -M main
   git remote add origin https://github.com/<username>/<repo>.git
   git push -u origin main
   ```
2. ไปที่ repo บน GitHub → **Settings** → **Pages**
3. ที่หัวข้อ **Source** เลือก **Deploy from a branch**
4. เลือก Branch = `main`, Folder = `/ (root)` แล้วกด **Save**
5. รอสักครู่ เว็บจะออนไลน์ที่ `https://<username>.github.io/<repo>/`

### ใช้โดเมนตัวเอง (ไม่บังคับ)
สร้างไฟล์ชื่อ `CNAME` (ไม่มีนามสกุล) ใส่ชื่อโดเมน เช่น `www.example.com`
แล้วตั้งค่า DNS ตามคู่มือของ GitHub Pages

## 🔍 ทดสอบในเครื่องก่อน deploy

เปิดไฟล์ `index.html` ด้วยเบราว์เซอร์ได้เลย หรือรันเซิร์ฟเวอร์ในเครื่อง:

```bash
python3 -m http.server 8000
# เปิด http://localhost:8000
```
