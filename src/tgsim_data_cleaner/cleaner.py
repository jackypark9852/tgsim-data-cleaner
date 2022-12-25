import graph as gr

# A fix is not valid if it implies id's were swapped
def IsValidFix(initial_id, changed_id, graph):
    if initial_id == changed_id:
        return True
    # Check if the graph forms a cycle afer adding new edge from changed_id to initial_id
    if changed_id in graph:
        return not gr.IsConnected(initial_id, changed_id, graph)
    return True


# Finds all rows to be changed and replaces id with initial_id
def FixId(initial_id: int, changed_id: int, time_first_seen_seconds: float, raw_data):
    margin_of_error = 1 / 60
    minimum_time = time_first_seen_seconds - margin_of_error
    raw_data.loc[
        (raw_data["id"] == changed_id) & ((raw_data["time"] >= minimum_time)), "id"
    ] = initial_id


def PrintInvalidFixes(invalid_fixes):
    if len(invalid_fixes) == 0:
        return
    print("ERROR - THE FOLLOWING FIXES WERE INVALID:")
    print("Index   Initial Id   Changed Id      Time First Seen")
    for index, initial_id, changed_id, time_first_seen in invalid_fixes:
        print(f"{index: 5d} {initial_id:12d} {changed_id:12d} {time_first_seen: 20f}")
    print("\n")


def PrintRedundantFixes(redundant_fixes):
    if len(redundant_fixes) == 0:
        return
    print("WARNING - THE FOLLOWING FIXES WERE REDUDANT: ")
    print("Index   Initial Id   Changed Id      Time First Seen")
    for index, initial_id, changed_id, time_first_seen in redundant_fixes:
        print(f"{index: 5d} {initial_id:12d} {changed_id:12d} {time_first_seen: 20f}")
    print("\n")
