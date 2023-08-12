# 1. ADD_MEMBER <id> <name> <number_of_super_coins> 
# a. Example : ADD_MEMBER 1 akshay 10000 
# b. Output : Akshay added successfully 
# c. Example : ADD_MEMBER 2 chris 5000 
# d. Output : Chris added successfully 
# 2. ADD_EVENT <id> <event_name> <prize_name> <date> 
# a. Example : ADD_EVENT 1 BBD IPHONE-14 2023-06-06 
# b. Output : BBD with prize IPHONE-14 added successfully 
# 3. REGISTER_MEMBER <member_id> <event_id> 
# a. Example : REGISTER_MEMBER 1 1 
# b. Output : Akshay registered to the BBD event successfully 
# 4. SUBMIT_BID <member_id> <event_id> <bid_1> <bid_2> <bid_3> <bid_4> <bid_5> a. Example : SUBMIT_BID 1 1 100 200 400 500 600 
# b. Output : BIDS submitted successfully 
# c. Example SUBMIT_BID 2 1 100 200 400 500 
# d. Output : BIDS submitted successfully 
# e. Example : SUBMIT_BID 10 1 100 200 300 400 500 
# f. Output : Member did not registered for this event 
# 5. DECLARE_WINNER EVENT_ID 
# a. Example : DECLARE_WINNER 1 
# b. Output : Akshay wins the IPHONE-14 with lowest bid 100 
# BONUS 
# 6. LIST_WINNERS <order_by> 
# a. Example : LIST_WINNERS asc 
# b. Output : [ {event_id, winner_name, lowest_bid, date} ] 

class User:
    def __init__(self, user_id ,user_name):
        self.id = user_id
        self.user_name= user_name

class Participant(User):
    def __init__(self, user_id, user_name, coins, bidding_list):
        super().__init__(user_id, user_name)
        self.coins = coins
        self.bidding_list = bidding_list


class Event:
    def __init__(self, event_id, event_name):
        self.event_id= event_id
        self.event_name = event_name

class StartEvent:
    def __init__(self, participant_count):
        self.participant_count = participant_count
        self.participant_list = []
        self.max_bid = 0
        self.event = None
        self.initialize_event()
        self.initialize_participants(participant_count)
        

    def initialize_event(self):
        print("Enter Event ID")
        event_id = int(input())
        print("Enter Event Name")
        event_name = input()
        self.event = Event(event_id, event_name)


    def initialize_participants(self, participant_count):

        if participant_count == 0:
            raise Exception("No Participants") 

        for participant in range(participant_count):
            print("Enter Player User ID")
            user_id = int(input())
            print("Enter Player User name")
            user_name = input()
            print("Enter Number of Coins Participant have")
            user_coins_count = int(input())
            if not user_coins_count or user_coins_count <= 0:
                raise Exception("Invalid coins count")
            print("Enter Bidding range")
            bidding_range = int(input())
            self.max_bid = max(self.max_bid,bidding_range)
            bidding_list = []
            for bidding_count in range(bidding_range):
                bidding_amount = int(input())
                if bidding_amount > user_coins_count:
                    raise Exception("Bidding Amount is Greater than user coins count")
                else:
                    bidding_list.append(bidding_amount)
            participant = Participant(user_id, user_name, user_coins_count, bidding_list)
            self.participant_list.append(participant)
            
    def start_game(self):

        per_bid_winner_list = []
        highest_bidder = None
        highest_bid = None
        

        # TODO move all bidding in different function
        for bid_round in range (self.max_bid-1):
            for participant_obj in self.participant_list:
                if len(participant_obj.bidding_list) > bid_round: 
                    if not highest_bidder:
                        # if hes the first bidder
                        highest_bidder = participant_obj.id
                        highest_bid = participant_obj.bidding_list[bid_round]
                        per_bid_winner_list.append({
                            "user_id": participant_obj.id,
                            "user_name": participant_obj.user_name,
                            "bid_amount": highest_bid,
                            "event_name": self.event.event_name
                        })
                    else:
                        # comparing with highest bidder
                        if participant_obj.bidding_list[bid_round] > highest_bid:
                            highest_bidder = participant_obj.id
                            highest_bid = participant_obj.bidding_list[bid_round]
                            per_bid_winner_list.append({
                                "user_id": participant_obj.id,
                                "user_name": participant_obj.user_name,
                                "bid_amount": highest_bid,
                                "event_name": self.event.event_name
                            })

        # all bidding is completed check winner
        winning_bid_obj = None
        for i in range(len(per_bid_winner_list) - 1, -1, -1):
            if i==len(per_bid_winner_list) - 1:
                winning_bid_obj = per_bid_winner_list[i]
            elif per_bid_winner_list[i].get("user_id") != winning_bid_obj.id:
                if per_bid_winner_list[i].get("bid_amount")>=winning_bid_obj.get("bid_amount"):
                    winning_bid_obj = per_bid_winner_list[i]
            else :
                winning_bid_obj = per_bid_winner_list[i]

        return winning_bid_obj
            
def run():

    print("Enter number of Days")
    days_count = int(input())
    winner_list = []
    for day in range(days_count):
        print("Enter Player count")
        player_count = int(input())
        event = StartEvent(player_count)
        game_winner = event.start_game()
        event_name = game_winner.get("event_name")
        winner_name = game_winner.get("user_name")
        bidded_amount = game_winner.get("bid_amount")
        print(f"{event_name} event won by {winner_name} by bidding {bidded_amount}")
        winner_list.append(game_winner)

run()
        