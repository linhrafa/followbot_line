# followbot_line HƯỚNG DẪN SỬ DỤNG TRƯỚC KHI DÙNG :D
1. Trước hết khởi tạo catkin workspace : http://wiki.ros.org/catkin/Tutorials/create_a_workspace
  $ mkdir ~/catkin_ws/src
  $ cd ~/catkin_ws/src
  $ catkin_init_workspace
  $ cd ~/catkin_ws
  $ catkin_make
2. Đăng ký môi trường của workspace hiện tại với ROS system (Chọn 1 trong 2)
  $ source ~/catkin_ws/devel/setup.bash
  // Chúng ta phải chạy câu lệnh trên mỗi lần mở bash session mới,nếu muốn tránh điều này, chúng ta cần thêm
  // source command vào .bashrc file, giúp chạy câu lệnh dăng ký mỗi khi có 1 bash session khác mở lên
  $ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
  $ source ~/.bashrc
3. Download thư mục followbot và để nó trong folder src
4. Quay lại thư mục catkin workspace và chạy catkin
  ~/catkin_ws$ catkin_make
5. Done! Giờ chúng ta chỉ cần chạy song song 3 terminal
  $ roscore
  $ roslaunch followbot course.launch
  $ python follower_p.py
GLHF!
  
