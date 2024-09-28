# ta antikeimena ths class node tha antiprosopevoun tous komvous tou dentrou
# exei 7 idiothtes: 
# h sunolikh aksia (v) kai varos (w) pou exei apokthsei me ta antikeimena pou exei mesa to knapsack ston sugekrimeno komvo
# to deksi (right), to aristero paidi (left) kai o gonios (parent)
# mia lista antikeimenwn pou den exoun mpei akoma sto knapsack (node_object_list)
# mia lista antikeimenwn pou vriskontai mesa sto knapsack (node_objects_saved)
class Node:
    def __init__(self, vol, wt, list, p = None):
        self.v = vol
        self.w = wt
        self.right = None
        self.left = None
        self.parent = p
        self.node_object_list = list
        self.node_objects_saved = []


# ta antikeimena ths class object einai ta antikeimena pou tha prostethoun mesa sto knapsack
# exei 4 idiothtes:
# to onoma (n), h aksia (v), to varos (w) kai to ratio (r) (diairesh v dia w)
class object:
    def __init__(self, n, given_v, given_w ):
        self.name = n
        self.v = given_v
        self.w = given_w
        self.r = self.v/self.w


# h sunartisi ratio pernei ws parametro ena object (A) kai mas epistrefei to ratio (r) tou object
def ratio(A):
    return A.r


# h sunartisi knapsack ektelei ton algorithmo backtracking gia thn epilush tou knapsack
# pernei ws parametrous:
# 1) thn lista me ta antikeimena pou theloume na valoume sto knapsack (obj_list)
# 2) se poio komvo tou dentrou vriskete o algorithmos (currentNode)
# 3) thn riza tou dedrou
# 4) sth dedomenh xwrhtikothta tou knapsack se varos (C)
# 5) ton veltisto komvo
def knapsack(obj_list, currentNode, root, C, m_n):
    
    # elegxei oti vriskete sthn riza kai oti uparxei aristero paidi gia na termatisei to knapsack 
    # (den xreiazete na sunexisoume deksia ths rizas)
    if currentNode.left != None and currentNode == root:
        return m_n

    # elegxei oti uparxoun antikeimena gia na mpoun sto knapsack
    if obj_list:

        # elegxei oti uparxei xwros sto knapsack ston komvo pou vriskete o algorithmos
        if currentNode.w < C:

            # elegxei an o komvos exei aristero paidi
            # ean den exei, dhmiourgei aristero paidi gia afton ton komvo
            # prostetontas to v kai w tou antikeimenou pou tha mpei sto knapsack
            if currentNode.left == None:
                node = Node(obj_list[0].v + currentNode.v, obj_list[0].w + currentNode.w, obj_list[1:], currentNode)
                node.node_objects_saved = currentNode.node_objects_saved.copy()
                node.node_objects_saved.append(obj_list[0])
                currentNode.left = node
                currentNode = node

            # dhmiourgei deksi paidi gia ton komvo me ta idia v, w 
            # den prostethete antikeimeno
            else:
                node = Node(currentNode.v, currentNode.w, obj_list[1:], currentNode)
                node.node_objects_saved = currentNode.node_objects_saved.copy()
                currentNode.right = node
                currentNode = node

            # kanei update to m_v an vrethei megalutero (efoson den exei upervei to C)
            if currentNode.v > m_n.v and currentNode.w < C:
                m_n = currentNode
                
        # periptosh pou exei gemisei to knapsack
        # me mia while loop kanei bactrack sto dentro mexri na vrei komvo pou den exei deksi paidi gia ksanakalesei to knapsack()
        else:
            currentNode = currentNode.parent
            while(currentNode.right != None and currentNode.left != None):    
                currentNode = currentNode.parent

    # periptosh pou den uparxoun alla antikeimena gia na mpoun
    # me mia while loop kanei bactrack sto dentro mexri na vrei komvo pou den exei deksi paidi gia ksanakalesei to knapsack()            
    else:
        currentNode = currentNode.parent
        while(currentNode.right != None and currentNode.left != None):     
            currentNode = currentNode.parent
    
    # ksanakalei to knapsack kathe fora me updated lista 
    # mexri o algorithmos me backtracking na ftaseixksana sthn riza 
    # kai na exei aristero paidi
    results = knapsack(list(currentNode.node_object_list), currentNode,  root, C, m_n)
    
    # epistrefei to results stis recursive knapsack mexri na epistrepsei sto vasiko programma
    return results
                

    

def main():
    A1 = object("A1",8,2)
    A2 = object("A2",12,6)
    A3 = object("A3",9,3)
    A4 = object("A4",10,2)

    object_list = [A1,A2,A3,A4]

    # kanoume sort thn lista me ta antikeimena apo to pio valuable sto ligotero valuable
    object_list.sort(reverse = True, key=ratio)
    root = Node(0, 0, object_list)
    currentNode = root
    C = 12
    global max_node
    max_node = root

    max_node = knapsack(object_list, currentNode, root, C, max_node)

    print(max_node.v, [i.name for i in max_node.node_objects_saved])



if __name__== '__main__':
    main()