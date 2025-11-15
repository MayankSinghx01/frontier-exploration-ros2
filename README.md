# Frontier Exploration Robot

## Aim

To create an autonomous frontier exploring robot capable of navigating through obstacles and creating an accurate 2D map of an unexplored environment.

## Prerequisites

* Ubuntu 22.04.5
* ROS 2 Humble
* Gazebo and RViz2
* Nav2 and SLAM Toolbox

## Working

1. **Frontier Cell Clustering**: Frontiers are cells are detected and clustered into frontier edges using BFS Algorithm.
2. **Centroid Selection**: Centroids are calculated for each frontier edge and centroid corresponding to largest frontier is chosen as goal.
3. **Path Generation and Autonomous Navigation**: Chosen goal is fed to Nav2 stack and an ideal path is generated and followed by the robot.
4. **Map Visualization**: Real-time map is generated on RViz2 as the bot moves and explores the environment.

## Turtlesim Package

Turtlesim is a beginner-friendly ROS 2 package used to learn the fundamentals of publishing, subscribing, topics, services, and actions. It provides a simple 2D turtle simulator where you can send velocity commands, draw shapes, control the turtle's pose, or interact through custom nodes. Turtlesim is extremely useful for understanding how ROS 2 communication works before moving on to real robots and complex systems like TurtleBot3, SLAM, and Nav2.

## Gazebo Classic

Gazebo Classic is a powerful 3D robotics simulator used to test and develop robot algorithms without needing real hardware. It provides a full physics engine, sensor simulation, and ROS 2 integration, allowing developers to run complete robotics pipelines in a virtual environment.

#### ROS 2 integration via `gazebo_ros_pkgs` enables:

* controlling simulated robots with ROS 2 nodes.
* publishing sensor data as ROS topics.
* sending velocity commands.
* spawning URDF/SDF models.
* running SLAM, navigation, and custom algorithms.

### TurtleBot3

TurtleBot3 is a modular, lightweight, and fully open-source mobile robot designed for learning and research in ROS 2. It comes with built-in packages for simulation, navigation, SLAM, and teleoperation. In Gazebo Classic, you can easily spawn different official models - `burger`, `waffel`, and `waffel_pi` - each with its own size, sensors, and capabilities. TurtleBot3 is widely used for testing algorithms like mapping, localization, frontier exploration, and path planning before deploying to real hardware.

## SLAM in ROS 2

In ROS 2, SLAM (Simultaneous Localisation and Mapping) is used to build a map of an unknown environment while estimating the robot's position within it. ROS 2 primarily uses two modern SLAM systems: **SLAM Toolbox**, the official and most widely supported 2D laser-based SLAM solution, and **Cartographer**, Google's graph-based LiDAR mapping system. SLAM Toolbox integrates tightly with Nav2, supports lifelong mapping, loop closure, and localization mode, while Cartographer provides fast and accurate scan matching for high-quality maps. These SLAM algorithms allow robots like TurtleBot3 to perform autonomous navigation, mapping, and exploration in both simulation and real-world environments.

## RViz2 Visualization Software

**RViz2** is the primary 3D visualization tool for ROS 2, used to observe and debug everything happening in a robot system. It displays sensor data (like LiDAR scans and depth images), the live SLAM-generated map, TF coordinate frames, robot pose, costmaps, planned paths, and Nav2 navigation outputs. It makes it easy to understand how the robot perceives its environment and helps verify that SLAM and navigation are working correctly.

## Nav2 Stack

Nav2 (Navigation2) is the ROS 2 system that lets a robot move to a goal on its own. It uses the map from SLAM, figures out where the robot is, plans a safe path, avoids obstacles, and sends smooth velocity commands to the robot. Nav2 works with TurtleBot3 in both Gazebo simulation and real hardware, making it essential for tasks like autonomous navigation, waypoint following, and exploring indoor environments.

## Installations

1. Install Gazebo (Gazebo Classic packages for ROS2)
```
sudo apt install -y ros-humble-gazebo-*
```

2. Create a workspace for TurtleBot3 packages
```
mkdir -p ~/turtlebot3_ws/src
cd ~/turtlebot3_ws/src
```

3. Clone the official TurtleBot3 repos
```
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
```

4. Build the workspace with colcon build and source the workspace
```
cd ~/turtlebot3_ws
colcon build --symlink-install
source ~/turtlebot3_ws/install/setup.bash
```
### Running a Gazebo Simulation with TurtleBot3:

1. Export your desired TurtleBot3 model. We will be using model `burger`
```
export TURTLEBOT3_MODEL=burger
```

2. Launch your desired world.
```
# empty world
ros2 launch turtlebot3_gazebo empty_world.launch.py

# full TurtleBot3 world
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

3. Operate your robot using teleoperation commands
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
