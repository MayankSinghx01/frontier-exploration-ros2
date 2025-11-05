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

