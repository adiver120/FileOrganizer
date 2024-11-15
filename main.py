import os
import shutil


directory = r"C:\Users\Aditya\Desktop\folder"


file_types={
    "Documents": [".pdf, .doc, .docx, .txt, .xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],

}

def file_organizer(directory, file_types):

    #creating folders for file types
    for folder in file_types.keys():
        os.makedirs(os.path.join(directory,folder), exist_ok=True)

    #moving files to desired folders
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory,file_name)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()

            for folder_name, extension in file_types.items():
                if file_extension in extension:
                    shutil.move(file_path, os.path.join(directory, folder_name, file_name))
                    break

    print("Files have been organized")


if __name__=="__main__":
    file_organizer(directory, file_types)















