class FileNode{
    String filename;
    int Filesize;
    FileNode next;

    public FileNode(String filename,int Filesize){
        this.filename=filename;
        this.Filesize=Filesize;
        this.next=null;
    }
}
class LinkedList{
    private FileNode head;

    public void createFile(String Filename,int FileSize){
        FileNode newnode=new FileNode(Filename,FileSize);
        if(head==null){
            head=newnode;
            return;
        }
        FileNode temp=head;
        while(temp.next!=null){
            temp=temp.next;
        }
        temp.next=newnode;
    }
}