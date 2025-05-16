import re


def strip_text(text):
    # 句号、逗号、-的空格摘除。
    # ' [^\w\s-] ' => 所有 非字母数字、空格 前后有空格的
    # '(?<!\s) - ' => 前瞻断言，没有\s才匹配' - '。
    r = r' \.|\. | ,|, | ，|， | 。|。 | [^\w\s-] |(?<!\s) - |[^\s]- '
    text = re.sub(r, lambda m: m.group(0).strip(), text)
    return text


def math_trans(text):
    r1 = r'\\\(|\)\\'
    r2 = r'\\[a-z|A-Z]'
    # \(和)\换成$，单斜杠的符号换成双斜杠
    text = re.sub(r1, '$', text)
    text = re.sub(r2, lambda m: '\\' + m.group(0), text)
    return text


def sub_dollar(text):
    text = re.sub('\$', '＄', text)
    return text


def all_func(text):
    tmp = strip_text(text)
    result = math_trans(tmp)

    return result
