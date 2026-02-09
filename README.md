# Ground Control System (GCS)

## Basic Description

This Ground Control System allows users to assign missions to one or more ground drones. A mission is basically a set of commands that the drone executes automatically. The user creates a mission by defining steps like moving to a location, taking pictures, or landing at a point. Once the mission starts, the drone follows these commands on its own without manual control at every step. The user does not need to control the drone at every step.

---

## Features

- **Mission Planning** – The user can create missions step by step using commands.  
- **Multi-Drone Control** – The system allows control of multiple drones from one interface.  
- **Autonomous Execution** – Drones execute the assigned mission automatically without manual control.  
- **Real-time Monitoring** – The user can monitor drone position, battery level, and mission status live.  
- **Data Collection** – The drone collects photos and sensor data during the mission.  
- **Safety Features** – The system includes emergency stop, manual control, and low battery alerts.  

---

## Stakeholders of GCS

1. **User**  
   Person who uses the Ground Control System.  

2. **Drone**  
   Drone receives commands and executes missions.  

3. **Mission Planner**  
   A user or team member who creates the plan, such as deciding the route, locations, and tasks.  

4. **Administrator**  
   Admin manages the system, settings, and security.  

5. **Technical Team**  
   Team that maintains the drones and the Ground Control System so the system works properly.  

6. **Organization**  
   Company or organization that uses the Ground Control System.  

7. **GPS / Mapping System**  
   External system that provides location and navigation data to drones.  

8. **Data Storage System**  
   Stores all system images, mission data, and logs.  

---

## Functional Requirements

**ID + User Type + Shall be able to + Feature**  

- **FR-01:** User shall be able to assign a mission to one or more drones.  
- **FR-02:** User shall be able to start a mission from the Ground Control System.  
- **FR-03:** Ground Control System shall be able to send mission commands to the drone automatically.  
- **FR-04:** User shall be able to monitor the drone’s status during the mission.  
- **FR-05:** User shall be able to view the current location of the drone.  
- **FR-06:** User shall be able to receive mission completion updates from the system.  
- **FR-07:** User shall be able to stop or abort a mission if needed.  

**Key Entities:**  
- User  
- Drone  
- Mission  
- Command  
- Location  
- Mission Status  
- Sensor Data  
- History  

---

## Components (Modules / Parts of the System)

- Authentication System (login/signup)  
- Map / Navigation System  
- Mission Planning and Management System  
- Data Collection System  
- Data Storage / Database System  
- Alert & Notification System  
- Monitoring System
