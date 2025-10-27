class User:
	def __init__(self, FIO: str, year: int, gender: str):
		self.FIO = FIO
		self.year = year
		self.gender = gender
		

	def get_info(self) -> str:
	    return f"{self.FIO}, день рождение - {self.year}, пол - {self.gender}"