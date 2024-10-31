

"""3 Function """
def convert(st):
    st = st.replace(":)", "🙂")
    st = st.replace(":(", "🙁")
    return st

st = input()
# st = st.replace(":)", "🙂")
st = convert(st)
print(st)