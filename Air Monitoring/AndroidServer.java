import java.io.*;  
import java.net.*;  
public class AndroidServer {  
public static void main(String[] args){  
while(true){
try{  
ServerSocket ss=new ServerSocket(6666);  

Socket s=ss.accept();//establishes connection   
DataInputStream dis=new DataInputStream(s.getInputStream());  
String  str=(String)dis.readUTF();  
System.out.println(str);  
try(FileWriter fw = new FileWriter("GPSCordinates.txt", true);
    BufferedWriter bw = new BufferedWriter(fw);
    PrintWriter out = new PrintWriter(bw))
{
    out.println(str);
    
    //more code
} catch (IOException e) {
    //exception handling left as an exercise for the reader
}
ss.close(); } 
catch(Exception e){System.out.println(e);}  
}  
}  }
/*15.392980, 73.880535, '9000ppm'
15.392556, 73.879044, '12000ppm'
15.391806, 73.880702, '18800ppm'*/