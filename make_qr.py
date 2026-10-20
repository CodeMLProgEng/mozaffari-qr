import qrcode

# ---------- اطلاعات مغازه (فقط این بخش رو عوض می‌کنی) ----------
SHOP = {
    "name": "تعمیرات تخصصی موبایل مظفری",
    "address": "خیابان ولیعصر، بالاتر از چهارراه فراعی",
    "phone": "09139470952",
    "whatsapp": "989139470952",
    "telegram": "",          # آیدی تلگرام بدون @ (خالی = دکمه نمایش داده نمی‌شه)
    "instagram": "mobilemozafaripc",
    "map": "",               # لینک نقشه (خالی = دکمه نمایش داده نمی‌شه)
}
PAGE_URL = "https://ml-fateme-aipro.github.io/mozaffari-qr/"
# ---------------------------------------------------------------

TEMPLATE = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__NAME__</title>
<style>
  body{font-family:Tahoma,sans-serif;background:#0f172a;color:#fff;margin:0;padding:24px;text-align:center}
  h1{font-size:22px;margin:8px 0}
  p{color:#94a3b8;margin:0 0 24px}
  a{display:block;margin:12px auto;max-width:360px;padding:14px;border-radius:12px;
    color:#fff;text-decoration:none;font-size:17px}
  .call{background:#2563eb}.wa{background:#16a34a}.tg{background:#0ea5e9}
  .ig{background:#c026d3}.map{background:#ea580c}
</style>
</head>
<body>
  <h1>__NAME__</h1>
  <p>__ADDRESS__</p>
  __BUTTONS__
</body>
</html>
"""


def button(css, text, link):
    return f'<a class="{css}" href="{link}">{text}</a>' if link else ""


def build_page(s):
    buttons = [
        button("call", "📞 تماس تلفنی", f"tel:{s['phone']}" if s["phone"] else ""),
        button("wa", "💬 واتساپ", f"https://wa.me/{s['whatsapp']}" if s["whatsapp"] else ""),
        button("tg", "✈️ تلگرام", f"https://t.me/{s['telegram']}" if s["telegram"] else ""),
        button("ig", "📸 اینستاگرام", f"https://instagram.com/{s['instagram']}" if s["instagram"] else ""),
        button("map", "📍 مسیریابی", s["map"]),
    ]
    html = TEMPLATE.replace("__NAME__", s["name"])
    html = html.replace("__ADDRESS__", s["address"])
    html = html.replace("__BUTTONS__", "\n  ".join(b for b in buttons if b))
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html ساخته شد")


def build_qr(url):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=12, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="#0f172a", back_color="white").save("qr.png")
    print("qr.png ساخته شد")


if __name__ == "__main__":
    build_page(SHOP)
    build_qr(PAGE_URL)