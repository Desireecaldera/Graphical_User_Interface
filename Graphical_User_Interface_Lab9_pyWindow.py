import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import csv
import glob
from mysql import connector


# iNITIAL DATABASE CREATION (Only executed once)
# cnx = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com')
# cursor = cnx.cursor()
# mycursor.execute("CREATE DATABASE imdb")


# CONNECTING TO DATABASE
cnx = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com', database='imdb')
cursor = cnx.cursor()


# IMPORTING CSVS IUTO EACH DATA FRAME
# akas_data = pd.read_csv(r"C:\Users\desiree.caldera958\Desktop\Lab9\Lab9 imdb\Lab9 imdb\akas_5000.csv")
# crew_data = pd.read_csv(r"C:\Users\desiree.caldera958\Desktop\Lab9\Lab9 imdb\Lab9 imdb\crew_5000.csv")
# episodes_data = pd.read_csv(r"C:\Users\desiree.caldera958\Desktop\Lab9\Lab9 imdb\Lab9 imdb\episodes_5000.csv")
# people_data = pd.read_csv(r"C:\Users\desiree.caldera958\Desktop\Lab9\Lab9 imdb\Lab9 imdb\people_5000.csv")
# ratings_data = pd.read_csv(r"C:\Users\desiree.caldera958\Desktop\Lab9\Lab9 imdb\Lab9 imdb\ratings_5000.csv")
# titles_data = pd.read_csv(r"C:\Users\desiree.caldera958\Desktop\Lab9\Lab9 imdb\Lab9 imdb\titles_5000.csv")

# HANDING NULL AND NAN VALUES
# akas_data = akas_data.astype(str).where((pd.notnull(akas_data)), None)
# crew_data = crew_data.where((pd.notnull(crew_data)), None)
# episodes_data = episodes_data.astype(str).where((pd.notnull(episodes_data)), None)
# people_data = people_data.astype(str).where((pd.notnull(people_data)), None)
# ratings_data = ratings_data.astype(str).where((pd.notnull(ratings_data)), None)
# titles_data = titles_data.astype(str).where((pd.notnull(titles_data)), None)

# CREATING THE TABLES
# akas_table = ("CREATE TABLE akas(title_id varchar(10),title varchar(553),region varchar(10),language varchar(3),type varchar(16),attributes varchar(62),is_original_title varchar(11))")
# # crew_table = ("CREATE TABLE crew(title_id varchar(10),person_id varchar(10),category varchar(20),job varchar(286))")
# episodes_table = ("CREATE TABLE episodes(episode_title_id varchar(10),show_title_id varchar(10),season_number int(11),episode_number int(11))")
# people_table = ("CREATE TABLE people(person_id varchar(10),name varchar(105),born int(11),died int(11),PRIMARY KEY (person_id))")
# # ratings_table = ("CREATE TABLE ratings(title_id varchar(10),rating FLOAT,votes int(11),PRIMARY KEY (title_id))")
# titles_table = ("CREATE TABLE titles(title_id varchar(10),type varchar(15),primary_title varchar(400),original_title varchar(400),is_adult int(11),premiered int(11),ended int(11),runtime_minutes int(11),genre varchar(50),PRIMARY KEY(title_id))")

# cursor.execute(akas_table)
# cursor.execute(crew_table)
# cursor.execute(episodes_table)
# cursor.execute(people_table)
# cursor.execute(ratings_table)
# cursor.execute(titles_table)


# INSERTING DATA INTO TABLES

# AKAS
# for i, row in akas_data.iterrows():
#             #here %S means string values
#             akas_sql = "INSERT INTO akas VALUES (%s,%s,%s,%s,%s,%s,%s)"
#             cursor.execute(akas_sql, tuple(row))
#             print("Record inserted")
#             # the connection is not auto committed by default, so we must commit to save our changes
#             cnx.commit()


#CREW
# for i, row in crew_data.iterrows():
#             #here %S means string values
#             crew_sql = "INSERT INTO crew VALUES (%s,%s,%s,%s)"
#             cursor.execute(crew_sql, tuple(row))
#             print("Record inserted")
#             # the connection is not auto committed by default, so we must commit to save our changes
#             cnx.commit()

# EPISODES
# for i, row in episodes_data.iterrows():
#             #here %S means string values
#             episodes_sql = "INSERT INTO episodes VALUES (%s,%s,%s,%s)"
#             cursor.execute(episodes_sql, tuple(row))
#             print("Record inserted")
#             # the connection is not auto committed by default, so we must commit to save our changes
#             cnx.commit()

# PEOPLE
# for i, row in people_data.iterrows():
#             #here %S means string values
#             people_sql = "INSERT INTO people VALUES (%s,%s,%s,%s)"
#             cursor.execute(people_sql, tuple(row))
#             print("Record inserted")
#             # the connection is not auto committed by default, so we must commit to save our changes
#             cnx.commit()

# RATINGS
# for i, row in ratings_data.iterrows():
#             #here %S means string values
#             ratings_sql = "INSERT INTO ratings VALUES (%s,%s,%s)"
#             cursor.execute(ratings_sql, tuple(row))
#             print("Record inserted")
#             # the connection is not auto committed by default, so we must commit to save our changes
#             cnx.commit()

# TITLES
# for i, row in titles_data.iterrows():
#             #here %S means string values
#             titles_sql = "INSERT INTO titles VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#             cursor.execute(titles_sql, tuple(row))
#             print("Record inserted")
#             # the connection is not auto committed by default, so we must commit to save our changes
#             cnx.commit()


HEIGHT = 800
WIDTH = 1100

# TITLES TABLE SECTION
#######################################################################################################################################################

# DROP TITLES TABLE PAGE
def delete_titles():

    canvas.forget()
    # DELETE titles CANVAS
    delete_titles_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    delete_titles_canvas.pack()

    main_delete_titles_label = tk.Label(delete_titles_canvas, text="Selected DB: imdb \n Dropping Table: titles", font=13, bg='#ffffff')
    main_delete_titles_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE titles FRAME
    delete_titles_frame = tk.Frame(delete_titles_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    delete_titles_frame.place(relx=0.23, rely=0.37, relwidth=.50, relheight=.20)

    titles_delete_text = tk.Label(delete_titles_canvas, text="Are you sure you want to drop table: titles", font=1, bg='#ffffff')
    titles_delete_text.place(relx=0.29, rely=0.39)

    drop_titles_button = tk.Button(delete_titles_frame, text="Delete",command=drop_titles)
    drop_titles_button.place(relx=0.18, rely=0.35, relwidth=0.3, relheight=0.3)

    cancel_titles_button = tk.Button(delete_titles_frame, text="Cancel", command=main_page)
    cancel_titles_button.place(relx=0.50, rely=0.35, relwidth=0.3, relheight=0.3)

def drop_titles():
    cnx_titles = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_titles = cnx.cursor()
    cursor_titles.execute("DROP TABLE titles")
    cnx_titles.commit()
    cnx_titles.close()

# ADD ROW TO TITLES PAGE
def add_titles():

    canvas.forget()
    # # ADD titles CANVAS
    add_titles_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    add_titles_canvas.pack()

    main_add_titles_label = tk.Label(add_titles_canvas, text="Selected DB: imdb \n Adding Row To Table: titles", font=13, bg='#ffffff')
    main_add_titles_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # ADD titles FRAME
    add_titles_frame = tk.Frame(add_titles_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    add_titles_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    titles_back_button = tk.Button(add_titles_frame, text="<< Back", command=main_page)
    titles_back_button.place(relx=0.13, rely=0.12, relwidth=0.12)

    enter_title_id = tk.Label(add_titles_canvas, text="Enter Title ID: ", bg='#ffffff',font=13)
    enter_title_id.place(relx=0.30, rely=.35)
    title_id_entry = tk.Entry(add_titles_canvas)
    title_id_entry.place(relx=0.43, rely=.35)

    enter_type = tk.Label(add_titles_canvas, text="Enter Type: ", bg='#ffffff', font=13)
    enter_type.place(relx=0.30, rely=.40)
    type_entry = tk.Entry(add_titles_canvas)
    type_entry.place(relx=0.41, rely=.40)

    enter_p_title = tk.Label(add_titles_canvas, text="Enter Primary Title: ", bg='#ffffff', font=13)
    enter_p_title.place(relx=0.30, rely=.45)
    p_title_entry = tk.Entry(add_titles_canvas)
    p_title_entry.place(relx=0.47, rely=.45)

    enter_og_title = tk.Label(add_titles_canvas, text="Enter Original Title: ", bg='#ffffff', font=13)
    enter_og_title.place(relx=0.30, rely=.50)
    og_title_entry = tk.Entry(add_titles_canvas)
    og_title_entry.place(relx=0.47, rely=.50)

    enter_is_ad = tk.Label(add_titles_canvas, text="Enter Is Adult: ", bg='#ffffff', font=13)
    enter_is_ad.place(relx=0.30, rely=.55)
    is_ad_entry = tk.Entry(add_titles_canvas)
    is_ad_entry.place(relx=0.43, rely=.55)

    enter_prem = tk.Label(add_titles_canvas, text="Enter Premiered: ", bg='#ffffff', font=13)
    enter_prem.place(relx=0.30, rely=.60)
    prem_entry = tk.Entry(add_titles_canvas)
    prem_entry.place(relx=0.45, rely=.60)

    ended_orginal = tk.Label(add_titles_canvas, text="Enter Ended: ", bg='#ffffff', font=13)
    ended_orginal.place(relx=0.30, rely=.65)
    ended_entry = tk.Entry(add_titles_canvas)
    ended_entry.place(relx=0.42, rely=.66)

    titles_add_button = tk.Button(add_titles_frame, text="+ Add") #command=add_titles_row
    titles_add_button.place(relx=0.13, rely=0.86, relwidth=0.12)



# def add_titles_row():
#     cnx_titles = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
#                             database='imdb')
#
#     cursor_titles = cnx.cursor()
#     cursor_titles.execute("INSERT INTO titles VALUES (:title_id, :type, :primary_title, :original_title, :is_adult, :premiered, :ended, :runtime_minutes, :genres)",{
#         #TOUPLE GOES HERE
#     })
#     cnx_titles.commit()
#     cnx_titles.close()

# BROWSE TITLES SECTION
def browse_titles():

    canvas.forget()
    # BROWSE titles CANVAS
    browse_titles_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    browse_titles_canvas.pack()

    main_titles_label = tk.Label(browse_titles_canvas, text="Selected DB: imdb \n Browsing Table: titles", font=13, bg='#ffffff')
    main_titles_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE titles FRAME
    browse_titles_frame = tk.Frame(browse_titles_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    browse_titles_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    #create back button

    # ESTABLISHING CONNECTION
    cnx_titles = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_titles = cnx.cursor()
    cursor_titles.execute("SELECT * from titles")
    rows = cursor_titles.fetchall()

    titles_back_button = tk.Button(browse_titles_frame, text="<< Back", command=main_page)
    titles_back_button.place(relx=0.12, rely=0.11, relwidth=0.12)

    browsing_titles_text = tk.Label(browse_titles_frame, text="Browsing: titles")
    browsing_titles_text.place(relx=0.12, rely=.25)

    titles_add_button = tk.Button(browse_titles_frame, text="+ Add Row", command=add_titles)
    titles_add_button.place(relx=0.75, rely=0.25, relwidth=0.12)

    # CREATING THE TABLE
    tv = ttk.Treeview(browse_titles_frame, columns=(1,2,3,4,5,6,7,8,9),show="headings",height="3")
    tv.place(relx=0.12, rely=0.33, relwidth=.75, relheight=.45 )

    tv.heading(1, text="title_id")
    tv.heading(2, text="typw")
    tv.heading(3, text="primary_title")
    tv.heading(4, text="original_title")
    tv.heading(5, text="is_adult")
    tv.heading(6, text="premiered")
    tv.heading(7, text="ended")
    tv.heading(8, text="runtime_minutes")
    tv.heading(9, text="genres")

    for i in rows:
        tv.insert('', 'end', values=i)

    # COMMITING & CLOSING THE CONNECTION
    cnx_titles.commit()
    cnx_titles.close()

# RATINGS TABLE SECTION
#######################################################################################################################################################

# DROP RATINGS TABLE PAGE
def delete_ratings():

    canvas.forget()
    # DELETE ratings CANVAS
    delete_ratings_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    delete_ratings_canvas.pack()

    main_delete_ratings_label = tk.Label(delete_ratings_canvas, text="Selected DB: imdb \n Dropping Table: ratings", font=13, bg='#ffffff')
    main_delete_ratings_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE ratings FRAME
    delete_ratings_frame = tk.Frame(delete_ratings_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    delete_ratings_frame.place(relx=0.23, rely=0.37, relwidth=.50, relheight=.20)

    ratings_delete_text = tk.Label(delete_ratings_canvas, text="Are you sure you want to drop table: ratings", font=1, bg='#ffffff')
    ratings_delete_text.place(relx=0.29, rely=0.39)

    drop_ratings_button = tk.Button(delete_ratings_frame, text="Delete",command=drop_ratings)
    drop_ratings_button.place(relx=0.18, rely=0.35, relwidth=0.3, relheight=0.3)

    cancel_ratings_button = tk.Button(delete_ratings_frame, text="Cancel", command=main_page)
    cancel_ratings_button.place(relx=0.50, rely=0.35, relwidth=0.3, relheight=0.3)

def drop_ratings():
    cnx_ratings = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_ratings = cnx.cursor()
    cursor_ratings.execute("DROP TABLE ratings")
    cnx_ratings.commit()
    cnx_ratings.close()

# ADD ROW TO RATINGS PAGE
def add_ratings():

    canvas.forget()
    # # ADD ratings CANVAS
    add_ratings_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    add_ratings_canvas.pack()

    main_add_ratings_label = tk.Label(add_ratings_canvas, text="Selected DB: imdb \n Adding Row To Table: ratings", font=13, bg='#ffffff')
    main_add_ratings_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # ADD ratings FRAME
    add_ratings_frame = tk.Frame(add_ratings_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    add_ratings_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    ratings_back_button = tk.Button(add_ratings_frame, text="<< Back", command=main_page)
    ratings_back_button.place(relx=0.13, rely=0.12, relwidth=0.12)

    enter_title_id = tk.Label(add_ratings_canvas, text="Enter Title ID: ", bg='#ffffff',font=13)
    enter_title_id.place(relx=0.30, rely=.35)
    title_id_entry = tk.Entry(add_ratings_canvas)
    title_id_entry.place(relx=0.43, rely=.35)

    enter_rating = tk.Label(add_ratings_canvas, text="Enter Rating: ", bg='#ffffff', font=13)
    enter_rating.place(relx=0.30, rely=.40)
    rating_entry = tk.Entry(add_ratings_canvas)
    rating_entry.place(relx=0.41, rely=.40)

    enter_votes = tk.Label(add_ratings_canvas, text="Enter Votes: ", bg='#ffffff', font=13)
    enter_votes.place(relx=0.30, rely=.45)
    votes_entry = tk.Entry(add_ratings_canvas)
    votes_entry.place(relx=0.43, rely=.45)

    ratings_add_button = tk.Button(add_ratings_frame, text="+ Add") #command=add_ratings_row
    ratings_add_button.place(relx=0.13, rely=0.86, relwidth=0.12)



# def add_ratings_row():
#     cnx_ratings = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
#                             database='imdb')
#
#     cursor_ratings = cnx.cursor()
#     cursor_ratings.execute("INSERT INTO ratings VALUES (:title_id, :rating, :votes)",{
#         # TOUPLE GOES HERE
#     })
#     cnx_ratings.commit()
#     cnx_ratings.close()

# BROWSE RATINGS PAGE
def browse_ratings():

    canvas.forget()
    # BROWSE ratings CANVAS
    browse_ratings_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    browse_ratings_canvas.pack()

    main_ratings_label = tk.Label(browse_ratings_canvas, text="Selected DB: imdb \n Browsing Table: ratings", font=13, bg='#ffffff')
    main_ratings_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE ratings FRAME
    browse_ratings_frame = tk.Frame(browse_ratings_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    browse_ratings_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    #create back button

    # ESTABLISHING CONNECTION
    cnx_ratings = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_ratings = cnx.cursor()
    cursor_ratings.execute("SELECT * from ratings")
    rows = cursor_ratings.fetchall()

    ratings_back_button = tk.Button(browse_ratings_frame, text="<< Back", command=main_page)
    ratings_back_button.place(relx=0.12, rely=0.11, relwidth=0.12)

    browsing_ratings_text = tk.Label(browse_ratings_frame, text="Browsing: ratings")
    browsing_ratings_text.place(relx=0.12, rely=.25)

    ratings_add_button = tk.Button(browse_ratings_frame, text="+ Add Row", command=add_ratings)
    ratings_add_button.place(relx=0.75, rely=0.25, relwidth=0.12)

    # CREATING THE TABLE
    tv = ttk.Treeview(browse_ratings_frame, columns=(1,2,3),show="headings",height="3")
    tv.place(relx=0.12, rely=0.33, relwidth=.75, relheight=.45 )

    tv.heading(1, text="title_id")
    tv.heading(2, text="rating")
    tv.heading(3, text="votes")

    for i in rows:
        tv.insert('', 'end', values=i)

    # COMMITING & CLOSING THE CONNECTION
    cnx_ratings.commit()
    cnx_ratings.close()

# PEOPLE TABLE SECTION
#######################################################################################################################################################

# DROP PEOPLE TABLE PAGE
def delete_people():

    canvas.forget()
    # DELETE people CANVAS
    delete_people_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    delete_people_canvas.pack()

    main_delete_people_label = tk.Label(delete_people_canvas, text="Selected DB: imdb \n Dropping Table: people", font=13, bg='#ffffff')
    main_delete_people_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE people FRAME
    delete_people_frame = tk.Frame(delete_people_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    delete_people_frame.place(relx=0.23, rely=0.37, relwidth=.50, relheight=.20)

    people_delete_text = tk.Label(delete_people_canvas, text="Are you sure you want to drop table: people", font=1, bg='#ffffff')
    people_delete_text.place(relx=0.29, rely=0.39)

    drop_people_button = tk.Button(delete_people_frame, text="Delete",command=drop_people)
    drop_people_button.place(relx=0.18, rely=0.35, relwidth=0.3, relheight=0.3)

    cancel_people_button = tk.Button(delete_people_frame, text="Cancel", command=main_page)
    cancel_people_button.place(relx=0.50, rely=0.35, relwidth=0.3, relheight=0.3)

def drop_people():
    cnx_people = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_people = cnx.cursor()
    cursor_people.execute("DROP TABLE people")
    cnx_people.commit()
    cnx_people.close()

# ADD ROW TO PEOPLE PAGE
def add_people():

    canvas.forget()
    # # ADD people CANVAS
    add_people_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    add_people_canvas.pack()

    main_add_people_label = tk.Label(add_people_canvas, text="Selected DB: imdb \n Adding Row To Table: people", font=13, bg='#ffffff')
    main_add_people_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # ADD people FRAME
    add_people_frame = tk.Frame(add_people_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    add_people_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    people_back_button = tk.Button(add_people_frame, text="<< Back", command=main_page)
    people_back_button.place(relx=0.13, rely=0.12, relwidth=0.12)

    enter_person_id = tk.Label(add_people_canvas, text="Enter Person ID: ", bg='#ffffff',font=13)
    enter_person_id.place(relx=0.30, rely=.35)
    person_id_entry = tk.Entry(add_people_canvas)
    person_id_entry.place(relx=0.46, rely=.35)

    enter_name = tk.Label(add_people_canvas, text="Enter Name: ", bg='#ffffff', font=13)
    enter_name.place(relx=0.30, rely=.40)
    name_entry = tk.Entry(add_people_canvas)
    name_entry.place(relx=0.42, rely=.40)

    enter_born = tk.Label(add_people_canvas, text="Enter Born: ", bg='#ffffff', font=13)
    enter_born.place(relx=0.30, rely=.45)
    born_entry = tk.Entry(add_people_canvas)
    born_entry.place(relx=0.41, rely=.45)

    enter_died = tk.Label(add_people_canvas, text="Enter Died: ", bg='#ffffff', font=13)
    enter_died.place(relx=0.30, rely=.50)
    died_entry = tk.Entry(add_people_canvas)
    died_entry.place(relx=0.41, rely=.50)

    people_add_button = tk.Button(add_people_frame, text="+ Add") #command=add_people_row
    people_add_button.place(relx=0.13, rely=0.86, relwidth=0.12)



# def add_people_row():
#     cnx_people = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
#                             database='imdb')
#
#     cursor_people = cnx.cursor()
#     cursor_people.execute("INSERT INTO people VALUES (:person_id, :name, :born, :died)",{
#         #TOUPLE GOES HERE
#     })
#     cnx_people.commit()
#     cnx_people.close()

# BROWSE PEOPLE PAGE
def browse_people():

    canvas.forget()
    # BROWSE people CANVAS
    browse_people_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    browse_people_canvas.pack()

    main_people_label = tk.Label(browse_people_canvas, text="Selected DB: imdb \n Browsing Table: people", font=13, bg='#ffffff')
    main_people_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE people FRAME
    browse_people_frame = tk.Frame(browse_people_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    browse_people_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    #create back button

    # ESTABLISHING CONNECTION
    cnx_people = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_people = cnx.cursor()
    cursor_people.execute("SELECT * from people")
    rows = cursor_people.fetchall()

    people_back_button = tk.Button(browse_people_frame, text="<< Back", command=main_page)
    people_back_button.place(relx=0.12, rely=0.11, relwidth=0.12)

    browsing_people_text = tk.Label(browse_people_frame, text="Browsing: people")
    browsing_people_text.place(relx=0.12, rely=.25)

    people_add_button = tk.Button(browse_people_frame, text="+ Add Row", command=add_people)
    people_add_button.place(relx=0.75, rely=0.25, relwidth=0.12)

    # CREATING THE TABLE
    tv = ttk.Treeview(browse_people_frame, columns=(1,2,3,4),show="headings",height="3")
    tv.place(relx=0.12, rely=0.33, relwidth=.75, relheight=.45 )

    tv.heading(1, text="person_id")
    tv.heading(2, text="name")
    tv.heading(3, text="born")
    tv.heading(4, text="died")

    for i in rows:
        tv.insert('', 'end', values=i)

    # COMMITING & CLOSING THE CONNECTION
    cnx_people.commit()
    cnx_people.close()

# EPISODE TABLE SECTIOM
#######################################################################################################################################################

# DROP EPISODES PAGE
def delete_episodes():

    canvas.forget()
    # DELETE episodes CANVAS
    delete_episodes_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    delete_episodes_canvas.pack()

    main_delete_episodes_label = tk.Label(delete_episodes_canvas, text="Selected DB: imdb \n Dropping Table: episodes", font=13, bg='#ffffff')
    main_delete_episodes_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE episodes FRAME
    delete_episodes_frame = tk.Frame(delete_episodes_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    delete_episodes_frame.place(relx=0.23, rely=0.37, relwidth=.50, relheight=.20)

    episodes_delete_text = tk.Label(delete_episodes_canvas, text="Are you sure you want to drop table: episodes", font=1, bg='#ffffff')
    episodes_delete_text.place(relx=0.29, rely=0.39)

    drop_episodes_button = tk.Button(delete_episodes_frame, text="Delete",command=drop_episodes)
    drop_episodes_button.place(relx=0.18, rely=0.35, relwidth=0.3, relheight=0.3)

    cancel_episodes_button = tk.Button(delete_episodes_frame, text="Cancel", command=main_page)
    cancel_episodes_button.place(relx=0.50, rely=0.35, relwidth=0.3, relheight=0.3)

def drop_episodes():
    cnx_episodes = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_episodes = cnx.cursor()
    cursor_episodes.execute("DROP TABLE episodes")
    cnx_episodes.commit()
    cnx_episodes.close()

# ADD ROW TO EPISODES PAGE
def add_episodes():

    canvas.forget()
    # # ADD episodes CANVAS
    add_episodes_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    add_episodes_canvas.pack()

    main_add_episodes_label = tk.Label(add_episodes_canvas, text="Selected DB: imdb \n Adding Row To Table: episodes", font=13, bg='#ffffff')
    main_add_episodes_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # ADD episodes FRAME
    add_episodes_frame = tk.Frame(add_episodes_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    add_episodes_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    episodes_back_button = tk.Button(add_episodes_frame, text="<< Back", command=main_page)
    episodes_back_button.place(relx=0.13, rely=0.12, relwidth=0.12)

    enter_ep_title = tk.Label(add_episodes_canvas, text="Enter Episode Title: ", bg='#ffffff',font=13)
    enter_ep_title.place(relx=0.30, rely=.35)
    ep_title_entry = tk.Entry(add_episodes_canvas)
    ep_title_entry.place(relx=0.48, rely=.35)

    enter_sh_title = tk.Label(add_episodes_canvas, text="Enter Show Title: ", bg='#ffffff', font=13)
    enter_sh_title.place(relx=0.30, rely=.40)
    sh_title_entry = tk.Entry(add_episodes_canvas)
    sh_title_entry.place(relx=0.46, rely=.40)

    enter_se_num = tk.Label(add_episodes_canvas, text="Enter Season Number: ", bg='#ffffff', font=13)
    enter_se_num.place(relx=0.30, rely=.45)
    se_num_entry = tk.Entry(add_episodes_canvas)
    se_num_entry.place(relx=0.50, rely=.45)

    enter_ep_num = tk.Label(add_episodes_canvas, text="Enter Episode Number: ", bg='#ffffff', font=13)
    enter_ep_num.place(relx=0.30, rely=.50)
    ep_num_entry = tk.Entry(add_episodes_canvas)
    ep_num_entry.place(relx=0.50, rely=.50)

    episodes_add_button = tk.Button(add_episodes_frame, text="+ Add") #command=add_episodes_row
    episodes_add_button.place(relx=0.13, rely=0.86, relwidth=0.12)

# def add_episodes_row():
#     cnx_episodes = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
#                             database='imdb')
#
#     cursor_episodes = cnx.cursor()
#     cursor_episodes.execute("INSERT INTO episodes VALUES (:episode_title, :show_title, :season_number, :episode_number)",{
#         #TOUPLE GOES HERE
#     })
#     cnx_episodes.commit()
#     cnx_episodes.close()

# BROWSE EPISODES PAGE
def browse_episodes():

    canvas.forget()
    # BROWSE episodes CANVAS
    browse_episodes_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    browse_episodes_canvas.pack()

    main_episodes_label = tk.Label(browse_episodes_canvas, text="Selected DB: imdb \n Browsing Table: episodes", font=13, bg='#ffffff')
    main_episodes_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE episodes FRAME
    browse_episodes_frame = tk.Frame(browse_episodes_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    browse_episodes_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)


    # ESTABLISHING CONNECTION
    cnx_episodes = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_episodes = cnx.cursor()
    cursor_episodes.execute("SELECT * from episodes")
    rows = cursor_episodes.fetchall()

    episodes_back_button = tk.Button(browse_episodes_frame, text="<< Back", command=main_page)
    episodes_back_button.place(relx=0.12, rely=0.11, relwidth=0.12)

    browsing_episodes_text = tk.Label(browse_episodes_frame, text="Browsing: episodes")
    browsing_episodes_text.place(relx=0.12, rely=.25)

    episodes_add_button = tk.Button(browse_episodes_frame, text="+ Add Row", command=add_episodes)
    episodes_add_button.place(relx=0.75, rely=0.25, relwidth=0.12)

    # CREATING THE TABLE
    tv = ttk.Treeview(browse_episodes_frame, columns=(1,2,3,4),show="headings",height="3")
    tv.place(relx=0.12, rely=0.33, relwidth=.75, relheight=.45 )

    tv.heading(1, text="episode_title")
    tv.heading(2, text="show_title")
    tv.heading(3, text="season_number")
    tv.heading(4, text="episode_number")

    for i in rows:
        tv.insert('', 'end', values=i)

    # COMMITING & CLOSING THE CONNECTION
    cnx_episodes.commit()
    cnx_episodes.close()


# CREW TABLE SECTION
#######################################################################################################################################################

# DROP CREW TABLE PAGE
def delete_crew():

    canvas.forget()
    # DELETE crew CANVAS
    delete_crew_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    delete_crew_canvas.pack()

    main_delete_crew_label = tk.Label(delete_crew_canvas, text="Selected DB: imdb \n Dropping Table: crew", font=13, bg='#ffffff')
    main_delete_crew_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE crew FRAME
    delete_crew_frame = tk.Frame(delete_crew_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    delete_crew_frame.place(relx=0.23, rely=0.37, relwidth=.50, relheight=.20)

    crew_delete_text = tk.Label(delete_crew_canvas, text="Are you sure you want to drop table: crew", font=1, bg='#ffffff')
    crew_delete_text.place(relx=0.29, rely=0.39)

    drop_crew_button = tk.Button(delete_crew_frame, text="Delete",command=drop_crew)
    drop_crew_button.place(relx=0.18, rely=0.35, relwidth=0.3, relheight=0.3)

    cancel_crew_button = tk.Button(delete_crew_frame, text="Cancel", command=main_page)
    cancel_crew_button.place(relx=0.50, rely=0.35, relwidth=0.3, relheight=0.3)

def drop_crew():
    cnx_crew = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_crew = cnx.cursor()
    cursor_crew.execute("DROP TABLE crew")
    cnx_crew.commit()
    cnx_crew.close()

# ADD ROW TO CREW PAGE
def add_crew():

    canvas.forget()
    # # ADD crew CANVAS
    add_crew_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    add_crew_canvas.pack()

    main_add_crew_label = tk.Label(add_crew_canvas, text="Selected DB: imdb \n Adding Row To Table: crew", font=13, bg='#ffffff')
    main_add_crew_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # ADD crew FRAME
    add_crew_frame = tk.Frame(add_crew_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    add_crew_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    crew_back_button = tk.Button(add_crew_frame, text="<< Back", command=main_page)
    crew_back_button.place(relx=0.13, rely=0.12, relwidth=0.12)

    enter_title_id = tk.Label(add_crew_canvas, text="Enter Title ID: ", bg='#ffffff',font=13)
    enter_title_id.place(relx=0.30, rely=.35)
    title_id_entry = tk.Entry(add_crew_canvas)
    title_id_entry.place(relx=0.43, rely=.35)

    enter_person = tk.Label(add_crew_canvas, text="Enter Person ID: ", bg='#ffffff', font=13)
    enter_person.place(relx=0.30, rely=.40)
    person_entry = tk.Entry(add_crew_canvas)
    person_entry.place(relx=0.46, rely=.40)

    enter_category = tk.Label(add_crew_canvas, text="Enter Category: ", bg='#ffffff', font=13)
    enter_category.place(relx=0.30, rely=.45)
    category_entry = tk.Entry(add_crew_canvas)
    category_entry.place(relx=0.44, rely=.45)

    enter_job = tk.Label(add_crew_canvas, text="Enter job: ", bg='#ffffff', font=13)
    enter_job.place(relx=0.30, rely=.50)
    job_entry = tk.Entry(add_crew_canvas)
    job_entry.place(relx=0.40, rely=.50)
    crew_add_button = tk.Button(add_crew_frame, text="+ Add") #command=add_crew_row
    crew_add_button.place(relx=0.13, rely=0.86, relwidth=0.12)


# def add_crew_row():
#     cnx_crew = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
#                             database='imdb')
#
#     cursor_crew = cnx.cursor()
#     cursor_crew.execute("INSERT INTO crew VALUES (:title_id, :person_id, :category, :job),
#     {
        #TOUPLE GOES HERE
#     }")
#     cnx_crew.commit()
#     cnx_crew.close()

# BROSE CREW PAGE
def browse_crew():

    canvas.forget()
    # BROWSE crew CANVAS
    browse_crew_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    browse_crew_canvas.pack()

    main_crew_label = tk.Label(browse_crew_canvas, text="Selected DB: imdb \n Browsing Table: crew", font=13, bg='#ffffff')
    main_crew_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE crew FRAME
    browse_crew_frame = tk.Frame(browse_crew_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    browse_crew_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    #create back button

    # ESTABLISHING CONNECTION
    cnx_crew = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_crew = cnx.cursor()
    cursor_crew.execute("SELECT * from crew")
    rows = cursor_crew.fetchall()

    crew_back_button = tk.Button(browse_crew_frame, text="<< Back", command=main_page)
    crew_back_button.place(relx=0.12, rely=0.11, relwidth=0.12)

    browsing_crew_text = tk.Label(browse_crew_frame, text="Browsing: crew")
    browsing_crew_text.place(relx=0.12, rely=.25)

    crew_add_button = tk.Button(browse_crew_frame, text="+ Add Row", command=add_crew)
    crew_add_button.place(relx=0.75, rely=0.25, relwidth=0.12)

    # CREATING THE TABLE
    tv = ttk.Treeview(browse_crew_frame, columns=(1,2,3,4),show="headings",height="3")
    tv.place(relx=0.12, rely=0.33, relwidth=.75, relheight=.45 )

    tv.heading(1, text="title_id")
    tv.heading(2, text="person_id")
    tv.heading(3, text="category")
    tv.heading(4, text="job")

    for i in rows:
        tv.insert('', 'end', values=i)

    # COMMITING & CLOSING THE CONNECTION
    cnx_crew.commit()
    cnx_crew.close()

# AKAS SECTION
#######################################################################################################################################################

# DELETE AKAS PAGE
def delete_akas():

    canvas.forget()
    # DELETE AKAS CANVAS
    delete_akas_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    delete_akas_canvas.pack()

    main_delete_akas_label = tk.Label(delete_akas_canvas, text="Selected DB: imdb \n Dropping Table: akas", font=13, bg='#ffffff')
    main_delete_akas_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE AKAS FRAME
    delete_akas_frame = tk.Frame(delete_akas_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    delete_akas_frame.place(relx=0.23, rely=0.37, relwidth=.50, relheight=.20)

    akas_delete_text = tk.Label(delete_akas_canvas, text="Are you sure you want to drop table: akas", font=1, bg='#ffffff')
    akas_delete_text.place(relx=0.29, rely=0.39)

    drop_akas_button = tk.Button(delete_akas_frame, text="Delete",command=drop_akas)
    drop_akas_button.place(relx=0.18, rely=0.35, relwidth=0.3, relheight=0.3)

    cancel_akas_button = tk.Button(delete_akas_frame, text="Cancel", command=main_page)
    cancel_akas_button.place(relx=0.50, rely=0.35, relwidth=0.3, relheight=0.3)

def drop_akas():
    cnx_akas = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_akas = cnx.cursor()
    cursor_akas.execute("DROP TABLE akas")
    cnx_akas.commit()
    cnx_akas.close()

# ADD ROW TO AKAS PAGE
def add_akas():

    canvas.forget()
    # # ADD AKAS CANVAS
    add_akas_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    add_akas_canvas.pack()

    main_add_akas_label = tk.Label(add_akas_canvas, text="Selected DB: imdb \n Adding Row To Table: akas", font=13, bg='#ffffff')
    main_add_akas_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # ADD AKAS FRAME
    add_akas_frame = tk.Frame(add_akas_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    add_akas_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    akas_back_button = tk.Button(add_akas_frame, text="<< Back", command=main_page)
    akas_back_button.place(relx=0.13, rely=0.12, relwidth=0.12)

    enter_title_id = tk.Label(add_akas_canvas, text="Enter Title ID: ", bg='#ffffff',font=13)
    enter_title_id.place(relx=0.30, rely=.35)
    title_id_entry = tk.Entry(add_akas_canvas)
    title_id_entry.place(relx=0.43, rely=.35)

    enter_title = tk.Label(add_akas_canvas, text="Enter Title: ", bg='#ffffff', font=13)
    enter_title.place(relx=0.30, rely=.40)
    title_entry = tk.Entry(add_akas_canvas)
    title_entry.place(relx=0.41, rely=.40)

    enter_region = tk.Label(add_akas_canvas, text="Enter Region: ", bg='#ffffff', font=13)
    enter_region.place(relx=0.30, rely=.45)
    region_entry = tk.Entry(add_akas_canvas)
    region_entry.place(relx=0.43, rely=.45)

    enter_language = tk.Label(add_akas_canvas, text="Enter Langauage: ", bg='#ffffff', font=13)
    enter_language.place(relx=0.30, rely=.50)
    langauge_entry = tk.Entry(add_akas_canvas)
    langauge_entry.place(relx=0.47, rely=.50)

    enter_type = tk.Label(add_akas_canvas, text="Enter Type: ", bg='#ffffff', font=13)
    enter_type.place(relx=0.30, rely=.55)
    type_entry = tk.Entry(add_akas_canvas)
    type_entry.place(relx=0.41, rely=.55)

    enter_attributes = tk.Label(add_akas_canvas, text="Enter Attributes: ", bg='#ffffff', font=13)
    enter_attributes.place(relx=0.30, rely=.60)
    attributes_entry = tk.Entry(add_akas_canvas)
    attributes_entry.place(relx=0.45, rely=.60)

    enter_orginal = tk.Label(add_akas_canvas, text="Enter Is Original Title: ", bg='#ffffff', font=13)
    enter_orginal.place(relx=0.30, rely=.65)
    orginal_entry = tk.Entry(add_akas_canvas)
    orginal_entry.place(relx=0.50, rely=.65)

    akas_add_button = tk.Button(add_akas_frame, text="+ Add") #command=add_akas_row
    akas_add_button.place(relx=0.13, rely=0.86, relwidth=0.12)

# def add_akas_row():
#     cnx_akas = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
#                             database='imdb')
#
#     cursor_akas = cnx.cursor()
#     cursor_akas.execute("INSERT INTO akas VALUES (:title_id, :title, :region, :language, :type, :attributes, :is_original_title)",
#                         {
#                             'title_id': title_id_entry.get(),
#                              'title': title_entry.get(),
#                               'region': region_entry.get(),
#                              'language': langauge_entry.get(),
#                              'type': type_entry.get(),
#                             'attributes': attributes_entry.get(),
#                             'is_original_title': orginal_entry.get()
#                         })
#     cnx_akas.commit()
#     cnx_akas.close()

# BROWSE AKAS PAGE
def browse_akas():

    canvas.forget()
    # BROWSE AKAS CANVAS
    browse_akas_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
    browse_akas_canvas.pack()

    main_akas_label = tk.Label(browse_akas_canvas, text="Selected DB: imdb \n Browsing Table: akas", font=13, bg='#ffffff')
    main_akas_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # BROWSE AKAS FRAME
    browse_akas_frame = tk.Frame(browse_akas_canvas, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    browse_akas_frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    #create back button

    # ESTABLISHING CONNECTION
    cnx_akas = connector.connect(user='root', password='comp420', host='ec2-44-209-170-160.compute-1.amazonaws.com',
                            database='imdb')

    cursor_akas = cnx.cursor()
    cursor_akas.execute("SELECT * from akas")
    rows = cursor_akas.fetchall()

    akas_back_button = tk.Button(browse_akas_frame, text="<< Back", command=main_page)
    akas_back_button.place(relx=0.12, rely=0.11, relwidth=0.12)

    browsing_akas_text = tk.Label(browse_akas_frame, text="Browsing: akas")
    browsing_akas_text.place(relx=0.12, rely=.25)

    akas_add_button = tk.Button(browse_akas_frame, text="+ Add Row", command=add_akas)
    akas_add_button.place(relx=0.75, rely=0.25, relwidth=0.12)

    # CREATING THE TABLE
    tv = ttk.Treeview(browse_akas_frame, columns=(1,2,3,4,5,6,7),show="headings",height="3")
    tv.place(relx=0.12, rely=0.33, relwidth=.75, relheight=.45 )

    tv.heading(1, text="title_id")
    tv.heading(2, text="title")
    tv.heading(3, text="region")
    tv.heading(4, text="language")
    tv.heading(5, text="type")
    tv.heading(6, text="attributes")
    tv.heading(7, text="is_original_title")

    for i in rows:
        tv.insert('', 'end', values=i)

    # COMMITING & CLOSING THE CONNECTION
    cnx_akas.commit()
    cnx_akas.close()

#######################################################################################################################################################

# MAIN PAGE
def main_page():
    # db label
    db_label = tk.Label(root, text="Selected db: imdb", bg='#ffffff')
    db_label.place(relx=0.12, rely=0.15, relwidth=0.25, relheight=0.1)

    # to organize the widgets on the screen use a frame
    frame = tk.Frame(root, bg='#ff6666', highlightbackground="black", highlightthickness=1)
    frame.place(relx=0.1, rely=0.3, relwidth=.75, relheight=.40)

    existing_tables = tk.Label(frame, text="Existing Tables:")
    existing_tables.place(relx=0.2, rely=0.15)

    # akas
    akas_label = tk.Label(frame, text="akas", bg='#ffffff')
    akas_label.place(relx=0.2, rely=0.24, relwidth=0.35, relheight=0.1)
    akas_browse_button = tk.Button(frame, text="Browse", command=browse_akas)
    akas_browse_button.place(relx=0.56, rely=0.24, relwidth=0.1, relheight=0.1)
    akas_delete_button = tk.Button(frame, text="Delete", command=delete_akas)
    akas_delete_button.place(relx=0.67, rely=0.24, relwidth=0.1, relheight=0.1)
    akas_add_row_button = tk.Button(frame, text="Add Row", command=add_akas)
    akas_add_row_button.place(relx=0.78, rely=0.24, relwidth=0.1, relheight=0.1)

    # crew
    crew_label = tk.Label(frame, text="crew", bg='#ffffff')
    crew_label.place(relx=0.2, rely=0.36, relwidth=0.35, relheight=0.1)
    crew_browse_button = tk.Button(frame, text="Browse",command=browse_crew)
    crew_browse_button.place(relx=0.56, rely=0.36, relwidth=0.1, relheight=0.1)
    crew_delete_button = tk.Button(frame, text="Delete",command=delete_crew)
    crew_delete_button.place(relx=0.67, rely=0.36, relwidth=0.1, relheight=0.1)
    crew_add_row_button = tk.Button(frame, text="Add Row", command=add_crew)
    crew_add_row_button.place(relx=0.78, rely=0.36, relwidth=0.1, relheight=0.1)

    # episodes
    episodes_label = tk.Label(frame, text="episodes", bg='#ffffff')
    episodes_label.place(relx=0.2, rely=0.48, relwidth=0.35, relheight=0.1)
    episodes_browse_button = tk.Button(frame, text="Browse",command=browse_episodes)
    episodes_browse_button.place(relx=0.56, rely=0.48, relwidth=0.1, relheight=0.1)
    episodes_delete_button = tk.Button(frame, text="Delete",command=delete_episodes)
    episodes_delete_button.place(relx=0.67, rely=0.48, relwidth=0.1, relheight=0.1)
    episodes_add_row_button = tk.Button(frame, text="Add Row", command=add_episodes)
    episodes_add_row_button.place(relx=0.78, rely=0.48, relwidth=0.1, relheight=0.1)

    # people
    people_label = tk.Label(frame, text="people", bg='#ffffff')
    people_label.place(relx=0.2, rely=0.60, relwidth=0.35, relheight=0.1)
    people_browse_button = tk.Button(frame, text="Browse",command=browse_people)
    people_browse_button.place(relx=0.56, rely=0.60, relwidth=0.1, relheight=0.1)
    people_delete_button = tk.Button(frame, text="Delete",command=delete_people)
    people_delete_button.place(relx=0.67, rely=0.60, relwidth=0.1, relheight=0.1)
    people_add_row_button = tk.Button(frame, text="Add Row", command=add_people)
    people_add_row_button.place(relx=0.78, rely=0.60, relwidth=0.1, relheight=0.1)

    # ratings
    ratings_label = tk.Label(frame, text="ratings", bg='#ffffff')
    ratings_label.place(relx=0.2, rely=0.72, relwidth=0.35, relheight=0.1)
    ratings_browse_button = tk.Button(frame, text="Browse",command=browse_ratings)
    ratings_browse_button.place(relx=0.56, rely=0.72, relwidth=0.1, relheight=0.1)
    ratings_delete_button = tk.Button(frame, text="Delete",command=delete_ratings)
    ratings_delete_button.place(relx=0.67, rely=0.72, relwidth=0.1, relheight=0.1)
    ratings_add_row_button = tk.Button(frame, text="Add Row", command=add_people)
    ratings_add_row_button.place(relx=0.78, rely=0.72, relwidth=0.1, relheight=0.1)

    # titles
    titles_label = tk.Label(frame, text="titles", bg='#ffffff')
    titles_label.place(relx=0.2, rely=0.84, relwidth=0.35, relheight=0.1)
    titles_browse_button = tk.Button(frame, text="Browse",command=browse_titles)
    titles_browse_button.place(relx=0.56, rely=0.84, relwidth=0.1, relheight=0.1)
    titles_delete_button = tk.Button(frame, text="Delete",command=delete_titles)
    titles_delete_button.place(relx=0.67, rely=0.84, relwidth=0.1, relheight=0.1)
    titles_add_row_button = tk.Button(frame, text="Add Row", command=add_titles)
    titles_add_row_button.place(relx=0.78, rely=0.84, relwidth=0.1, relheight=0.1)

####################################################################################################################################################
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ff6666')
canvas.pack()
main_page()

root.mainloop()

