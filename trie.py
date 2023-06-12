# !!Node 구현 (key, data, children)
# key : 값으로 입력될 문자
# data : 문자열의 종료를 알리는 플래그
# children : 자식노드 저장
class Node(object):
    def __init_(self, key, data=None): # data의 default값이 None이라는 의미?
        self.key = key # 
        self.data= data
        self.children ={}

# Trie 자료구조 구현
class Trie:
    def __init__(self):
        self.head =Node(None) # 루트노드는 빈노드
    
    # 문자열 삽입
    def insert(self, string):
        current_node=self.head #시작은 현재노드가 루트노드!

        for char in string: #문자열의 길이만큼 반복
            if char not in current_node.children:  # 1. 문자열의 특정 문자가 현재 노드의 자식 노드에 없다면
                current_node.children[char] =Node(char) # 문자열의 자식 노드로 삽입
            current_node = current_node.children[char] # 2. 그 자식노드를 현재노드로 만들기
        #1,2 반복 후
        current_node.data = string # 현재 노드의 플래그에 문자열 넣기

    # 문자열 탐색
    def search(self, string):
        current_node = self.head 
        # 탐색하기
        for char in string:
            if char in current_node.childeren: # 현재 노드의 자식 노드에 찾고자 하는 string의 문자(char)가 있다면
                current_node = current_node.children[char] # 일치하는 문자(다음노드)로 넘어가서 검사하기 위해서
            else:
                return False
        # 반복문이 종료되면 current_node에 찾고자 하는 문자열의 마지막 노드가 저장되어 있을 것
        
        # 탐색 종료 후 플래그 값이 있다면 treu, 없으면 false 
            # (app을 찾는데  apple만 있어도 true가 되지 않도록)
        # false는 당연히 찾고자 하는 문자열이 해당 trie에 존재하지 않는다는 의미!
        if current_node.data: 
            return True
        else:
            return False

    # 필수는 아니어 보임
    # prefix(접두어) 로 시작하는 단어를 찾고 배열로 리턴하는 함수
        # 예를들어 (replay, rebro, hi, high) 를 가지고 있는 trie중에서 prefix=re라면
        # [replay, rebro] 를 배열로 반환
    def starts_with(self, prefix):
        current_node = self.head # 시작노드는 루트 노드
        words=[] # 최종적으로 반환값을 저장하기 위한 빈 배열

        for pre in prefix:
            if pre in current_node.children:
                current_node = current_node.children[pre]
            else:
                return Node

        current_node = [current_node]
        next_node =[]
        # 핵심 logic
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node)!=0:
                current_node =next_node
                next_node=[]
            else: 
                break # 탈출
        return words