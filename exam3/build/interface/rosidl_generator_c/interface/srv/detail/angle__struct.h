// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interface:srv/Angle.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE__SRV__DETAIL__ANGLE__STRUCT_H_
#define INTERFACE__SRV__DETAIL__ANGLE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Angle in the package interface.
typedef struct interface__srv__Angle_Request
{
  double theta1;
  double theta2;
  double theta3;
  double theta4;
} interface__srv__Angle_Request;

// Struct for a sequence of interface__srv__Angle_Request.
typedef struct interface__srv__Angle_Request__Sequence
{
  interface__srv__Angle_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interface__srv__Angle_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Angle in the package interface.
typedef struct interface__srv__Angle_Response
{
  double x;
  double y;
  double z;
  double roll;
  double pitch;
  double yaw;
} interface__srv__Angle_Response;

// Struct for a sequence of interface__srv__Angle_Response.
typedef struct interface__srv__Angle_Response__Sequence
{
  interface__srv__Angle_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interface__srv__Angle_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACE__SRV__DETAIL__ANGLE__STRUCT_H_
