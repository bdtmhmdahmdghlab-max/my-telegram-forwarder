from pyrogram import Client, filters
from config import Config

# الكلمات المفتاحية (تمت إضافة تنوع في الهمزات لضمان الصيد)
KEYWORDS = [
    "ابغى", "أبغى", "اريد", "أريد", "واجب", "اختبار", "كويز", "حل", 
    "مساعدة", "مساعده", "بحوث", "مشروع", "مشاريع", "في حد", "من يعرف"
]

# الفلتر يشمل المجموعات العادية والخارقة (Supergroups)
@Client.on_message(filters.group & ~filters.service & ~filters.me)
async def hunter_handler(client, message):
    if not message.text:
        return

    msg_text = message.text.lower()
    
    # التحقق من وجود أي كلمة مفتاحية
    if any(word in msg_text for word in KEYWORDS):
        try:
            # تجهيز معلومات الصياد (المجموعة والمرسل)
            chat_name = message.chat.title
            user_name = message.from_user.first_name if message.from_user else "مستخدم مخفي"
            
            alert = (
                "🎯 **تم رصد صيد جديد!**\n"
                f"👤 **المرسل:** {user_name}\n"
                f"📢 **المجموعة:** {chat_name}\n"
                f"🔗 **الرابط:** [اضغط هنا]({message.link})\n"
                "--------------------------\n"
                f"📝 **النص:**\n`{message.text}`"
            )

            # إرسال التنبيه إلى مجموعتك الخاصة
            await client.send_message(
                chat_id=Config.TARGET_ID,
                text=alert,
                disable_web_page_preview=True
            )
        except Exception as e:
            print(f"⚠️ خطأ أثناء التوجيه: {e}")
