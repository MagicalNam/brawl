import random
import math
import cmath
import time

voters = [
  {
      "name": "Communist",
      "abreviation": "Cmu",
      "convinced_player_1" : 0,
      "convinced_player_2" : 0,
      "important_topics" : [],
      "good_lines" : [
        "YAAAAAAAAA!!!!!!!!!!!!!",
        "CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP",
        "FINALY!!!!",
        "Viva La Revolution!!",
      ],
      "neutral_lines" : [
        "Yawn",
        "-----",
        "And what exactly does that do for the people?",
        "Make a real difference!",
      ],
      "bad_lines" : [
        "SHAME",
        "BOOOOOOOOO",
        "You are an Enemy of the Working Class!",
        "What are you doing here??",
      ],
  },
  {
      "name": "Socialist",
      "abreviation": "Soc",
      "convinced_player_1" : 0,
      "convinced_player_2" : 0,
      "important_topics" : [],
      "good_lines" : [
        " CLAP CLAP CLAP CLAP",
        "CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP",
        "WWOOOOOOOO!!!!",
        "YESSSS!!!!!!!!!!!!!!!!!!!!!!!!!",
      ],
      "neutral_lines" : [
        "*Gasp*",
        "*Yawn*",
        "---------",
        "-------------------------------------",
      ],
      "bad_lines" : [
        "BOOOOOOOOOOOOOOOOO",
        "SCANDAL!!",
        "WHAT?!?!?!?!?!?!",
        "BBBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
      ],
  },
  {
      "name": "Progressive",
      "abreviation": "Prg",
      "convinced_player_1" : 0,
      "convinced_player_2" : 0,
      "important_topics" : [],
      "good_lines" : [
        "WOOOOOOOOOOOOOOOOOOO",
        "FINALY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
        " CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP",
        "CLAP CLAP CLAP CLAP CLAP CLAP CLAP",
      ],
      "neutral_lines" : [
        "------------------",
        "------",
        "--------------------------------------",
        "*ZZZZzzzzzzZZZzzzzZZZZzzzzzz ZZZzzzz*",
      ],
      "bad_lines" : [
        "boooooooooooooooo!",
        "BBBBBBBBBBBBBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!",
        "BOOOOOOOOOOOOOOOOOO",
        "WHAT?!?!"
      ], 
  },
  {
      "name": "Centrist",
      "abreviation": "Ctr",
      "convinced_player_1" : 0,
      "convinced_player_2" : 0,
      "important_topics" : [],
      "good_lines" : [
        " CLAP CLAP CLAP CLAP CLAP CLAP CLAP",
        "clap clap clap clap clap",
        "clap clap clap clap clap clap clap clap clap clap clap clap clap clap clap",
        " CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP!!!!!",
      ],
      "neutral_lines" : [
        "clap clap clap",
        "--------------",
        "...................",
        "zzzZZZZZzzzzZZZZZZZZzzz ZZZZzzzz",
      ],
      "bad_lines" : [
        "BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!",
        "BBBUUUUUUUUUUUUUU!",
        "BOOOOOO!!!",
        "BUUUUUUUUUUUUUUUUUUUUUUUU",
      ],
  },    
  {
      "name": "Libertarian",
      "abreviation": "Lib",
      "convinced_player_1" : 0,
      "convinced_player_2" : 0,
      "important_topics" : [],
      "good_lines" : [
        "clap clap clap clap clap clap clap clap!!!",
        "  clap! clap! clap! clap! clap! clap! clap! clap! clap! clap!",
        " clap clap clap clap clap clap clap clap clap clap clap clap",
        "CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP!!!!",
      ],
      "neutral_lines" : [
        "zzzZZZZzzzzzzZZZZZzzzzzz",
        "ZZZZZZZZzzzzzzZZZzzzz",
        "ZZZzzzZZZzzz",
        "ZZZZZZZZzzzzzzzzzzZZZZZZZZZZzzzzzzzzZZZZZzzzzz",
      ],
      "bad_lines" : [
        "Boooooo!!!!!!!!!!!!!!!!!!!!!1",
        "BOOOO!!!!!!!!!!!!!!!!!!",
        "Booo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
        "bOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!",
      ],
  },
  {
      "name": "Cristian-democrat",
      "abreviation": "Cri",
      "convinced_player_1" : 0,
      "convinced_player_2" : 0,
      "important_topics" : [],
      "good_lines" : [
        "God loves you!",
        "JESUS",
        "Clap clap clap clap clap clap clap!!!!11",
        "  CLAP CLAP CLAP CLAP CLAP CLP CLAP CLAP!!!!!",
      ],
      "neutral_lines" : [
        "------------",
        "----",
        "------ ---------- --------",
        "*ZZZzzzZZZZzzzzzz*",        
      ],
      "bad_lines" : [
        "They are SATAN",
        "THE RAPTURE IS COMMING",
        "BOOOOOO!!!!!!!!!",
        "How could you!?",
      ],
  },
  {
      "name": "Moderate",
      "abreviation": "Mod",
      "convinced_player_1" : 0,
      "convinced_player_2" : 0,
      "important_topics" : [],
      "good_lines" : [
        "WOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!",
        "WWOOOOOOOOO!!!!!",
        "YAAAAAAAAAAAAAAA!!!!!",
        "WOOOO!!! WOOOOOOOOOO!!!!!",
      ],
      "neutral_lines" : [
        "This is so borring",
        "*GASP*....",
        "*YAWN*.......",
        "-------------------------------------------",
      ],
      "bad_lines" : [
        "This is outrageous!",
        "BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!",
        "BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!",
        "BOOOOOOOOOOOOOOOOOOO!!! BOOOOOOOOOOOO!!!!!!!",
      ],
  },
  {
      "name": "Republican",
      "abreviation": "Rpb",
      "convinced_player_1" : 0,
      "convinced_player_2" : 0,
      "important_topics" : [],
      "good_lines" : [
        "WOOOOOOOOOOOOOOOOOOOOO",
        "CLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAP",
        "CLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAP",
        "CLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAP",
      ],
      "neutral_lines" : [
        "BORRING!!!!",
        "BORRING!!",
        ".....",
        "....",
      ],
      "bad_lines" : [
        "BOOOOO BOOO BOOOOOOO",
        "BOOOO!!! BOOOOOOO!!!! BOOOOOOOOOO!! BOOOOOOOOO!!!",
        " BOOOOOOOOOOO",
        "Boooooo!!! Booooooooooooo!!!!",
      ],
  },
]

audiences = [
  {
    "name": "Swedish Electorate",
    "constituents": [1, 1, 1, 1, 1, 1, 1, 1],
  },
  {
    "name": "American Electorate",
    "constituents": [0, 2, 1, 0, 2, 2, 1, 3],
  },
  {
    "name": "Umea Public",
    "constituents": [2, 1, 3, 1, 1, 0, 1, 1],
  },
  {
    "name": "New York Public",
    "constituents": [1, 2, 1, 0, 1, 2, 3, 0],
  },
  {
    "name": "University Campus",
    "constituents": [3, 0, 3, 0, 1, 0, 0, 1],
  },
  {
    "name": "Trump Rally",
    "constituents": [0, 0, 0, 0, 1, 2, 1, 4],
  }
]

speakers = [
 {
    "name": "Burney Sanders",
    "arguments": [0, 1],
    "opponent_arguments": [],
    "rallys": [],
    "power1": "I call Bulshit",
    "power2": "The Facts says No",
    "lines": [
      "Line",
      "Line",
      "Line",
      "Line",
    ],
  },
  {
    "name": "Donald Trump",
    "arguments": [0, 2],
    "opponent_arguments": [],
    "rallys": [],
    "power1": "Corruption",
    "power2": "Make America Great Again",
    "lines": [
      "MAKE AMERICA GREAT AGAIN",
      "They are awfull scum. Very bad people indeed",
      "I AM THE ONLY ONE WHO CAN FIX THIS",
      "THEY ARE THE WORST PEOPLE. THE WORST PEOPLE IN THE ENTIRE WORLD",
    ],
  },
{
    "name": "Zorahn Mambdani",
    "arguments": [1, 3],
    "opponent_arguments": [],
    "rallys": [],
    "power1": "Big D#ck Energy",
    "power2": "Fill the holes",
    "lines": [
      "FOR ORDINARY PEOPLE",
      "Because we actually care about YOU",
      "You do NOT stand alone in this, we will fix this.",
      "WE will fix it.",
    ],
  },
{
    "name": "Elon Musk",
    "arguments": [2],
    "opponent_arguments": [],
    "rallys": [],
    "power1": "Buy it",
    "power2": "Shadowbann",
    "lines": [
      "Uh,",
      "This is, like this is probably the end of humanity.",
      "...",
      "Everyone else is no much stupider.",
    ],
  }    
]

arguments = [
  { 
    "name":"The economy is trash",
      "persuation":[2.2, 3.1, 3.6, 4.7, 7.7, 8.1, 7.7, 1.2,],
      "topics":["Frustration"],
      "speech":[
        "I know your wallet is tight.",
        "It's to hard to buy what you need!",
        "You deserve MORE!",
        "THE ECONOMY IS AWFULL!!",
        "THE LINES ARE GOING DOWN",
        "Every single resecion indicator is through the roof!",
        "The financial system is broken.",
      ],
    },
  { 
    "name":"Tax the rich",
      "persuation":[12.4, 9.3, 7.5, 2.7, -2.1, -0.1, -4.7, -5.5],
      "topics":["Policy"],
      "speech":[
        "Of course they can afford it!",
        "The definition of rich is having money to spare.",
        "The 99 procent are the MAJORITY",
        "FOR THE PEOPLE!!",
        "If the rich can't afford it, who can?!",
        "Capital is a DISSEASE!",
        "Capitalism is A FAILED SYSTEM!!!",
        "DON'T BE CONTENT WITH THEIR CRUMBS!!!!!!!!",
      ],
    },
  { 
    "name":"Close the borders",
      "persuation":[-7.1, -3.8, -5.9, 0.8, 7.7, 1.1, 4.9, 11.2],
      "topics":["Homophobia"],
      "speech":[
        "Migration is increasing. We will fix it.",
        "The Migrants are coming!!",
        "They will STEAL your jobs!",
        "They have OTHER cultures!",
        "Their food is BAD!!!!",
        "We need Emergency measures",
        "WE NEED WALLS",
        "INCREASE SECURITY.",
        "Fences EVERYWHERE",
      ],
    },
  { 
    "name":"Climatechange will kill us",
      "persuation":[5.9, 4.4, 10.2, 4.1, -2.7, 3.1, 1.3, -7.2],
      "topics":["Enviroment"],
      "speech":[
        "Think about the poor seaturtles!",
        "YOU WILL DIE",
        "THINK ABOUT THE CHILDREN!!!",
        "The floods will be huge, they will swallow entire cities!",
        "THE SUFFERING!!",
        "Ecosystem collapse will cause irepairable harm for all of future.",
        "Agriculture will be harder and harder and MILIONS will starve.",
      ],
    },
  ]

def option_ui(var, options):
  counter = 0
  temp_list = []
  for i, option in enumerate(options):
    temp_list.append(str(i + 1))
    print(i + 1, ":", option["name"])
  print(" ")
  while True:
    var = input("Choose: ")
    if var in temp_list:
      print(" ")
      break
    else:
      print("Try again.\n")
  return (int(var) - 1)

player_1 = 0
player_2 = 0
audience = 0

print("Player 1   Choose your Champion\n")
player_1 = int(option_ui(player_1, speakers))

print("Player 2   Choose your Champion\n")
player_2 = int(option_ui(player_2, speakers))

print("Choose the Audience\n")
audience = int(option_ui(audience, audiences))

turn = 1
to_play = 1
oppinion = 0

while True:
    if turn % 2 == 1:
        to_play = player_1
    if turn % 2 == 0:
        to_play = player_2

    print(speakers[to_play]["name"])
    print(" ")
    argument_number = 1

    print("SPEAK!\n")
    argument = 0
    #argument = int(option_ui(speakers[to_play], arguments))
    temp_dict = {}
    
    for i in speakers[to_play]["arguments"]:
      temp_dict[str(argument_number)] = i
      print(argument_number,":", arguments[i]["name"])
      argument_number += 1
    while True:
      argument = input("choose your argument:")
      if argument in temp_dict or argument == "quit":
        print("\n")
        argument = temp_dict[argument]
        break
      else :
        print("Try again.\n")
    print(arguments[argument]["name"])

    if argument == "quit":
        break

    speaker_lines = 2*(speakers[to_play]["lines"] + arguments[argument]["speech"]) + speakers[to_play]["lines"] + arguments[argument]["speech"]
    time_sleeper = 0.1
    counter = 0
    random.shuffle(speaker_lines)
    for i in speaker_lines:
      counter += 1
      if counter <= 4:
        time_sleeper = time_sleeper * 0.38
      if counter >= 8 and counter <= 24:
        time_sleeper = time_sleeper*1.16
      if counter >= 25 and counter <= 28:
        time_sleeper = 0.09
      if counter >= 33:
        break
      print(counter,"-",i)
      time.sleep(time_sleeper)

    for i, voter in enumerate(voters):
      #print(voter["abreviation"])
      if turn % 2 == 1:
        voters[i]["convinced_player_1"] += arguments[argument]["persuation"][i]
        if voters[i]["convinced_player_1"] < 0:
          voters[i]["convinced_player_1"] = 0
        if voters[i]["convinced_player_1"] > 100:
          voters[i]["convinced_player_1"] = 100
      if turn % 2 == 0:
        voters[i]["convinced_player_2"] += arguments[argument]["persuation"][i]
        if voters[i]["convinced_player_2"] < 0:
          voters[i]["convinced_player_2"] = 0
        if voters[i]["convinced_player_2"] > 100:
          voters[i]["convinced_player_2"] = 100

    response_lines = []
    response_lines_destilled = []
    for i, voter_persons in enumerate(voters):
      if arguments[argument]["persuation"][i] >= 2.5:
        response_lines.append(voters[i]["good_lines"])
      if arguments[argument]["persuation"][i] < 2.5 and arguments[argument]["persuation"][i] >= -0.5:
        response_lines.append(voters[i]["neutral_lines"])
      if arguments[argument]["persuation"][i] < -0.5:
        response_lines.append(voters[i]["bad_lines"])

    for line in response_lines:
      for element in line:
        response_lines_destilled.append(element)
    random.shuffle(response_lines_destilled)
    time_sleeper = 0.1
    counter = 0
    for i in response_lines_destilled:
      counter += 1
      if counter <= 4:
        time_sleeper = time_sleeper * 0.38
      if counter >= 8 and counter <= 24:
        time_sleeper = time_sleeper*1.16
      if counter >= 25 and counter <= 28:
        time_sleeper = 0.09
      if counter >= 33:
        break
      print(i)
      time.sleep(time_sleeper)

    oppinion = 0
    for i, constituent in enumerate(audiences[audience]["constituents"]):
      #print("))", i)
      oppinion += (audiences[audience]["constituents"][i])*(voters[i]["convinced_player_1"]-voters[i]["convinced_player_2"])
    if oppinion > 0:
      print(speakers[player_1]["name"], "is winning")
      print("+",abs(oppinion/8),"points\n")
    if oppinion < 0:
      print(speakers[player_2]["name"], "is winning")
      print("+",abs(oppinion/8),"points\n")
    if oppinion == 0:
      print("It's 50/50")
      print("+0 points\n")
      #voters[i]["convinced_player_1"] +=

    



    turn += 1
