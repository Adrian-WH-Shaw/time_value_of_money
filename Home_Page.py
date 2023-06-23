import streamlit as st

st.set_page_config(page_title="Multipage App")
st.title("Future Value Calculator")
#st.sidebar.success("Select a page above.")

#if "my_input" not in st.session_state:
#    st.session_state = ""

principal = st.number_input('Input present value here:',10000)
interest_rate = st.number_input("Input the interest rate here:",value=0.0375)
years = st.number_input("Input the number of years here:",20)
periods = st.number_input("Input the numer of periods here: ",12)

#thing = st.number_input("Prop Line", value=5.5, step=0.5, format="%0.1u")

a = 1+(interest_rate/periods)
b = years*periods
c = a**b
d = a*principal

string_2 = "Future Value = Present Value  x   (1 + Interest Rate / Periods)^(Years * Periods)"
string_3 = "Future Value = " + str(principal) + " x (1 + " + str(interest_rate) + "/" + str(periods) + " )^(" + str(years) + " x " + str(periods) + ")"
string_4 = "Future Value = " + str(principal) + " x (" + str(a) + " )^(" + str(b)+ ")"
string_5 = "Future Value = " + str(principal) + " x ("+ str(c) + ")"

st.write(string_2)
st.write(string_3)
st.write(string_4)
string_1 = "In " + str(years) + " years, $" + str(principal) + " invested today, at " + str(interest_rate) + " pa (compounding " + str(years) + " times a year) is worth " + str(a) +"."

submit = st.button("Submit")
if submit:
    #st.session_state["my_input"]=my_input
    st.write(string_1)

years_ = st.slider("How many years should the mortgage last??", 0, 30, 25, format="%dyrs")
st.write("Mortgage duration", years_, "years")

age = st.slider("How old are you?", 0, 130, 25, format="$%dk")
st.write("I'm ", age, "years old")
#number = st.number_input("Insert a number", value=0, format="$%dk")
#st.write("The current number is ", number)
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)