def swap_case(s):
    new_st = ""
    for st in s:
        if st.lower() == st:
            new_st += st.upper()
        else:
            new_st +=st.lower() 
    return new_st

if __name__ == '__main__':
