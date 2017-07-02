# followbot_line Read me! Read me!:D
#ROS_Indigo #Gazebo2 #OpenCv #Ubuntu14.04
1. Trước hết khởi tạo catkin workspace : http://wiki.ros.org/catkin/Tutorials/create_a_workspace <br>
  $ mkdir ~/catkin_ws/src <br>
  $ cd ~/catkin_ws/src <br>
  $ catkin_init_workspace <br>
  $ cd ~/catkin_ws <br>
  $ catkin_make <br>
2. Đăng ký môi trường của workspace hiện tại với ROS system (Chọn 1 trong 2) <br>
  $ source ~/catkin_ws/devel/setup.bash <br>
  // Chúng ta phải chạy câu lệnh trên mỗi lần mở bash session mới,nếu muốn tránh điều này, chúng ta cần thêm <br>
  // source command vào .bashrc file, giúp chạy câu lệnh dăng ký mỗi khi có 1 bash session khác mở lên <br>
  $ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc <br>
  $ source ~/.bashrc <br>
3. Download thư mục followbot và để nó trong folder src <br>
4. Quay lại thư mục catkin workspace và chạy catkin <br>
  ~/catkin_ws$ catkin_make <br>
5. Done! Giờ chúng ta chỉ cần chạy song song 3 terminal <br>
  $ roscore <br>
  $ roslaunch followbot course.launch <br>
  $ python follower_p.py <br>
GLHF!
  
