text = '''asdfasdf;ldjasfklj jda;gjd;las j;jr;kag ;kjnLGJLHLHLHJHJP:J
adsfhasdlhfjdlashjHJLHLSDHLDHJSFkljh ljsdhfkljdshlkjhlHLHLHSDHLHFJDS
dasfhjdashfkljhdsf klliuhq  ;[rupwqerui[oqewruuib nm,nfiuy5h2145uy18ryu89q-ewyfhjv
fhasd;fkjkj nhakjh2 690u25896 uobn kvjh34o5y934-fhLI G :HJHG I:HGJ OHSDJ :LHF&( ^Y*(YRUI#B
kyjgO BT(YWE_*Y9-yy3423 b h5u ty78g fjevgb p2p34i hjn d;la vh;ao134tbj'''

count = [0] * 128
for char in text:
    count[ord(char)] += 1

for i in range(128):
    if count[i] > 0:
        print(chr(i), count[i])