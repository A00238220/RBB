from flask import Flask, render_template
import random

app = Flask('app')

#defining home end point
@app.route("/")
def home():

  #creating list and dictionaries for player details
  round_2_players = []
  champion = []
  player_roster = {}
  
  #defining a function for bracket 1 matches
  def bracket_1():

    bracket_1 = ['ada', 'ken', 'mike', 'dan']

    match_1_bracket_1 = []
    match_2_bracket_1 = []
    final_match_bracket_1 = []
    
    m1_score = []
    m2_score = []
    m3_score = []


    for x in range(1):
      player1 = random.choice(bracket_1)
      match_1_bracket_1.append(player1)
      bracket_1.remove(player1)
      

      player2 = random.choice(bracket_1)
      match_1_bracket_1.append(player2)
      bracket_1.remove(player2)
      

      winner = random.choice(match_1_bracket_1)    
      final_match_bracket_1.append(winner)

      p1_score, p2_score = 0, 0
      if winner == player1:
        p1_score += 1
        m1_score.append(p1_score)
        m1_score.append(p2_score)
      elif winner == player2:
        p2_score += 1        
        m1_score.append(p1_score)
        m1_score.append(p2_score) 

      print(match_1_bracket_1)
      print(f"The winnner for this matchup is {winner}")
      player_roster['match 1'] = match_1_bracket_1, winner, m1_score

    for x in range(1):
      player1 = random.choice(bracket_1)
      match_2_bracket_1.append(player1)
      bracket_1.remove(player1)

      player2 = random.choice(bracket_1)
      match_2_bracket_1.append(player2)
      bracket_1.remove(player2)

      winner = random.choice(match_2_bracket_1)
      final_match_bracket_1.append(winner)

      p1_score, p2_score = 0, 0
      if winner == player1:
        p1_score += 1
        m2_score.append(p1_score)
        m2_score.append(p2_score)
      elif winner == player2:
        p2_score += 1
        m2_score.append(p1_score)
        m2_score.append(p2_score) 
       

      print(match_2_bracket_1)
      print(f"The winnner for this matchup is {winner}")
      player_roster['match 2'] = match_2_bracket_1, winner, m2_score

    print(final_match_bracket_1)
    winner = random.choice(final_match_bracket_1)    
    round_2_players.append(winner)
        
    p1_score, p2_score = 0, 0
    if winner == final_match_bracket_1[0]:
      p1_score += 2
      p2_score += 1
      m3_score.append(p1_score)
      m3_score.append(p2_score)
    elif winner == final_match_bracket_1[1]:
      p2_score += 2
      p1_score += 1      
      m3_score.append(p1_score)
      m3_score.append(p2_score)
 
      

    print(f"The winnner for this bracket is {winner}")
    print(bracket_1)
    player_roster['match 3'] = final_match_bracket_1, winner, m3_score
    

  #defining a function for bracket 2 matches
  def bracket_2():

    bracket_2 = ['sam', 'bob', 'john', 'eve']

    match_1_bracket_2 = []
    match_2_bracket_2 = []
    final_match_bracket_2 = []
    m1_score = []
    m2_score = []
    m3_score = []

    for x in range(1):
      player1 = random.choice(bracket_2)
      match_1_bracket_2.append(player1)
      bracket_2.remove(player1)

      player2 = random.choice(bracket_2)
      match_1_bracket_2.append(player2)
      bracket_2.remove(player2)

      winner = random.choice(match_1_bracket_2)
      final_match_bracket_2.append(winner)

      p1_score, p2_score = 0, 0
      if winner == player1:
        p1_score += 1
        m1_score.append(p1_score)
        m1_score.append(p2_score)
      elif winner == player2:
        p2_score += 1        
        m1_score.append(p1_score)
        m1_score.append(p2_score)

      print(match_1_bracket_2)
      print(f"The winnner for this matchup is {winner}")
      player_roster['match 4'] = match_1_bracket_2, winner, m1_score

    for x in range(1):
      player1 = random.choice(bracket_2)
      match_2_bracket_2.append(player1)
      bracket_2.remove(player1)

      player2 = random.choice(bracket_2)
      match_2_bracket_2.append(player2)
      bracket_2.remove(player2)

      winner = random.choice(match_2_bracket_2)
      final_match_bracket_2.append(winner)

      p1_score, p2_score = 0, 0
      if winner == player1:
        p1_score += 1
        m2_score.append(p1_score)
        m2_score.append(p2_score)
      elif winner == player2:
        p2_score += 1        
        m2_score.append(p1_score)
        m2_score.append(p2_score)

      print(match_2_bracket_2)
      print(f"The winnner for this matchup is {winner}")
      player_roster['match 5'] = match_2_bracket_2, winner, m2_score
      

    print(final_match_bracket_2)
    winner = random.choice(final_match_bracket_2)
    round_2_players.append(winner)

    p1_score, p2_score = 0, 0
    if winner == final_match_bracket_2[0]:
      p1_score += 2
      p2_score += 1
      m3_score.append(p1_score)
      m3_score.append(p2_score)
    elif winner == final_match_bracket_2[1]:
      p2_score += 2
      p1_score += 1      
      m3_score.append(p1_score)
      m3_score.append(p2_score)

    print(f"The winnner for this bracket is {winner}")
    print(bracket_2)
    player_roster['match 6'] = final_match_bracket_2, winner, m3_score
    
  #defining a function for bracket 3 matches
  def bracket_3():

    bracket_3 = ['ben', 'dave', 'goodnews', 'jen']

    match_1_bracket_3 = []
    match_2_bracket_3 = []
    final_match_bracket_3 = []
    m1_score = []
    m2_score = []
    m3_score = []

    for x in range(1):
      player1 = random.choice(bracket_3)
      match_1_bracket_3.append(player1)
      bracket_3.remove(player1)

      player2 = random.choice(bracket_3)
      match_1_bracket_3.append(player2)
      bracket_3.remove(player2)

      winner = random.choice(match_1_bracket_3)
      final_match_bracket_3.append(winner)

      p1_score, p2_score = 0, 0
      if winner == player1:
        p1_score += 1
        m1_score.append(p1_score)
        m1_score.append(p2_score)
      elif winner == player2:
        p2_score += 1        
        m1_score.append(p1_score)
        m1_score.append(p2_score)

      print(match_1_bracket_3)
      print(f"The winnner for this matchup is {winner}")
      player_roster['match 7'] = match_1_bracket_3, winner, m1_score

    for x in range(1):
      player1 = random.choice(bracket_3)
      match_2_bracket_3.append(player1)
      bracket_3.remove(player1)

      player2 = random.choice(bracket_3)
      match_2_bracket_3.append(player2)
      bracket_3.remove(player2)

      winner = random.choice(match_2_bracket_3)
      final_match_bracket_3.append(winner)

      p1_score, p2_score = 0, 0
      if winner == player1:
        p1_score += 1
        m2_score.append(p1_score)
        m2_score.append(p2_score)
      elif winner == player2:
        p2_score += 1        
        m2_score.append(p1_score)
        m2_score.append(p2_score)

      print(match_2_bracket_3)
      print(f"The winnner for this matchup is {winner}")
      player_roster['match 8'] = match_2_bracket_3, winner, m2_score

    print(final_match_bracket_3)
    winner = random.choice(final_match_bracket_3)
    round_2_players.append(winner)

    p1_score, p2_score = 0, 0
    if winner == final_match_bracket_3[0]:
      p1_score += 2
      p2_score += 1
      m3_score.append(p1_score)
      m3_score.append(p2_score)
    elif winner == final_match_bracket_3[1]:
      p2_score += 2
      p1_score += 1      
      m3_score.append(p1_score)
      m3_score.append(p2_score)

    print(f"The winnner for this bracket is {winner}")
    print(bracket_3)
    player_roster['match 9'] = final_match_bracket_3, winner, m3_score
    

  #defining a function for bracket 4 matches
  def bracket_4():

    bracket_4 = ['sharon', 'mercy', 'idris', 'fatima']

    match_1_bracket_4 = []
    match_2_bracket_4 = []
    final_match_bracket_4 = []
    m1_score = []
    m2_score = []
    m3_score = []

    for x in range(1):
      player1 = random.choice(bracket_4)
      match_1_bracket_4.append(player1)
      bracket_4.remove(player1)

      player2 = random.choice(bracket_4)
      match_1_bracket_4.append(player2)
      bracket_4.remove(player2)

      winner = random.choice(match_1_bracket_4)
      final_match_bracket_4.append(winner)

      p1_score, p2_score = 0, 0
      if winner == player1:
        p1_score += 1
        m1_score.append(p1_score)
        m1_score.append(p2_score)
      elif winner == player2:
        p2_score += 1        
        m1_score.append(p1_score)
        m1_score.append(p2_score)

      print(match_1_bracket_4)
      print(f"The winnner for this matchup is {winner}")
      player_roster['match 10'] = match_1_bracket_4, winner, m1_score

    for x in range(1):
      player1 = random.choice(bracket_4)
      match_2_bracket_4.append(player1)
      bracket_4.remove(player1)

      player2 = random.choice(bracket_4)
      match_2_bracket_4.append(player2)
      bracket_4.remove(player2)

      winner = random.choice(match_2_bracket_4)
      final_match_bracket_4.append(winner)

      p1_score, p2_score = 0, 0
      if winner == player1:
        p1_score += 1
        m2_score.append(p1_score)
        m2_score.append(p2_score)
      elif winner == player2:
        p2_score += 1        
        m2_score.append(p1_score)
        m2_score.append(p2_score)

      print(match_2_bracket_4)
      print(f"The winnner for this matchup is {winner}")
      player_roster['match 11'] = match_2_bracket_4, winner, m2_score

    print(final_match_bracket_4)
    winner = random.choice(final_match_bracket_4)
    round_2_players.append(winner)

    p1_score, p2_score = 0, 0
    if winner == final_match_bracket_4[0]:
      p1_score += 2
      p2_score += 1
      m3_score.append(p1_score)
      m3_score.append(p2_score)
    elif winner == final_match_bracket_4[1]:
      p2_score += 2
      p1_score += 1      
      m3_score.append(p1_score)
      m3_score.append(p2_score)

    print(f"The winnner for this bracket is {winner}")
    print(bracket_4)
    player_roster['match 12'] = final_match_bracket_4, winner, m3_score
    


  bracket_1()
  print()
  bracket_2()
  print()
  bracket_3()
  print()
  bracket_4()
  print(round_2_players)

  #defining a function for round 2 matches
  def round_2():
    match_1_round_2 = []
    match_2_round_2 = []
    final_match_round_2 = []
    m1_score = []
    m2_score = []
    m3_score = []

    for x in range(1):

      player1 = random.choice(round_2_players)
      match_1_round_2.append(player1)
      round_2_players.remove(player1)

      player2 = random.choice(round_2_players)
      match_1_round_2.append(player2)
      round_2_players.remove(player2)

      winner = random.choice(match_1_round_2)
      final_match_round_2.append(winner)

      p1_score, p2_score = 2, 2
      if winner == player1:
        p1_score += 1
        m1_score.append(p1_score)
        m1_score.append(p2_score)
      elif winner == player2:
        p2_score += 1        
        m1_score.append(p1_score)
        m1_score.append(p2_score)

      print(match_1_round_2)
      print(f"The winnner for this matchup is {winner}")
      player_roster['match 13'] = match_1_round_2, winner, m1_score

    for x in range(1):

      player1 = random.choice(round_2_players)
      match_2_round_2.append(player1)
      round_2_players.remove(player1)

      player2 = random.choice(round_2_players)
      match_2_round_2.append(player2)
      round_2_players.remove(player2)

      winner = random.choice(match_2_round_2)
      final_match_round_2.append(winner)

      p1_score, p2_score = 2, 2
      if winner == player1:
        p1_score += 1
        m2_score.append(p1_score)
        m2_score.append(p2_score)
      elif winner == player2:
        p2_score += 1        
        m2_score.append(p1_score)
        m2_score.append(p2_score)

      print(match_2_round_2)
      print(f"The winnner for this matchup is {winner}")
      player_roster['match 14'] = match_2_round_2, winner, m2_score

    print(final_match_round_2)
    winner = random.choice(final_match_round_2)
    champion.append(winner)

    #final round matches
    p1_score, p2_score = 0, 0
    if winner == final_match_round_2[0]:
      p1_score += 4
      p2_score += 3
      m3_score.append(p1_score)
      m3_score.append(p2_score)
    elif winner == final_match_round_2[1]:
      p2_score += 4
      p1_score += 3      
      m3_score.append(p1_score)
      m3_score.append(p2_score)
    print(f"The champion of the Robot Bracket Game is {winner.title()}")
    print(round_2_players)
    player_roster['match 15'] = final_match_round_2, winner, m3_score
    

  print()
  round_2()

  print()
  print(player_roster)
  return render_template("index.html", player_roster=player_roster)

app.run(host='0.0.0.0', port=8080, debug=True)