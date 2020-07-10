#  Hint:  You may not need all of these.  Remove the unused functions.

#if source is none, destination is starting destination
#if destination is none than ending is reached
#tickets is our array with tickets
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    #loop through desintations in tickets
    # for tickets in tickets:
    #     cache[ticket.source]= ticket.destination
    cache = {} # flight path
    # starting_destination = cache['NONE']
    
    route = [None] * length
    for ticket in tickets:
        #set source as first element as startring dest if source is none
        if ticket.source == 'NONE':
            route[0] = ticket.destination
        else:
            cache[ticket.source] = ticket.destination
        
    if length > 1:
        for index in range(1, length):
            route[index] = cache[route[index-1]]

    return route


 
        




   


# tickets = [
#                  { source: "PIT", destination: "ORD" },
# ]
#         ticket_1 = Ticket("NONE", "PDX")
#         ticket_2 = Ticket("PDX", "DCA")
#         ticket_3 = Ticket("DCA", "NONE")

#          should return this ["PDX", "DCA", "NONE"]
