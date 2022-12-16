BACKGROUND_COLOR = "#B1DDC6"

print("test batch of code for update on github")


from tkinter import *
import pandas
import random

# ---------------------------- Variables ------------------------------- #
used_words=[]
correct_words={}

# # ---------------------------- Reading save data ------------------------------- #
data=pandas.read_csv("data/french_words.csv")
correct_data=pandas.read_csv("Words learnt.csv")

correct_french_word=correct_data['French'].to_list()

correct_english_word = correct_data['English'].to_list()
correct_used_words=correct_data['#'].to_list()

data = data.drop(correct_used_words)


# ---------------------------- Brains ------------------------------- #
def correct():
    if len(used_words) ==0 :
        generate_word()
        pass
    else:

        french_word=used_words[len(used_words)-1]
        correct_french_word.append(data["French"][french_word])
        correct_english_word.append(data["English"][french_word])
        correct_used_words.append(used_words[len(used_words)-1])
        correct_words={
            "#":correct_used_words,
            "French":correct_french_word,
            "English":correct_english_word
        }

        Correct_words_data = pandas.DataFrame(correct_words)

        Correct_words_data.to_csv("Words learnt.csv")

        generate_word()



def incorrect():
    if len(used_words) == 0:
        generate_word()
        pass
    else:
        generate_word()





def generate_word():
    random_row = random.randint(0,len(data)-1)
    if random_row not in used_words:
        used_words.append(random_row)
        french_word=data['French'][random_row]
    else:
        generate_word()
        return
    canvas.itemconfig(fr_title, text=f"French")
    canvas.itemconfig(fr_word,text=f"{french_word}")
    canvas.itemconfig(card, image=front_img)
    timer(random_row)

def timer(random_row):
    window.after(3000, flip,random_row)

def flip(random_row):
    english_word=data['English'][random_row]
    canvas.itemconfig(fr_word, text=f"{english_word}")
    canvas.itemconfig(fr_title, text=f"English")
    canvas.itemconfig(card,image=back_img)



# ---------------------------- User Interface ------------------------------- #
#window
window =Tk()
window.title("French Flash Cards")
window.config(padx= 50, pady=50,bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_img=PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400,263,image=front_img)
canvas.grid(row=0, column=0, columnspan=2)


fr_title = canvas.create_text(400,150,text='', font= ("Ariel",40,"italic") )
fr_word = canvas.create_text(400,253,text='Start', font= ("Ariel",60,"bold") )

correct_img = PhotoImage(file="images/right.png")
check_button = Button(image=correct_img,highlightthickness=0,command=correct)
check_button.grid(row=1,column=1)

wrong = PhotoImage(file="images/wrong.png")
x_button = Button(image= wrong,highlightthickness=0,command=incorrect)
x_button.grid(row=1,column=0)


# ---------------------------- Testing Zone ------------------------------- #







# ---------------------------- End ------------------------------- #
window.mainloop()