import os

class Config:
    # الكود سيبحث عن القيمة في Railway، وإذا لم يجدها سيستخدم القيمة الافتراضية
    API_ID = int(os.environ.get("API_ID", "2040")) 
    API_HASH = os.environ.get("API_HASH", "b18441a1ed629410971e434e0639e79d")
    
    # هذه القيم "حساسة" لذا نتركها بدون قيمة افتراضية ليتم جلبها من Railway فقط
    SESSION_STRING = os.environ.get("SESSION_STRING") 
    TARGET_ID = int(os.environ.get("TARGET_ID", "-100123456789"))

