import json
import re
import pathlib

QUESTIONS_INDEX = "question_index"
QUESTIONS_INDEX_CHI = "问题收集与解答"
QUESTION_SPAN_MARK = "Q"
NEWS_INDEX = "news_index"
NEWS_INDEX_CHI = "新闻索引"
NEWSS_SPAN_MARK = "N"
root = pathlib.Path(__file__).parent.resolve()


def get_span(s):
    return "<span id=\"{}\"></span>".format(s)


# [ [title, context, answer, date  ] ]
def create_index(l: list, s1: str, s2: str, m: str):
    res = get_span(s1) + "\n" \
          + "## " + s2 + "\n" \
          + ''.join(["- [{}]({})  **{}**\n".format(l[_][0], '#' + m + str(_), l[_][3]) for _ in range(len(l))])
    return res


# 创建问题索引
def create_question_index(l: list):
    return create_index(l, QUESTIONS_INDEX, QUESTIONS_INDEX_CHI, QUESTION_SPAN_MARK)


def create_question(l: list):
    return ''.join(
        [get_span(QUESTION_SPAN_MARK + str(_)) + '\n' + "#### Q:{} \n**A**:{}\n\n---\n".format(l[_][1], l[_][2]) for _
         in range(len(l))])


# 创建新闻索引
def create_news_index(l: list):
    return create_index(l, NEWS_INDEX, NEWS_INDEX_CHI, NEWSS_SPAN_MARK)


def create_news(l):
    return ''.join(
        [get_span(NEWSS_SPAN_MARK + str(_)) + '\n' + "#### {} \n{}\n".format(l[_][0], l[_][1]) for _ in range(len(l))])


# 创建目录
def create_directory():
    pass


def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)


# ## directory
#   - [index_1](span_id)
#   - [index_2][span_id]
# <span id="news_1"></span>
# ## news_1
# <span id="news_2"></span>
# ## news_2
# <span id="news_3"></span>
# ## news_3
# ## questions_directory
#   - [questions_1](span_id)
#   - [questions_2](span_id)
# <span id="question_1"></span>
# #### Q: [question_1]
# #### A:
# 目录下面有一个问题总索引、问题总索引下面会有问题索引。
# every_index 标记一些新闻、链接等信息。
# 创建格式


if __name__ == '__main__':
    r = open('question.json', 'r')
    l = json.load(r)
    questions = create_question_index(l) + '\n' + create_question(l)
    readme = root / 'index.md'
    readme_contents = readme.open().read()
    rewritten = replace_chunk(readme_contents, "questions", questions)
    readme.open("w").write(rewritten)
