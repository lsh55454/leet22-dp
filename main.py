class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        list = []
        min = ""
        min += '0'*n
        min += '1'*n
        min = int(min, 2)
        max = ""
        max += '1'*n
        max += '0'*n
        max = int(max, 2)

        for i in range(min, max+1):
            ''' 소문제로 분할하려면?
                스택으로 해서 왼쪽이 들어온 만큼 오른쪽을 만들어야 된다고 하면,
                이전과 다른 조합을 생성하려면, 그들을 code할 필요가 있다.
                0011   0101
                000111 001011 001101 010011 010101
                dfs? 로 탐색하다가 어느 지점에서든 )이 (의 개수보다 작거나 같게
                111000 110100 110010 110001                
            '''
            pst = ""
            i = f"{i:0{2*n}b}"
            for j in i:
                if j == '0':
                    pst += '('
                else:
                    pst += ')'
            
            if self.legality(pst):
                list.append(pst)
        return list

    def legality(self, pst: str) -> bool:
        l = 0
        for _ in pst:
            if (_ == '('): l += 1
            else: l -= 1
            if l < 0: return False
        
        return l==0
