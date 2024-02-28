from pymongo import MongoClient
from bson import ObjectId

client=MongoClient("mongodb+srv://username:password@cluster0.iadydvs.mongodb.net/")
# print(client)
db=client["ytmanager"]
video_collection= db["videos"]
# print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time:{video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name":name, "time": time})

def update_video(index,new_name,new_time):
    video_collection.update_one(
        {'_id':ObjectId(index)},
        {"$set":{"name":new_name, "time":new_time}}
    )

def delete_video(index):
    video_collection.delete_one({'_id':ObjectId(index)})

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
            index=input("Enter the video number to update: ")
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

if __name__=="__main__":
    main()