from block import Block
from position import Position

# 위의 코드는 게임 실행을 위한 라이브러리 호출

class LBlock(Block): # LBlock을 사용하기 위해 클래스 선언 - L 모양의 블록을 정의
	def __init__(self):
		super().__init__(id = 1) # 상위 클래스의 생성자를 호출하여 이 블록의 고유 id를 1로 설정
		self.cells = { # L모양 블록의 회전상태에 따른 각 셀의 위치를 정의
			0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
			1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
			2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
			3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
		}
		self.move(0, 3) # 초기 위치로 블록을 이동

class JBlock(Block): # J모양의 블록을 정의
    def __init__(self):
        super().__init__(id = 2) # 상위 클래스의 생성자를 호출하여 이 블록의 고유 id를 2로 설정
        self.cells = { # J모양 블록의 회전상태에 따른 각 셀의 위치를 정의
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3) # 초기 위치로 블록을 이동

class IBlock(Block): # I모양의 블록을 정의
    def __init__(self):
        super().__init__(id = 3) # 상위 클래스의 생성자를 호출하여 이 블록의 고유 id를 3으로 설정
        self.cells = { # I모양 블록의 회전상태에 따른 각 셀의 위치를 정의
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3) # 초기 위치로 블록을 이동

class OBlock(Block): # O모양의 블록을 정의
    def __init__(self):
        super().__init__(id = 4) # 상위 클래스의 생성자를 호출하여 이 블록의 고유 id를 4로 설정
        self.cells = { # O모양 블록은 회전해도 모양이 변하지 않으므로 하나의 상태만 정의
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4) # 초기 위치로 블록을 이동

class SBlock(Block): # S 모양의 블록을 정의
    def __init__(self):
        super().__init__(id = 5) # 상위 클래스의 생성자를 호출하여 이 블록의 고유 id를 5로 설정
        self.cells = { # S모양 블록의 회전상태에 따른 각 셀의 위치를 정의
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3) # 초기 위치로 블록을 이동

class TBlock(Block): # T모양의 블록을 정의
    def __init__(self):
        super().__init__(id = 6) # 상위 클래스의 생성자를 호출하여 id 값을 6으로 설정
        self.cells = { # T모양 블록의 회전상태에 따른 각 셀의 위치를 정의
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3) # 초기 위치로 블록을 이동

class ZBlock(Block): # Z모양의 블록을 정의
    def __init__(self):
        super().__init__(id = 7) # 상위 클래스의 생성자를 호출하여 id 값을 7으로 설정
        self.cells = { # Z모양 블록의 회전상태에 따른 각 셀의 위치를 정의
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3) # 초기 위치로 블록을 이동