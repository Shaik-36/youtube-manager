import sqlite3

con = sqlite3.connect("youtube_video.db")

cur = con.cursor()

cur.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
 ''')


def list_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_id, new_name, new_time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cur.execute("DELETE from videos WHERE id = ?", (video_id,))
    con.commit()

def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit App")
        choice = input("\n Enter your Choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
           name = input("Enter the Video Name: ")
           time =  input("Enter the Video Time: ")
           add_video(name, time)
        elif choice == '3':
           video_id = int(input("Enter video ID to Update : "))
           name = input("Enter the Video Name: ")
           time =  input("Enter the Video Time: ")
           update_video(video_id, name, time)
        elif choice == '4':
           video_id = int(input("Enter video ID to Delete : "))
           delete_video(video_id)
        elif choice == '5':
           break
        else:
            print("Invalid Choice")

    con.close()


if __name__ == "__main__":
    main()