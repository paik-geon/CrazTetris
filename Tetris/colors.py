class Colors: # 각 블록의 색을 지정하기 위해 RGB 값을 저장하기 위해 클래스 선언
	dark_grey = (26, 31, 40)
	green = (47, 230, 23)
	red = (232, 18, 18)
	orange = (226, 116, 17)
	yellow = (237, 234, 4)
	purple = (166, 0, 247)
	cyan = (21, 204, 209)
	blue = (13, 64, 216)
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)

	@classmethod
	def get_cell_colors(cls): # 현재 클래스를 호출하고 get_cell_colors라는 함수 정의
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue] # 각 색상을 반환
