Algorithme moyenne_note
Variables
        N , n1 , n2 , n3 : reel
Debut
    ecrire(¨taper la note 1 et note 2 et note 3 : ¨)
    lire(n1 , n2 , n3)
    tantque n1>20 ou n1<0 faire
    ecrire("taper la note 2 un nombre entre 0 et 20 : ")
    lire(n1)
    fin tantque
    tantque n2>20 ou n2<0 faire 
    ecrire(¨taper la note 2 un nombre entre 0 et 20 : ¨)
    lire(n2)
    fin tantque
    tantque n3>20 ou n3<0 faire 
    ecrire(¨taper dans la  note 3 un nombre entre 0 et 20 : ¨)
     lire(n3)    
    fin tantque
N<=(n1+n2+n3)/3
si N>=16 alors:
ecrire("cet la moynne des note est:",N,"tres bien")
sinon
si 14=<N>16 alors: 
ecrire("cet la moynne des note est:",N,"bien")
sinon
si 12=<N>14 alors:
ecrire("cet la moynne des note est:",N,"accez bien")
sinon
si 10=<N>12 alors:
ecrire("cet la moynne des note est:",N,"passable")
sinon
si 10<N alors:
ecrire("cet la moynne des note est:",N,"insuffisant")
finsi
finsi
finsi
finsi
finsi
fin