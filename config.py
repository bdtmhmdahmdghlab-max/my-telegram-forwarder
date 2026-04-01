import os

class Config:
    API_ID = int(os.environ.get("API_ID", "2040")) # الـ ID الافتراضي الرسمي
    API_HASH = os.environ.get("API_HASH", "b18441a1ed629410971e434e0639e79d")
    # الـ Session الذي استخرجته من ترمكس
    SESSION = os.environ.get("SESSION_STRING") 
    # الـ ID الخاص بالمجموعة التي ستستقبل "الصيد" (يجب أن يبدأ بـ -100)
    TARGET_ID = int(os.environ.get("TARGET_ID", "-100123456789"))
  
