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
    "for x in [21,2]:",
    "    ss.append(s[x])",
    "a,b=0,len(s)",
    "while a<b-1:",
    "    ss.append(s[3]+f(s[a])+chr(44))",
    "    a += 1",
    "ss.append(s[3]+f(s[a])+chr(93))",
    "for x in [0,1,2,3,4,5,6,7,8]:",
    "    ss.append(s[b-9+x])",
    "#halt with <A_2B_2>",
    "for x in ss:",
    "    print(x)",
    "-- A_2 -> <C>",
    "-- B_2(<C>) -> <A_1B_1>",
    "g::String -> String",
    "g x = (s!!3 ++) . flip (++) ([toEnum 44]) . show $ x",
    "f::[String] -> [String]",
    "f x = ((map g) $ init x) ++ [(flip (++) [toEnum 93] . (init.g) $ last x)]",
    "ss::[String]",
    "ss=take 3 s ++ f s ++ (take 17 $ drop 4 s)",
    "-- halt with <A_1B_1>",
    "main=putStrLn.unlines $ ss"]
#B_1(<C>) -> <A_2B_2>
q=chr(34)
def f(x):
    return q+x+q
ss=[]
for x in [21,2]:
    ss.append(s[x])
a,b=0,len(s)
while a<b-1:
    ss.append(s[3]+f(s[a])+chr(44))
    a += 1
ss.append(s[3]+f(s[a])+chr(93))
for x in [0,1,2,3,4,5,6,7,8]:
    ss.append(s[b-9+x])
#halt with <A_2B_2>
for x in ss:
    print(x)

