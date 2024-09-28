from copy import deepcopy

# function gia na eleksw an to x einai mikrotero apo to teleftaio stoixeio mias grammis
def check(x,row, tableau):
    # epistrefw an to x > tou teleytaioy stoixeiou tou row pou vriskomaste
    return not x > tableau[row][-1]

# function gia thn prosthesi stoixeiou sto tableau me xrhsh bumping
def add(x,row, tableau):
    # an to row pou vriskomaste yparxei
    if row <= len(tableau)-1:
        # kai an mporw na eisagw to stoixeio sto telos h endiamesa tou row
        if check(x,row, tableau):
            # gia kathe stoixeio tou row pou vriskomaste
            for i, col in enumerate(tableau[row]):
                # an to stoixeio pou theloume na prosthesoume 
                # einai mikrotero tou stoixeiou pou vriskomaste
                # shmainei oti mporoume na eisagoume to stoixeio 
                # giati psaxmoune to prwto mikrotero stoixeio apo ta arister
                if x < col:
                    # eisagoume to stoixeio kai epistrefoume afto pou vgalame
                    temp = col
                    tableau[row][i] = x
                    return temp
            # an den mpainei pouthena epistrefoume to stoixeio x gia na dokimasoume se epomeno row
            return x
        else:
            # an mporoume na to valoume sto telos apla to eisagoume 
            # kai epistrefoume 0 afou den xreiazetai na prosthesoume allo
            tableau[row].append(x)
            return 0
    else: 
        # an exoume teleiwsei me ola ta rows alla 
        # den exoume valei to x tote to prothetoumai 
        # sto telos tou tableau
        tableau.append([x])
        return 0

            

# algorithmos gia prosthiki stoixeiou sto tableau
def bumping(x, tableau):
    # to counter elegxei kathe fora to row pou vriskomaste
    counter = 0
    while x != 0:
        # prosthetw to x stoixeio kai epistrefw sto x to stoixeio pou evgala
        x = add(x, counter, tableau)
        # paw sto epomeno row
        counter+=1
        # an den exw allo stoixeio na prosthesw spaw thn loupa

#kanw reset to tableau sto arxiko
def reset():
    return [[1,2,2,3,3],[2,3,5],[5,6]]

# function gia na epistrepsoume ston xrhsth 
# me vash 2 pinakes poio stoixeio prostethike me bumping ston prwto pinaka
def revBumping(endTableau, tableau):

    # elegxei an ta duo tableau exoun ton idio
    # arithmo seirwn
    if len(endTableau) == len(tableau):

        for i, row in enumerate(tableau):

            # elegxei an oi dyo seires twn tableau
            # exoun diaforetiko mhkos gia na psaksei to stoixeio
            if len(endTableau[i]) != len(tableau[i]):
                # apothikevei to noumero ths seiras
                counter = i
                start = [i, -1]
    
    # alliws kseroume oti to stoixio pou psaxnoume 
    # einai to teleftaio stoixeio ths teleftaias grammis
    else:
        counter = 3
        start = [-1,-1]
    
    # apothikevei to stoixeio pou tha afairesei
    x = endTableau[start[0]].pop(start[1])

    while counter >=1:

        # oso ta tableau exoun diafores stin kathe seira afairei to x
        if endTableau[counter-1] != tableau[counter-1]:
            x = remove(endTableau, x, counter-1)
        counter-=1
    return x
    

# afairei to x apo to endTableau
def remove(endTableau, x, counter):    

    # an to x einai to megalutero stoixeio ths seiras   
    if check(x,counter, endTableau):

        # elegxei pio einai to prwto stoixeio (temp) pou einai mikrotero
        # apo to x apo to telos ths seiras pros thn arxh
        # kai to antikathista me to x, epistrefontas to temp
        for i, col in enumerate(reversed(endTableau[counter])):
            if x > col:
                temp = col
                endTableau[counter][i] = x
                return temp
        return x
    
    # an to x einai to megalutero ths seiras, 
    # apothikevei to teleftaio stoixeio se temp, antikathista to x
    # me to teleftaio stoixeio kai epistrefei to temp
    else:
        temp = endTableau[counter][-1]
        endTableau[counter][-1] = x
        return temp
    
# function gia thn ektypwsh enos tableau 
def print_tableau(T):
    for col in T:
        print(col)

# function pou upologizei to product 2 Tableau xrhsimopoiontas bumping
def prod(T, U):
    # xreiazetai na prosthesoume 
    # ta stoixeia apo katw pros 
    # ta panw aristera pros deksia
    for i in reversed(U):
        for j in i:
            bumping(j, T)

# function pou dhmiourgei ena skew Tableau, 
# kai to epistrefei mazi me ta sxhmata twn 
# tableau pou xrhsimopoithikan gia thn kataskeyh
def generateSkew(T, U):
    # pairnei prwta to sxhma tou tableau pou tha bei katw apo to mhdeniko matrix
    l = len(T[0])
    # kai epeita tou pinaka pou tha mpei sto plai
    m = len(U)

    # ftiaxnei ena mhdeniko matrix
    skewTableau = [[0 for i in range(l)] for j in range(m)]

    # gia kathe stoixeio tou pinaka pou tha mpei sta aristera
    for i,row in enumerate(U):
        for j in row:
            # to prosthetei sto swsto row
            skewTableau[i].append(j)

    # gia kathe stoixeio tou pinaka pou tha mpei apo katw
    for i,row in enumerate(T):
        skewTableau.append(row)

    return skewTableau, l, m

# elegxei an mporei na ginei enallagh sthn thesh
def can_slide(T, x, y):
    try:
        # prospathei na dei prwta an yparxei apo katw stoixeio kai ayto den einai 0
        down = str(T[x + 1][y] != 0)
    except IndexError:
        # se periptwsh pou den yparxei kan apo katw stoixeio 
        # de theloume na epistrepsoume oute true oute false
        down = "error"
            
    # shmeiwsh: to type casting se string vohthaei 
    # na apofygoume tyxon provlhmata se periptwsh 
    # epistrofhs timwn True, "error" gia paradeigma
    try:
        right = str(T[x][y + 1] != 0)
    except IndexError:
        right = "error"

    # an to stoixeio einai 0
    if  T[x][y] == 0: 
        # kai vriskete se ekswterikh gwnia
        if down == "error" and right == "error":
            #afairese to
            T[x].pop(y)

        # kai epestrepse ta apolesmata tou querry
        return down, right

# vres to prwto blackbox pou einai eswterikh gwnia
def find_slide(T, bb_cols, bb_rows):
    # arkei na elenksoume mono gia kathe i, j sta rows kai ta cols tou black box(tou sxhmatos lxm)
    for i in range(bb_rows):
        for j in range(bb_cols):
            try:
                # prospathoume na doume an yparxei thesh deksia kai katw apo to kouti pou vriskomaste
                x, y = can_slide(T,i,j)
            except:
                # an apotyxoume pame sthn epomenh epanalhpsh
                continue

            # an exei kai katw kai deksia vrhkame thn prwth eswterikh gwnia.
            if x == "True" and y == "True":
                return i, j
    
    #den yparxei eswterikh gwnia, ara stelnw -1,-1 gia eksodo apo sliding
    return -1,-1


# algorithmos pou kalei to sliding gia na petyxei thn enallagh 2 timwn
def slide(T, x, y, verbose = False):
    # prwta pernei to apo katw kai deksia kelh.
    down,right = can_slide(T, x, y)
    # an kai ta 2 apo afta ta kelia exei timh, mporei na ginei enallagh deksia kai katw
    # shmeiwsh: den mas endiaferei na checkaroume sthn sygkekrimenh periptwsh 
    # gia to an to x,y einai eswterikh gwnia giati sigoura gia na kleithei h slide
    # apaiteitai h x,y na einai hdh eswterikes.
    if down != "error" and right != "error":
        # an to deksia stoixeio einai mikrotero tou apo katw 
        # (pou kanonika exei protaireothta se periptwsh pou katw == deksia)
        if T[x][y+1] < T[x+1][y]:
            # kane thn enallagh
            T[x][y] = T[x][y+1]
            T[x][y+1] = 0
            # kai apothikeyse thn nea thesh tou black box(0)
            new_x = x
            new_y = y+1
        else:
            # se kathe allh periptwsh kane thn antimetathesh meto apo katw stoixeio
            T[x][y] = T[x+1][y]
            T[x+1][y] = 0
            # kai apothikeyse pali thn nea thesi tou black box(0)
            new_x = x+1
            new_y = y
    # an ginete na ginei enallagh mono pros ta katw
    elif down != "error" and right == "error":
        # kane thn enallagh
        T[x][y] = T[x+1][y]
        T[x+1][y] = 0
        new_x = x+1
        new_y = y
    # an ginete na ginei enallagh mono pros ta deksia
    elif down == "error" and right != "error":
        T[x][y] = T[x][y+1]
        T[x][y+1] = 0
        new_x = x
        new_y = y+1
    # alliws exei ginei h enallagh epityxws kai eksafanisame ena blackbox (0)
    else:
        return True
    
    if verbose:
        print(f"swapping: {T[x][y]}")
        print_tableau(T)
    
    #synexise na kaneis slide to kainourgio stoixeio mexri na 
    # ftasei to blackbox se ekswterikh gwnia kai na eksafanistei
    slide(T, new_x, new_y, verbose)
    return True

# algortihmos sliding pou xrhsimopoieitai gia ton ypologismo tou skew tableau
def sliding(T, cols, rows, verbose = False):
    # prwta ypologizei poio black box (0) tha kounithei
    x, y = find_slide(T, cols, rows)
    if x == -1:
        # an den vrei tote shmainei oti to sliding oloklhrwthike
        return
    
    # an ginei to slide epitixos:
    if slide(T, x, y, verbose):
        # kai an mporei kalei ton eyato tou, gia na synexistei to slide
        sliding(T, cols, rows,verbose)



def main():

    #arxikopoioumai tableau kai metavlhtes x,y,z gia bumping
    tableau = [[1,2,2,3,3],[2,3,5],[5,6]]

    x = 2
    y = 3
    z = 4

    # arxizoumai kai kaloume tis bumping metavlhtes, 
    # emfanizoume ta tableau kai telos kanoume reset ta tableau
    # epishs ftiaxnoume ena copy tou telikou tableau pou tha 
    # xrhsimopoiethei meta sto reverse bumping
    bumping(x, tableau)
    print_tableau(tableau)
    print("-------------------")
    endTableau1 = deepcopy(tableau)
    tableau = reset()

    bumping(y, tableau)
    print_tableau(tableau)
    print("-------------------")
    endTableau2 = deepcopy(tableau)
    tableau = reset()

    bumping(z, tableau)
    print_tableau(tableau)
    print("-------------------")
    endTableau3 = deepcopy(tableau)
    tableau = reset()

    # kaloume to reverse bumping gia na vroume to x,y,z pou prosthesame prin sta endtableau
    print(revBumping(endTableau1, tableau))
    print(revBumping(endTableau2, tableau))
    print(revBumping(endTableau3, tableau))
    
    # arxikopoioume pinakes T kai U gia tous pollaplasiasmous
    T = [[1,2,4], 
         [3]]
    
    U = [[1,2,5], 
         [3,4], 
         [6]]
    
    # xrhsimopoioume to deepcopy gia na 
    # kanoume clone ton T pinaka pou tha xrhsimopoiethei sto prod
    # kaloume thn prod kai ektypwnoume to apotelesma
    t_prod = deepcopy(T)
    prod(t_prod, U)
    print("product of T*U:")
    print_tableau(t_prod)
    
    # paragoume to skewTable kathws kai ta sxhmata l kai m me vash ta tables T, U 
    SkewT, l, m = generateSkew(T, U)

    # kaloumai thn sliding
    sliding(SkewT, l, m)

    print("Rect(T*U):")

    # katharizoume ta empty kelia tou skewTable
    remove = []
    for i in SkewT:
        if not i:
            remove.append(i)

    for i in remove:
        SkewT.remove(i)

    # Ektyponoume to SkewTableau 
    print_tableau(SkewT)




if __name__== '__main__':
    main()