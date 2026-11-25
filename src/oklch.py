import math
def lin(c): c=c/255; return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def oklch(h):
    h=h.lstrip('#'); r,g,b=[lin(int(h[i:i+2],16)) for i in (0,2,4)]
    l=0.4122214708*r+0.5363325363*g+0.0514459929*b; m=0.2119034982*r+0.6806995451*g+0.1073969566*b; s=0.0883024619*r+0.2817188376*g+0.6299787005*b
    l,m,s=[x**(1/3) for x in (l,m,s)]
    L=0.2104542553*l+0.7936177850*m-0.0040720468*s; a=1.9779984951*l-2.4285922050*m+0.4505937099*s; bb=0.0259040371*l+0.7827717662*m-0.8086757660*s
    return round(L,3), round(math.hypot(a,bb),3), round(math.degrees(math.atan2(bb,a))%360,1)
def lum(h):
    h=h.lstrip('#'); c=[lin(int(h[i:i+2],16)) for i in (0,2,4)]; return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def cr(a,b):
    x,y=sorted([lum(a),lum(b)],reverse=True); return round((x+.05)/(y+.05),2)
