from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
أهلا {}

أهلا بك في {}

هذا البوت مخصص لاستخراج كود تيرمكس .. البوت آمن 100% 
المطور : @YDDDE
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" - إبدا باستخراخ كود تيرمكس .", callback_data="generate")],
        [InlineKeyboardButton(text="الصفحة الرئيسية .", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥إبدأ الاستخراج الآن .", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("- إبدأ الاستخراج .", callback_data="generate")],
        [InlineKeyboardButton("✨ المطور ✨", url="https://t.me/YDDDE")],
        [
            InlineKeyboardButton("- طريقة الاستعمال .", callback_data="help"),
            InlineKeyboardButton(" ", callback_data="about")
        ],
        [InlineKeyboardButton(" - معلومات أخرى .", url="https://t.me/zVVVn")],
    ]

    # Help Message
    HELP = """
✨ **الأوامر المتوفرة** ✨

/about - معلومات البوت
/help - رسالة المساعدة
/start - رسالة البدأ
/generate - استخراج تيرمكس
/cancel - الغاء العملية
/restart - اعادة التشغيل
المطور : @zVVVn
"""

    # About Message
    ABOUT = """
**About This Bot** 

هذا البوت مخصص لاستخراج كود تيرمكس
**String Session** ..
**Developer** : @YDDDE .
    """
