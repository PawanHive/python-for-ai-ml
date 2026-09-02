# match-case example: (rarely used in real word application)

color = input("enter color : ")

match color : 
  case "green":
    print("Go")
  case "yellow":
    print("Slow")
  case "red":
    print("Stop")
  case _:
    print("Wrong color!")