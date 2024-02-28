import sqlite3

conn=sqlite3.connect('youtube_videos.db')
cursor=conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')
        
def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    conn.commit()

def update_video(index,name,time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?",(name,time,index))
    conn.commit()

def delete_video(index):
    cursor.execute("DELETE FROM videos WHERE id=?",(index,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager App with DB | Choose one ")
        print("1. List all videos ")
        print("2. Add a video ")
        print("3. Update a video ")
        print("4. Delete a video ")
        print("5. Exit ")

        choice=input("Enter your choice: ")
        
        if choice=='1':
            list_all_videos()

        elif choice=='2':
            name=input("Enter Video Name: ")
            time=input("Enter Video Time: ")
            add_video(name,time)

        elif choice=='3':
            index=int(input("Enter the video number to update: "))
            name=input("Enter New Video Name: ")
            time=input("Enter New Video Time: ")
            update_video(index, name,time)

        elif choice=='4':
            index=int(input("Enter the video number to delete: "))
            delete_video(index)

        elif choice=='5':
            break

        else:
            print("Invalid choice! ")
        
    conn.close()

if __name__=="__main__":
    main()