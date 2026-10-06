
def user_story(names):
    # last_name = names[-1]
    if len(names) < 3:
        result_string = " & ".join(names)
    else:
        result_string = ", ".join(names[:-1]) + " & " + names[-1]
        # result_string = names[-1]

    

    # for name in names:
    #     result_string += name
    return result_string