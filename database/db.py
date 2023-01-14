import sqlite3,json

j={
    "hello":"world",
    "foo":"bar"
}

j=json(j)

con = sqlite3.connect("./database/game.db")
cur=con.cursor()
# cur.execute("CREATE TABLE skill(name,effect,describe)")
cur.execute("create table js(body text,id integer ")
cur.execute("INSERT INTO skill values ('test4',123,'这是一段描述');")
con.commit()
res=cur.execute("SELECT * from skill")
print(res.fetchall())

                