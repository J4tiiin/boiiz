import mechanize
import facebook
import time

# Browser
br = mechanize.Browser()



# Browser settings
br.set_handle_equiv( True )
br.set_handle_gzip( True )
br.set_handle_redirect( True )
br.set_handle_referer( True )
br.set_handle_robots( False )


br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 999999 )

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/1608071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]
br.open("https://www.facebook.com/")
br.geturl()

print ("[+] TH3 S4NG4 RUL3XX [+]")
print ("[+] BY J4T1N S1NGH [+]")
msg=str(input("Enter your Token : "))
poct=str(input("Enter your post Link :  "))
npl=str(input(" Enter your np last line :  "))
aa= "7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P 3 '-,-'  ^8^H^()^ <3 '-,-'  XD3 '-,-'  M=3 '-,-'  M=^ <(") !!(=+=) L^()^ <3 '-,-'  WD^ <(")  D^ <(") ^ <(") L K :P R 7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^()^ <3 '-,-'   M=^ <(") !!(=+=) C^H=^()^ <3 '-,-'  UD J^ <(") U^6^ <(")  L^()^ <3 '-,-'  WD3 '-,-'  K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W ^ <(") ^ <(") J^ <(")  ^8^3 '-,-' HC^()^ <3 '-,-'  D K :P 3 '-,-'  L^()^ <3 '-,-'  WD3 '-,-'  =]] <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


ss= "^8^H^()^ <3 '-,-'  XD!!(=+=)K :P 3 '-,-'  7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P 3 '-,-'  ^8^^()^ <3 '-,-'  ^()^ <3 '-,-'  R K :P ^()^ <3 '-,-'   M=^ <(") !!(=+=) C^H=3 '-,-' 3 '-,-' R J^ <(") U^6^ <(")  L^()^ <3 '-,-'  WD3 '-,-'  K :P 3 '-,-'  D!!(=+=)^^3 '-,-'  7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^()^ <3 '-,-'   M=^ <(") !!(=+=) M=^ <(") R7 :D 3 '-,-'  J^ <(") U ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  ^8^^ <(") CC^H=WW =]] <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


dd="F!!(=+=)R 7 :D U M=3 '-,-' R^ <(")  L^()^ <3 '-,-'  WD^ <(")  C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  X^^ <(")  H3 '-,-' H3 '-,-' H3 '-,-' H3 '-,-' H3 '-,-' H :D 7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ ^8^H!!(=+=) ^ <(") !!(=+=)X^ <(")  H!!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  X7 :D !!(=+=) H^ <(") !!(=+=) M=3 '-,-' R^ <(")  L^()^ <3 '-,-'  WD^ <(")  =]] <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


ff= "7 :D 3 '-,-' R!!(=+=) M=^ <(") ^ <(")  ^8^3 '-,-' H3 '-,-' ^ K :P ^()^ <3 '-,-'   M=^ <(") !!(=+=) ^8^!!(=+=)C^H= R^()^ <3 '-,-'  ^ <(") D P3 '-,-'  L^ <(") ^6^ <(")  K :P R K :P R K :P 3 '-,-'  M=^ <(") !!(=+=) D^ <(") ^C3 '-,-'  K :P R^ <(")  DU^6^ <(")  ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  L^()^ <3 '-,-'  WD3 '-,-'  F!!(=+=)R 7 :D 3 '-,-' R!!(=+=) M=^ <(") ^ <(")  ^8^3 '-,-' H3 '-,-' ^ K :P ^ <(")  K :P Y^ <(")  H^ <(") ^ <(") L H^()^ <3 '-,-'  6^ <(")  H3 '-,-' ^ ^8^H!!(=+=)K :P H^ <(") R!!(=+=) K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W :D :D <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


gg= "7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^()^ <3 '-,-'   R^ <(") P3 '-,-'  K :P RK :P 3 '-,-'  Y^ <(") H!!(=+=) P3 '-,-'  XUL^ <(")  DU^6^ <(")  L^()^ <3 '-,-'  WD3 '-,-'  X^ <(") ^8^X3 '-,-'  C^H=UD^3 '-,-'  W^ <(") L3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W =]] <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[H^9^T^3^R___((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #ALON3_RUL3XXX_______H_3_R_3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


hh= "X^ <(") L^ <(")  ^()^ <3 '-,-'  K :P ^ <(") ^ <(") 7 :D  L3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W 7 :D U ^ <(") Y^ <(")  7 :D H^ <(")  ^8^^ <(") ^ <(") P X3 '-,-'  L^ <(") D^3 '-,-'  R^ <(") ^ <(") ^D K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W 7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  7 :D ^()^ <3 '-,-'   R^()^ <3 '-,-'  Y3 '-,-'  J^ <(") ^ <(")  RH!!(=+=) H^ <(") !!(=+=) ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  D!!(=+=)^^3 '-,-'  ^ <(") !!(=+=)X^ <(")  R^()^ <3 '-,-'  7 :D !!(=+=) H^ <(") !!(=+=) 7 :D 3 '-,-' R!!(=+=) M=^ <(") ^ <(")   :D :P <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #H4TT34___P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


jj= "7 :D 3 '-,-' R!!(=+=) M=^ <(") ^ <(")  K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^ <(") !!(=+=)X3 '-,-'  K :P ^ <(") L^ <(") P RH!!(=+=) H^ <(") !!(=+=) J^ <(") R^ <(")  D3 '-,-' K :P H ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W 7 :D U 7 :D ^()^ <3 '-,-'   ^ <(") ^8^ R^()^ <3 '-,-'   D!!(=+=)Y^ <(")  H^ <(") !!(=+=) ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  L^()^ <3 '-,-'  WD3 '-,-'  M=^ <(") ^ <(")  K :P 3 '-,-'  D!!(=+=)^^3 '-,-'  :D <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ 4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


kk= "M=^ <(") 7 :D H3 '-,-' RC^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  D!!(=+=)^^3 '-,-'  M=UJH3 '-,-'  ^^ <(") W P^ <(") 7 :D ^ <(")  7 :D H^ <(")  H^ <(") W^ ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  D!!(=+=)^^3 '-,-'  K :P !!(=+=) 7 :D U !!(=+=)7 :D ^^ <(")  R^()^ <3 '-,-'   D3 '-,-' 6^ <(")  :^()^ <3 '-,-'   ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  LW^()^ <3 '-,-'  D3 '-,-'  :V !!(=+=)7 :D ^^ <(")  K :P ^()^ <3 '-,-'  !!(=+=) R^()^ <3 '-,-'  7 :D ^ <(")  H^ <(") X :^()^ <3 '-,-'   <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #H4TT34___P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


ll= "C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P 3 '-,-'  P3 '-,-' 3 '-,-' XU M=3 '-,-' R3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W 7 :D 3 '-,-' RU!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^()^ <3 '-,-'   7 :D ^()^ <3 '-,-'   M=^ <(") !!(=+=) ^ <(") ^ <(") J K :P !!(=+=)LX^ <(")  K :P !!(=+=)LX^ <(") ^ <(")  K :P 3 '-,-'  H!!(=+=) M=^ <(") ^ <(") R DU^6^ <(")  R^ <(") ^ <(") ^D K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W :P <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


zz= "K :P !!(=+=)7 :D ^^ <(")  K :P ^ <(") L^ <(") P7 :D ^ <(")  H^ <(") !!(=+=) Y3 '-,-'  M=3 '-,-' R^ <(")  ^8^^ <(") C^H=^ <(")   :V !!(=+=)XK :P !!(=+=) M=^ <(") ^ <(")  K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^()^ <3 '-,-'   7 :D ^()^ <3 '-,-'   M=^ <(") !!(=+=) C^H=3 '-,-' 3 '-,-' R M=^ <(") RU^6^ <(")  R^ <(") ^D!!(=+=)!!(=+=)!!(=+=) K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W  :V 7 :D U ^ <(") ^ <(") J ^^ <(") W M=3 '-,-' R^ <(")  L^()^ <3 '-,-'  WD^ <(")  C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  X3 '-,-' 6^ <(")  :P <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


xx= "R^ <(") ^D!!(=+=)!!(=+=) K :P 3 '-,-'  ^ <(") UL^ <(") ^ <(") D 7 :D U K :P R3 '-,-' 6^ <(")  ^8^^ <(") ^ <(") P X3 '-,-'  F^ <(") D^ <(") ^ <(")  ^ <(") J^ <(") ^ <(")  ^8^3 '-,-'  L^()^ <3 '-,-'  WD3 '-,-'  7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^()^ <3 '-,-'   7 :D ^()^ <3 '-,-'   M=^ <(") ^ <(") R H!!(=+=) D!!(=+=)Y^ <(")  HU^ =]] <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


cc= "^ <(") ^8^ 7 :D 3 '-,-' R!!(=+=) ^8^^ <(") ^ <(") J!!(=+=)!!(=+=) K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^()^ <3 '-,-'   J^ <(") R^ <(")  M=^ <(") !!(=+=) M=^ <(") RU L^()^ <3 '-,-'  WD3 '-,-'  K :P 3 '-,-'  ^8^^ <(") ^ <(") L :V :D =]] <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


vv= "^8^X 7 :D U K :P ^ <(") L^ <(") P^^ <(")  ^^ <(") H!!(=+=) M=3 '-,-' R3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W  :V 7 :D U K :P ^ <(") P7 :D ^ <(")  H^ <(") !!(=+=) 7 :D ^()^ <3 '-,-'   M=3 '-,-' R3 '-,-'  L^()^ <3 '-,-'  WD3 '-,-'  K :P ^()^ <3 '-,-'   XH^ <(") RM= ^ <(") J^ <(") 7 :D ^ <(")  H^ <(") !!(=+=) H3 '-,-' H3 '-,-' H3 '-,-' H3 '-,-' H3 '-,-' H3 '-,-' H3 '-,-'   :D =]] <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


bb= "H!!(=+=)JR3 '-,-'  K :P !!(=+=) ^()^ <3 '-,-'  L^ <(") ^ <(") ^ <(") D  :P X^ <(") L^ <(")  7 :D 3 '-,-' R^ <(")  ^8^^ <(") ^ <(") P H!!(=+=)JD^ <(")  7 :D ^()^ <3 '-,-'   7 :D U ^8^H!!(=+=) H!!(=+=)JD^ <(")  :V <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


nn= "6^ <(") ^ <(") ^DUXX K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W 7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  M=3 '-,-'  M=^ <(") !!(=+=) X^ <(") RX^()^ <3 '-,-'   K :P ^ <(") ^ <(")  7 :D 3 '-,-' L L^ <(") 6^ <(")  K :P 3 '-,-'  7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^()^ <3 '-,-'   M=^ <(") !!(=+=) P^ <(") ^ <(") ^!!(=+=) H!!(=+=) P^ <(") ^ <(") ^!!(=+=) K :P R DU^6^ <(")  H3 '-,-' H3 '-,-' H3 '-,-' H :D <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


mm= "XU^ <(") R K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W  :P X^ <(") L^ <(")  6^ <(") ^ <(") ^D3 '-,-'  ^^ <(") ^ <(") L!!(=+=) K :P 3 '-,-'  K :P !!(=+=)D3 '-,-'  :D H3 '-,-' H3 '-,-' H3 '-,-' H3 '-,-' H3 '-,-' H :V 7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  M=3 '-,-'  M=^ <(") !!(=+=) ^ <(") K :P R^()^ <3 '-,-'  7 :D 7 :D  D^ <(") ^ <(") L DU ^8^3 '-,-'  ^8^H^()^ <3 '-,-'  XDK :P 3 '-,-'   :P H3 '-,-' H3 '-,-' H3 '-,-' HH3 '-,-' 3 '-,-' HH3 '-,-'  :D <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


ww= "M=3 '-,-' R^ <(")  L^()^ <3 '-,-'  WD^ <(")  ^ <(") ^ <(") ^ <(") J F3 '-,-' LL K :P R ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W D3 '-,-' K :P H 7 :D 3 '-,-' R!!(=+=) M=^ <(") ^ <(")  ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^ <(") !!(=+=)X3 '-,-'  F^ <(") 7 :D !!(=+=) J^ <(") ^ <(")  RH!!(=+=) H^ <(") !!(=+=) ^8^H!!(=+=)K :P H^ <(") ^ <(") R!!(=+=) K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W K :P !!(=+=)L^ <(") X ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD :D <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


ee= "7 :D U K :P !!(=+=)LX7 :D 3 '-,-'  J^ <(") ^ <(") Y3 '-,-' 6^ <(")  M=3 '-,-' R^ <(")  L^()^ <3 '-,-'  WD^ <(")  7 :D 3 '-,-' R!!(=+=) M=^ <(") ^ <(")  K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  M=3 '-,-'  J^ <(") ^ <(") 7 :D 3 '-,-'  R^ <(") H3 '-,-' 6^ <(")  ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  D!!(=+=)^^3 '-,-'  ^8^^ <(") ^ <(") P X3 '-,-'  L^ <(") D7 :D ^ <(")  H^ <(") !!(=+=) ^^ <(") W 7 :D ^()^ <3 '-,-'   L!!(=+=)K :P H^3 '-,-'  ^8^H!!(=+=) ^^ <(") W ^ <(") 7 :D ^ <(")  H^ <(") !!(=+=)=]] <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


tt= "7 :D 3 '-,-' R!!(=+=) D^ <(") ^ <(") ^ <(") D!!(=+=)!!(=+=) K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  M=3 '-,-'  M=^ <(") !!(=+=) L3 '-,-' D!!(=+=) K :P ^ <(") ^ <(")  7 :D 3 '-,-' L L^ <(") 6^ <(")  K :P 3 '-,-'  M=^ <(") !!(=+=) ^ <(") !!(=+=)X^ <(")  M=^ <(") ^ <(") R M=^ <(") RU^6^ <(")  K :P !!(=+=) 7 :D 3 '-,-' R!!(=+=) D^ <(") ^ <(") D!!(=+=)!!(=+=) K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  K :P ^ <(") L^ <(") P U7 :D H3 '-,-' 6!!(=+=) ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W H3 '-,-' H3 '-,-' H3 '-,-' H3 '-,-' H :D <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3______P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #S9NG9___RUL3XXX_______H_3_R_3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


yy= "7 :D 3 '-,-' R!!(=+=) ^8^^ <(") ^ <(") J!!(=+=) K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  M=3 '-,-'  M=^ <(") !!(=+=) XU^3 '-,-' H^ <(") R!!(=+=) L^()^ <3 '-,-'  WD3 '-,-'  K :P 3 '-,-'  ^ <(") 7 :D ^ <(") K :P D3 '-,-' 3 '-,-' R L^ <(") 6^ <(")  DU^6^ <(")  R^ <(") ^ <(") ^D K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W  K :P !!(=+=) 7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) ^8^^()^ <3 '-,-'  ^()^ <3 '-,-'  R K :P ^ <(") P7 :D 3 '-,-'  F!!(=+=)R3 '-,-' 6!!(=+=) L^()^ <3 '-,-'  WD3 '-,-'  :D <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #4LL__CH0T3_____P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TX___Y0UR____D4DDY___H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"


op= "XD^ <(") L^ <(")  8| ^()^ <3 '-,-'  K :P ^ <(") ^ <(") 7 :D  L3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W 7 :D U ^ <(") Y^ <(")  7 :D H^ <(")  ^8^^ <(") ^ <(") P X3 '-,-'  L^ <(") D^3 '-,-'  R^ <(") ^ <(") ^D K :P 3 '-,-'  ^8^^ <(") CC^H=3 '-,-' W 7 :D 3 '-,-' R!!(=+=) ^8^3 '-,-' H3 '-,-' ^ K :P !!(=+=) C^H=^()^ <3 '-,-'  ^()^ <3 '-,-'  7 :D  7 :D ^()^ <3 '-,-'   R^()^ <3 '-,-'  Y3 '-,-'  J^ <(") ^ <(")  RH!!(=+=) H^ <(") !!(=+=) ^8^3 '-,-' H3 '-,-' ^ C^H=^()^ <3 '-,-'  UD K :P 3 '-,-'  D!!(=+=)^^3 '-,-'  ^ <(") !!(=+=)X^ <(")  R^()^ <3 '-,-'  7 :D !!(=+=) H^ <(") !!(=+=) 7 :D 3 '-,-' R!!(=+=) M=^ <(") ^ <(")   :D :P <3 :D [[ <(") N^ <3 :D  ||> _____ <3 <3 (Y) [[ #H4TT34___P^1^L^3__((__||__))___P^3 ]] ____ 3:) ____ <3 ____ ! ____ ]]  #1TXX_____Y0UR_____D9DDY______H3R3 ]] (Y) <3 (^^^) (Y) <(") (Y) <3 (Y) (Y) = <3"






token=msg
def auto_post():
 
 while True:
    graph = facebook.GraphAPI(access_token=token,version='2.8')
    
    graph.put_object(parent_object= poct, connection_name='comments',message=aa+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    
    graph.put_object(parent_object=poct, connection_name='comments',message=ss+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object=poct, connection_name='comments',message=dd+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object=poct, connection_name='comments',message=ff+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object= poct, connection_name='comments',message=gg+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    
    graph.put_object(parent_object=poct, connection_name='comments',message=hh+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object=poct, connection_name='comments',message=jj+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object=poct, connection_name='comments',message=kk+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object= poct, connection_name='comments',message=ll+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    
    graph.put_object(parent_object=poct, connection_name='comments',message=zz+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object=poct, connection_name='comments',message=xx+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object=poct, connection_name='comments',message=cc+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object= poct, connection_name='comments',message=vv+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    
    graph.put_object(parent_object=poct, connection_name='comments',message=bb+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object=poct, connection_name='comments',message=nn+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object=poct, connection_name='comments',message=mm+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object= poct, connection_name='comments',message=ww+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    
    graph.put_object(parent_object=poct, connection_name='comments',message=ee+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)
    graph.put_object(parent_object=poct, connection_name='comments',message=tt+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(10)
    graph.put_object(parent_object=poct, connection_name='comments',message=yy+npl)
    print ("COMM3NT S3NT DON3!\n")
    time.sleep(160)

    
if __name__ == '__main__':
    auto_post()
    print ("COMM3NT S3NT DON3!\n")
#YOUR D9DDY J4T1N DON H3R3
