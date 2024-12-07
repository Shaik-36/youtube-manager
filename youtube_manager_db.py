import sqlite3

con = sqlite3.connect("youtube_videos.db")

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

def update_video(video_id, name, time):
    cur.execute(" UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    con.commit() 

def delete_video(video_id):
    cur.execute(" DELETE FROM videos  WHERE id = ?", (video_id,))
    con.commit() 

def main():
    while True:
        print("\n\n YouTube Manager with SQLite DB \n")
        print("=============  Choose an Option ===========")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video ")
        print("4. Delete Video")
        print("5. Exit the App\n")

        choice = input("\nEnter your choice :   ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the Video Name : ")
                time = input("Enter the Video Time : ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the Video ID to Update : ")
                name = input("Enter the Video Name : ")
                time = input("Enter the Video Time : ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the Video ID to Delete : ")
                delete_video(video_id)
            case '5':
                print("Exiting application....!!!")
            case _:
                print("Invalid Selection")
    con.close()
       


if __name__ == "__main__":
    main()