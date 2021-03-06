;; Auto-generated. Do not edit!


(when (boundp 'scara_cpe_kinematics::GoToXY)
  (if (not (find-package "SCARA_CPE_KINEMATICS"))
    (make-package "SCARA_CPE_KINEMATICS"))
  (shadow 'GoToXY (find-package "SCARA_CPE_KINEMATICS")))
(unless (find-package "SCARA_CPE_KINEMATICS::GOTOXY")
  (make-package "SCARA_CPE_KINEMATICS::GOTOXY"))
(unless (find-package "SCARA_CPE_KINEMATICS::GOTOXYREQUEST")
  (make-package "SCARA_CPE_KINEMATICS::GOTOXYREQUEST"))
(unless (find-package "SCARA_CPE_KINEMATICS::GOTOXYRESPONSE")
  (make-package "SCARA_CPE_KINEMATICS::GOTOXYRESPONSE"))

(in-package "ROS")





(defclass scara_cpe_kinematics::GoToXYRequest
  :super ros::object
  :slots (_x _y ))

(defmethod scara_cpe_kinematics::GoToXYRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass scara_cpe_kinematics::GoToXYResponse
  :super ros::object
  :slots (_finished ))

(defmethod scara_cpe_kinematics::GoToXYResponse
  (:init
   (&key
    ((:finished __finished) nil)
    )
   (send-super :init)
   (setq _finished __finished)
   self)
  (:finished
   (&optional __finished)
   (if __finished (setq _finished __finished)) _finished)
  (:serialization-length
   ()
   (+
    ;; bool _finished
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _finished
       (if _finished (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _finished
     (setq _finished (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass scara_cpe_kinematics::GoToXY
  :super ros::object
  :slots ())

(setf (get scara_cpe_kinematics::GoToXY :md5sum-) "37872fb1b1aa19c26302f3aa18acdaf5")
(setf (get scara_cpe_kinematics::GoToXY :datatype-) "scara_cpe_kinematics/GoToXY")
(setf (get scara_cpe_kinematics::GoToXY :request) scara_cpe_kinematics::GoToXYRequest)
(setf (get scara_cpe_kinematics::GoToXY :response) scara_cpe_kinematics::GoToXYResponse)

(defmethod scara_cpe_kinematics::GoToXYRequest
  (:response () (instance scara_cpe_kinematics::GoToXYResponse :init)))

(setf (get scara_cpe_kinematics::GoToXYRequest :md5sum-) "37872fb1b1aa19c26302f3aa18acdaf5")
(setf (get scara_cpe_kinematics::GoToXYRequest :datatype-) "scara_cpe_kinematics/GoToXYRequest")
(setf (get scara_cpe_kinematics::GoToXYRequest :definition-)
      "float64 x
float64 y
---
bool finished
")

(setf (get scara_cpe_kinematics::GoToXYResponse :md5sum-) "37872fb1b1aa19c26302f3aa18acdaf5")
(setf (get scara_cpe_kinematics::GoToXYResponse :datatype-) "scara_cpe_kinematics/GoToXYResponse")
(setf (get scara_cpe_kinematics::GoToXYResponse :definition-)
      "float64 x
float64 y
---
bool finished
")



(provide :scara_cpe_kinematics/GoToXY "37872fb1b1aa19c26302f3aa18acdaf5")


