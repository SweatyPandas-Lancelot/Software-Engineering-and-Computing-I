from flask import Flask
from flask import request
from flask import jsonify
import json
app = Flask(__name__)


@app.route('/', methods=['POST'])
def translate():
    s = json.loads(str(request.get_data(),'utf-8'))['str']
    s = s.strip(' ')
    s = s.split('\n')
    t = ''
    stack = []
    for i in s:
        var1 = 0
        if len(i) == 0:
            continue
        if i[0] != ' ':
            t = t + "[" + delete_space(i)
            stack.append(0)
            continue
        else:
            for j in i:
                if j == ' ':
                    var1 += 1
                else:
                    break
        if var1 > stack[len(stack) - 1]:
            t = t + ' [' + delete_space(i)
            stack.append(var1)
        elif var1 == stack[len(stack) - 1]:
            t = t + '] [' + delete_space(i)
            stack.pop(len(stack) - 1)
            stack.append(var1)
        else:
            while var1 <= stack[len(stack) - 1]:
                t = t + '] '
                stack.pop(len(stack) - 1)
            t = t + '[' + delete_space(i)
            stack.append(var1)
    t = t + ']' * len(stack)
    return t


def delete_space(s: str):
    for i in range(len(s)):
        if s[i] != ' ':
            s = s[i:]
            break
    for i in range(len(s)):
        if s[i] == ' ':
            s = s[:i]
            break
    return s


if __name__ == '__main__':
    app.run()
#     s = '''Program (1)
#       ExtDefList (1)
#         ExtDef (1)
#           Specifier (1)
#             TYPE: int
#           FunDec (1)
#             ID: main
#             LP
#             RP
#           CompSt (2)
#             LC
#             DefList (3)
#               Def (3)
#                 Specifier (3)
#                   TYPE: int
#                 DecList (3)
#                   Dec (3)
#                     VarDec (3)
#                       ID: a
#                     ASSIGNOP
#                     Exp (3)
#                       INT: 0
#                 SEMI
#             StmtList (4)
#               Stmt (4)
#                 Exp (4)
#                   Exp (4)
#                     ID: a
#                   ASSIGNOP
#                   Exp (4)
#                     INT: 1
#                 SEMI
#             RC'''
#     print(s)
#     print(translate(s))
