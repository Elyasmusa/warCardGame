from tkinter import *
import random
from tkinter import messagebox
from PIL import Image, ImageTk


warGame = Tk()
warGame.title('War Card Game')
warGame.geometry('900x600')
warGame.configure(background ="silver")

frame = Frame(warGame, bg = "silver")
frame.pack(pady=25)

#opens the imagies
def getImage(card):
    cardImage = Image.open(card)
    
    cardImageResize = cardImage.resize((138,200))
    global openImage
    openImage = ImageTk.PhotoImage(cardImageResize)
    
    return openImage



  
#calls new game
def newGame():
    #creates deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    cardRange = range(2,15)
    
    global deck
    deck = []
    
    for x in suits:
        for y in cardRange:
            deck.append(f'{y}_of_{x}')
    
    #creates players and scores
    global dealer, player, rounds, dealerScore, playerScore, wars
    dealer = []
    player = []
    dealerScore = []
    playerScore = []
    wars = []
    rounds = 0
    
    #shuffles deck
    while(len(deck) > 0):
        #spliting deck into 2 decks 1 for dealer and 1 for player
        dealCard = random.choice(deck)
        deck.remove(dealCard)
        dealer.append(dealCard)
    
        playerCard = random.choice(deck)
        deck.remove(playerCard)
        player.append(playerCard)
        
    #starts game by seeing winner of first turn
    score(dealer, player)
    
  
        
def nextTurn():
    try:
        #call score for next turn
        score(dealer, player)
        
    except:
        #see if game ends
        if(len(dealer) == 0 or len(player) == 0):
            warsHappened = len(wars)
            rounds = (len(playerScore) + len(dealerScore)) - len(wars) 
            if (len(dealer) == 0):    
                messagebox.showinfo("You Won" ,f'You Won play again, Rounds Played = {rounds}, Wars fought {warsHappened}')
            else:
                messagebox.showinfo("You Lost" ,f'You lost play again, Rounds Played = {rounds}, Wars fought {warsHappened}')

#what happens when there is a war              
def war(dealer_card, player_card):
    #Save top cards and remove them from the deck
    warCardDealer = dealer_card[0]
    warCardPlayer = player_card[0]
    dealer.remove(dealer_card[0])
    player.remove(player_card[0])
    
    #see if correct cards are removed in terminal
    print(warCardDealer)
    print(warCardPlayer)
    
    #get the 2nd card in the deck as face up
    dealercard = 0
    playercard = 0
    dealercard = int(dealer_card[1].split("_", 1)[0])
    playercard = int(player_card[1].split("_", 1)[0])
    
    #see the new war cards in terminal
    print("war")
    print(dealercard)
    print(playercard)
    
    #load images
    global dealerCardImage
    dealerCardImage = getImage(f'PNG-cards-1.3/{dealer_card[0]}.png')
    labelForDealer.config(image = dealerCardImage)

    global playerCardImage
    playerCardImage = getImage(f'PNG-cards-1.3/{player_card[0]}.png')
    labelForPlayer.config(image = playerCardImage)
    
    #see if its a tie
    if dealercard == playercard:
        RoundLabel.config(text="Tie! WarTime!")
        #call war again and count wars that happened
        war(dealer, player)
        wars.append("x")
        
    #if dealer wins
    elif dealercard > playercard:
        warLabel.config(text="Dealer Wins this war")
        #wars award three points
        dealerScore.append("x")
        dealerScore.append("x")
        dealerScore.append("x")
        #dealer takes all cards and puts them at the back of the deck
        dealer.append(player_card[0])
        player.remove(player_card[0])
        dealer.append(dealer_card[0])
        dealer.remove(dealer_card[0])
        dealer.append(player_card[1])
        player.remove(player_card[1])
        dealer.append(dealer_card[1])
        dealer.remove(dealer_card[1])
        dealer.append(warCardDealer)
        dealer.append(warCardPlayer)
        #update deck and scores
        dDeck = len(dealer)
        dscore = len(dealerScore)
        frameForDealer.config(text = f'Dealer: {dscore}, Deck {dDeck}')
        pDeck = len(player)
        pscore=len(playerScore)
        frameForPlayer.config(text = f'Player: {pscore}, Deck: {pDeck}')
  

    else:
        warLabel.config(text="Player Wins this war")
        #three points awarded
        playerScore.append("x")
        playerScore.append("x")
        playerScore.append("x")
        #take all cards and place at end of deck
        player.append(dealer_card[0])
        dealer.remove(dealer_card[0])
        player.append(player_card[0])
        player.remove(player_card[0])
        player.append(dealer_card[1])
        dealer.remove(dealer_card[1])
        player.append(player_card[1])
        player.remove(player_card[1])
        player.append(warCardDealer)
        player.append(warCardPlayer)
        #update score and deck
        pDeck = len(player)
        pscore=len(playerScore)
        frameForPlayer.config(text = f'Player: {pscore}, Deck: {pDeck}')
        dDeck = len(dealer)
        dscore = len(dealerScore)
        frameForDealer.config(text = f'Dealer: {dscore}, Deck {dDeck}')
    
    
    
                
def score(dealer_card, player_card):
    #get the first card in deck
    dealercard = 0
    playercard = 0
    dealercard = int(dealer_card[0].split("_", 1)[0])
    playercard = int(player_card[0].split("_", 1)[0])
    
    #terminal for debugging
    print(dealer)
    print(dealercard)
    print(player)
    print(playercard)
    
    warLabel.config(text="No war ATM")
    
    global dealerCardImage
    dealerCardImage = getImage(f'PNG-cards-1.3/{dealer_card[0]}.png')
    labelForDealer.config(image = dealerCardImage)

    global playerCardImage
    playerCardImage = getImage(f'PNG-cards-1.3/{player_card[0]}.png')
    labelForPlayer.config(image = playerCardImage)
    
    
    
	# Compare Card numbers for tie
    if dealercard == playercard:
        RoundLabel.config(text="Tie! WarTime!")
        #call war if tie
        war(dealer, player)
        wars.append("x")
        
    #comapre cards for delaer win
    elif dealercard > playercard:
        RoundLabel.config(text="Dealer Wins!")
        #one point award for normal win and take cards to end of deck
        dealerScore.append("x")
        dealer.append(player_card[0])
        player.remove(player_card[0])
        dealer.append(dealer_card[0])
        dealer.remove(dealer_card[0])
        #update deck and score status
        pDeck = len(player)
        pscore=len(playerScore)
        frameForPlayer.config(text = f'Player: {pscore}, Deck: {pDeck}')
        dDeck = len(dealer)
        dscore = len(dealerScore)
        frameForDealer.config(text = f'Dealer: {dscore}, Deck {dDeck}')
  

    else:
        RoundLabel.config(text="Player Wins!")
        #one point award for normal win and take cards to end of deck
        playerScore.append("x")
        player.append(dealer_card[0])
        dealer.remove(dealer_card[0])
        player.append(player_card[0])
        player.remove(player_card[0])
        #update deck and score status
        pDeck = len(player)
        pscore=len(playerScore)
        frameForPlayer.config(text = f'Player: {pscore}, Deck: {pDeck}')
        dDeck = len(dealer)
        dscore = len(dealerScore)
        frameForDealer.config(text = f'Dealer: {dscore}, Deck {dDeck}')

def finishGame():
    while(len(player) != 0 and len(dealer) != 0):
        nextTurn()
        
#dealer label frame for ui
frameForDealer = LabelFrame(frame, text="Dealer: 0", bd =0)
frameForDealer.grid(row = 0, column = 0, padx= 25, ipadx=20)
labelForDealer = Label(frameForDealer, text = '')
labelForDealer.pack(pady=15)

#player label frame for ui
frameForPlayer = LabelFrame(frame, text="Player: 0", bd = 0)
frameForPlayer.grid(row = 0, column = 1, ipadx=20)
labelForPlayer = Label(frameForPlayer, text = '')
labelForPlayer.pack(pady=15)

#shows winner of turn currently in
RoundLabel= Label(warGame, text="", bg="green")
RoundLabel.pack(pady=20)

#shows winner of war if it happens
warLabel = Label(warGame, text="No war ATM", bg="silver")
warLabel.pack(pady=20)

#newgame button
restartGameButton = Button(warGame, text = "New Game", command = newGame)
restartGameButton.place(x=750, y=500, height = 40, width = 100)

#next turn button
nextTurnButton = Button(warGame, text="Next Turn Draw", command = nextTurn)
nextTurnButton.pack(pady=25)

#Finish game button
finishGameButton = Button(warGame, text = "Click To Run Full Game", command = finishGame)
finishGameButton.place(x=50, y=500, height = 40, width = 200)

newGame()
warGame.mainloop()