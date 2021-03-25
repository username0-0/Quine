#!/usr/bin/env python3
#A_1 -> <C>
s=[
    "#!/usr/bin/env python3",
    "#A_1 -> <C>",
    "s=[",
    "    ",
    "#B_1(<C>) -> <A_2B_2>",
    "q=chr(34)",
    "def f(x):",
    "    return q+x+q",
    "ss=[]",
    "a, b, c = 0, len(s), 11",
    "for x in [b-c,b-c+1]:",
    "    ss.append(s[x])",
    "while a<b-1:",
    "    ss.append(s[3]+f(s[a])+chr(44))",
    "    a += 1",
    "ss.append(s[3]+f(s[a])+chr(93))",
    "a=0",
    "while a<c-2:",
    "    ss.append(s[b-c+2+a])",
    "    a += 1",
    "#halt with <A_2B_2>",
    "for x in ss:",
    "    print(x)",
    "-- A_2 -> <C>",
    "s=[",
    "-- B_2(<C>) -> <A_1B_1>",
    "g::String -> String",
    "g x = (s!!3 ++) . flip (++) [','] . show $ x",
    "f::[String] -> [String]",
    "f x = ((map g) $ init x) ++ [flip (++) [']'] . (init.g) $ last x]",
    "ss::[String]",
    "ss=take 3 s ++ f s ++ (take 19 $ drop 4 s)",
    "-- halt with <A_1B_1>",
    "main=putStrLn.unlines $ ss"]
#B_1(<C>) -> <A_2B_2>
q=chr(34)
def f(x):
    return q+x+q
ss=[]
a, b, c = 0, len(s), 11
for x in [b-c,b-c+1]:
    ss.append(s[x])
while a<b-1:
    ss.append(s[3]+f(s[a])+chr(44))
    a += 1
ss.append(s[3]+f(s[a])+chr(93))
a=0
while a<c-2:
    ss.append(s[b-c+2+a])
    a += 1
#halt with <A_2B_2>
for x in ss:
    print(x)

