## 히히 커밋
## 커밋 또 조지기



## 히힣 난 마스터
## 히히 난 데브다
## 히히 나도 데브다
## 마스터 변경
## 마스터 변경 
## hihi
## 히히

## 히히 풀 해야지

## ㅎ히히히 하하하하
## 이태균 금연해라
## 현윤선 배신자
## 상협이형 바보
## 건률이형 하고 싶은거 다해~

## 조준우는 몰카범
## 준우 담배 ㄱ?

## 상협이형 그만 종이접기해

## 다들 2열람실로~

## 히히히히히히히

## 다들 몇시까지 할거에요?
## 전 갑니다,,,

## 231018 마지막 git push test. Checkmate. - pjh
class TNode:
    def __init__(self, data, left, right):
        self.data=data
        self.left=left
        self.right=right
        
def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)
        
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')
        
def levelorder(n):
    q=[]
    q.append(n)
    while len(q) != 0 :
        n=q.pop(0) #데큐
        if n is not None:
            print(n.data, end=' ')
            q.append(n.left) #인큐
            q.append(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)
    

def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)
    

def calc_heiht(n):
    if n is None:
        return 0
    hLeft = calc_heiht(n.left)
    hRight = calc_heiht(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1
    
            
n9=TNode('B', None, None)
n8=TNode('A',None,None)
n6=TNode('/', n8, n9)
n7=TNode('C',None,None)
n4=TNode('*', n6, n7)
n5=TNode('D', None, None)
n2=TNode('*', n4, n5)
n3=TNode('E', None, None)
n1=TNode('+', n2, n3)

print('\n Pre-order : ', end='')
preorder(n1)
print('\n In-order : ', end='')
inorder(n1)
print('\n Post-order : ', end='')
postorder(n1)
print('\n Level-order : ', end='')
levelorder(n1)
print()

print("노드의 개수 = %d개" % count_node(n1))
print("단말의 개수 = %d개" % count_leaf(n1))
print("트리의 높이 = %d" % calc_heiht(n1))

2024
