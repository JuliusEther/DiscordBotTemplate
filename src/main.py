from logs import Logs
from bot.core import Core

def main():
	Logs.Init()
	Core.Init(Logs.GetLogger())
	

if __name__ == "__main__":
	main()
