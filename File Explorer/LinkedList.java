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
    public void deleteFile(String filename){
        FileNode temp=head;
        if(head==null){
            System.out.println("There are no files in the directory");
            return;
        }
        if(head.filename.equals(filename)){
            head=head.next;
            System.out.println("The file is deleted succesfully");
            return;
        }
        while(temp.next!=null){
            if(temp.next.filename.equals(filename)){
                temp.next=temp.next.next
                System.out.println("The file is deleted succesfully");
                return;
            }
            temp=temp.next;
        }
        System.out.println("The file is not found");
    }
}