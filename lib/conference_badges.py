def badge_maker(name):
    return f"Hello, my name is {name}"
# print(badge_maker("Elisha"))

def batch_badge_creator(names):
    list_of_speakers = []
    for name in names:
        list_of_speakers.append(f"Hello, my name is {name}.")
    return list_of_speakers

    # Using list comprehension
    # return [f"Hello, my name is {name}." for name in names ]
# print(batch_badge_creator(["Arel", "Carol"])) 


def assign_rooms(names):
    speaker_rooms = []
    for room, name in enumerate(names, start=1):
        speaker_rooms.append(f"Hello, {name}! You'll be assigned to room {room}!")
    return speaker_rooms
# print(assign_rooms(["Arel", "Carol", "Elisha", "Emmanuel"]))

def printer(names):
    speaker_list = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for speaker in speaker_list:
        print(speaker)
        
    for room_assignment in room_assignments:
        print(room_assignment)
printer(["Arel", "Carol"])