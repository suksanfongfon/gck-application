# -*- coding: utf-8 -*-
"""สร้างหน้ารายละเอียด (landing page) สำหรับ extension ใน Roadmap 6 ตัว
สถานะ "เร็ว ๆ นี้ / กำลังพัฒนา" — โค้ด extension จริงจะตามมาทีหลังทีละตัว
python3 make_detail_pages.py"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FB = "https://www.facebook.com/GCKApplication"
EMAIL = "suksan.cmu@gmail.com"

PAGE = """<!DOCTYPE html>
<html lang="th">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} — GCK Chrome Extension</title>
    <meta name="description" content="{meta}" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="css/style.css" />
  </head>
  <body>
    <header class="site-header">
      <div class="container nav">
        <a href="index.html" class="logo">
          <span class="logo-mark">G</span>
          GCK Chrome Extension
        </a>
        <ul class="nav-links">
          <li><a href="index.html">หน้าแรก</a></li>
          <li><a href="index.html#extensions">ส่วนขยาย</a></li>
          <li><a href="usage.html">วิธีใช้งาน</a></li>
          <li><a href="faq.html">คำถามที่พบบ่อย</a></li>
          <li><a href="privacy.html">ความเป็นส่วนตัว</a></li>
          <li>
            <a href="#install" class="btn btn-primary" style="padding: 8px 18px">🔔 แจ้งเตือนเมื่อพร้อม</a>
          </li>
        </ul>
        <button class="nav-toggle" aria-label="เปิดเมนู">☰</button>
      </div>
    </header>

    <!-- Hero -->
    <section class="page-hero">
      <div class="container">
        <div style="display:flex;align-items:center;gap:20px;flex-wrap:wrap">
          <div class="ext-icon has-img" style="width:80px;height:80px;flex-shrink:0;box-shadow:var(--shadow-sm)">
            <img src="images/{slug}.png" alt="{title}" />
          </div>
          <div>
            <h1 style="margin-bottom:4px">{title}</h1>
            <p><span class="status soon">เร็ว ๆ นี้</span> กำลังพัฒนา • สำหรับ {target}</p>
          </div>
        </div>
        <p style="margin-top:18px;max-width:660px">
          {hero}
        </p>
        <div class="btn-row" style="margin-top:22px">
          <a href="{fb}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">🔔 แจ้งเตือนเมื่อพร้อม</a>
          <a href="#screenshots" class="btn btn-ghost btn-lg">ดูตัวอย่าง</a>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section style="padding-top:56px">
      <div class="container">
        <div class="section-head">
          <h2>ความสามารถ</h2>
          <p>{features_sub}</p>
        </div>
        <div class="features">
{features}
        </div>
      </div>
    </section>

    <!-- Screenshots -->
    <section id="screenshots" class="bg-soft">
      <div class="container">
        <div class="section-head">
          <h2>ตัวอย่างหน้าตา (ออกแบบไว้)</h2>
          <p>ภาพตัวอย่างดีไซน์ก่อนเปิดตัวจริง — หน้าตาจริงอาจปรับเปลี่ยนได้</p>
        </div>
        <div class="screenshot-gallery">
          <img src="images/{slug}-ss-1.png" alt="{title} ตัวอย่างที่ 1" />
          <img src="images/{slug}-ss-2.png" alt="{title} ตัวอย่างที่ 2" />
          <img src="images/{slug}-ss-3.png" alt="{title} ตัวอย่างที่ 3" />
          <img src="images/{slug}-ss-4.png" alt="{title} ตัวอย่างที่ 4" />
          <img src="images/{slug}-ss-5.png" alt="{title} ตัวอย่างที่ 5" />
        </div>
      </div>
    </section>

    <!-- How it works -->
    <section>
      <div class="container">
        <div class="section-head">
          <h2>วิธีใช้งาน (แผนการออกแบบ)</h2>
          <p>{steps_sub}</p>
        </div>
        <div class="steps">
{steps}
        </div>
        <div class="callout" style="max-width:780px;margin:32px auto 0">
          {callout}
        </div>
      </div>
    </section>

    <!-- Install / coming soon CTA -->
    <section id="install" class="bg-soft">
      <div class="container">
        <div class="service-band">
          <div>
            <span class="price-tag">🔔 กำลังพัฒนา</span>
            <h2>{title} กำลังจะมา เร็ว ๆ นี้</h2>
            <p>
              ส่วนขยายนี้อยู่ระหว่างพัฒนา กดติดตาม Facebook Page ของ GCK
              เพื่อรับแจ้งเตือนทันทีที่เปิดให้ติดตั้งบน Chrome Web Store
            </p>
          </div>
          <div class="service-band-actions">
            <a href="{fb}" target="_blank" rel="noopener noreferrer" class="btn btn-facebook btn-lg">
              💬 ติดตามเพื่อรับแจ้งเตือน
            </a>
            <a href="mailto:{email}" class="btn btn-ghost btn-lg"
              style="border-color:rgba(255,255,255,0.3);color:#fff">
              ✉️ อีเมล
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Permissions -->
    <article class="prose">
      <h2>สิทธิ์การเข้าถึงที่วางแผนจะใช้</h2>
      <ul>
{perms}
      </ul>
      <div class="callout">
        🔒 ส่วนขยายของ GCK ยึดหลัก <strong>ไม่ส่งข้อมูลออกนอกเครื่อง</strong>
        การตั้งค่าทั้งหมดเก็บใน <code>chrome.storage.local</code> และลบออกได้ตลอดเวลา
        อ่านนโยบายฉบับเต็มได้ที่ <a href="privacy.html">หน้านโยบายความเป็นส่วนตัว</a>
      </div>
{warning}
      <p style="margin-top:32px;color:var(--text-muted);font-size:0.9rem">
        {disclaimer}
      </p>
      <p style="margin-top:16px"><a href="index.html#extensions">← กลับไปดูส่วนขยายทั้งหมด</a></p>
    </article>

    <footer class="site-footer">
      <div class="container">
        <div class="footer-grid">
          <div>
            <div class="logo"><span class="logo-mark">G</span> GCK Chrome Extension</div>
            <p>ศูนย์รวมส่วนขยาย Chrome ภาษาไทยจาก GCK ที่ช่วยให้การทำงานบนเว็บของคุณง่ายและรวดเร็วยิ่งขึ้น</p>
          </div>
          <div class="footer-col">
            <h4>เมนู</h4>
            <ul>
              <li><a href="index.html">หน้าแรก</a></li>
              <li><a href="index.html#extensions">ส่วนขยาย</a></li>
              <li><a href="usage.html">วิธีใช้งาน</a></li>
              <li><a href="faq.html">คำถามที่พบบ่อย</a></li>
              <li><a href="privacy.html">นโยบายความเป็นส่วนตัว</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>ติดต่อ</h4>
            <ul>
              <li><a href="mailto:{email}">{email}</a></li>
              <li><a href="index.html#extensions">ส่วนขยายทั้งหมด</a></li>
              <li><a href="{fb}" target="_blank" rel="noopener noreferrer">Facebook Page</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">© <span data-year>2026</span> GCK Chrome Extension • สงวนลิขสิทธิ์</div>
      </div>
    </footer>
    <script src="js/main.js"></script>
  </body>
</html>
"""

def feature(icon, title, desc):
    return f"""          <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
          </div>"""

def step(num, title, desc):
    return f"""          <div class="step">
            <div class="step-num">{num}</div>
            <div>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>
          </div>"""

def perm(code, desc):
    return f"        <li><code>{code}</code> — {desc}</li>"

WARN = """      <div class="callout" style="margin-top:16px">
        ⚠️ {w}
      </div>"""

EXTS = [
    {
        "slug": "price-compare", "title": "Price Compare",
        "target": "หน้าสินค้า Lazada / Shopee / JD Central",
        "meta": "Price Compare: เปรียบเทียบราคาสินค้าแบบเรียลไทม์ข้ามแพลตฟอร์ม Lazada Shopee JD Central คลิกเดียวรู้ทันทีว่าที่ไหนถูกสุด",
        "hero": "เปรียบเทียบราคาสินค้าแบบเรียลไทม์ข้ามแพลตฟอร์ม — Lazada, Shopee และ JD Central "
                "เปิดหน้าสินค้าแล้วรู้ทันทีว่าร้านไหนถูกที่สุด รวมส่วนลดและคูปองในการคำนวณ "
                "พร้อมกราฟราคาย้อนหลังช่วยตัดสินใจว่าควรซื้อตอนนี้หรือรอ",
        "features_sub": "ออกแบบสำหรับนักช้อปและพ่อค้าแม่ค้าออนไลน์ที่อยากได้ของถูกที่สุดโดยไม่ต้องเปิดหลายแท็บเทียบเอง",
        "features": [
            ("🔍", "ดึงราคา 3 แพลตฟอร์ม", "เปิดหน้าสินค้าแล้วระบบดึงราคาจาก Lazada, Shopee และ JD Central มาเทียบให้แบบเรียลไทม์"),
            ("🏆", "ไฮไลต์ร้านที่ถูกสุด", "จัดอันดับราคาจากถูกไปแพง พร้อมไฮไลต์ร้านที่คุ้มที่สุดให้เห็นชัดในคลิกเดียว"),
            ("🎟️", "รวมส่วนลด / คูปอง", "คำนวณราคาสุทธิหลังหักโค้ดส่วนลดและค่าส่ง ไม่ใช่แค่ราคาป้าย"),
            ("📉", "กราฟราคาย้อนหลัง", "เก็บประวัติราคาในเครื่อง ดูกราฟ 30 วันย้อนหลังว่าตอนนี้ถูกจริงหรือแค่ป้ายลดหลอกตา"),
            ("🔔", "เตือนเมื่อราคาต่ำกว่าค่าเฉลี่ย", "บอกทันทีเมื่อราคาปัจจุบันต่ำกว่าค่าเฉลี่ยที่ผ่านมา จังหวะเหมาะที่จะซื้อ"),
            ("🔒", "ทำงานในเครื่องคุณ", "อ่านเฉพาะหน้าสินค้าที่คุณเปิด ไม่ส่งข้อมูลออกนอกเครื่อง และไม่เก็บข้อมูลส่วนตัว"),
        ],
        "steps_sub": "เปิดหน้าสินค้าแล้วคลิกไอคอน ใช้งานได้ทันที",
        "steps": [
            ("①", "เปิดหน้าสินค้าที่สนใจ", "เปิดหน้าสินค้าบน Lazada, Shopee หรือ JD Central ตามปกติ"),
            ("②", "คลิกไอคอน Price Compare", "ระบบจะค้นหาสินค้าเดียวกันบนแพลตฟอร์มอื่นและดึงราคามาเทียบให้อัตโนมัติ"),
            ("③", "ดูร้านที่ถูกที่สุด", "เห็นราคาสุทธิหลังหักโค้ดของแต่ละร้าน เรียงจากถูกไปแพง พร้อมลิงก์ไปซื้อ"),
            ("④", "ติดตามราคาย้อนหลัง", "เปิดแท็บประวัติเพื่อดูกราฟราคา 30 วัน และตั้งให้เตือนเมื่อราคาลด"),
        ],
        "callout": "💡 เทียบราคาสุทธิหลังหักโค้ดเสมอ บางร้านราคาป้ายสูงกว่าแต่มีคูปองทำให้ถูกกว่าจริง",
        "perms": [
            ("storage", "บันทึกการตั้งค่าและประวัติราคาในเครื่อง"),
            ("tabs", "ตรวจสอบหน้าสินค้าที่เปิดอยู่เพื่อค้นหาสินค้าเดียวกันบนแพลตฟอร์มอื่น"),
            ("host: lazada.co.th, shopee.co.th, jd.co.th", "อ่านชื่อและราคาสินค้าที่ปรากฏบนหน้าเว็บเท่านั้น"),
        ],
        "warning": "",
        "disclaimer": "ส่วนขยายนี้เป็นเครื่องมือของบุคคลที่สาม ไม่ได้เกี่ยวข้องหรือได้รับการรับรองจาก Lazada, Shopee หรือ JD Central",
    },
    {
        "slug": "facebook-toolkit", "title": "Facebook Toolkit",
        "target": "facebook.com",
        "meta": "Facebook Toolkit: จัดการ Facebook อัตโนมัติ — follow/unfollow เพจและคน ไลก์/คอมเมนต์ตามเงื่อนไข พร้อมลิมิตต่อชั่วโมง/ต่อวัน",
        "hero": "เครื่องมือจัดการ Facebook อัตโนมัติ — follow/unfollow เพจและคนตามเงื่อนไข "
                "ไลก์โพสต์ในฟีดตามเกณฑ์ ตั้งหน่วงเวลาแบบสุ่มเหมือนคนจริง "
                "และคุมความเสี่ยงด้วยลิมิตต่อชั่วโมง/ต่อวัน ทำงานต่อแม้ปิด popup",
        "features_sub": "ออกแบบสำหรับแอดมินเพจและนักการตลาดที่อยากโตบน Facebook โดยไม่ต้องนั่งกดเอง",
        "features": [
            ("➕", "Follow อัตโนมัติตามเงื่อนไข", "เปิดหน้าผู้ติดตามเพจอื่นหรือผลค้นหา แล้วกด Start ระบบกดติดตามให้ พร้อม Whitelist"),
            ("🧹", "Unfollow คนที่ไม่ Follow กลับ", "เก็บกวาดรายการติดตามให้สะอาด เลือกเฉพาะคนที่ไม่ติดตามกลับ"),
            ("❤️", "ไลก์โพสต์ตามเกณฑ์", "ไลก์เฉพาะโพสต์ในฟีดที่ผ่านคำค้น ข้ามโพสต์โฆษณา และเลื่อนฟีดต่อให้อัตโนมัติ"),
            ("⏱️", "หน่วงเวลาแบบสุ่ม", "ตั้งช่วงหน่วงเวลา min–max วินาที ระบบสุ่มจังหวะให้เหมือนคนจริง ลดความเสี่ยงโดนตรวจจับ"),
            ("📊", "ลิมิตต่อชั่วโมง / ต่อวัน", "กำหนดเพดาน action พร้อมตัวนับ usage แบบเรียลไทม์ และหยุดอัตโนมัติเมื่อถึงลิมิต"),
            ("🔌", "ทำงานต่อแม้ปิด popup", "เครื่องยนต์รันเบื้องหลังด้วย service worker ปิดหน้าต่างได้ งานยังเดินต่อ"),
        ],
        "steps_sub": "เปิดหน้า Facebook แล้วกด Start ได้เลย",
        "steps": [
            ("①", "เลือกโหมด Follow หรือ Like", "เปิด popup เลือกแท็บที่ต้องการ ตั้งกลุ่มเป้าหมายและเงื่อนไข"),
            ("②", "ตั้งลิมิตและหน่วงเวลา", "กำหนดจำนวนสูงสุดต่อรอบ ช่วงหน่วงเวลา และ Whitelist ที่ห้ามแตะ"),
            ("③", "กด Start", "ระบบทำงานตามเงื่อนไขให้อัตโนมัติ พร้อมตัวนับแสดงความคืบหน้า"),
            ("④", "คุมความเสี่ยงในแท็บตั้งค่า", "ดูตัวนับ usage รายชั่วโมง/รายวัน และปรับลิมิตได้ทุกเมื่อ"),
        ],
        "callout": "💡 เริ่มต้นด้วยลิมิตต่ำ ๆ และหน่วงเวลาช้า ๆ ก่อน แล้วค่อยปรับขึ้นทีละนิด เพื่อความปลอดภัยของบัญชี",
        "perms": [
            ("storage", "บันทึกการตั้งค่าและตัวนับลิมิตในเครื่อง"),
            ("tabs, scripting", "ตรวจสอบแท็บ Facebook ที่เปิดอยู่และสั่งงานบนหน้าเว็บ"),
            ("host: www.facebook.com", "อ่านและคลิกองค์ประกอบที่ปรากฏบนหน้าจอเหมือนผู้ใช้ทั่วไป"),
        ],
        "warning": "Facebook มีระบบตรวจจับการใช้งานอัตโนมัติ — โปรดใช้ด้วยความระมัดระวัง ตั้งหน่วงเวลาช้า ๆ และลิมิตต่ำ ๆ การใช้เครื่องมืออัตโนมัติเป็นความรับผิดชอบของผู้ใช้เอง",
        "disclaimer": "ส่วนขยายนี้เป็นเครื่องมือของบุคคลที่สาม ไม่ได้เกี่ยวข้องหรือได้รับการรับรองจาก Facebook / Meta",
    },
    {
        "slug": "youtube-toolkit", "title": "YouTube Toolkit",
        "target": "youtube.com",
        "meta": "YouTube Toolkit: จัดการ YouTube อัตโนมัติ — subscribe/unsubscribe ไลก์วิดีโอ กรองตามยอดวิว ผู้ติดตาม หรือ keyword ในชื่อวิดีโอ",
        "hero": "เครื่องมือจัดการ YouTube อัตโนมัติ — subscribe/unsubscribe ช่องตามเงื่อนไข "
                "ไลก์วิดีโอที่ผ่านเกณฑ์ยอดวิว/คำค้น กรองตามยอดผู้ติดตาม "
                "ตั้งหน่วงเวลาแบบสุ่ม และคุมความเสี่ยงด้วยลิมิตต่อชั่วโมง/ต่อวัน",
        "features_sub": "ออกแบบสำหรับครีเอเตอร์และนักการตลาดที่อยากเติบโตบน YouTube อย่างเป็นระบบ",
        "features": [
            ("➕", "Subscribe ตามเงื่อนไข", "subscribe ช่องจากผลค้นหา กรองตามยอดผู้ติดตามขั้นต่ำ พร้อม Whitelist"),
            ("🧹", "Unsubscribe เก็บกวาด", "ยกเลิกการติดตามช่องที่ไม่ต้องการได้เป็นชุด เลือกเงื่อนไขได้"),
            ("❤️", "ไลก์วิดีโอตามเกณฑ์", "ไลก์เฉพาะวิดีโอที่ผ่านยอดวิวขั้นต่ำ ความยาว และคำค้นในชื่อวิดีโอ"),
            ("🔎", "กรองละเอียด", "กรองตามยอดวิว ยอดผู้ติดตาม และ keyword เจาะเฉพาะกลุ่มเป้าหมายจริง"),
            ("📊", "ลิมิตต่อชั่วโมง / ต่อวัน", "กำหนดเพดาน action พร้อมตัวนับเรียลไทม์ หยุดอัตโนมัติเมื่อถึงลิมิต"),
            ("🔌", "ทำงานต่อแม้ปิด popup", "เครื่องยนต์รันเบื้องหลัง ปิดหน้าต่าง popup ได้ งานยังเดินต่อ"),
        ],
        "steps_sub": "เปิดหน้า YouTube แล้วกด Start ได้เลย",
        "steps": [
            ("①", "เลือกโหมด Subscribe หรือ Like", "เปิด popup เลือกแท็บ ตั้งคำค้นและเกณฑ์ที่ต้องการ"),
            ("②", "ตั้งตัวกรอง", "กำหนดยอดผู้ติดตาม/ยอดวิวขั้นต่ำ และ keyword ในชื่อ"),
            ("③", "กด Start", "ระบบ subscribe หรือไลก์เฉพาะรายการที่ผ่านเกณฑ์ให้อัตโนมัติ"),
            ("④", "คุมลิมิตในแท็บตั้งค่า", "ดูตัวนับ usage และปรับเพดานต่อชั่วโมง/ต่อวันได้ทุกเมื่อ"),
        ],
        "callout": "💡 ตั้งเกณฑ์ยอดวิว/ผู้ติดตามให้ตรงกลุ่มเป้าหมาย เพื่อให้การติดตามมีคุณภาพมากกว่าปริมาณ",
        "perms": [
            ("storage", "บันทึกการตั้งค่าและตัวนับลิมิตในเครื่อง"),
            ("tabs, scripting", "ตรวจสอบแท็บ YouTube ที่เปิดอยู่และสั่งงานบนหน้าเว็บ"),
            ("host: www.youtube.com", "อ่านและคลิกองค์ประกอบที่ปรากฏบนหน้าจอเหมือนผู้ใช้ทั่วไป"),
        ],
        "warning": "YouTube มีระบบตรวจจับการใช้งานอัตโนมัติ — โปรดใช้ด้วยความระมัดระวัง ตั้งหน่วงเวลาช้า ๆ และลิมิตต่ำ ๆ การใช้เครื่องมืออัตโนมัติเป็นความรับผิดชอบของผู้ใช้เอง",
        "disclaimer": "ส่วนขยายนี้เป็นเครื่องมือของบุคคลที่สาม ไม่ได้เกี่ยวข้องหรือได้รับการรับรองจาก YouTube / Google",
    },
    {
        "slug": "instagram-toolkit", "title": "Instagram Toolkit",
        "target": "instagram.com",
        "meta": "Instagram Toolkit: follow/unfollow บน Instagram ตามเงื่อนไข — เฉพาะบัญชี verified, keyword ใน bio หรือผู้ติดตามขั้นต่ำ พร้อม Whitelist",
        "hero": "เครื่องมือจัดการ Instagram อัตโนมัติ — follow/unfollow ตามเงื่อนไขละเอียด "
                "เลือกเฉพาะบัญชี verified, มี keyword ใน bio หรือผู้ติดตามขั้นต่ำ "
                "เก็บกวาดคนที่ไม่ติดตามกลับ พร้อม Whitelist กันลบผิดคน",
        "features_sub": "ออกแบบสำหรับครีเอเตอร์และแบรนด์ที่อยากโตบน Instagram อย่างมีกลยุทธ์",
        "features": [
            ("➕", "Follow ตามเงื่อนไข", "follow จากผู้ติดตามบัญชีอื่นหรือผลค้นหา ตามเกณฑ์ที่ตั้งไว้"),
            ("🔎", "ตัวกรองละเอียด", "เลือกเฉพาะบัญชี verified, มี keyword ใน bio, ผู้ติดตามขั้นต่ำ หรือข้ามบัญชีส่วนตัว"),
            ("🧹", "Unfollow คนที่ไม่ตามกลับ", "เก็บกวาด Following ให้สะอาด เลือกเฉพาะ Non-mutual"),
            ("🛡️", "Whitelist กันลบผิดคน", "ใส่รายชื่อที่ห้าม unfollow ไม่ว่ากรณีใด ปลอดภัยกับคนสำคัญ"),
            ("⏱️", "หน่วงเวลาแบบสุ่ม", "สุ่มจังหวะ action เหมือนคนจริง ลดความเสี่ยงโดนระบบตรวจจับ"),
            ("📊", "ลิมิตต่อชั่วโมง / ต่อวัน", "กำหนดเพดาน action พร้อมตัวนับเรียลไทม์ และหยุดอัตโนมัติเมื่อถึงลิมิต"),
        ],
        "steps_sub": "เปิดหน้า Instagram แล้วกด Start ได้เลย",
        "steps": [
            ("①", "เลือกโหมด Follow หรือ Unfollow", "เปิด popup เลือกแท็บ ตั้งกลุ่มเป้าหมาย"),
            ("②", "ตั้งตัวกรองและ Whitelist", "เลือกเงื่อนไข verified / keyword / ผู้ติดตาม และใส่รายชื่อที่ห้ามแตะ"),
            ("③", "กด Start", "ระบบ follow/unfollow เฉพาะบัญชีที่ตรงเงื่อนไขให้อัตโนมัติ"),
            ("④", "คุมลิมิตในแท็บตั้งค่า", "ดูตัวนับ usage และปรับเพดานได้ทุกเมื่อ"),
        ],
        "callout": "💡 Instagram เข้มกับการใช้งานอัตโนมัติเป็นพิเศษ — ตั้งลิมิตต่ำมาก ๆ และหน่วงเวลานาน ๆ เพื่อความปลอดภัย",
        "perms": [
            ("storage", "บันทึกการตั้งค่า Whitelist และตัวนับลิมิตในเครื่อง"),
            ("tabs, scripting", "ตรวจสอบแท็บ Instagram ที่เปิดอยู่และสั่งงานบนหน้าเว็บ"),
            ("host: www.instagram.com", "อ่านและคลิกองค์ประกอบที่ปรากฏบนหน้าจอเหมือนผู้ใช้ทั่วไป"),
        ],
        "warning": "Instagram มีระบบตรวจจับการใช้งานอัตโนมัติที่เข้มงวด — โปรดใช้ด้วยความระมัดระวังอย่างยิ่ง การใช้เครื่องมืออัตโนมัติเป็นความรับผิดชอบของผู้ใช้เอง",
        "disclaimer": "ส่วนขยายนี้เป็นเครื่องมือของบุคคลที่สาม ไม่ได้เกี่ยวข้องหรือได้รับการรับรองจาก Instagram / Meta",
    },
    {
        "slug": "stock-alert", "title": "Stock Alert",
        "target": "หน้าสินค้า Lazada / Shopee",
        "meta": "Stock Alert: แจ้งเตือนเมื่อสินค้าที่ติดตามบน Lazada/Shopee ลดราคาถึงเกณฑ์หรือกลับมามีสต็อก ไม่พลาดดีลอีกต่อไป",
        "hero": "เครื่องมือติดตามราคาและสต็อกสินค้าบน Lazada และ Shopee — "
                "ตั้งราคาเป้าหมายต่อสินค้า ระบบจะแจ้งเตือนผ่าน Chrome ทันทีเมื่อราคาลดถึงเกณฑ์ "
                "มีโค้ดส่วนลด หรือสินค้ากลับมามีสต็อก ไม่พลาดดีลอีกต่อไป",
        "features_sub": "ออกแบบสำหรับนักช้อปที่ตามล่าดีลและพ่อค้าแม่ค้าที่ต้องเติมสต็อกตรงเวลา",
        "features": [
            ("🎯", "ตั้งราคาเป้าหมาย", "กดเพิ่มสินค้าจากหน้าเว็บ ตั้งราคาที่อยากให้เตือนได้ต่อรายการ"),
            ("🔔", "เตือนเมื่อราคาลด", "ได้รับ notification ทันทีที่ราคาลดถึงเกณฑ์ที่ตั้งไว้"),
            ("📦", "เตือนเมื่อกลับมามีสต็อก", "ของหมดอยู่? ระบบเช็คให้และเตือนทันทีเมื่อกลับมามีของ"),
            ("🎟️", "เตือนเมื่อมีโค้ดส่วนลด", "จับโค้ด/คูปองใหม่บนหน้าสินค้าที่ติดตาม"),
            ("⏱️", "เช็คอัตโนมัติเบื้องหลัง", "ตั้งความถี่การตรวจสอบ ระบบทำงานเองแม้ไม่เปิดเว็บ"),
            ("🔒", "ข้อมูลอยู่ในเครื่อง", "รายการติดตามและประวัติราคาเก็บในเครื่อง ลบได้ตลอดเวลา"),
        ],
        "steps_sub": "เพิ่มสินค้าจากหน้าเว็บ แล้วปล่อยให้ระบบเฝ้าให้",
        "steps": [
            ("①", "เปิดหน้าสินค้าที่อยากตาม", "เปิดหน้าสินค้าบน Lazada หรือ Shopee"),
            ("②", "กดเพิ่มเข้ารายการติดตาม", "คลิกไอคอน ตั้งราคาเป้าหมายที่อยากให้เตือน"),
            ("③", "เลือกประเภทการเตือน", "เปิด-ปิดการเตือนราคาลด / มีโค้ด / กลับมามีสต็อก ตามต้องการ"),
            ("④", "รอรับแจ้งเตือน", "ระบบเช็คให้เบื้องหลัง และเด้ง notification ทันทีที่ถึงเกณฑ์"),
        ],
        "callout": "💡 ตั้งราคาเป้าหมายให้ต่ำกว่าราคาปัจจุบันเล็กน้อย เพื่อให้ได้รับเตือนตอนมีโปรจริง ๆ",
        "perms": [
            ("storage", "บันทึกรายการสินค้าที่ติดตามและประวัติราคาในเครื่อง"),
            ("alarms", "ตั้งเวลาให้ระบบเช็คราคาและสต็อกเป็นระยะแบบเบื้องหลัง"),
            ("notifications", "แสดงการแจ้งเตือนผ่าน Chrome เมื่อถึงเกณฑ์ที่ตั้งไว้"),
            ("host: lazada.co.th, shopee.co.th", "อ่านราคาและสถานะสต็อกของสินค้าที่คุณติดตามเท่านั้น"),
        ],
        "warning": "",
        "disclaimer": "ส่วนขยายนี้เป็นเครื่องมือของบุคคลที่สาม ไม่ได้เกี่ยวข้องหรือได้รับการรับรองจาก Lazada หรือ Shopee",
    },
    {
        "slug": "social-analytics", "title": "Social Analytics",
        "target": "Instagram / Facebook / TikTok",
        "meta": "Social Analytics: ดูสถิติบัญชี Social Media ของตัวเองแบบเรียลไทม์ — engagement rate, growth rate และเปรียบเทียบกับคู่แข่ง",
        "hero": "เครื่องมือดูสถิติบัญชี Social Media ของตัวเองแบบเรียลไทม์ — "
                "คำนวณ engagement rate และ growth rate ให้อัตโนมัติ ดูโพสต์ที่ปังที่สุด "
                "และเปรียบเทียบกับคู่แข่งได้ในที่เดียว",
        "features_sub": "ออกแบบสำหรับครีเอเตอร์และนักการตลาดที่อยากวัดผลและเอาชนะคู่แข่งด้วยข้อมูล",
        "features": [
            ("📈", "สถิติเรียลไทม์", "ดูตัวเลขบัญชีตัวเองสด ๆ — ผู้ติดตาม, reach, engagement ในที่เดียว"),
            ("❤️", "Engagement Rate อัตโนมัติ", "คำนวณ ER จาก like + comment + share ให้ ไม่ต้องนั่งคิดเอง"),
            ("🚀", "Growth Rate รายวัน", "ติดตามอัตราการเติบโตของผู้ติดตามเป็นรายวัน/รายสัปดาห์"),
            ("🏁", "เปรียบเทียบกับคู่แข่ง", "ใส่บัญชีคู่แข่ง ดูว่าใครโตเร็วกว่า ER ใครสูงกว่า"),
            ("🔥", "หาโพสต์ที่ปังที่สุด", "จัดอันดับโพสต์ตาม engagement เห็นว่าคอนเทนต์แบบไหนเวิร์ก"),
            ("🔒", "อ่านข้อมูลสาธารณะ", "อ่านเฉพาะข้อมูลสาธารณะที่แสดงบนหน้าเว็บ ไม่ส่งออกนอกเครื่อง"),
        ],
        "steps_sub": "เปิดหน้าโปรไฟล์แล้วดูสถิติได้ทันที",
        "steps": [
            ("①", "เลือกแพลตฟอร์มที่ติดตาม", "เปิด-ปิด Instagram / Facebook Page / TikTok ตามที่ใช้งาน"),
            ("②", "เปิดหน้าโปรไฟล์", "เปิดหน้าบัญชีของคุณ ระบบดึงตัวเลขมาคำนวณให้"),
            ("③", "ดูภาพรวมและ ER", "ดู engagement rate, growth rate และโพสต์ที่ปังที่สุด"),
            ("④", "เทียบกับคู่แข่ง", "ใส่บัญชีคู่แข่งเพื่อเทียบ follower / ER / ความถี่โพสต์"),
        ],
        "callout": "💡 โฟกัสที่ engagement rate มากกว่ายอดผู้ติดตามดิบ — บัญชีเล็กที่ ER สูงมักขายได้ดีกว่า",
        "perms": [
            ("storage", "บันทึกการตั้งค่าและสถิติย้อนหลังในเครื่อง"),
            ("tabs, scripting", "ตรวจสอบแท็บโปรไฟล์ที่เปิดอยู่และอ่านตัวเลขที่แสดงบนหน้าเว็บ"),
            ("host: instagram.com, facebook.com, tiktok.com", "อ่านเฉพาะข้อมูลสาธารณะที่ปรากฏบนหน้าจอ"),
        ],
        "warning": "",
        "disclaimer": "ส่วนขยายนี้เป็นเครื่องมือของบุคคลที่สาม ไม่ได้เกี่ยวข้องหรือได้รับการรับรองจากแพลตฟอร์มใด ๆ",
    },
]

for ext in EXTS:
    features_html = "\n".join(feature(*f) for f in ext["features"])
    steps_html = "\n".join(step(*s) for s in ext["steps"])
    perms_html = "\n".join(perm(*p) for p in ext["perms"])
    warning_html = WARN.format(w=ext["warning"]) if ext["warning"] else ""
    html = PAGE.format(
        title=ext["title"], slug=ext["slug"], target=ext["target"],
        meta=ext["meta"], hero=ext["hero"],
        features_sub=ext["features_sub"], features=features_html,
        steps_sub=ext["steps_sub"], steps=steps_html, callout=ext["callout"],
        perms=perms_html, warning=warning_html, disclaimer=ext["disclaimer"],
        fb=FB, email=EMAIL,
    )
    path = os.path.join(HERE, f"{ext['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK {ext['slug']}.html")

print("\nDONE")
