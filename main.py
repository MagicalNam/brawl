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
        "CLAP CLAP 😃 CLAP CLAP CLAP 😃😃 CLAP CLAP CLAP CLAP CLAP 😃 CLAP CLAP",
        "FINALY😆😆!",
        "Viva La Revolution!!😆",
      ],
      "neutral_lines" : [
        "Yawn",
        "-----",
        "And what exactly does that do for the people?",
        "Make a real difference!",
      ],
      "bad_lines" : [
        "👿👿👿SHAME🤢",
        "BOOOOOOOOO🤢🤢👿👿",
        "You are an Enemy of the Working Class!👿👿👿",
        "What are you doing here👿👿👿??",
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
        "CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP 😃😃",
        "WWOOOOOOOO😆😆!!!!",
        "YESSSS!!!!!!!!!!!!!!!!!!!!!!!!!",
      ],
      "neutral_lines" : [
        "*Gasp*",
        "*Yawn*",
        "---------",
        "-------------------------------------",
      ],
      "bad_lines" : [
        "👿BOOOOOOOOOOOOOOOOO🤢🤢🤢🤢",
        "👿👿👿👿👿👿SCANDAL!!",
        "WHAT?!?!?!?!?!?!👿👿",
        "👿👿👿👿BBBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
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
        " CLAP CLAP CLAP CLAP CLAP 😆😆",
        "CLAP CLAP CLAP CLAP 😃😃😃😃😃😃😃😃😃😃",
      ],
      "neutral_lines" : [
        "------------------",
        "------",
        "--------------------------------------",
        "*ZZZZzzzzzzZZZzzzzZZZZzzzzzz ZZZzzzz*",
      ],
      "bad_lines" : [
        "boooooooooooooooo👿!",
        "👿BBBBBBBBBBBBBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!👿👿👿",
        "👿👿👿BOOOOOOOOOOOOOOOOOO👿👿👿👿👿👿👿👿👿👿👿👿👿👿👿👿",
        "WHAT?!?!👿"
      ], 
  },
  {
      "name": "Centrist",
      "abreviation": "Ctr",
      "convinced_player_1" : 0,
      "convinced_player_2" : 0,
      "important_topics" : [],
      "good_lines" : [
        " CLAP CLAP CLAP CLAP CLAP CLAP CLAP😃😃😃",
        "😃😃😃😃😃",
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
        "BOOOOOOOOOO🤢OOOO🤢OOOOOOOOOOO🤢OOOOOOOOOOO🤢O!!!!!!!!!!!",
        "BBBUUUUUUUUUUUUUU!🤢",
        "BOOOOOO🤢🤢🤢🤢!!!",
        "BUUUUUUUUUUUUUUUUUUUUUUUU🤢🤢🤢🤢",
      ],
  },    
  {
      "name": "Libertarian",
      "abreviation": "Lib",
      "convinced_player_1" : 0,
      "convinced_player_2" : 0,
      "important_topics" : [],
      "good_lines" : [
        "clap clap clap clap clap 😆😆😆😆!!!",
        "  clap! clap! clap! clap! clap! clap! clap! clap! clap! clap!😄😄😄😄",
        " clap clap clap clap clap clap clap clap clap 😃",
        "CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP😄😄!!!!",
      ],
      "neutral_lines" : [
        "zzzZZZZzzzzzzZZZZZzzzzzz",
        "ZZZZZZZZzzzzzzZZZzzzz",
        "ZZZzzzZZZzzz",
        "ZZZZZZZZzzzzzzzzzzZZZZZZZZZZzzzzzzzzZZZZZzzzzz",
      ],
      "bad_lines" : [
        "Boooooo🤢!!!!!!!!!!!!!!!!!!!!!1",
        "BOOOO🤢🤢!!!!!!!!!!!!!!!!!!",
        "Booo🤢!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
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
        "God loves you!😇😇😇😇😇",
        "JESUS😇",
        "Clap clap clap clap clap clap clap😇😇!!!!11",
        "  CLAP CLAP CLAP CLAP CLAP CLP CLAP CLAP😇😇😇!!",
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
        "BOOOOOO😡!!!!!!!!!",
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
        "WWOOOOOOOOO😆😆😆!!!!!",
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
        "This is outrageous!🤬🤬🤬",
        "😡😡BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!",
        "BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!",
        "😡😡😡BOOOOOOOOOOOOOOOOOOO!!! 🤢BOOOOOOOOOOOO!!!!!!!",
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
        "CLAP😆CLAP😆CLAP😆CLAP😆CLAP😆CLAP😆CLAP😆CLAP😆",
        "CLAPCLAPCLAPCLAPCLAPCLAPCLAP😆😆😆",
        "CLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAPCLAP😆😆",
      ],
      "neutral_lines" : [
        "BORRING!!!!",
        "BORRING!!",
        ".....",
        "....",
      ],
      "bad_lines" : [
        "BOOOOO BOOO BOOOOOOO🤬🤬🤬",
        "BOOOO!!! BOOOOOOO!!!! BOOOOOOOOOO!! BOOOOOOOOO!!!🤬🤬🤬",
        " 🤬🤬BOOOOOOOOOOO",
        "😡🤬😡😡Boooooo!!! 😡😡😡😡Booooooooooooo!!!!",
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
    "arguments": [0, 1, 4, 7, 9],
    "opponent_arguments": [],
    "rallys": [],
    "power1": "I call Bulshit",
    "power2": "The Facts says No",
    "lines": [
      "Take the POWER BACK TO THE PEOPLE",
      "We NEED to FIX this!!!",
      "For the people of our country. We need to do this. We need to fix it NOW!",
      "They are keeping your future away from you. The rich are AWFULL",
    ],
  },
  {
    "name": "Donald Trump",
    "arguments": [2, 5, 10, 11, 12, 13, 15],
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
    "arguments": [1, 3, 7, 8],
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
    "arguments": [2, 5, 6, 14, 15],
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
  },
  {
    "name": "Ursula von der Leyen",
    "arguments": [0, 1, 4, 7, 9],
    "opponent_arguments": [],
    "rallys": [],
    "power1": "I call Bulshit",
    "power2": "The Facts says No",
    "lines": [
      "Take the POWER BACK TO THE PEOPLE",
      "We NEED to FIX this!!!",
      "For the people of our country. We need to do this. We need to fix it NOW!",
      "They are keeping your future away from you. The rich are AWFULL",
    ],
  },
  {
    "name": "Charlie Kirk",
    "arguments": [2, 5, 10, 11, 12, 13, 15],
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
    "name": "Emanuel Macron",
    "arguments": [1, 3, 7, 8],
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
    "name": "Vladimir Putin",
    "arguments": [2, 5, 6, 14, 15],
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
  },      
#######################################################################################################
#######################################################################################################
]




arguments = [
  #0
  { 
    "name":"The economy is trash",
      "persuasion":[2.2, 3.1, 3.6, 4.7, 7.7, 8.1, 7.7, 1.2,],
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
    #1
  { 
    "name":"Tax the rich",
      "persuasion":[12.4, 9.3, 7.5, 2.7, -2.1, -0.1, -4.7, -5.5],
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
    #2
  { 
    "name":"Close the borders",
      "persuasion":[-7.1, -3.8, -5.9, 0.8, 7.7, 1.1, 4.9, 11.2],
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
    #3
  { 
    "name":"Climatechange will kill us",
      "persuasion":[5.9, 4.4, 10.2, 4.1, -2.7, 3.1, 1.3, -7.2],
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
    #4
    { 
    "name":"End Discrimination",
      "persuasion":[5.2, 4.1, 13.6, 4.9, 3.1, 1.1, -2.2, -6.3,],
      "topics":["Equality"],
      "speech":[
        "They are RACISTS!!!",
        "They divide YOU!!!!!!",
        "YOU HAVE THE RIGHT TO BE YOU.",
        "YOUR RIGHTS!!!",
        "They are SEXIST.",
        "We are allowed to just be people",
        "Protect DEMOCRACY!!!! protect FREEDOM!!!!!",
      ],
    },
    #5
  { 
    "name":"Everything is GREAT",
      "persuasion":[0.0, -3.8, -7.5, 2.9, 2.1, 3.4, 3.7, 5.5],
      "topics":["Moral boost"],
      "speech":[
        "Everything is so fantastic",
        "All the lines are going UPP!!!.",
        "Think about the shareholders",
        "The investors LOVE it",
        "AI!!!!!",
        "All the mergersand IPOs!! It's GREAT!!!!",
        "CAPITALISM",
        "We are riseing at a beautifull 2 precent EVERY single year!",
      ],
    },
    #6
  { 
    "name":"Cancel the foregin aid",
      "persuasion":[-5.2, -1.9, -4.1, -4.9, 2.4, -1.5, 7.9, 6.2],
      "topics":["Homophobia"],
      "speech":[
        "The money must stay here",
        "What about OUR people",
        "The money will go to YOu!!!",
        "They have other cultures!",
        "How do you benefit from it?!",
        "What do we GAIN???",
        "THEY",
        "They are terrorists and infidells.",
        "Why would we benefit from caring about others?!",
        "It's their Problem.",
      ],
    },
    #7
  { 
    "name":"Stop the wars",
      "persuasion":[4.1, 3.0, 6.2, 4.1, -4.7, 2.1, 4.1, -1.0],
      "topics":["Policy"],
      "speech":[
        "PEACE",
        "YOU WILL DIE",
        "THINK ABOUT THE CHILDREN!!",
        "HAVE A HEART",
        "THE SUFFERING",
        "THE ENDLESS TORTURE. THINK OF ALL INOCENT CIVILIANS",
        "THE INFINATE DEATH MUST STOP",
      ],
    },
    ###################################################################################################
    ###################################################################################################
    #8
  { 
    "name":"Fill those potholes",
      "persuasion":[6.5, 8.2, 4.9, 5.1, 3.5, 4.1, 3.7, 2.2,],
      "topics":["Frustration"],
      "speech":[
        "We need to Fix Our Streets",
        "We can't have it this way!",
        "You deserve MORE!!",
        "To improve YOUR life",
        "Your driving should Not be dangerous!!",
        "Our Busses",
      ],
    },
    #9
  { 
    "name":"Public Healthcare fo All",
      "persuasion":[9.1, 9.3, 8.5, 4.7, -1.2, 0.1, -0.7, -1.5],
      "topics":["Equality"],
      "speech":[
        "Healthcare is NOT a Product1!!!",
        "We are the PEOPLE. We have RIGHTS!!!!",
        "SAVE LIVES",
        "FOR THE PEOPLE!!",
        "YOUR HUMAN RIGHT",
        "Capital is the disease. WE WILL CURE IT!!!!",
        "FOR YOU!!!!!",
      ],
    },
    #10
  { 
    "name":"Lower all the taxes",
      "persuasion":[-9.4, -4.2, -5.5, -1.8, 6.7, 4.1, 6.5, 12.1],
      "topics":["Policy"],
      "speech":[
        "The rich can't afford it!!",
        "The budget does not work.",
        "THE DEFECIT",
        "How dare you attack those poor Bilionares?!",
        "Their food is BAD!!!!",
        "CRISIS",
        "Good for buisness",
      ],
    },
    #11
  { 
    "name":"Remove the sales tax",
      "persuasion":[5.2, -5.4, -4.2, 1.1, 2.8, 3.1, 4.2, 5.1],
      "topics":["Policy"],
      "speech":[
        "You can't afford it!",
        "IT IS NOT WORTH IT",
        "Why even have it?!",
        "The sales tax does not benefit anyone!!!!!",
        "Your wallet matters!!",
        "It's Awfull for the economy",
      ],
    },
    #12
  { 
    "name":"Our kids - Our education",
      "persuasion":[-4.3, -8.2, -7.1, -6.2, 9.1, -1.3, 3.2, 7.3,],
      "topics":["Policy"],
      "speech":[
        "They are RACISTS!!!",
        "They divide YOU!!!!!!",
        "YOU HAVE THE RIGHT TO BE YOU.",
        "YOUR RIGHTS!!!",
        "They are SEXIST.",
        "We are allowed to just be people",
        "Protect DEMOCRACY!!!! protect FREEDOM!!!!!",
      ],
    },
    #13
  { 
    "name":"Our military needs money",
      "persuasion":[-6.6, -4.8, -5.6, 4.1, 2.2, 4.4, 6.8, 9.9],
      "topics":["Moral boost"],
      "speech":[
        "WE ARE NOT SAFE!!!!!",
        "THEY ARE COMMING FOR US!!",
        "THE TERRORISTS ARE COMMING FOR YOU!!!!!!!",
        "Think about the poor poor military contractors.",
        "We need DEFENCE!",
        "War is actually not that bad when you think about it",
        "TO PROTECT DEMOCRACY!!!!!!!!!!!!!!!!!!",
        "What about the shareholders?!",
      ],
    },
    #14
  { 
    "name":"Electric cars will save the world",
      "persuasion":[-5.2, -1.9, -4.1, -4.9, 2.4, -1.5, 7.9, 6.2],
      "topics":["Homophobia"],
      "speech":[
        "Oil is bad",
        "We need to like stop climate change.",
        "The new cars are the FUTURE!!!",
        "Elecrtic is Modern",
        "They will be faster, the electric cars will solve trafic!!",
        "The plants love lithium you know.",
        "They are quiet..",
      ],
    },
    #15
  { 
    "name":"The Gays",
      "persuasion":[-4.1, -3.8, -18.3, -4.1, -4.7, 2.1, 4.1, 9.8],
      "topics":["Homophobia"],
      "speech":[
        "THOSE DISGUSTING RAINBOWS",
        "THEY WILL TURN YOUR KIDS GAY",
        "THIS IS A CONSPIRACY",
        "WE CAN'T LET THIS HAPPEN",
        "DO YOU WANT TO BE GAY?!",
        "THWY ARE GROOMING OUR CHILDREN",
        "I mean, they have a great sence of fassion, Butt, THEY ARE GAY!!!",
        "Yes I did do that to, butt i said no homo",
      ],
    },
  ]

def option_ui(var, options):
  counter = 0
  temp_list = []
  for i, option in enumerate(options):
    temp_list.append(str(i + 1))
    print(i + 1, ":", option["name"])
    time.sleep(print_speed)
  print(" ")
  time.sleep(print_speed)
  while True:
    var = input("Choose: ")
    if var in temp_list:
      print(" ")
      time.sleep(print_speed)
      break
    else:
      print("Try again")
      time.sleep(print_speed)
      print("")
      time.sleep(print_speed)
  return (int(var) - 1)

player_1 = 0
player_2 = 0
audience = 0
print_speed = 0.04

time.sleep(print_speed)
print("Player 1   Choose your Champion\n")
player_1 = int(option_ui(player_1, speakers))

time.sleep(print_speed)
print("Player 2   Choose your Champion\n")
player_2 = int(option_ui(player_2, speakers))

time.sleep(print_speed)
print("Choose the Audience\n")
audience = int(option_ui(audience, audiences))

turn = 1
to_play = 1
oppinion = 0
player_1_combo = 0
player_2_combo = 0

while True:
    if turn % 2 == 1:
        to_play = player_1
    if turn % 2 == 0:
        to_play = player_2

    time.sleep(print_speed)
    print(speakers[to_play]["name"])
    time.sleep(print_speed)
    print(" ")
    argument_number = 1

    time.sleep(print_speed)
    print("SPEAK!")
    time.sleep(print_speed)
    print("")
    argument = 0
    #argument = int(option_ui(speakers[to_play], arguments))
    temp_dict = {}
    
    for i in speakers[to_play]["arguments"]:
      temp_dict[str(argument_number)] = i
      time.sleep(print_speed/2)
      print(argument_number,":", arguments[i]["name"])
      argument_number += 1
    while True:
      argument = input("choose your argument:")
      if argument in temp_dict or argument == "quit":
        time.sleep(print_speed)
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
        time_sleeper = time_sleeper * 0.41
      if counter >= 7 and counter <= 24:
        time_sleeper = time_sleeper*1.15
      if counter >= 25 and counter <= 28:
        time_sleeper = 0.065
      if counter >= 33:
        break
      print("-",i)
      time.sleep(time_sleeper)

    for i, voter in enumerate(voters):
      #print(voter["abreviation"])
      if turn % 2 == 1:
        voters[i]["convinced_player_1"] += arguments[argument]["persuasion"][i]
        if voters[i]["convinced_player_1"] < 0:
          voters[i]["convinced_player_1"] = 0
        if voters[i]["convinced_player_1"] > 100:
          voters[i]["convinced_player_1"] = 100
      if turn % 2 == 0:
        voters[i]["convinced_player_2"] += arguments[argument]["persuasion"][i]
        if voters[i]["convinced_player_2"] < 0:
          voters[i]["convinced_player_2"] = 0
        if voters[i]["convinced_player_2"] > 100:
          voters[i]["convinced_player_2"] = 100

    response_lines = []
    response_lines_destilled = []
    for i, voter_persons in enumerate(voters):
      if arguments[argument]["persuasion"][i] >= 3.9:
        response_lines.append(voters[i]["good_lines"])
      if arguments[argument]["persuasion"][i] < 3.9 and arguments[argument]["persuasion"][i] >= 0.1:
        response_lines.append(voters[i]["neutral_lines"])
      if arguments[argument]["persuasion"][i] < 0.1:
        response_lines.append(voters[i]["bad_lines"])

    for line in response_lines:
      for element in line:
        response_lines_destilled.append(element)
        response_lines_destilled.append(element)
        response_lines_destilled.append(element)
        response_lines_destilled.append(element)
    random.shuffle(response_lines_destilled)
    time_sleeper = 0.1
    counter = 0
    for i in response_lines_destilled:
      counter += 1
      if counter <= 6:
        time_sleeper = time_sleeper * 0.38
      if counter >= 8 and counter <= 124:
        time_sleeper = time_sleeper*1.04
      if counter >= 124:
        time_sleeper = 0.08
      if counter >= 128:
        break
      print(i)
      time.sleep(time_sleeper)

    print("")

    oppinion = 0
    for i, constituent in enumerate(audiences[audience]["constituents"]):
      #print("))", i)
      oppinion += (audiences[audience]["constituents"][i])*(voters[i]["convinced_player_1"]-voters[i]["convinced_player_2"])
    oppinion_ajusted = int(abs(oppinion/8)*100)/100
    if oppinion > 0:
      time.sleep(print_speed/3)
      print(speakers[player_1]["name"], "is winning")
      time.sleep(print_speed)
      print("+",oppinion_ajusted,"points")
      time.sleep(print_speed)
      print("")
    if oppinion < 0:
      time.sleep(print_speed/3)
      print(speakers[player_2]["name"], "is winning")
      time.sleep(print_speed)
      print("+",abs(oppinion_ajusted),"points")
      time.sleep(print_speed)
      print("")
    if oppinion == 0:
      time.sleep(print_speed/3)
      print("It's 50/50")
      time.sleep(print_speed)
      print("+0 points")
      time.sleep(print_speed)
      print("")
      
      #voters[i]["convinced_player_1"] +=

    



    turn += 1
