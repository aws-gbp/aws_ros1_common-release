Name:           ros-melodic-aws-ros1-common
Version:        2.0.1
Release:        1%{?dist}
Summary:        ROS aws_ros1_common package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/aws_ros1_common
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-aws-common
Requires:       ros-melodic-roscpp
BuildRequires:  gtest-devel
BuildRequires:  ros-melodic-aws-common
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rostest

%description
Common utilities for ROS1 nodes using Amazon Web Services

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Aug 01 2019 AWS RoboMaker <ros-contributions@amazon.com> - 2.0.1-1
- Autogenerated by Bloom

* Wed Mar 20 2019 AWS RoboMaker <ros-contributions@amazon.com> - 2.0.0-0
- Autogenerated by Bloom

