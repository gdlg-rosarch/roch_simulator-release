# Script generated with Bloom
pkgdesc="ROS - SawYer roch Simulator bringup"
url='http://ros.org/wiki/roch_gazebo'

pkgname='ros-kinetic-roch-gazebo'
pkgver='2.0.12_6'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-roslaunch'
)

depends=('ros-kinetic-controller-manager'
'ros-kinetic-gazebo-plugins'
'ros-kinetic-gazebo-ros'
'ros-kinetic-gazebo-ros-control'
'ros-kinetic-hector-gazebo-plugins'
'ros-kinetic-map-server'
'ros-kinetic-pointcloud-to-laserscan'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-roch-bringup'
'ros-kinetic-roch-control'
'ros-kinetic-roch-description'
'ros-kinetic-roch-navigation'
'ros-kinetic-rostopic'
)

conflicts=()
replaces=()

_dir=roch_gazebo
source=()
md5sums=()

prepare() {
    cp -R $startdir/roch_gazebo $srcdir/roch_gazebo
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

