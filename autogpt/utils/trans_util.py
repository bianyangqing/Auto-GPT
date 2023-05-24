from translate import Translator

def translate_english_to_chinese(text):
    translator = Translator(to_lang="zh")
    translation = translator.translate(text)
    return translation

# 调用函数进行翻译
english_text = "Hello, world!"
chinese_text = translate_english_to_chinese(english_text)
print(chinese_text)

