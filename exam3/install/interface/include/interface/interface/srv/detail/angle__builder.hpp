// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interface:srv/Angle.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE__SRV__DETAIL__ANGLE__BUILDER_HPP_
#define INTERFACE__SRV__DETAIL__ANGLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interface/srv/detail/angle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interface
{

namespace srv
{

namespace builder
{

class Init_Angle_Request_theta4
{
public:
  explicit Init_Angle_Request_theta4(::interface::srv::Angle_Request & msg)
  : msg_(msg)
  {}
  ::interface::srv::Angle_Request theta4(::interface::srv::Angle_Request::_theta4_type arg)
  {
    msg_.theta4 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interface::srv::Angle_Request msg_;
};

class Init_Angle_Request_theta3
{
public:
  explicit Init_Angle_Request_theta3(::interface::srv::Angle_Request & msg)
  : msg_(msg)
  {}
  Init_Angle_Request_theta4 theta3(::interface::srv::Angle_Request::_theta3_type arg)
  {
    msg_.theta3 = std::move(arg);
    return Init_Angle_Request_theta4(msg_);
  }

private:
  ::interface::srv::Angle_Request msg_;
};

class Init_Angle_Request_theta2
{
public:
  explicit Init_Angle_Request_theta2(::interface::srv::Angle_Request & msg)
  : msg_(msg)
  {}
  Init_Angle_Request_theta3 theta2(::interface::srv::Angle_Request::_theta2_type arg)
  {
    msg_.theta2 = std::move(arg);
    return Init_Angle_Request_theta3(msg_);
  }

private:
  ::interface::srv::Angle_Request msg_;
};

class Init_Angle_Request_theta1
{
public:
  Init_Angle_Request_theta1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Angle_Request_theta2 theta1(::interface::srv::Angle_Request::_theta1_type arg)
  {
    msg_.theta1 = std::move(arg);
    return Init_Angle_Request_theta2(msg_);
  }

private:
  ::interface::srv::Angle_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interface::srv::Angle_Request>()
{
  return interface::srv::builder::Init_Angle_Request_theta1();
}

}  // namespace interface


namespace interface
{

namespace srv
{

namespace builder
{

class Init_Angle_Response_yaw
{
public:
  explicit Init_Angle_Response_yaw(::interface::srv::Angle_Response & msg)
  : msg_(msg)
  {}
  ::interface::srv::Angle_Response yaw(::interface::srv::Angle_Response::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interface::srv::Angle_Response msg_;
};

class Init_Angle_Response_pitch
{
public:
  explicit Init_Angle_Response_pitch(::interface::srv::Angle_Response & msg)
  : msg_(msg)
  {}
  Init_Angle_Response_yaw pitch(::interface::srv::Angle_Response::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_Angle_Response_yaw(msg_);
  }

private:
  ::interface::srv::Angle_Response msg_;
};

class Init_Angle_Response_roll
{
public:
  explicit Init_Angle_Response_roll(::interface::srv::Angle_Response & msg)
  : msg_(msg)
  {}
  Init_Angle_Response_pitch roll(::interface::srv::Angle_Response::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_Angle_Response_pitch(msg_);
  }

private:
  ::interface::srv::Angle_Response msg_;
};

class Init_Angle_Response_z
{
public:
  explicit Init_Angle_Response_z(::interface::srv::Angle_Response & msg)
  : msg_(msg)
  {}
  Init_Angle_Response_roll z(::interface::srv::Angle_Response::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_Angle_Response_roll(msg_);
  }

private:
  ::interface::srv::Angle_Response msg_;
};

class Init_Angle_Response_y
{
public:
  explicit Init_Angle_Response_y(::interface::srv::Angle_Response & msg)
  : msg_(msg)
  {}
  Init_Angle_Response_z y(::interface::srv::Angle_Response::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Angle_Response_z(msg_);
  }

private:
  ::interface::srv::Angle_Response msg_;
};

class Init_Angle_Response_x
{
public:
  Init_Angle_Response_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Angle_Response_y x(::interface::srv::Angle_Response::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Angle_Response_y(msg_);
  }

private:
  ::interface::srv::Angle_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interface::srv::Angle_Response>()
{
  return interface::srv::builder::Init_Angle_Response_x();
}

}  // namespace interface

#endif  // INTERFACE__SRV__DETAIL__ANGLE__BUILDER_HPP_
