import string,random,base64,dis

def rec(x):

# 	  4       0 LOAD_FAST                0 (x)
#               2 LOAD_CONST               1 (1)
#               4 COMPARE_OP               2 (==)
#               6 POP_JUMP_IF_FALSE       12

#   5           8 LOAD_CONST               1 (1)
#              10 RETURN_VALUE

#   7     >>   12 LOAD_FAST                0 (x)
#              14 LOAD_GLOBAL              0 (rec)
#              16 LOAD_FAST                0 (x)
#              18 LOAD_CONST               1 (1)
#              20 BINARY_SUBTRACT
#              22 CALL_FUNCTION            1
#              24 BINARY_MULTIPLY
#              26 RETURN_VALUE
#              28 LOAD_CONST               0 (None)
#              30 RETURN_VALUE
# None	

def generate_key(length):
#  10           0 LOAD_CONST               1 ('')
#               2 STORE_FAST               1 (tmp)

#  11           4 LOAD_GLOBAL              0 (string)
#               6 LOAD_ATTR                1 (ascii_letters)
#               8 STORE_FAST               2 (char)

#  12          10 SETUP_LOOP              30 (to 42)
#              12 LOAD_GLOBAL              2 (range)
#              14 LOAD_FAST                0 (length)
#              16 CALL_FUNCTION            1
#              18 GET_ITER
#         >>   20 FOR_ITER                18 (to 40)
#              22 STORE_FAST               3 (i)

#  13          24 LOAD_FAST                1 (tmp)
#              26 LOAD_GLOBAL              3 (random)
#              28 LOAD_METHOD              4 (choice)
#              30 LOAD_FAST                2 (char)
#              32 CALL_METHOD              1
#              34 INPLACE_ADD
#              36 STORE_FAST               1 (tmp)
#              38 JUMP_ABSOLUTE           20
#         >>   40 POP_BLOCK

#  14     >>   42 LOAD_FAST                1 (tmp)
#              44 RETURN_VALUE
# None


def enc_now(key, flag):
#  18           0 LOAD_CONST               1 ('')
#               2 STORE_FAST               2 (tmp_key)

#  19           4 LOAD_CONST               1 ('')
#               6 STORE_FAST               3 (change_key)

#  20           8 LOAD_CONST               1 ('')
#              10 STORE_FAST               4 (tmp_flag)

#  21          12 LOAD_GLOBAL              0 (len)
#              14 LOAD_FAST                0 (key)
#              16 CALL_FUNCTION            1
#              18 STORE_FAST               5 (len_key)

#  22          20 LOAD_GLOBAL              0 (len)
#              22 LOAD_FAST                1 (flag)
#              24 CALL_FUNCTION            1
#              26 STORE_FAST               6 (len_string)

#  24          28 LOAD_GLOBAL              1 (int)
#              30 LOAD_FAST                5 (len_key)
#              32 LOAD_CONST               2 (2)
#              34 BINARY_TRUE_DIVIDE
#              36 CALL_FUNCTION            1
#              38 STORE_FAST               7 (xky)

#  26          40 LOAD_FAST                6 (len_string)
#              42 LOAD_FAST                5 (len_key)
#              44 COMPARE_OP               3 (!=)
#              46 POP_JUMP_IF_FALSE       86

#  27          48 SETUP_LOOP              32 (to 82)
#              50 LOAD_GLOBAL              2 (range)
#              52 LOAD_FAST                6 (len_string)
#              54 CALL_FUNCTION            1
#              56 GET_ITER
#         >>   58 FOR_ITER                20 (to 80)
#              60 STORE_FAST               8 (c)

#  28          62 LOAD_FAST                3 (change_key)
#              64 LOAD_GLOBAL              3 (random)
#              66 LOAD_METHOD              4 (choice)
#              68 LOAD_GLOBAL              5 (string)
#              70 LOAD_ATTR                6 (ascii_letters)
#              72 CALL_METHOD              1
#              74 INPLACE_ADD
#              76 STORE_FAST               3 (change_key)
#              78 JUMP_ABSOLUTE           58
#         >>   80 POP_BLOCK

#  30     >>   82 LOAD_FAST                3 (change_key)
#              84 STORE_FAST               0 (key)

#  32     >>   86 SETUP_LOOP              32 (to 120)
#              88 LOAD_FAST                0 (key)
#              90 GET_ITER
#         >>   92 FOR_ITER                24 (to 118)
#              94 STORE_FAST               9 (a)

#  33          96 LOAD_FAST                2 (tmp_key)
#              98 LOAD_GLOBAL              7 (chr)
#             100 LOAD_GLOBAL              8 (ord)
#             102 LOAD_FAST                9 (a)
#             104 CALL_FUNCTION            1
#             106 LOAD_FAST                7 (xky)
#             108 BINARY_ADD
#             110 CALL_FUNCTION            1
#             112 INPLACE_ADD
#             114 STORE_FAST               2 (tmp_key)
#             116 JUMP_ABSOLUTE           92
#         >>  118 POP_BLOCK

#  35     >>  120 SETUP_LOOP              52 (to 174)
#             122 LOAD_GLOBAL              2 (range)
#             124 LOAD_GLOBAL              0 (len)
#             126 LOAD_FAST                1 (flag)
#             128 CALL_FUNCTION            1
#             130 CALL_FUNCTION            1
#             132 GET_ITER
#         >>  134 FOR_ITER                36 (to 172)
#             136 STORE_FAST              10 (i)

#  36         138 LOAD_FAST                4 (tmp_flag)
#             140 LOAD_GLOBAL              7 (chr)
#             142 LOAD_GLOBAL              8 (ord)
#             144 LOAD_FAST                0 (key)
#             146 LOAD_FAST               10 (i)
#             148 BINARY_SUBSCR
#             150 CALL_FUNCTION            1
#             152 LOAD_GLOBAL              8 (ord)
#             154 LOAD_FAST                1 (flag)
#             156 LOAD_FAST               10 (i)
#             158 BINARY_SUBSCR
#             160 CALL_FUNCTION            1
#             162 BINARY_XOR
#             164 CALL_FUNCTION            1
#             166 INPLACE_ADD
#             168 STORE_FAST               4 (tmp_flag)
#             170 JUMP_ABSOLUTE          134
#         >>  172 POP_BLOCK

#  38     >>  174 LOAD_GLOBAL              9 (print)
#             176 LOAD_CONST               3 ('Here your key: ')
#             178 LOAD_GLOBAL             10 (base64)
#             180 LOAD_METHOD             11 (b64encode)
#             182 LOAD_FAST                2 (tmp_key)
#             184 LOAD_METHOD             12 (encode)
#             186 LOAD_CONST               4 ('utf-8]')
#             188 CALL_METHOD              1
#             190 CALL_METHOD              1
#             192 CALL_FUNCTION            2
#             194 POP_TOP

#  39         196 LOAD_GLOBAL              9 (print)
#             198 LOAD_CONST               5 ('Here your flag: ')
#             200 LOAD_GLOBAL             10 (base64)
#             202 LOAD_METHOD             11 (b64encode)
#             204 LOAD_FAST                4 (tmp_flag)
#             206 LOAD_METHOD             12 (encode)
#             208 LOAD_CONST               6 ('utf-8')
#             210 CALL_METHOD              1
#             212 CALL_METHOD              1
#             214 CALL_FUNCTION            2
#             216 POP_TOP
#             218 LOAD_CONST               0 (None)
#             220 RETURN_VALUE
# None

# flag   = "redacted"
length = rec(4)
key    = generate_key(length)
enc_now(key,flag)