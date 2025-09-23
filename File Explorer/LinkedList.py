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