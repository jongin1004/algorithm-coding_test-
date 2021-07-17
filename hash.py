def solution(participant, completion):
    for completion_people in completion:
        participant.remove(completion_people)

    return participant[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]



