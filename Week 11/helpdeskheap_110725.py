import heapq

def helpdesk():
    heap = []
    
    while True:
        print("\n1. Add Ticket")
        print("\n2. Get Next ticket")
        print("\n3. Exit")
        
        choice = input("Choose an option ").strip()
        
        if choice == "1":
            ticket_id = input("Enter ticket ID: ").strip()
            priority = int(input("Enter priority (1-10, higher means more urgent): ").strip())
            heapq.heappush(heap, (-priority, ticket_id))
            print(f"Ticket '{ticket_id}' added with priority {priority}.")
            
        elif choice == "2":
            if not heap:
                print()
            else:
                neg_p, ticket_id = heapq.heappop(heap)
                priority = -neg_p
                print(f"Next ticket to be handled is '{ticket_id}' (priority {priority}).")
            
        elif choice == "3":
            print("Exiting helpdesk.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
            
if __name__ == "__main__":
    helpdesk()