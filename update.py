QUESTIONS_INDEX = "question_index"
QUESTIONS_INDEX_CHI = "问题索引"
QUESTION_SPAN_MARK = "#Q"


def get_span(s):
    return "<span id=\"{}\"></span>".format(s)


# 创建问题索引
# [["为什么git clone的时候一直出现密码错误?", "用户名请使用url里面的.cn后接着的那块看起来很像用户名的东西，密码是发送到邮箱之中的密码。",2021.3.5]]
def create_question_index(l: list):
    res = get_span(QUESTIONS_INDEX) + "\n" \
          + "## " + QUESTIONS_INDEX_CHI + "\n" \
          + ''.join(["- [{}]({})\n".format(l[_][0] + ' ' + l[_][2], "#Q" + str(_)) for _ in range(len(l))])
    return res


# 创建新闻索引
def create_news_index():
    pass


# 创建目录
def create_directory():
    pass


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
def generate_format():
    pass


# 插入信息
def insert_info():
    pass


if __name__ == '__main__':
    l = [["为什么git clone的时候一直出现密码错误?", "用户名请使用url里面的.cn后接着的那块看起来很像用户名的东西，密码是发送到邮箱之中的密码。", "2021.3.5"]]
    print(create_question_index(l))
