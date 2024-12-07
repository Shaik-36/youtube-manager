
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            json.load(file)
    except FileNotFoundError:
        return []
    

# A helper method to save data
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, {video['time']}")



def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")

    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Video Number to Update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new Video Name: ")
        time = input("Enter the new Video Time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
        print("Details Updated !!!")
    else:
        print("Invalid Index selected")
    

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video index you want to Delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video Deleted !!!")
    else:
        print("Invalid Index Selected")


def main():
    videos = load_data()

    while True:
        print("\n YouTube Manager | Choose an Option")
        print("1. List a favourite videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube Video details")
        print("4. Delete a YouTube Video")
        print("5. Exit the App\n")

        choice = input("\nEnter your choice :   ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice") 

if __name__ == "__main__":
    main()