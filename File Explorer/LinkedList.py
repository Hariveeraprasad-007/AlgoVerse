class FileNode:
    def __init__(self,filename,filesize):
        self.filename=filename
        self.filesize=filesize
        self.next=None
class FileManager:
    def __init__(self):
        self.head=None
    def create_file(self,filename,filesize):
        new_node=FileNode(filename,filesize)
        if self.head is None:
            self.head=new_node
            return
        temp_node=self.head
        while(temp_node.next):
            temp=temp.next
        temp.next=new_node
    def delete_file(self,filename):
        if self.head is None:
            print("No files are there to delete")
            return
        if self.head.filename==filename:
            self.head=self.head.next
            print("file deleted succesfully")
            return
        temp=self.head
        while(temp.next):
            if temp.next.filename==filename:
                temp=temp.next.next
                print("File deleted succesfully")
                return
            temp=temp.next
        print("File not found")
    def update_file(self,oldfilename,newfilename):
        temp=self.head
        while(temp):
            if(temp.filename==oldfilename):
                temp.filename=newfilename
                print("File name is updated succesfully")
                return 
            temp=temp.next
        print("file is not found")
    def display_files(self):
        if(self.head is None):
            print("No files are there")
        temp=self.head
        while(temp):
            print("File name:",temp.filename," File size:",temp.filesize)
            temp=temp.next
        
