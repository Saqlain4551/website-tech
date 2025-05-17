import streamlit as st

st.title("Welcome to my Website Tech")
st.header("Python.com")
st.subheader("Java")
st.markdown("Python Code")

st.code("""import random
import hangman_stages

word_list = ["apple", "snowfall", "kashmir"]
lives = 6
chosen_word = random.choice(word_list)

print("Welcome to Hangman!")

#  Display underscores for each letter
display = ["_"] * len(chosen_word)
print("Current word:", " ".join(display))

game_over = False

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    
    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guessed_letter:
                display[position] = guessed_letter
        print("Good guess!")
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("BAD LUCK! You lose !! ")

    
    print("Current word:", " ".join(display))

    
    print(hangman_stages.stages[lives])

    
    if "_" not in display:
        game_over = True
        print(" CONGRATULATION! You win the game hope you enjoy it !!")

""")

Name= st.text_input("Enter your name:")
Fname= st.text_input("Enter your father name :")
Address= st.text_area("Enter your text:" )
class_data= st.selectbox("Enter your class:",(1,2,3,4,5,6,7,8,))

button= st.button("Done:")
if button:
    st.markdown(f"""
    Name: {Name}
    Father name: {Fname}    
    Address : {Address}    
    class data : {class_data}  """ )