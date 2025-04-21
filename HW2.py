#1

#def basic_calculator(num1 , num2 , operator):
#    try:
#        if operator == "+":
#            print( num1 + num2 )
#        elif operator == "-":
#            print( num1 - num2 )
#        elif operator == "/":
#            print( num1 / num2 )
#        elif operator == "*":
#            print( num1 * num2 )
#    except Exception as e:
#        print(e)
#
#basic_calculator(4,2,"+")



#2

#def parse_contacts():
#    dict = {}
#    with open("data.txt" ,"r") as file:
#        for line in file:
#            name , email = line.strip().split(",")
#            dict[name] = email
#    for name , email in dict.items():
#        print(f"{name}: {email}")
#
#parse_contacts()



#3

#def replace_content(pattern_string , replacement_string , file_input , file_output):
#    try:
#        with open (file_input , "r") as file:
#            x = file.read()
#            x.replace(pattern_string , replacement_string)
#        with open (file_output) as file:
#            file.write(x)
#    except Exception as e:
#        print(e)



#4

# import os
# from datetime import datetime

# class InvalidDateTimeError(Exception):
#     pass

# def add_event():
#     title = input("Enter event title: ")
#     date = input("Enter event date (YYYY-MM-DD): ")
#     time = input("Enter event time (HH:MM): ")
    
#     try:
#         # Validate the date and time
#         validate_date_time(date, time)
        
#         # Read existing events
#         events = read_file()
        
#         # Add the new event
#         events.append({"title": title, "date": date, "time": time})
        
#         # Write events back to file
#         write_events_to_file(events)
        
#         print("Event added successfully!")
#     except InvalidDateTimeError as e:
#         print(f"Error: {e}")


# def delete_event():
#     title_to_delete = input("Enter the title of the event to delete: ")
    
#     # Read all existing events
#     events = read_file()
    
#     # Find and remove the event with the matching title
#     updated_events = [event for event in events if event["title"] != title_to_delete]
    
#     # Check if the event was deleted
#     if len(events) == len(updated_events):
#         print("Event not found.")
#     else:
#         write_events_to_file(updated_events)
#         print("Event deleted successfully!")


# def view_events():
#     # Read events from file
#     events = read_file()
    
#     # Sort events by date and time
#     sorted_events = sorted(events, key=lambda event: (event["date"], event["time"]))
    
#     # Display events
#     if not sorted_events:
#         print("No events scheduled.")
#     else:
#         print("\nScheduled Events:")
#         for event in sorted_events:
#             print(f"Title: {event['title']}, Date: {event['date']}, Time: {event['time']}")

# def edit_event():
#     title_to_edit = input("Enter the title of the event to edit: ")
    
#     # Read existing events
#     events = read_file()
    
#     # Find the event to edit
#     for event in events:
#         if event["title"] == title_to_edit:
#             print(f"Current Details: Title: {event['title']}, Date: {event['date']}, Time: {event['time']}")
            
#             # Prompt for new details
#             new_title = input("Enter new title (leave blank to keep current title): ") or event["title"]
#             new_date = input("Enter new date (YYYY-MM-DD) (leave blank to keep current date): ") or event["date"]
#             new_time = input("Enter new time (HH:MM) (leave blank to keep current time): ") or event["time"]
            
#             try:
#                 # Validate new date and time
#                 validate_date_time(new_date, new_time)
                
#                 # Update event details
#                 event["title"] = new_title
#                 event["date"] = new_date
#                 event["time"] = new_time
                
#                 # Write updated events back to file
#                 write_events_to_file(events)
#                 print("Event updated successfully!")
#                 return
#             except InvalidDateTimeError as e:
#                 print(f"Error: {e}")
#                 return
    
#     print("Event not found.")



# def read_file():
#     event = []
#     if os.path.exists("events.txt"):
#         with open("events.txt" , "r")as file_1:
#             for lines in file_1:
#                 title , date , time = lines.strip().split("|")
#                 event.append({"title":title , "date":date , "time":time})
#     return event

# def write_events_to_file(events):
#     with open("events.txt", "w") as file:
#         for event in events:
#             file.write(f"{event['title']} | {event['date']} | {event['time']}\n")


# def validate_date_time(date_str, time_str):
#     try:
#         datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
#         return True
#     except ValueError:
#         raise InvalidDateTimeError("Invalid date or time format. Use 'YYYY-MM-DD' and 'HH:MM'.")



# def main():
#     while True:
#         print("Event Schedular Menu:")
#         print("1. Add Event")
#         print("2. Delete Event")
#         print("3. View Events")
#         print("4. Edit Event")
#         print("5. Exit")
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             add_event()
#         elif choice == "2":
#             delete_event()
#         elif choice == "3":
#             view_events()
#         elif choice == "4":
#             edit_event()
#         elif choice == "5":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# # Entry point
# if __name__ == "__main__":
#     main()
