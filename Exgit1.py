n1=float(input("tapez la note 1 entre 0 a 20 : "))
n2=float(input("tapez la note 2 entre 0 a 20 : "))
n3=float(input("tapez la note 3 entre 0 a 20 : "))
while n1>20 or n1<0 :
 n1=float(input("tapez la note 1 entre 0 a 20 : "))
while n2>20 or n2<0:
 n2=float(input("tapez la note 2 entre 0 a 20 : "))
while n3>20 or n3<0 :
 n3=float(input("tapez la note 3 entre 0 a 20 : "))
N=(n1+n2+n3)/3
if N>=16 :
 print("cet la moynne des note est:",N,"tres bien")
elif 14<=N>16 : 
 print("cet la moynne des note est:",N,"bien")
elif 12<=N>14 :
 print("cet la moynne des note est:",N,"accez bien")
elif 10<=N>12 :
 print("cet la moynne des note est:",N,"passable")
elif 10<N :
 print("cet la moynne des note est:",N,"insuffisant")