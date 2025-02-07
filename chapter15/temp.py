from lxml.html import HtmlElement, fromstring
from lxml.html import etree
import re

html = open('detail.html', encoding='utf-8').read()
element = fromstring(html)

# 提取标题
metas = [
    '//meta[starts-with(@property, "og:title")]/@content',
    '//meta[starts-with(@name, "og:title")]/@content',
    '//meta[starts-with(@property, "title")]/@content',
    '//meta[starts-with(@name, "title")]/@content',
    '//meta[starts-with(@property, "page:title")]/@content',
]

def extract_by_meta(element: HtmlElement) -> str:
    for xpath in metas:
        title = element.xpath(xpath)
        if title:
            return ''.join(title)

def extract_by_title(element: HtmlElement):
    return ''.join(element.xpath('//title//text()')).strip()

def extract_by_h(element: HtmlElement):
    h_s = element.xpath('//h1//text()|//h2//text()|//h3//text()')
    return h_s or []

# 使用基本的相似度算法Jaccard，用两个字符串中的交集字符数量除以两个字符串的并集字符数量
def similarity(s1, s2):
    if not s1 or not s2:
        return 0
    # 将两个字符串拆分成集合
    s1_set = set(list(s1))
    s2_set = set(list(s2))
    # 求两个集合的交集和并集
    intersection = s1_set.intersection(s2_set)
    union = s1_set.intersection(s2_set)
    return len(intersection) / len(union)

def extract_title(element: HtmlElement):
    title_extract_by_meta = extract_by_meta(element)
    title_extract_by_h = extract_by_h(element)
    title_extract_by_title = extract_by_title(element)

    if title_extract_by_meta:
        return title_extract_by_meta

    title_extract_by_h = sorted(title_extract_by_h,
                                key=lambda x: similarity(x, title_extract_by_title), reverse=True)

    if title_extract_by_h:
        return title_extract_by_h[0]

    return title_extract_by_title

# 提取正文
content_useless_tags = ['meta', 'style', 'script', 'link', 'video', 'audio', 'iframe', 'source', 'svg', 'path', 'symbol', 'img', 'footer', 'header']
content_strip_tags = ['span', 'blockquote']
content_noise_xpath = [
    '//div[contains(@class, "comment")]',
    '//div[contains(@class, "advertisement")]',
    '//div[contains(@class, "advert")]',
    '//div[contains(@style, "display: none")]',
]

def remove_element(element: HtmlElement):
    parent = element.getparent()
    if parent is not None:
        parent.remove(element)

def remove_children(element: HtmlElement, xpaths=None):
    if not xpaths:
        return
    for xpath in xpaths:
        nodes = element.xpath(xpath)
        for node in nodes:
            remove_element(node)
    return element

def children(element: HtmlElement):
    yield element
    for child_element in element:
        if isinstance(child_element, HtmlElement):
            yield from children(child_element)

def preprocess4content(element: HtmlElement):
    # 删除标签和内容
    etree.strip_elements(element, *content_useless_tags)
    # 只删除标签对
    etree.strip_tags(element, *content_strip_tags)
    # 只删除噪声标签
    remove_children(element, content_noise_xpath)

    for child in children(element):
        # 合并span和strong标签的文本
        if child.tag.lower() == 'p':
            etree.strip_tags(child, 'span')
            etree.strip_tags(child, 'strong')
            if not (child.text and child.text.strip()):
                remove_element(child)
        # 如果div里没有子节点就转化成p节点
        if child.tag.lower() =='div' and not child.getchildren():
            child.tag = 'p'

class Element(HtmlElement):
    # 节点的唯一ID
    id: int = None
    # 标签名
    tag_name: str = None
    # 节点的总字符数
    number_of_char: int = None
    # 节点内带超链接的字符数
    number_of_a_char: int = None
    # 节点的子孙节点数
    number_of_descendants: int = None
    # 节点内带链接的节点数
    number_of_a_descendants: int = None
    # p的节点数
    number_of_p_descendants: int = None
    # 节点内的标签符号数
    number_of_punctuation: int = None
    # 符号密度
    density_of_punctuation: float = None
    # 文本密度
    density_of_text: float = None
    # 最终评分
    density_score: float = None

def number_of_a_char(element: Element):
    if element is None:
        return 0
    text = ''.join(element.xpath('.//a//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    return len(text)

def number_of_p_descendants(element: Element):
    if element is None:
        return 0
    return len(element.xpath('.//p'))

punctuation = set('''！，。？、；：“”‘’《》%（）<>{}「」【】*~`,.?:;'"!%()''')

def number_of_punctuation(element: Element):
    if element is None:
        return 0
    text =''.join(element.xpath('.//text()'))
    text = re.sub(r'\s*', '', text, flags=re.S)
    punctuations = [c for c in text if c in punctuation]
    return len(punctuations)

def density_of_text(element: Element):
    if element.number_of_descendants - element.number_of_a_descendants == 0:
        return 0
    return(element.number_of_char - element.number_of_a_char) / (element.number_of_descendants - element.number_of_a_descendants)

def density_of_punctuation(element: Element):
    result = (element.number_of_char - element.number_of_a_char) / (element.number_of_punctuation + 1)
    return result or 1

def process(element: Element):
    # 预处理
    preprocess4content(element)
    # 找出当前节点的子孙节点
    # descendants = descendants_of_body(element)
    