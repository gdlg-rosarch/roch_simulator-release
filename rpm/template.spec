Name:           ros-kinetic-roch-gazebo
Version:        2.0.12
Release:        5%{?dist}
Summary:        ROS roch_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roch_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-gazebo-plugins
Requires:       ros-kinetic-gazebo-ros
Requires:       ros-kinetic-gazebo-ros-control
Requires:       ros-kinetic-hector-gazebo-plugins
Requires:       ros-kinetic-map-server
Requires:       ros-kinetic-pointcloud-to-laserscan
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-roch-bringup
Requires:       ros-kinetic-roch-control
Requires:       ros-kinetic-roch-description
Requires:       ros-kinetic-roch-navigation
Requires:       ros-kinetic-rostopic
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roslaunch

%description
SawYer roch Simulator bringup

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Sep 18 2017 Carl <wzhang@softrobtech.com> - 2.0.12-5
- Autogenerated by Bloom

* Mon Sep 18 2017 Carl <wzhang@softrobtech.com> - 2.0.12-4
- Autogenerated by Bloom

* Mon Sep 18 2017 Carl <wzhang@softrobtech.com> - 2.0.12-3
- Autogenerated by Bloom

* Mon Sep 18 2017 Carl <wzhang@softrobtech.com> - 2.0.12-2
- Autogenerated by Bloom

* Mon Sep 18 2017 Carl <wzhang@softrobtech.com> - 2.0.12-1
- Autogenerated by Bloom

* Mon Sep 18 2017 Carl <wzhang@softrobtech.com> - 2.0.12-0
- Autogenerated by Bloom

